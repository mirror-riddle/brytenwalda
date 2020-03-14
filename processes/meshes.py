from modules.meshes import meshes
from processes.common import replace_spaces
from module_processor import ModuleProcessor


def save_mesh(file, mesh):
  file.write("mesh_%s %d %s %f %f %f %f %f %f %f %f %f\n" % (
    mesh[0], mesh[1], replace_spaces(mesh[2]), mesh[3], mesh[4], 
    mesh[5], mesh[6], mesh[7], mesh[8], mesh[9], mesh[10], mesh[11])
  )


class MeshProcessor(ModuleProcessor):
  id_prefix = "mesh_"
  id_name = "meshes.py"
  export_name = "meshes.txt"

  def after_open_export_file(self):
    self.export_file.write("%d\n" % len(meshes))

  def write_export_file(self, mesh):
    save_mesh(self.export_file, mesh)

def process_meshes():
  print("exporting meshes...")
  processor = MeshProcessor()
  for index, mesh in enumerate(meshes):
    processor.write(mesh, index)
  processor.close()
