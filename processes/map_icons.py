from modules.map_icons import map_icons
from simple_triggers import save_simple_triggers
from module_processor import ModuleProcessor


def save_map_icon(ofile, map_icon):
  triggers = []
  if (len(map_icon) >= 8):
    ofile.write("%s %d %s %f %d %f %f %f " % (
        map_icon[0], map_icon[1], map_icon[2], map_icon[3], 
        map_icon[4], map_icon[5], map_icon[6], map_icon[7])
    )
    if (len(map_icon) == 9):
      triggers = map_icon[8]
  else:
    ofile.write("%s %d %s %f %d 0 0 0 " % (map_icon[0], map_icon[1], map_icon[2], map_icon[3], map_icon[4]))
    if (len(map_icon) == 6):
      triggers = map_icon[5]
  save_simple_triggers(ofile, triggers)


class MapIconProcessor(ModuleProcessor):
  id_prefix = "icon_"
  id_name = "map_icons.py"
  export_name = "map_icons.txt"

  def after_open_export_file(self):
    self.export_file.write("map_icons_file version 1\n")
    self.export_file.write("%d\n" % len(map_icons))

  def write_export_file(self, map_icon):
    save_map_icon(self.export_file, map_icon)

def process_map_icons():
  print("exporting map icons...")
  processor = MapIconProcessor()
  for index, map_icon in enumerate(map_icons):
    processor.write(map_icon, index)
  processor.close()
