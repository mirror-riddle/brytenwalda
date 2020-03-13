from modules.info import export_dir
from modules.simple_triggers import simple_triggers
from operations import save_statement_block
from common import (
    load_variables, save_variables, load_quick_strings, save_quick_strings
)


def save_simple_triggers_2(variable_list, variable_uses, triggers, tag_uses, quick_strings):
  file = open(export_dir + "simple_triggers.txt", "w")
  file.write("simple_triggers_file version 1\n")
  file.write("%d\n" % len(simple_triggers))
  for i in range(len(simple_triggers)):
    simple_trigger = simple_triggers[i]
    file.write("%f " % (simple_trigger[0]))
    save_statement_block(file, 0, 1, simple_trigger[1], variable_list, variable_uses, tag_uses, quick_strings)
    file.write("\n")
  file.close()


def process_simple_tiggers():
  print("exporting simple triggers...")
  quick_strings = load_quick_strings()
  variables, variable_uses = load_variables()

  save_simple_triggers_2(variables, variable_uses, simple_triggers, [], quick_strings)

  save_quick_strings(quick_strings)
  save_variables(variables, variable_uses)
