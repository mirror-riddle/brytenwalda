from modules.info import export_dir
from modules.game_menus import game_menus
from operations import save_statement_block
from common import (
  lf_open, load_variables, save_variables, 
  load_quick_strings, save_quick_strings
)


def save_game_menu_item(ofile, variable_list, variable_uses, menu_item, quick_strings):
    ofile.write(" mno_%s " % (menu_item[0]))
    save_statement_block(ofile, 0, 1, menu_item[1], variable_list, variable_uses, [], quick_strings)
    ofile.write(" %s " % (menu_item[2].replace(" ", "_")))
    save_statement_block(ofile, 0, 1, menu_item[3], variable_list, variable_uses, [], quick_strings)
    door_name = "."
    if (len(menu_item) > 4):
        door_name = menu_item[4]
    ofile.write(" %s " % (door_name.replace(" ", "_")))


def save_game_menus(variable_list, variable_uses, quick_strings):
    ofile = open(export_dir + "menus.txt", "w")
    ofile.write("menusfile version 1\n")
    ofile.write(" %d\n" % (len(game_menus)))
    for game_menu in game_menus:
        ofile.write("menu_%s %d %s %s" % (game_menu[0], game_menu[1], game_menu[2].replace(" ", "_"), game_menu[3]))
        save_statement_block(ofile, 0, 1, game_menu[4], variable_list, variable_uses, [], quick_strings)
        menu_items = game_menu[5]
        ofile.write("%d\n" % (len(menu_items)))
        for menu_item in menu_items:
            save_game_menu_item(ofile, variable_list, variable_uses, menu_item, quick_strings)
        ofile.write("\n")
    ofile.close()


def save_python_header():
    ofile = lf_open("../ids/menus.py", "w")
    for i_game_menu in range(len(game_menus)):
        ofile.write("menu_%s = %d\n" % (game_menus[i_game_menu][0], i_game_menu))
    ofile.close()


def process_game_menus():
    print("Exporting game menus data...")
    save_python_header()
    quick_strings = load_quick_strings()
    variables, variable_uses = load_variables()
    
    save_game_menus(variables, variable_uses, quick_strings)
    
    save_quick_strings(quick_strings)
    save_variables(variables, variable_uses)
