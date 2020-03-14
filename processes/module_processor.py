import os
from modules.info import export_dir
from common import lf_open, convert_to_identifier


class ModuleProcessor():
  id_prefix = "id_"
  id_name = "ids.py"
  export_name = "export.txt"
  clean_ids_file = False

  def __init__(self):
    self.id_path = "../ids/" + self.id_name
    self.export_path = export_dir + self.export_name
    self.id_file = lf_open(self.id_path, "w")
    self.export_file = lf_open(self.export_path, "w")
    self.after_open()

  def after_open_id_file(self):
    pass

  def after_open_export_file(self):
    pass

  def after_open(self):
    self.after_open_id_file()
    self.after_open_export_file()

  def write_id_file(self, item, index):
    item_id = convert_to_identifier(item[0])
    self.id_file.write("%s%s = %d\n" % (self.id_prefix, item_id, index))

  def write_export_file(self, item, *extra_data):
    pass

  def write(self, item, index, *extra_data):
    self.write_id_file(item, index)
    self.write_export_file(item, *extra_data)

  def before_close_id_file(self):
    pass

  def before_close_export_file(self):
    pass

  def before_close(self):
    self.before_close_id_file()
    self.before_close_export_file()

  def close(self):
    self.before_close_id_file()
    self.before_close_export_file()
    self.id_file.close()
    self.export_file.close()
    if self.clean_ids_file:
      os.remove(self.id_path)
