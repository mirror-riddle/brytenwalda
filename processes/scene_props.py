from modules.info import export_dir
from modules.scene_props import *
from common import (
    lf_open, load_variables, save_variables,
    load_quick_strings, save_quick_strings
)
from operations import get_spr_hit_points, save_simple_triggers


def save_scene_props(variable_list, variable_uses, tag_uses, quick_strings):
  ofile = open(export_dir + "scene_props.txt", "w")
  ofile.write("scene_propsfile version 1\n")
  ofile.write(" %d\n" % (len(scene_props)))
  for scene_prop in scene_props:
    ofile.write("spr_%s %d %d %s %s " % (scene_prop[0], scene_prop[1],
                                         get_spr_hit_points(scene_prop[1]), scene_prop[2], scene_prop[3]))
    save_simple_triggers(ofile, scene_prop[4], variable_list, variable_uses, tag_uses, quick_strings)
    ofile.write("\n")
  ofile.close()


def save_python_header():
  file = lf_open("../ids/scene_props.py", "w")
  for i_scene_prop in range(len(scene_props)):
    file.write("spr_%s = %d\n" % (scene_props[i_scene_prop][0], i_scene_prop))
  file.close()


def process_scene_props():
  print("Exporting scene props...")
  save_python_header()
  quick_strings = load_quick_strings()
  variables, variable_uses = load_variables()

  save_scene_props(variables, variable_uses, [], quick_strings)

  save_quick_strings(quick_strings)
  save_variables(variables, variable_uses)
