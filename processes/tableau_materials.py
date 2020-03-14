from modules.tableau_materials import tableaus
from module_processor import ModuleProcessor
from operations import save_statement_block


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
    save_statement_block(self.export_file, 0, 1, tableau[9])
    self.export_file.write("\n")


def process_tableau_materials():
  print("exporting tableau materials...")
  processor = TableauMaterialProcessor()
  for index, tableau in enumerate(tableaus):
    processor.write(tableau, index)
  processor.close()
