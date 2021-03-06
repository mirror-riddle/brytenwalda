from modules.triggers import triggers
from modules.dialogs import dialogs
from modules.simple_triggers import simple_triggers
from modules.presentations import presentations
from modules.variables import reserved_variables
from modules.scene_props import scene_props
from modules.game_menus import game_menus
from modules.scripts import scripts
from modules.mission_templates import mission_templates
from operations import compile_global_vars, add_variable
from global_variables import variables, variable_uses, quick_strings


def compile_all_global_vars():
  temp_list = []
  list_type = type(temp_list)
  for varb in reserved_variables:
    try:
      add_variable(varb, variables, variable_uses)
    except:
      print("Error in variable:")
      print(varb)

  for trigger in triggers:
    try:
      compile_global_vars(trigger[3], variables, variable_uses),
      compile_global_vars(trigger[4], variables, variable_uses),
    except:
      print("Error in trigger:")
      print(trigger)

  for scene_prop in scene_props:
    try:
      sp_triggers = scene_prop[4]
      for sp_trigger in sp_triggers:
        compile_global_vars(sp_trigger[1], variables, variable_uses)
    except:
      print("Error in scene prop:")
      print(scene_prop)

  for dialog in dialogs:
    try:
      compile_global_vars(dialog[2], variables, variable_uses),
      compile_global_vars(dialog[5], variables, variable_uses),
    except:
      print("Error in dialog line:")
      print(dialog)

  for game_menu in game_menus:
    try:
      compile_global_vars(game_menu[4], variables, variable_uses)
      menu_items = game_menu[5]
      for menu_item in menu_items:
        compile_global_vars(menu_item[1], variables, variable_uses)
        compile_global_vars(menu_item[3], variables, variable_uses)
    except:
      print("Error in game menu:")
      print(game_menu)

  for mission_template in mission_templates:
    try:
      mt_triggers = mission_template[5]
      for mt_trigger in mt_triggers:
        compile_global_vars(mt_trigger[3], variables, variable_uses)
        compile_global_vars(mt_trigger[4], variables, variable_uses)
    except:
      print("Error in mission template:")
      print(mission_template)

  for presentation in presentations:
    try:
      prsnt_triggers = presentation[3]
      for prsnt_trigger in prsnt_triggers:
        compile_global_vars(prsnt_trigger[1], variables, variable_uses)
    except:
      print("Error in presentation:")
      print(presentation)

  for i_script in range(len(scripts)):
    try:
      func = scripts[i_script]
      if (type(func[1]) == list_type):
        compile_global_vars(func[1], variables, variable_uses)
      else:
        compile_global_vars(func[2], variables, variable_uses)
    except:
      print("Error in script:")
      print(func)

  for simple_trigger in simple_triggers:
    try:
      compile_global_vars(simple_trigger[1], variables, variable_uses)
    except:
      print("Error in simple trigger:")
      print(simple_trigger)


def process_init():
  print("initializing...")
  compile_all_global_vars()
