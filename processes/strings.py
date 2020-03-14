from modules.strings import strings
from processes.common import convert_to_identifier, replace_spaces
from module_processor import ModuleProcessor


def save_string(file, string):
  identity = convert_to_identifier(string[0])
  content = replace_spaces(string[1])
  file.write("str_%s %s\n" % (identity, content))


class StringProcessor(ModuleProcessor):
  id_prefix = "str_"
  id_name = "strings.py"
  export_name = "strings.txt"

  def after_open_export_file(self):
    self.export_file.write("stringsfile version 1\n")
    self.export_file.write("%d\n" % len(strings))

  def write_export_file(self, string):
    save_string(self.export_file, string)


def process_strings():
  print("exporting strings...")
  processor = StringProcessor()
  for index, string in enumerate(strings):
    processor.write(string, index)
  processor.close()
