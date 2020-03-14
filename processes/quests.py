from headers.common import opmask_quest_index
from modules.quests import quests
from module_processor import ModuleProcessor
from common import replace_spaces


def save_quest(file, quest):
  file.write("qst_%s %s %d %s\n" % (
    quest[0], replace_spaces(quest[1]), quest[2], replace_spaces(quest[3]))
  )


class QuestProcessor(ModuleProcessor):
  id_prefix = "qst_"
  id_name = "quests.py"
  export_name = "quests.txt"
  qst_tags = []

  def after_open_export_file(self):
    self.export_file.write("questsfile version 1\n")
    self.export_file.write("%d\n" % len(quests))

  def write_export_file(self, quest):
    save_quest(self.export_file, quest)

  def save_qst_tag(self, quest, index):
    string = "qsttag_%s = %d\n" % (quest[0], opmask_quest_index | index)
    self.qst_tags.append(string)

  def write_qst_tags(self):
    string = "".join(self.qst_tags)
    self.id_file.write(string)

def process_quests():
  print("exporting quests...")
  processor = QuestProcessor()
  for index, quest in enumerate(quests):
    processor.write(quest, index)
    processor.save_qst_tag(quest, index)
  processor.write_qst_tags()
  processor.close()