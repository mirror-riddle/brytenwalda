from modules.simple_triggers import simple_triggers
from operations import save_statement_block
from module_processor import ModuleProcessor


def save_simple_trigger(file, simple_trigger):
  file.write("%f " % (simple_trigger[0]))
  save_statement_block(file, 0, 1, simple_trigger[1])
  file.write("\n")


def save_simple_triggers(file, triggers):
  file.write("%d\n" % len(triggers))
  for trigger in triggers:
    save_simple_trigger(file, trigger)


class SimpleTriggerProcessor(ModuleProcessor):
  clean_ids_file = True
  export_name = "simple_triggers.txt"

  def after_open_export_file(self):
    self.export_file.write("simple_triggers_file version 1\n")
    self.export_file.write("%d\n" % len(simple_triggers))

  def write_export_file(self, simple_trigger):
    save_simple_trigger(self.export_file, simple_trigger)


def process_simple_tiggers():
  print("exporting simple triggers...")
  processor = SimpleTriggerProcessor()
  for index, simple_trigger in enumerate(simple_triggers):
    processor.write(simple_trigger, index)
  processor.close()
