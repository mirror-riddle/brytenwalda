import os
from modules.triggers import triggers
from operations import save_statement_block
from common import (
  load_variables, save_variables, load_quick_strings, save_quick_strings,
  is_file_exist
)
from module_processor import ModuleProcessor


def save_trigger(file, trigger, variables, variable_uses, quick_strings):
    file.write("%f %f %f " % (trigger[0], trigger[1], trigger[2]))
    for block in (trigger[3], trigger[4]):
      save_statement_block(
        file, 0, 1, block,
        variables, variable_uses, [], quick_strings
      )
    file.write("\n")

class TriggerProcessor(ModuleProcessor):
  export_name = "triggers.txt"

  def after_open_export_file(self):
    self.export_file.write("triggersfile version 1\n")
    self.export_file.write("%d\n" % len(triggers))

  def write_id_file(self, tigger, index):
    pass

  def write_export_file(self, trigger, variables, variable_uses, quick_strings):
    save_trigger(self.export_file, trigger, variables, variable_uses, quick_strings)

  def after_close(self):
    ids_path = "../ids/" + self.id_name
    if is_file_exist(ids_path):
      os.remove(ids_path)

def process_triggers():
  print("exporting triggers...")
  quick_strings = load_quick_strings()
  variables, variable_uses = load_variables()
  
  processor = TriggerProcessor()
  for index, trigger in enumerate(triggers):
    processor.write(trigger, index, variables, variable_uses, quick_strings)
  processor.close()

  save_quick_strings(quick_strings)
  save_variables(variables, variable_uses)