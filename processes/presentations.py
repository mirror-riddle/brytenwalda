from modules.info import export_dir
from modules.presentations import presentations
from common import (
    lf_open, load_variables, save_variables,
    load_quick_strings, save_quick_strings
)
from operations import save_simple_triggers


def save_presentations(variable_list, variable_uses, quick_strings):
  ofile = open(export_dir + "presentations.txt", "w")
  ofile.write("presentationsfile version 1\n")
  ofile.write(" %d\n" % (len(presentations)))
  for presentation in presentations:
    ofile.write("prsnt_%s %d %d " % (presentation[0], presentation[1], presentation[2]))
    save_simple_triggers(ofile, presentation[3], variable_list, variable_uses, [], quick_strings)
    ofile.write("\n")
  ofile.close()


def save_python_header():
  file = lf_open("../ids/presentations.py", "w")
  for i_presentation in range(len(presentations)):
    file.write("prsnt_%s = %d\n" % (presentations[i_presentation][0], i_presentation))
  file.close()


def process_presentations():
  print("Exporting presentations...")
  save_python_header()
  quick_strings = load_quick_strings()
  variables, variable_uses = load_variables()
  print(len(variables))

  save_presentations(variables, variable_uses, quick_strings)

  save_quick_strings(quick_strings)
  save_variables(variables, variable_uses)
