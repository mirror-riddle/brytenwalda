from modules.info import export_dir
from modules.party_templates import party_templates
from common import convert_to_identifier, replace_spaces, lf_open
from module_processor import ModuleProcessor


def save_party_template_troop(file, troop):
  if troop:
    file.write("%d %d %d " % (troop[0], troop[1], troop[2]))
    if (len(troop) > 3):
      file.write("%d " % troop[3])
    else:
      file.write("0 ")
  else:
    file.write("-1 ")


def save_party_template(file, template):
  identity = convert_to_identifier(template[0])
  name = replace_spaces(template[1])
  file.write("pt_%s %s %d %d %d %d " %(
    identity, name, template[2], template[3], template[4], template[5]
  ))
  members = template[6]
  if (len(members) > 6):
    print("Error! NUMBER OF TEMPLATE MEMBERS EXCEEDS 6 " + template[0])
    members = members[0:6]
  for member in members:
    save_party_template_troop(file, member)
  for i in range(6 - len(members)):
    save_party_template_troop(file, 0)
  file.write("\n")


class PartyTemplateProcessor(ModuleProcessor):
  id_prefix = "pt_"
  id_name = "party_templates.py"
  export_name = "party_templates.txt"

  def after_open_export_file(self):
    self.export_file.write("partytemplatesfile version 1\n")
    self.export_file.write("%d\n" % len(party_templates))

  def write_export_file(self, patry_template):
    save_party_template(self.export_file, patry_template)


def process_party_tmps():
  print("Exporting party_templates...")
  processor = PartyTemplateProcessor()
  for index, party_template in enumerate(party_templates):
    processor.write(party_template, index)
  processor.close()