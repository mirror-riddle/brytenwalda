from modules.skills import skills
from processes.common import replace_spaces
from module_processor import ModuleProcessor


def save_skill(file, skill):
  file.write("skl_%s %s " % (skill[0], replace_spaces(skill[1])))
  file.write("%d %d %s\n" % (skill[2], skill[3],replace_spaces(skill[4])))


class SkillProcessor(ModuleProcessor):
  id_prefix = "skl_"
  id_name = "skills.py"
  export_name = "skills.txt"

  def after_open_export_file(self):
    self.export_file.write("%d\n" % len(skills))

  def write_export_file(self, skill):
    save_skill(self.export_file, skill)


def process_skills():
  print("exporting skills...")
  processor = SkillProcessor()
  for index, skill in enumerate(skills):
    processor.write(skill, index)
  processor.close()