from modules.game_menus import game_menus
from modules.parties import parties
from operations import find_object
from common import convert_to_identifier, replace_spaces
from module_processor import ModuleProcessor


def save_party(file, party, index):
  identity = convert_to_identifier(party[0])
  name = replace_spaces(party[1])
  file.write("1 %d %d p_%s %s %d " % (index, index, identity, name, party[2]))
  menu_no = 0
  menu_param = party[3]
  if isinstance(menu_param, str):
    menu_no = find_object(game_menus, menu_param)
    if (menu_no < 0):
      print("Error: Unable to find menu-id :" + menu_param)
  else:
    menu_no = menu_param
  file.write("%d " % (menu_no))

  file.write("%d %d %d %d %d " % (party[4], party[5], party[6], party[6], party[7]))
  ai_behavior_object = 0
  ai_param = party[8]
  if isinstance(ai_param, str):
    ai_behavior_object = find_object(parties, ai_param)
    if (ai_behavior_object < 0):
      print("Error: Unable to find party-id :" + ai_param)
  else:
    ai_behavior_object = ai_param
  file.write("%d %d " % (ai_behavior_object, ai_behavior_object))
  position = party[9]
  default_behavior_location = position
  file.write("%f %f " % (default_behavior_location[0], default_behavior_location[1]))
  file.write("%f %f " % (default_behavior_location[0], default_behavior_location[1]))
  file.write("%f %f 0.0 " % position)
  member_list = party[10]
  file.write("%d " % len(member_list))
  for member in member_list:
    file.write("%d %d 0 %d " % (member[0], member[1], member[2]))
  bearing = 0.0
  if (len(party) > 11):
    bearing = (3.1415926 / 180.0) * party[11]
  file.write("\n%f\n" % (bearing))


class PartyProcessor(ModuleProcessor):
  id_prefix = "p_"
  id_name = "parties.py"
  export_name = "parties.txt"

  def after_open_export_file(self):
    self.export_file.write("partiesfile version 1\n")
    self.export_file.write("%d %d\n" % (len(parties), len(parties)))

  def write_export_file(self, party, index):
    save_party(self.export_file, party, index)


def process_parties():
  print("exporting parties...")
  processor = PartyProcessor()
  for index, party in enumerate(parties):
    processor.write(party, index, index)
  processor.close()
