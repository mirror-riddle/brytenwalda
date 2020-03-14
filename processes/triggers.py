from modules.triggers import triggers
from operations import save_statement_block
from module_processor import ModuleProcessor


def save_trigger(file, trigger):
  file.write("%f %f %f " % (trigger[0], trigger[1], trigger[2]))
  for block in (trigger[3], trigger[4]):
    save_statement_block(file, 0, 1, block)
  file.write("\n")


class TriggerProcessor(ModuleProcessor):
  clean_ids_file = True
  export_name = "triggers.txt"

  def after_open_export_file(self):
    self.export_file.write("triggersfile version 1\n")
    self.export_file.write("%d\n" % len(triggers))

  def write_id_file(self, tigger, index):
    pass

  def write_export_file(self, trigger):
    save_trigger(self.export_file, trigger)


def process_triggers():
  print("exporting triggers...")
  processor = TriggerProcessor()
  for index, trigger in enumerate(triggers):
    processor.write(trigger, index)
  processor.close()
