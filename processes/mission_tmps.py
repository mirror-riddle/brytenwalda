from modules.mission_templates import mission_templates
from operations import save_statement_block
from common import convert_to_identifier, replace_spaces
from module_processor import ModuleProcessor
from triggers import save_trigger


def save_triggers(file, triggers):
  file.write("%d\n" % len(triggers))
  for trigger in triggers:
    save_trigger(file, trigger)


def save_mission_template_group(file, entry):
  if (len(entry[5]) > 8):
    print("ERROR: Too many item_overrides!")
  file.write("%d %d %d %d %d %d " % (entry[0], entry[1], entry[2], entry[3], entry[4], len(entry[5])))
  for item_override in entry[5]:
    file.write("%d " % (item_override))
  file.write("\n")


def save_mission_template(file, mission_template):
  identity = convert_to_identifier(mission_template[0])
  file.write("mst_%s %s %d %d\n" % (identity, identity, mission_template[1], mission_template[2]))
  file.write("%s\n" % replace_spaces(mission_template[3]))
  file.write("%d " % len(mission_template[4]))
  for group in mission_template[4]:
    save_mission_template_group(file, group)


class MissionTemplateProcessor(ModuleProcessor):
  id_prefix = "mst_"
  id_name = "mission_templates.py"
  export_name = "mission_templates.txt"

  def after_open_export_file(self):
    self.export_file.write("missionsfile version 1\n")
    self.export_file.write(" %d\n" % len(mission_templates))

  def write_export_file(self, mission_template):
    save_mission_template(self.export_file, mission_template)
    save_triggers(self.export_file, mission_template[5])


def process_mission_tmps():
  print("exporting mission_templates...")
  processor = MissionTemplateProcessor()
  for index, mission_template in enumerate(mission_templates):
    processor.write(mission_template, index)
  processor.close()
