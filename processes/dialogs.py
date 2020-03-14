from uuid import uuid1
from modules.info import export_dir
from modules.dialogs import dialogs
from operations import save_statement_block
from common import convert_to_identifier, replace_spaces
from module_processor import ModuleProcessor


auto_ids = {}

# -------------------------------------------------------


def save_dialog_states(dialog_states):
  file = open(export_dir + "dialog_states.txt", "w")
  for dialog_state in dialog_states:
    file.write("%s\n" % dialog_state)
  file.close()


# =================================================================
def compile_dialog_tokens(dialogs):
  input_tokens = []
  output_tokens = []
  dialog_states = [
      "start", "party_encounter", "prisoner_liberated", "enemy_defeated", "party_relieved",
      "event_triggered", "close_window", "trade", "exchange_members", "trade_prisoners",
      "buy_mercenaries", "view_char", "training", "member_chat", "prisoner_chat"
  ]
  dialog_state_usages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  for dialog in dialogs:
    output_token_id = -1
    output_token = dialog[4]
    found = 0
    for i_t in range(len(dialog_states)):
      if output_token == dialog_states[i_t]:
        output_token_id = i_t
        found = 1
        break
    if not found:
      dialog_states.append(output_token)
      dialog_state_usages.append(0)
      output_token_id = len(dialog_states) - 1
    output_tokens.append(output_token_id)
  for dialog in dialogs:
    input_token_id = -1
    input_token = dialog[1]
    found = 0
    for i_t in range(len(dialog_states)):
      if input_token == dialog_states[i_t]:
        input_token_id = i_t
        dialog_state_usages[i_t] = dialog_state_usages[i_t] + 1
        found = 1
        break
    if not found:
      print(dialog[1])
      print(dialog[3])
      print(dialog[4])
      print("**********************************************************************************")
      print("ERROR: INPUT TOKEN NOT FOUND:" + input_token)
      print("**********************************************************************************")
      print("**********************************************************************************")
    input_tokens.append(input_token_id)
  save_dialog_states(dialog_states)
  for i_t in range(len(dialog_states)):
    if dialog_state_usages[i_t] == 0:
      print("ERROR: Output token not found: " + dialog_states[i_t])
  return (input_tokens, output_tokens)


def create_auto_id2(dialog, auto_ids):
  text = dialog[3]
  token_ipt = convert_to_identifier(dialog[1])
  token_opt = convert_to_identifier(dialog[4])
  done = 0
  auto_id = "dlga_" + token_ipt + ":" + token_opt
  done = 0
  if auto_id not in auto_ids:
    done = 1
  else:
    if auto_ids[auto_id] == text:
      done = 1
  if not done:
    number = 1
    new_auto_id = auto_id + "." + str(number)
    while new_auto_id in auto_ids:
      number += 1
      new_auto_id = auto_id + "." + str(number)
    auto_id = new_auto_id
  auto_ids[auto_id] = text
  return auto_id


def save_dialog(file, dialog, input_state, output_state):
  dialog_id = create_auto_id2(dialog, auto_ids)
  file.write("%s %d %d " % (dialog_id, dialog[0], input_state))
  save_statement_block(file, 0, 1, dialog[2])
  file.write("%s " % replace_spaces(dialog[3]))
  if (len(dialog[3]) == 0):
    file.write("NO_TEXT ")
  file.write(" %d " % output_state)
  save_statement_block(file, 0, 1, dialog[5])
  if (len(dialog) > 6):
    file.write("%s " % dialog[6])
  else:
    file.write("NO_VOICEOVER ")
  file.write("\n")


class DialogProcessor(ModuleProcessor):
  clean_ids_file = True
  export_name = "conversation.txt"

  def after_open_export_file(self):
    self.export_file.write("dialogsfile version 2\n")
    self.export_file.write("%d\n" % len(dialogs))

  def write_export_file(self, dialog, input_state, output_state):
    save_dialog(self.export_file, dialog, input_state, output_state)

def process_dialogs():
  print("exporting dialogs...")
  input_states, output_states = compile_dialog_tokens(dialogs)
  processor = DialogProcessor()
  for index, dialog in enumerate(dialogs):
    processor.write(dialog, index, input_states[index], output_states[index])
  processor.close()
