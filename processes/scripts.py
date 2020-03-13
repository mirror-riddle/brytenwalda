from modules.info import export_dir
from modules.scripts import scripts
from operations import save_statement_block
from common import (
    convert_to_identifier, lf_open, load_variables, save_variables,
    load_quick_strings, save_quick_strings
)
from module_processor import ModuleProcessor


def save_script(file, script, variables, variable_uses, quick_strings):
  identity = convert_to_identifier(script[0])
  block = script[1]
  if isinstance(block, list):
    file.write("%s -1\n" % identity)
  else:
    file.write("%s %f\n" % (identity, script[1]))
    block = script[2]
  save_statement_block(file, identity, 0, block, variables, variable_uses, [], quick_strings)
  file.write("\n")


class ScriptProcessor(ModuleProcessor):
  id_prefix = "script_"
  id_name = "scripts.py"
  export_name = "scripts.txt"

  def after_open_export_file(self):
    self.export_file.write("scriptsfile version 1\n")
    self.export_file.write("%d\n" % len(scripts))

  def write_export_file(self, script, variables, variable_uses, quick_strings):
    save_script(self.export_file, script, variables, variable_uses, quick_strings)


def process_scripts():
  print("Exporting scripts...")
  quick_strings = load_quick_strings()
  variables, variable_uses = load_variables()

  processor = ScriptProcessor()
  for index, script in enumerate(scripts):
    processor.write(script, index, variables, variable_uses, quick_strings)
  processor.close()

  save_quick_strings(quick_strings)
  save_variables(variables, variable_uses)
