import os
import sys

sys.path.append(os.curdir)

os.chdir('./processes')

from processes.init import process_init
from processes.global_variables import process_global_variables
from processes.strings import process_strings
from processes.skills import process_skills
from processes.music import process_musics
from processes.animations import process_animations
from processes.meshes import process_meshes
from processes.sounds import process_sounds
from processes.skins import process_skins
from processes.map_icons import process_map_icons
from processes.factions import process_factions
from processes.items import process_items
from processes.scenes import process_scenes
from processes.troops import process_troops
from processes.particle_sys import process_particle_sys
from processes.scene_props import process_scene_props
from processes.tableau_materials import process_tableau_materials
from processes.presentations import process_presentations
from processes.party_tmps import process_party_tmps
from processes.parties import process_parties
from processes.quests import process_quests
from processes.info_pages import process_info_pages
from processes.scripts import process_scripts
from processes.mission_tmps import process_mission_tmps
from processes.game_menus import process_game_menus
from processes.simple_triggers import process_simple_tiggers
from processes.dialogs import process_dialogs
from processes.global_variables_unused import process_global_variables_unused
from processes.postfx import process_postfx


process_functions = {
    # 'init': process_init,
    # 'global_variables': process_global_variables,
    'strings': process_strings,
    'skills': process_skills,
    'musics': process_musics,
    'animations': process_animations,
    'meshes': process_meshes,
    'sounds': process_sounds,
    'skins': process_skins,
    'map_icons': process_map_icons,
    'factions': process_factions,
    'items': process_items,
    'scenes': process_scenes,
    'troops': process_troops,
    'particle_sys': process_particle_sys,
    'scene_props': process_scene_props,
    'tableau_materials': process_tableau_materials,
    'presentations': process_presentations,
    'party_tmps': process_party_tmps,
    'parties': process_parties,
    'quests': process_quests,
    'info_pages': process_info_pages,
    'scripts': process_scripts,
    'mission_tmps': process_mission_tmps,
    'game_menus': process_game_menus,
    'simple_triggers': process_simple_tiggers,
    'dialogs': process_dialogs,
    'postfx': process_postfx
    # 'global_variables_unused': process_global_variables_unused,    

}

def process_all():
    process_start()
    
    process_strings()
    process_skills()
    process_musics()
    process_animations()
    process_meshes()
    process_sounds()
    process_skins()
    process_map_icons()
    process_factions()
    process_items()
    process_scenes()
    process_troops()
    process_particle_sys()
    process_scene_props()
    process_tableau_materials()
    process_presentations()
    process_party_tmps()
    process_parties()
    process_quests()
    process_info_pages()
    process_scripts()
    process_mission_tmps()
    process_game_menus()
    process_simple_tiggers()
    process_dialogs()
    process_postfx()
    
    process_end()


def process_start():
    print('Script processing starts now.')
    print('______________________________')

    process_init()
    process_global_variables()


def process_end():
    process_global_variables_unused()

    print('______________________________')
    print('Script processing has ended.')


def process_one(name):
    process_function = process_functions.get(name)
    if process_function:
        process_function()


def process_by_names(names):
    process_start()
    [process_one(name) for name in names]
    process_end()


if __name__ == '__main__':
    names = sys.argv[1:]
    
    if (len(names) == 0):
        process_all()
    else:
        process_by_names(names)