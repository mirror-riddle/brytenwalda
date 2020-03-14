from modules.info import export_dir
from modules.game_menus import game_menus
from operations import save_statement_block
from common import (
    lf_open, load_variables, save_variables, replace_spaces,
    load_quick_strings, save_quick_strings
)
from module_processor import ModuleProcessor


def save_game_menu_item(ofile, variable_list, variable_uses, menu_item, quick_strings):
  ofile.write(" mno_%s " % (menu_item[0]))
  save_statement_block(ofile, 0, 1, menu_item[1], variable_list, variable_uses, [], quick_strings)
  ofile.write(" %s " % (menu_item[2].replace(" ", "_")))
  save_statement_block(ofile, 0, 1, menu_item[3], variable_list, variable_uses, [], quick_strings)
  door_name = "."
  if (len(menu_item) > 4):
    door_name = menu_item[4]
  ofile.write(" %s " % (door_name.replace(" ", "_")))


def save_game_menu(ofile, game_menu, variable_list, variable_uses, quick_strings):
  ofile.write("menu_%s %d %s %s" % (game_menu[0], game_menu[1], replace_spaces(game_menu[2]), game_menu[3]))
  save_statement_block(ofile, 0, 1, game_menu[4], variable_list, variable_uses, [], quick_strings)
  menu_items = game_menu[5]
  ofile.write("%d\n" % (len(menu_items)))
  for menu_item in menu_items:
    save_game_menu_item(ofile, variable_list, variable_uses, menu_item, quick_strings)
  ofile.write("\n")


class GameMenuProcessor(ModuleProcessor):
  id_prefix = "menu_"
  id_name = "menus.py"
  export_name = "menus.txt"

  def after_open_export_file(self):
    self.export_file.write("menusfile version 1\n")
    self.export_file.write(" %d\n" % len(game_menus))

  def write_export_file(self, game_menu, variables, variable_uses, quick_strings):
    save_game_menu(self.export_file, game_menu, variables, variable_uses, quick_strings)


def process_game_menus():
  print("Exporting game menus...")
  quick_strings = load_quick_strings()
  variables, variable_uses = load_variables()

  processor = GameMenuProcessor()
  for index, game_menu in enumerate(game_menus):
    processor.write(game_menu, index, variables, variable_uses, quick_strings)
  processor.close()

  save_quick_strings(quick_strings)
  save_variables(variables, variable_uses)
