from modules.info import export_dir
from modules.map_icons import map_icons
from common import (
    lf_open, load_variables, save_variables,
    load_quick_strings, save_quick_strings
)
from operations import save_simple_triggers
from module_processor import ModuleProcessor


def save_map_icon(ofile, map_icon, variable_list, variable_uses, quick_strings):
  triggers = []
  if (len(map_icon) >= 8):
    ofile.write("%s %d %s %f %d %f %f %f " % (
        map_icon[0], map_icon[1], map_icon[2], map_icon[3], map_icon[4], map_icon[5], map_icon[6], map_icon[7]))
    if (len(map_icon) == 9):
      triggers = map_icon[8]
  else:
    ofile.write("%s %d %s %f %d 0 0 0 " % (map_icon[0], map_icon[1], map_icon[2], map_icon[3], map_icon[4]))
    if (len(map_icon) == 6):
      triggers = map_icon[5]
  save_simple_triggers(ofile, triggers, variable_list, variable_uses, [], quick_strings)
  ofile.write("\n")


class MapIconProcessor(ModuleProcessor):
  id_prefix = "icon_"
  id_name = "map_icons.py"
  export_name = "map_icons.txt"

  def after_open_export_file(self):
    self.export_file.write("map_icons_file version 1\n")
    self.export_file.write("%d\n" % len(map_icons))

  def write_export_file(self, map_icon, variables, variable_uses, quick_strings):
    save_map_icon(self.export_file, map_icon, variables, variable_uses, quick_strings)

def process_map_icons():
  print("Exporting map icons...")
  quick_strings = load_quick_strings()
  variables, variable_uses = load_variables()

  processor = MapIconProcessor()
  for index, map_icon in enumerate(map_icons):
    processor.write(map_icon, index, variables, variable_uses, quick_strings)
  processor.close()

  save_quick_strings(quick_strings)
  save_variables(variables, variable_uses)
