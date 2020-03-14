from modules.scenes import scenes
from modules.troops import troops, find_troop
from module_processor import ModuleProcessor
from common import convert_to_identifier, replace_spaces


def write_vec(ofile, vec):
  ofile.write(" %f %f %f " % vec)


def write_passage(ofile, scenes, passage):
  scene_no = 0
  found = 0
  while (not found) and (scene_no < len(scenes)):
    if (scenes[scene_no][0] == passage):
      found = 1
    else:
      scene_no += 1
  if (passage == "exit"):
    scene_no = 100000
  elif (passage == ""):
    scene_no = 0
  elif not found:
    print("Error passage not found:")
    print(passage)
  ofile.write(" %d " % scene_no)


def save_scene(ofile, scene):
  identity = convert_to_identifier(scene[0])
  name = replace_spaces(scene[0])
  ofile.write("scn_%s %s %d %s %s %f %f %f %f %f %s " % (
      identity, name, scene[1], scene[2], scene[3], scene[4][0],
      scene[4][1], scene[5][0], scene[5][1], scene[6], scene[7])
  )
  passages = scene[8]
  ofile.write("\n  %d " % len(passages))
  for passage in passages:
    write_passage(ofile, scenes, passage)
  chest_troops = scene[9]
  ofile.write("\n  %d " % len(chest_troops))
  for chest_troop in chest_troops:
    troop_no = find_troop(troops, chest_troop)
    if (troop_no < 0):
      print("Error unable to find chest-troop: " + chest_troop)
      troop_no = 0
    else:
      pass
    ofile.write(" %d " % troop_no)
  ofile.write("\n")
  if (len(scene) > 10):
    ofile.write(" %s " % scene[10])
  else:
    ofile.write(" 0 ")
  ofile.write("\n")


class SceneProcessor(ModuleProcessor):
  id_prefix = "scn_"
  id_name = "scenes.py"
  export_name = "scenes.txt"

  def after_open_export_file(self):
    self.export_file.write("scenesfile version 1\n")
    self.export_file.write(" %d\n" % len(scenes))

  def write_export_file(self, scene):
    save_scene(self.export_file, scene)


def process_scenes():
  print("exporting scenes...")
  processor = SceneProcessor()
  for index, scene in enumerate(scenes):
    processor.write(scene, index)
  processor.close()