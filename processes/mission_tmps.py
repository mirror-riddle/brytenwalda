from headers.triggers import (
    trigger_check_pos, trigger_conditions_pos, trigger_consequences_pos,
    trigger_delay_pos, trigger_rearm_pos
)
from modules.info import export_dir
from modules.mission_templates import mission_templates
from operations import (
    save_statement_block,
)
from common import (
    convert_to_identifier, lf_open, load_variables, replace_spaces,
    save_variables, load_quick_strings, save_quick_strings
)
from module_processor import ModuleProcessor

mission_template_name_pos = 0
mission_template_flags_pos = 1
mission_template_types_pos = 2
mission_template_desc_pos = 3
mission_template_groups_pos = 4
mission_template_triggers_pos = 5


def save_triggers(file, template_name, triggers, variable_list, variable_uses, quick_strings):
  file.write("%d\n" % len(triggers))
  for trigger in triggers:
    file.write("%f %f %f " % (trigger[trigger_check_pos], trigger[trigger_delay_pos], trigger[trigger_rearm_pos]))
    save_statement_block(file, 0, 1, trigger[trigger_conditions_pos], variable_list, variable_uses, [], quick_strings)
    save_statement_block(file, 0, 1, trigger[trigger_consequences_pos], variable_list, variable_uses, [], quick_strings)
    file.write("\n")


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

  def write_tiggers(self, mission_template, variables, variable_uses, quick_strings):
    identity = convert_to_identifier(mission_template[0])
    save_triggers(self.export_file, identity, mission_template[5], variables, variable_uses, quick_strings)


def process_mission_tmps():
  print("Exporting mission_template...")
  quick_strings = load_quick_strings()
  variables, variable_uses = load_variables()

  processor = MissionTemplateProcessor()
  for index, mission_template in enumerate(mission_templates):
    processor.write(mission_template, index)
    processor.write_tiggers(mission_template, variables, variable_uses, quick_strings)
  processor.close()

  save_quick_strings(quick_strings)
  save_variables(variables, variable_uses)
