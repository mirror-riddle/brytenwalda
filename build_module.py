import os
import sys
import processes

sys.path.append(os.curdir)

os.chdir('./processes')

from processes.init import process_init
from processes.global_variables_unused import process_global_variables_unused
from processes.strings import process_strings
from processes.skills import process_skills
from processes.music import process_musics
from processes.animations import process_animations
from processes.meshes import process_meshes
from processes.sounds import process_sounds

process_init()
process_global_variables_unused()
process_strings()
process_skills()
process_musics()
process_animations()
process_meshes()
process_sounds()

import processes.skins
import processes.map_icons
import processes.factions
import processes.items
import processes.scenes
import processes.troops
import processes.particle_sys
import processes.scene_props
import processes.tableau_materials
import processes.presentations
import processes.party_tmps
import processes.parties
import processes.quests
import processes.info_pages
import processes.scripts
import processes.mission_tmps
import processes.game_menus
import processes.simple_triggers
import processes.dialogs
import processes.global_variables_unused
import processes.postfx
