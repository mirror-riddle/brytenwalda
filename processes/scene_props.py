from headers.scene_props import get_spr_hit_points
from modules.scene_props import scene_props
from simple_triggers import save_simple_triggers
from module_processor import ModuleProcessor


def save_scene_prop(ofile, scene_prop):
  ofile.write("spr_%s %d %d %s %s " % (
      scene_prop[0], scene_prop[1],
      get_spr_hit_points(scene_prop[1]),
      scene_prop[2], scene_prop[3])
  )
  save_simple_triggers(ofile, scene_prop[4])


class ScenePropProcessor(ModuleProcessor):
  id_prefix = "spr_"
  id_name = "scene_props.py"
  export_name = "scene_props.txt"

  def after_open_export_file(self):
    self.export_file.write("scene_propsfile version 1\n")
    self.export_file.write(" %d\n" % len(scene_props))

  def write_export_file(self, scene_prop):
    save_scene_prop(self.export_file, scene_prop)


def process_scene_props():
  print("exporting scene props...")
  processor = ScenePropProcessor()
  for index, scene_prop in enumerate(scene_props):
    processor.write(scene_prop, index)
  processor.close()
