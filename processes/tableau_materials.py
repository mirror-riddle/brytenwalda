from modules.info import export_dir
from modules.tableau_materials import tableaus
from operations import save_statement_block
from common import (
    load_variables, load_quick_strings,
    save_variables, save_quick_strings, lf_open
)
from module_processor import ModuleProcessor


def save_tableau_materials(ofile, tableau):
  tableau_info = (
      tableau[0],
      tableau[1],
      tableau[2],
      tableau[3],
      tableau[4],
      tableau[5],
      tableau[6],
      tableau[7],
      tableau[8]
  )
  ofile.write("tab_%s %d %s %d %d %d %d %d %d" % tableau_info)


class TableauMaterialProcessor(ModuleProcessor):
  id_prefix = "tableau_"
  id_name = "tableau_materials.py"
  export_name = "tableau_materials.txt"

  def after_open_export_file(self):
    self.export_file.write("%d\n" % len(tableaus))

  def write_export_file(self, tableau):
    save_tableau_materials(self.export_file, tableau)

  def save_statements(self, tableau, variables, variable_uses, quick_strings):
    save_statement_block(self.export_file, 0, 1, tableau[9], variables, variable_uses, [], quick_strings)
    self.export_file.write("\n")


def process_tableau_materials():
  print("Exporting tableau materials data...")
  quick_strings = load_quick_strings()
  variables, variable_uses = load_variables()

  processor = TableauMaterialProcessor()
  for index, tableau in enumerate(tableaus):
    processor.write(tableau, index)
    processor.save_statements(tableau, variables, variable_uses, quick_strings)
  processor.close()

  save_quick_strings(quick_strings)
  save_variables(variables, variable_uses)
