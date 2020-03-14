from modules.postfx import postfx_params
from module_processor import ModuleProcessor


def save_postfx(ofile, postfx_param):
  ofile.write("pfx_%s %d %d" % (postfx_param[0], postfx_param[1], postfx_param[2]))
  params_list1 = postfx_param[3]
  params_list2 = postfx_param[4]
  params_list3 = postfx_param[5]
  ofile.write("  %f %f %f %f" % (params_list1[0], params_list1[1], params_list1[2], params_list1[3]))
  ofile.write("  %f %f %f %f" % (params_list2[0], params_list2[1], params_list2[2], params_list2[3]))
  ofile.write("  %f %f %f %f\n" % (params_list3[0], params_list3[1], params_list3[2], params_list3[3]))


class PostfxProcessor(ModuleProcessor):
  id_prefix = "pfx_"
  id_name = "postfx.py"
  export_name = "postfx_params.txt"

  def after_open_export_file(self):
    self.export_file.write("postfx_paramsfile version 1\n")
    self.export_file.write("%d\n" % len(postfx_params))

  def write_export_file(self, postfx):
    save_postfx(self.export_file, postfx)


def process_postfx():
  print("exporting postfx_params...")
  processor = PostfxProcessor()
  for index, postfx in enumerate(postfx_params):
    processor.write(postfx, index)
  processor.close()
