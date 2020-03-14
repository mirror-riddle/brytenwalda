from modules.game_menus import game_menus
from operations import save_statement_block
from module_processor import ModuleProcessor
from common import replace_spaces


def save_game_menu_item(ofile, menu_item):
  ofile.write(" mno_%s " % (menu_item[0]))
  save_statement_block(ofile, 0, 1, menu_item[1])
  ofile.write(" %s " % (menu_item[2].replace(" ", "_")))
  save_statement_block(ofile, 0, 1, menu_item[3])
  door_name = "."
  if (len(menu_item) > 4):
    door_name = menu_item[4]
  ofile.write(" %s " % (door_name.replace(" ", "_")))


def save_game_menu(ofile, game_menu):
  ofile.write("menu_%s %d %s %s" % (
    game_menu[0], game_menu[1], replace_spaces(game_menu[2]), game_menu[3])
  )
  save_statement_block(ofile, 0, 1, game_menu[4])
  menu_items = game_menu[5]
  ofile.write("%d\n" % (len(menu_items)))
  for menu_item in menu_items:
    save_game_menu_item(ofile, menu_item)
  ofile.write("\n")


class GameMenuProcessor(ModuleProcessor):
  id_prefix = "menu_"
  id_name = "menus.py"
  export_name = "menus.txt"

  def after_open_export_file(self):
    self.export_file.write("menusfile version 1\n")
    self.export_file.write(" %d\n" % len(game_menus))

  def write_export_file(self, game_menu):
    save_game_menu(self.export_file, game_menu)


def process_game_menus():
  print("exporting game menus...")
  processor = GameMenuProcessor()
  for index, game_menu in enumerate(game_menus):
    processor.write(game_menu, index)
  processor.close()