from modules.presentations import presentations
from simple_triggers import save_simple_triggers
from module_processor import ModuleProcessor


def save_presentation(ofile, presentation):
  ofile.write("prsnt_%s %d %d " % (presentation[0], presentation[1], presentation[2]))
  save_simple_triggers(ofile, presentation[3])


class PresentationProcessor(ModuleProcessor):
  id_prefix = "prsnt_"
  id_name = "presentations.py"
  export_name = "presentations.txt"

  def after_open_export_file(self):
    self.export_file.write("presentationsfile version 1\n")
    self.export_file.write(" %d\n" % len(presentations))

  def write_export_file(self, presentation):
    save_presentation(self.export_file, presentation)


def process_presentations():
  print("exporting presentations...")
  processor = PresentationProcessor()
  for index, presentation in enumerate(presentations):
    processor.write(presentation, index)
  processor.close()
