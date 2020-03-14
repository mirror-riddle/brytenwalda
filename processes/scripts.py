from modules.scripts import scripts
from operations import save_statement_block
from module_processor import ModuleProcessor
from common import convert_to_identifier


def save_script(file, script):
  identity = convert_to_identifier(script[0])
  block = script[1]
  if isinstance(block, list):
    file.write("%s -1\n" % identity)
  else:
    file.write("%s %f\n" % (identity, script[1]))
    block = script[2]
  save_statement_block(file, identity, 0, block)
  file.write("\n")


class ScriptProcessor(ModuleProcessor):
  id_prefix = "script_"
  id_name = "scripts.py"
  export_name = "scripts.txt"

  def after_open_export_file(self):
    self.export_file.write("scriptsfile version 1\n")
    self.export_file.write("%d\n" % len(scripts))

  def write_export_file(self, script):
    save_script(self.export_file, script)


def process_scripts():
  print("exporting scripts...")
  processor = ScriptProcessor()
  for index, script in enumerate(scripts):
    processor.write(script, index)
  processor.close()