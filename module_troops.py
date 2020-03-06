import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below...
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  #  r = 10 + int(x / 10)
  #  n |= wp_one_handed(x + random.randrange(r))
  #  n |= wp_two_handed(x + random.randrange(r))
  #  n |= wp_polearm(x + random.randrange(r))
  #  n |= wp_archery(x + random.randrange(r))
  #  n |= wp_crossbow(x + random.randrange(r))
  #  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x) #chief quita para hacerlo especifico
  n |= wp_crossbow(x) #chief quita para hacerlo especifico
  n |= wp_throwing(x)
  n |= wp_firearm(x) #chief anade para hondas
  return n

def wpe(m,a,c,t):
  n = 0
  n |= wp_one_handed(m)
  n |= wp_two_handed(m)
  n |= wp_polearm(m)
  n |= wp_archery(a)
  n |= wp_crossbow(c)
  n |= wp_throwing(t)
  return n

def wpex(o,w,p,a,c,t):
  n = 0
  n |= wp_one_handed(o)
  n |= wp_two_handed(w)
  n |= wp_polearm(p)
  n |= wp_archery(a)
  n |= wp_crossbow(c)
  n |= wp_throwing(t)
  return n

def wp_melee(x):
  n = 0
  #  r = 10 + int(x / 10)
  #  n |= wp_one_handed(x + random.randrange(r))
  #  n |= wp_two_handed(x + random.randrange(r))
  #  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

#Skills cambios chief
knows_common = knows_weapon_master_3|knows_ironflesh_1|knows_athletics_3|knows_riding_3|knows_power_strike_3|knows_shield_2|knows_inventory_management_1|knows_power_throw_4 #cambiado chief
#Warrior
def_attrib = str_16 | agi_9 | int_6 | cha_8
def_attrib2 = str_22 | agi_14 | int_8 | cha_10
def_attrib3 = str_30 | agi_20 | int_12 | cha_14
def_attrib_multiplayer = str_14 | agi_14 | int_9 | cha_9

#Ranged
basic_ranged_attrib = str_10|agi_16|int_8|cha_7
veteran_ranged_attrib = str_17|agi_22|int_8|cha_7
elite_ranged_attrib = str_24|agi_30|int_12|cha_10

knows_lord_1 = knows_riding_6|knows_trade_2|knows_inventory_management_2|knows_tactics_6|knows_prisoner_management_5|knows_shield_3|knows_leadership_9 #cambiado chief

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_5|knows_power_strike_2|knows_riding_1|knows_shield_2|knows_inventory_management_2 #cambiado chief
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

knows_warrior_basic = knows_weapon_master_3|knows_ironflesh_4|knows_athletics_6|knows_riding_3|knows_power_strike_1|knows_shield_2|knows_inventory_management_1|knows_power_throw_2 #cambiado chief
knows_warrior_normal = knows_weapon_master_5|knows_ironflesh_5|knows_athletics_6|knows_riding_4|knows_power_strike_2|knows_shield_2|knows_inventory_management_2|knows_power_throw_3 #cambiado chief
knows_warrior_veteran = knows_weapon_master_7|knows_ironflesh_7|knows_athletics_6|knows_riding_7|knows_power_strike_3|knows_shield_3|knows_inventory_management_3|knows_power_throw_4 #cambiado chief
knows_warrior_elite = knows_weapon_master_9|knows_ironflesh_9|knows_athletics_6|knows_riding_9|knows_power_strike_3|knows_shield_3|knows_inventory_management_4|knows_power_throw_5 #cambiado chief

knows_cleric = knows_athletics_1|knows_trade_2|knows_wound_treatment_4|knows_first_aid_4|knows_surgery_4

lord_attrib = str_23|agi_19|int_18|cha_22|level(32) #cambiado chief
#cambiado chief
knight_attrib_1 = str_26|agi_26|int_17|cha_20|level(34)
knight_attrib_2 = str_27|agi_27|int_19|cha_22|level(38)
knight_attrib_3 = str_28|agi_28|int_23|cha_24|level(42)
knight_attrib_4 = str_29|agi_29|int_26|cha_26|level(46)
knight_attrib_5 = str_30|agi_30|int_30|cha_30|level(52)
knight_skills_1 = knows_weapon_master_7|knows_riding_5|knows_ironflesh_8|knows_power_strike_8|knows_athletics_6|knows_shield_3|knows_tactics_7|knows_prisoner_management_7|knows_leadership_7|knows_wound_treatment_8|knows_first_aid_8|knows_surgery_8|knows_power_throw_5
knight_skills_2 = knows_weapon_master_8|knows_riding_6|knows_ironflesh_9|knows_power_strike_9|knows_athletics_6|knows_shield_3|knows_tactics_8|knows_prisoner_management_8|knows_leadership_8|knows_wound_treatment_8|knows_first_aid_8|knows_surgery_8|knows_power_throw_5
knight_skills_3 = knows_weapon_master_8|knows_riding_7|knows_ironflesh_9|knows_power_strike_9|knows_athletics_6|knows_shield_3|knows_tactics_8|knows_prisoner_management_8|knows_leadership_9|knows_wound_treatment_8|knows_first_aid_8|knows_surgery_8|knows_power_throw_5
knight_skills_4 = knows_weapon_master_9|knows_riding_8|knows_ironflesh_10|knows_power_strike_10|knows_athletics_6|knows_shield_3|knows_tactics_9|knows_prisoner_management_9|knows_leadership_9|knows_wound_treatment_8|knows_first_aid_8|knows_surgery_8|knows_power_throw_5
knight_skills_5 = knows_weapon_master_10|knows_riding_9|knows_ironflesh_10|knows_power_strike_10|knows_athletics_6|knows_shield_3|knows_tactics_10|knows_prisoner_management_9|knows_leadership_10|knows_wound_treatment_9|knows_first_aid_8|knows_surgery_8|knows_power_throw_5
#cambiado chief end
#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0
#chief cambia caras nemchenk
swadian_face_younger_1 = 0x0000000000002001355335371861249200000000001c96520000000000000000
swadian_face_young_1   = 0x00000004400023c1355335371861249200000000001c96520000000000000000
swadian_face_middle_1  = 0x00000008000023c1355335371861249200000000001c96520000000000000000
swadian_face_old_1     = 0x0000000e000023c0355335371861249200000000001c96520000000000000000
swadian_face_older_1   = 0x0000000fc00023c0355335371861249200000000001c96520000000000000000

swadian_face_younger_2 = 0x000000003a0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_young_2   = 0x000000033a0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_middle_2  = 0x00000007ba0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_old_2     = 0x0000000e3b0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_older_2   = 0x0000000ffa0045c549fddefdffffffff00000000001e6db60000000000000000
#cambias caras britones termina y empieza jutos
vaegir_face_younger_1 = 0x000000000008234958d1b515664a5aa200000000001f49510000000000000000
vaegir_face_young_1   = 0x000000030008234958d1b515664a5aa200000000001f49510000000000000000
vaegir_face_middle_1  = 0x000000080008234958d1b515664a5aa200000000001f49510000000000000000
vaegir_face_old_1     = 0x0000000dc008234958d1b515664a5aa200000000001f49510000000000000000
vaegir_face_older_1   = 0x0000000fc008234958d1b515664a5aa200000000001f49510000000000000000

vaegir_face_younger_2 = 0x00000000001002c7471d312321b14a9c00000000001ebae90000000000000000
vaegir_face_young_2   = 0x00000002801002c7471d312321b14a9c00000000001ebae90000000000000000
vaegir_face_middle_2  = 0x00000009001002c7471d312321b14a9c00000000001ebae90000000000000000
vaegir_face_old_2     = 0x0000000ec01002c7471d312321b14a9c00000000001ebae90000000000000000
vaegir_face_older_2   = 0x0000000fc01002c7471d312321b14a9c00000000001ebae90000000000000000
#chief cambio jutos y empieza pictos
khergit_face_younger_1 = 0x000000018000d00736db6db6db6db6db00000000001db6db0000000000000000
khergit_face_young_1   = 0x00000005ad00d10736db6db6db6db6db00000000001db6db0000000000000000
khergit_face_middle_1  = 0x0000000a7c00d34736db6db6db6db6db00000000001db6db0000000000000000
khergit_face_old_1     = 0x0000000d1d00d1c736db6db6db6db6db00000000001db6db0000000000000000
khergit_face_older_1   = 0x0000000fff00d1c736db6db6db6db6db00000000001db6db0000000000000000

khergit_face_younger_2 = 0x000000003f0cc00a0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_young_2   = 0x00000002bf0cc00a0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_middle_2  = 0x00000008bf0cc00a0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_old_2     = 0x0000000cbf0cc00a0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_older_4   = 0x0000000fff0cc00a0ed1b6adbbadb91200000000001eb8d80000000000000000

khergit_face_younger_3 = 0x00000001bf0ca00a0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_young_3   = 0x000000067f0ca00a0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_middle_3  = 0x000000087f0ca0470ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_old_3     = 0x0000000c3f0ca3130ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_older_3   = 0x0000000fff0ca3130ed1b6adbbadb91200000000001eb8d80000000000000000

khergit_face_younger_4 = 0x000000003f0c814f0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_young_4   = 0x000000027e0c808f0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_middle_4  = 0x00000006be0c810a0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_old_4     = 0x0000000c3f0c82ca0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_older_4   = 0x0000000fff0c82ca0ed1b6adbbadb91200000000001eb8d80000000000000000
#chief cambio acaba
nord_face_younger_1 = 0x000000000000014104c200928801249200000000001d24100000000000000000
nord_face_young_1   = 0x000000044000014104c200928801249200000000001d24100000000000000000
nord_face_middle_1  = 0x000000084000014104c200928801249200000000001d24100000000000000000
nord_face_old_1     = 0x0000000e0000014104c200928801249200000000001d24100000000000000000
nord_face_older_1   = 0x0000000e0000014004c200928801249200000000001d24100000000000000000

nord_face_younger_2 = 0x000000002b00218a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_young_2   = 0x000000036b00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_middle_2  = 0x00000007eb00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_old_2     = 0x0000000deb00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_older_2   = 0x0000000feb0023465bfcbdbb67b7ff7f00000000001eeb6f0000000000000000

rhodok_face_younger_1 = 0x0000000000003144355355370861008200000000001c96520000000000000000
rhodok_face_young_1   = 0x0000000500003141355355370861008200000000001c96520000000000000000
rhodok_face_middle_1  = 0x0000000840003141355355370861008200000000001c96520000000000000000
rhodok_face_old_1     = 0x0000000dc0003192355355370861008200000000001c96520000000000000000
rhodok_face_older_1   = 0x0000000fc0003192355355370861008200000000001c96520000000000000000

rhodok_face_younger_2 = 0x000000003e0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_young_2   = 0x000000037e0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_middle_2  = 0x000000083e0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_old_2     = 0x0000000dfe0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_older_2   = 0x0000000ffe0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
#chief cambia
man_face_younger_1 = 0x000000003f0c1280478b74ca9a6ecd5c00000000001d39120000000000000000
man_face_young_1   = 0x000000033f0c1281478b74ca9a6ecd5c00000000001d39120000000000000000
man_face_middle_1  = 0x0000000cff0c1281478b74ca9a6ecd5c00000000001d39120000000000000000
man_face_old_1     = 0x0000000fff0c1281478b74ca9a6ecd5c00000000001d39120000000000000000
man_face_older_1   = 0x0000000fff0c1292478b74ca9a6ecd5c00000000001d39120000000000000000

man_face_younger_2 = 0x000000002c045184475aa2a4c9bc48a800000000001dca250000000000000000
man_face_young_2   = 0x000000046c045184475aa2a4c9bc48a800000000001dca250000000000000000
man_face_middle_2  = 0x0000000e6c045184475aa2a4c9bc48a800000000001dca250000000000000000
man_face_old_2     = 0x0000000fec045184475aa2a4c9bc48a800000000001dca250000000000000000
man_face_older_2   = 0x0000000fec0451c0475aa2a4c9bc48a800000000001dca250000000000000000

bandit_face_younger_1 = 0x00000000391071443a5d4e491a136b0d00000000001e99140000000000000000
bandit_face_young_1   = 0x00000005f91071443a5d4e491a136b0d00000000001e99140000000000000000
bandit_face_middle_1  = 0x0000000d391071443a5d4e491a136b0d00000000001e99140000000000000000
bandit_face_old_1     = 0x0000000ff91071443a5d4e491a136b0d00000000001e99140000000000000000
bandit_face_older_1   = 0x0000000ff91071853a5d4e491a136b0d00000000001e99140000000000000000

bandit_face_younger_2 = 0x0000000016089111316b361aaf74e41d00000000001e469a0000000000000000
bandit_face_young_2   = 0x00000004d6089111316b361aaf74e41d00000000001e469a0000000000000000
bandit_face_middle_2  = 0x0000000b96089111316b361aaf74e41d00000000001e469a0000000000000000
bandit_face_old_2     = 0x0000000fd608a111316b361aaf74e41d00000000001e469a0000000000000000
bandit_face_older_2   = 0x0000000fd6089100316b361aaf74e41d00000000001e469a0000000000000000
#chief bandidos acaba
#quastuosa chief empieza
quastuosa_woman_face_1 = 0x0000000199041002736b7b6b14cab89b00000000001a390d0000000000000000
quastuosa_woman_face_2 = 0x00000001ae10500129a5aeb52b3a186300000000001d44dc0000000000000000
quastuosa_woman_face_3 = 0x000000018010800116ee82411c98cc6300000000001d169c0000000000000000
quastuosa_woman_face_4 = 0x0000000182007003689d8cb92a70c69b00000000001ca85a0000000000000000
quastuosa_woman_face_5 = 0x000000048000900624ddb1d75b7d653400000000001e6b1a0000000000000000
quastuosa_woman_face_6 = 0x0000000480000005450b0f48dd2568d600000000001deb740000000000000000
#quastuosa termina
#chief caras de sacerdotes batalla
sac_face_younger_1 = 0x000000003100000e478b8a27137238ec00000000001e651c0000000000000000
sac_face_young_1   = 0x000000023100000e478b8a27137238ec00000000001e651c0000000000000000
sac_face_middle_1  = 0x000000043100000e478b8a27137238ec00000000001e651c0000000000000000
sac_face_old_1     = 0x0000000e3100000e478b8a27137238ec00000000001e651c0000000000000000
sac_face_older_1   = 0x0000000ff100000e478b8a27137238ec00000000001e651c0000000000000000

sac_face_younger_2 = 0x000000000208e5d2485d71cb1b7346db00000000001da72d0000000000000000
sac_face_young_2   = 0x000000030208e5d2485d71cb1b7346db00000000001da72d0000000000000000
sac_face_middle_2  = 0x000000090208e5d2485d71cb1b7346db00000000001da72d0000000000000000
sac_face_old_2     = 0x0000000e4208e5d2485d71cb1b7346db00000000001da72d0000000000000000
sac_face_older_2   = 0x0000000fc208e5d2485d71cb1b7346db00000000001da72d0000000000000000


sac_face_1    = sac_face_younger_1
sac_face_2    = sac_face_older_2
#chief sacerdotes acaba
merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

#chief ampliado
khergit_woman_face_1 = 0x000000026d10c0011854c9ed2c79345100000000001ec9f50000000000000000
khergit_woman_face_2 = 0x000000003900c00448d5aa6c5235591400000000001ed88c0000000000000000
khergit_woman_face_3 = 0x000000097f08e0013b996ddc93cd58df00000000001eaa630000000000000000
khergit_woman_face_4 = 0x000000095c0cf0053a646ae69b31c4b200000000001eab240000000000000000
khergit_woman_face_5 = 0x0000000fed1020011854c9ed2c79345100000000001ec9f50000000000000000
khergit_woman_face_6 = 0x0000000fcc08b00152da31d4997638f600000000001cb7210000000000000000
#chief ampliado

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2
#cambiados chief bandidos
bandit_face1  = bandit_face_young_1
bandit_face2  = bandit_face_older_2
#cambiados chief bandidos acaba
undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield


troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [],
   str_4|agi_4|int_4|cha_4,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_leather_jerkin, itm_ankle_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_leather_jerkin, itm_ankle_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
  ##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

   ####################################################################################################################
  # Troops before this point are hardwired into the game and their order should not be changed!
  ####################################################################################################################
  ["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_club,itm_leather_jerkin,itm_ankle_boots], #cambiado chief
   str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
  ["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_tutorial_short_bow,itm_tutorial_arrows,itm_linen_tunic,itm_ankle_boots], #cambiado chief
   str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
  ["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_sword,itm_leather_jerkin,itm_ankle_boots], #cambiado chief
   str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
    [itm_ankle_boots], #cambiado chief
    str_6|agi_6|level(15),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_ankle_boots],
   str_12|agi_12|level(23),wp(170),knows_warrior_normal|knows_riding_1|knows_shield_2,mercenary_face_1, mercenary_face_2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,
   [itm_ankle_boots],
   str_14|agi_14|level(29),wp(240),knows_warrior_veteran|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_ankle_boots],
   str_18|agi_18|level(35),wp(270),knows_warrior_elite|knows_ironflesh_5|knows_power_strike_5|knows_athletics_5|knows_riding_3|knows_shield_4,mercenary_face_1, mercenary_face_2],
  #cambios jik chief end
   ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
    [itm_ankle_boots],
    str_7|agi_6|level(15),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_ankle_boots],
   str_8|agi_6|level(17),wp(120),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_ankle_boots],
   str_12|agi_12|level(23),wp(170),knows_warrior_normal|knows_riding_1|knows_shield_2,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_ankle_boots],
   str_12|agi_12|level(23),wp(170),knows_warrior_normal|knows_riding_1|knows_shield_2,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_ankle_boots],
   str_12|agi_12|level(23),wp(170),knows_warrior_normal|knows_riding_1|knows_shield_2,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_ankle_boots],
   str_14|agi_14|level(27),wp(230),knows_warrior_veteran|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_ankle_boots],
   str_14|agi_14|level(27),wp(230),knows_warrior_veteran|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_ankle_boots],
   str_14|agi_14|level(27),wp(230),knows_warrior_veteran|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_ankle_boots],
   str_18|agi_18|level(33),wp(270),knows_warrior_elite|knows_ironflesh_5|knows_power_strike_5|knows_athletics_5|knows_riding_3|knows_shield_4,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_ankle_boots],
   str_18|agi_18|level(33),wp(270),knows_warrior_elite|knows_ironflesh_5|knows_power_strike_5|knows_athletics_5|knows_riding_3|knows_shield_4,mercenary_face_1, mercenary_face_2],
  #cambios chief end
  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],

#soldiers:
  #This troop is the troop marked as soldiers_begin
  [
    "farmer","Farmer (Lig. I.)","Farmers",
    tf_guarantee_boots|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
    [
      itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,
      itm_pitch_fork,itm_cudgel,itm_battle_fork,itm_staff,itm_quarter_staff,itm_sickle,
      itm_carbatinae_2_bare,itm_carbatinae_1_bare,itm_ankle_boots,
      itm_woolen_cap_newgrn,itm_woolen_cap_newwht,itm_woolen_cap,
      itm_shirt,itm_roman_shirt,itm_bl_tunicsr02,itm_shirtb,itm_shirtd,itm_shirte,
    ],
    def_attrib|level(15),wp(110),knows_common,man_face_middle_1, man_face_old_2
  ],

  ##JIK chief - new troop entry
   [
     "cantaber_iuventus","Cantaber Iuventus","Cantaber Iuventi",
     tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
     [
       itm_javelin,itm_spear_2,itm_spatha,itm_hunting_dagger,
       itm_turret_hat_blue,itm_turret_hat_green,itm_bare_legs_blue,itm_carbatinae_2_bare,
       itm_roman_shirt,itm_shirtc,itm_shirtd,itm_shirte,itm_khergit_elite_armor,itm_hauberk6,itm_mail_shirt_a_copy,
       itm_rathos_spangenhelm_a,itm_bowl_helmet,itm_norman_helmet,itm_leather_cap,
       itm_cantabro_shield_1,itm_cantabro_shield_2,itm_cantabro_shield_3,itm_cantabro_shield_4,itm_cantabro_shield_5,
       itm_cantabro_shield_6,itm_cantabro_shield_7,itm_cantabro_shield_8,itm_cantabro_shield_9,itm_cantabro_shield_10
     ],
     def_attrib3|level(32),wp(260),knows_warrior_elite,mercenary_face_1, mercenary_face_2
   ], #chief cambiado

   [
     "townsman","Townsman (Lig. I.)","Townsmen",
     tf_guarantee_boots,no_scene,reserved,fac_commoners,
     [
       itm_knife,itm_cudgel,itm_hatchet,
       itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,itm_stones,
       itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
       itm_woolen_cap_newblu,itm_woolen_cap_newred,itm_woolen_cap_newblk,
       itm_shirt,itm_roman_shirt,itm_bl_tunicsr01_2,itm_bl_tunicsr01,itm_shirtb,itm_shirtc,itm_fat_body
     ],
     def_attrib|level(15),wp(110),knows_common,mercenary_face_1, mercenary_face_2
   ],

   [
     "watchman","Watchman (Lig. I.)","Watchmen",
     tf_guarantee_boots,no_scene,reserved,fac_commoners,
     [
       itm_spiked_club,itm_boar_spear,itm_hand_axe,itm_talak_seax,
       itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
       itm_ankle_boots,itm_wrapping_boots,itm_woolen_cap_newred,
       itm_woolen_cap_newgrn,itm_woolen_cap_newwht,itm_woolen_cap,
       itm_shirtb,itm_shirtc,itm_shirtd,itm_shirte,itm_green_tunic,itm_red_tunic,itm_blue_tunic,
       itm_buckler28,itm_buckler16,itm_buckler15
     ],
     def_attrib2|level(19),wp(140),knows_warrior_basic,mercenary_face_1, mercenary_face_2
   ],

#tempered chief anadido
   [
     "shepherd","Shepherd (Lig. I.)","Shepherds",
     tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
     [
       itm_shepherds_crook,itm_knife,itm_staff,
       itm_sniper_crossbow,itm_flintlock_pistol,itm_flintlock_pistol_militar,
       itm_mule,itm_donkey_mount,itm_bare_legs_blue,itm_carbatinae_2_bare,
       itm_carbatinae_1_bare,itm_woolen_cap_newwht,itm_woolen_cap,
       itm_shirt,itm_roman_shirt,itm_shirtb,itm_shirtc,itm_shirtd,itm_shirte,
     ],
     def_attrib|level(15),wp(110),knows_common|knows_pathfinding_1|knows_tracking_1,man_face_middle_1, man_face_old_2
   ],

#tempered chief acaba
   [
     "caravan_guard","Caravan Guard (Med. I.)","Caravan Guards",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,0,fac_commoners,
     [
       itm_spear_3,itm_hand_axe,itm_talak_seax,
       itm_javelin,itm_javelin,itm_javelin,itm_javelin,
       itm_carbatinae_2_green,itm_carbatinae_1_blue,itm_carbatinae_2_grey,
       itm_black_cloak,itm_piel_coat01,itm_piel_coat02,itm_white_cloak_hood,itm_white_cloak,
       itm_armor_8,itm_armor_9,itm_linen_tunic,itm_green_tunic,itm_red_tunic,itm_blue_tunic,
       itm_leathershield_small_b,itm_woodenshield_small,itm_woodenshield_small_d,itm_leathershield_small_d,
     ],
     def_attrib2|level(23),wp(170),knows_warrior_normal,mercenary_face_1, mercenary_face_2
   ],

   [
     "mercenary_swordsman","Milite (Hv. I.)","Milites",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
     [
       itm_spear_1,itm_spear_6,itm_had_seax,itm_scianshort,
       itm_throwing_spears,itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
       itm_decorated_leather_shoes,itm_carbatinae_2,itm_decorated_leather_shoes_blue,
       itm_coat_of_plates4,itm_mail_shirt_bluehorses,itm_padded_jack_6_trig,itm_padded_jack_7_trig,
       itm_woolen_cap_newred,itm_woolen_cap_newgrn,itm_woolen_cap,itm_bowl_helmet,itm_norman_helmet,itm_leather_cap,
       itm_leathershield_medium,itm_leathershield_medium_y,itm_leathershield_medium_b,itm_woodenshield_medium
     ],
     def_attrib3|level(27),wp(200),knows_warrior_veteran,mercenary_face_1, mercenary_face_2
   ],

   [
     "hired_blade","Veteran Warrior (Hv. I.)","Veterans Warriors",
     tf_guarantee_all_wo_ranged,no_scene,reserved,fac_commoners,
     [
       itm_leather_gloves,
       itm_throwing_spears,itm_throwing_spears3,
       itm_scythe,itm_lance,itm_le_pictishsword2,itm_bl_sword01_01,itm_le_bamburghsword,
       itm_decorated_leather_shoes_grey,itm_carbatinae_1_grey,itm_decorated_leather_shoes_orange,itm_iron_greaves,
       itm_mail_shirt_greenhorses,itm_mail_shirt_red,itm_mail_shirt_reddragon,
       itm_mail_shirt_redhorses,itm_mail_shirt_whiteaxes,
       itm_rath_spangenlord5,itm_bowl_helmet,itm_vaegir_war_helmet,itm_briton_helm,
       itm_celtic_vae_shield1,itm_celtic_vae_shield2,itm_celtic_vae_shield3,itm_celtic_vae_shield4
     ],
     def_attrib3|level(30),wp(230),knows_warrior_elite,mercenary_face_1, mercenary_face_2
   ],

   [
     "frisian_warrior","Professional Mercenary (Hv. I.)","Professional Mercenaries",
     tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
     [
       itm_throwing_spears,itm_throwing_spears3,
       itm_carbatinae_2,itm_decorated_leather_shoes_green,itm_decorated_leather_shoes_blue,
       itm_mail_shirt_bluehorses,itm_mail_shirt_blueunicorn,itm_mail_shirt_whiteraven,itm_mail_shirt_green,itm_mail_shirt_red,itm_mail_shirt_grn,
       itm_rath_spangenlord5,itm_bowl_helmet,itm_vaegir_war_helmet,itm_briton_helm5,
       itm_bamburghsword2,itm_bl_sword01_03,itm_new_sword2,itm_axe_2,itm_axehammer_2,itm_axehammer_1,
       itm_leathershield_medium,itm_leathershield_medium_y,itm_leathershield_medium_b,itm_woodenshield_medium
     ],
     def_attrib3|level(27),wp(200),knows_warrior_veteran,mercenary_face_1, mercenary_face_2
   ],

   [
     "mercenary_crossbowman","Archer","Archers",
     tf_guarantee_boots|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
     [
       itm_arrows,itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_short_bow,
       itm_ankle_boots,itm_wrapping_boots,
       itm_shirt,itm_roman_shirt,
       itm_hunting_dagger,itm_club_one,itm_head_wrappings,itm_spiked_club
     ],
     veteran_ranged_attrib|level(19),wp_one_handed (60)|wp_polearm (60) |wp_archery(140),
     knows_tracker_npc|knows_power_draw_3|knows_athletics_2|knows_shield_1,
     mercenary_face_1, mercenary_face_2
   ],

   [
     "slingers","Slinger","Slingers",
     tf_guarantee_boots|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
     [
       itm_flintlock_pistol_militar,itm_sniper_lead,
       itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
       itm_turret_hat_blue,itm_turret_hat_green,
       itm_shirt,itm_roman_shirt,
       itm_knife,itm_hatchet
     ],
     veteran_ranged_attrib|level(19),wp(140),
     knows_tracker_npc|knows_power_draw_3|knows_athletics_2|knows_shield_1,
     mercenary_face_1, mercenary_face_2
   ],

   [
     "mercenary_horseman","Horseman (Lig. C.)","Horsemen",
     tf_mounted|tf_guarantee_all,no_scene,reserved,fac_commoners,
     [
       itm_javelin_jinetes,itm_javelin_jinetes,
       itm_sumpter_horse,itm_saddle_horse,itm_steppe_horse,itm_charger,itm_normal_horse11,
       itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,
       itm_carbatinae_2_green,itm_carbatinae_2_grey,
       itm_piel_coat04,itm_piel_coat03,itm_blue_cloak,itm_red_cloak,
       itm_armor_8,itm_armor_9,itm_short_tunic,itm_green_tunic,itm_blue_tunic,
       itm_padded_jack_7_trig,itm_padded_jack_9_trig,
       itm_spear_2,itm_hand_axe,itm_talak_seax,
       itm_leathershield_small_b,itm_woodenshield_small,itm_woodenshield_small_d,itm_leathershield_small_d
     ],
     def_attrib2|level(23),wp(170),knows_warrior_normal,mercenary_face_1, mercenary_face_2
   ],

###mercenarios escolta chief para crear parties
   [
     "mercenary_leader","Mercenary Captain","Mercenary Captains",
     tf_mounted|tf_guarantee_all,no_scene,reserved,fac_commoners,
     [
       itm_throwing_spears,itm_arabian_horse_b,itm_courser,itm_arabian_horse_b2,
       itm_arabian_horse_a3,itm_arabian_horse_b3,
       itm_spatha,itm_had_seax,itm_mail_shirt_red,itm_mail_shirt_ylw,itm_mail_shirt_blk,
       itm_mail_shirt_wht,itm_carbatinae_2_blue,itm_leather_gloves,itm_celtic_vae_shield1,
       itm_celtic_vae_shield2,itm_celtic_vae_shield3,itm_celtic_vae_shield4,itm_celtic_vae_shield5
     ],
     def_attrib2|level(40),wp_one_handed(192)|wp_two_handed(100)|wp_polearm(187)|wp_archery(60)|wp_crossbow(90)|wp_throwing(76),
     knows_warrior_elite, mercenary_face_1, mercenary_face_2
   ],

#Tempered chief  mercenary skirmisher added for spying and skirmishing
   [
     "mercenary_skirmisher","Spy","Spies",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
     [
       itm_javelin,itm_hunting_bow,itm_arrows,
       itm_leather_gloves,itm_carbatinae_2,itm_carbatinae_1_grey,
       itm_youhou_assassin_hood,itm_green_cloak_hoodc,itm_brown_cloak_hoodc,itm_black_cloak_hoodc,itm_grey_cloak_hoodc,
       itm_linen_tunic,itm_armor_9,
       itm_club,itm_hand_axe,itm_knife
     ],
     elite_ranged_attrib|level(27),wp_archery(120)|wp(100),
     knows_tracker_npc|knows_riding_8|knows_ironflesh_3|knows_shield_2|knows_power_strike_1|knows_power_draw_3|knows_horse_archery_4,
     mercenary_face_1, mercenary_face_2
   ],  #Tempered  mercenary scouts for skirmisher party template

   [
     "mercenary_cavalry","Equite (Hv. C.)","Equites",
     tf_mounted|tf_guarantee_all,no_scene,reserved,fac_commoners,
     [
       itm_throwing_spears,itm_arabian_horse_b,itm_courser,itm_arabian_horse_a4,
       itm_arabian_horse_b4,itm_courser4,itm_courser5,
       itm_iron_greaves,
       itm_mail_shirt_blk,itm_mail_shirt_wht,itm_mail_shirt_grn,itm_padded_jack_3_trig,itm_padded_jack_4_trig,
       itm_rath_spangenlord5,itm_vaegir_war_helmet,itm_briton_helm4,
       itm_celtic_vae_shield2,itm_celtic_vae_shield3,itm_celtic_vae_shield4,itm_celtic_vae_shield5,
       itm_had_seax,itm_spear_8,itm_spear_4,itm_spatha
     ],
     def_attrib3|level(27),wp(200),knows_warrior_veteran,mercenary_face_1, mercenary_face_2
   ],

   [
     "mercenaries_end","mercenaries_end","mercenaries_end",0,no_scene,reserved,fac_commoners,
     [],
     def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2
   ],


#peasant - retainer - footman - man-at-arms -  knight - cantware
   [
     "sarranid_recruit","Gebur Jute (Lig. I.)","Geburas Jutes",
     tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,
       itm_ankle_boots,itm_wrapping_boots,
       itm_woolen_cap_newblu,itm_woolen_cap_newwht,itm_woolen_cap,
       itm_shirt,itm_roman_shirt,itm_fattiglinenskjortir,itm_bl_tunicsr01_2,itm_bl_tunicsr02,
       itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsr01,itm_fat_body,
       itm_knife,itm_pitch_fork,itm_cudgel,itm_stones,itm_battle_fork,itm_staff,itm_sickle
     ],
     def_attrib|level(15),wp(110),knows_warrior_basic, vaegir_face_younger_1, vaegir_face_middle_2
   ],

   [
     "sarranid_footman","Kotsetla Jute (Lig. I.)","Kotsetlas Jutes",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,
     [
       itm_javelin,itm_javelin,itm_javelin,itm_sniper_crossbow,itm_flintlock_pistol,itm_heavy_crossbow,
       itm_ankle_boots,itm_wrapping_boots,
       itm_woolen_cap_newblu,itm_woolen_cap_newwht,itm_woolen_cap,
       itm_bl_tunic03,itm_bluevikingshirt,itm_redvikingshirt,itm_redtunic,itm_bl_tunic03,
       itm_piel_coat01,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
       itm_wessex_tunic3,itm_bl_tunicsr02,itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsleather,
       itm_idi_furjacket4,itm_idi_furjacket5,itm_idi_furjacket6,
       itm_palka4,itm_palka5,itm_scimitar,itm_axefaradon2,
       itm_buckler7,itm_buckler6,itm_buckler8,itm_buckler9
     ],
     def_attrib2|level(19),wp(140),knows_warrior_basic, vaegir_face_young_1, vaegir_face_middle_2
   ],

   [
     "sarranid_skirmisher","Sceotand Jute (Missile)","Sceotandas Jutes",
     tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
     [
       itm_arrows,itm_arrows,itm_short_bow,itm_short_bow,itm_short_bow,itm_hunting_bow,
       itm_carbatinae_1_bare,itm_ankle_boots,itm_wrapping_boots,
       itm_woolen_cap_newblk,itm_woolen_cap_newwht,itm_woolen_cap,
       itm_shirt,itm_roman_shirt,itm_woolen_hood,itm_bl_tunicsr01_2,
       itm_leather_steppe_cap_a,itm_mercia_tunic1,itm_blue_short_tunic,
       itm_cudgel,itm_dagger,
     ],
     basic_ranged_attrib|str_10|level(15),wp_one_handed(40)|wp_polearm (40) |wp_archery(110),
     knows_ironflesh_1|knows_power_draw_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_old_2
   ],

   [
     "sarranid_veteran_footman","Geneata Jute (Med. I.)","Geneatas Jutes",
     tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_javelin,itm_javelin,itm_javelin,itm_javelin,
       itm_carbatinae_1_grey,itm_carbatinae_1_green,itm_carbatinae_2_orange,
       itm_woolen_cap_newblk,itm_woolen_cap_newwht,itm_woolen_cap,
       itm_rathos_bowl_helmet,itm_bowl_helmet,
       itm_bl_tunicsleather,itm_bl_tunicsleather_2,itm_bl_tunicsleather_3,
       itm_blue_short_tunic2,itm_bluevikingshirt,itm_pelt_coat2,itm_idi_furjacket4,
       itm_leather_vest_red,itm_leather_vest_green,itm_leather_vest_blue,
       itm_vikingaxeb,itm_saxon_spear,itm_spear_3,itm_lance,itm_langseax,itm_falchion,itm_spear_3,
       itm_ad_viking_shield_round_01,itm_ad_viking_shield_round_02,itm_ad_viking_shield_round_03,
       itm_ad_viking_shield_round_04,itm_ad_viking_shield_round_05,itm_ad_viking_shield_round_06,
       itm_ad_viking_shield_round_07
     ],
     def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1, vaegir_face_old_2
   ],

   [
     "centware_portaestandarte","Tacnberend","Tacnberend",
     tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_carbatinae_2_grey,itm_carbatinae_1_grey,itm_carbatinae_1_green,itm_carbatinae_1_orange,
       itm_piel_coat03,itm_piel_coat04,itm_piel_coat05,itm_piel_coat01,itm_piel_coat06,
       itm_shirt,itm_roman_shirt,itm_wessex_tunic3,itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsleather,
       itm_goat_cap,itm_felt_steppe_cap,itm_boar_helmet,
       itm_wessexbanner5,itm_personalbanner,itm_trophy_b
     ],
     def_attrib2|level(23),wp_one_handed(170)|wp_polearm (125)|wp(80),
     knows_warrior_normal,vaegir_face_young_1, vaegir_face_old_2
   ],

   [
     "centware_sacerdote","Jute Cleric","Jutes Clerics",
     tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_carbatinae_1_green,itm_carbatinae_1_orange,itm_carbatinae_2_orange,
       itm_blue_gambeson,itm_skirmisher_armor,
       itm_stones,itm_staff
     ],
     def_attrib|level(23),wp(170),knows_cleric,sac_face_1, sac_face_2
   ],

   [
     "sarranid_infantry","Geoguth Jute (Med. I.)","Geoguthas Jutes",
     tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_spear_6,itm_spear_3,itm_langseax,
       itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
       itm_carbatinae_1,itm_carbatinae_1_green,itm_carbatinae_1_orange,
       itm_woolen_cap_newblu,itm_woolen_cap_newgrn,itm_leather_cap,itm_horn_helmet_2,itm_horn_helmet,
       itm_coat_of_plates1,itm_coat_of_plates3,itm_coat_of_plates4,itm_coat_of_plates5,itm_coat_of_plates9,
       itm_norman_shield_4,itm_norman_shield_5,itm_norman_shield_6,itm_norman_shield_7,itm_norman_shield_8,
       itm_plate_covered_round_shield
     ],
     def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1, vaegir_face_older_2
   ],

   [
     "sarranid_guard","Beadu rinc Jute (Med. I.)","Beadu rincas Jutes",
     tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_neutral,
     [
       itm_throwing_spears3,itm_throwing_spears4,itm_javelin,itm_jarid,itm_javelin,
       itm_carbatinae_1_grey,itm_carbatinae_1_green,itm_carbatinae_2_orange,
       itm_piel_coat02,itm_piel_coat07,itm_bl_boar_fur,
       itm_leather_armor_c2,itm_leather_armor_c,itm_vae_thick_coat2,itm_vae_thick_coat3,
       itm_tattered_leather_armor_gr,itm_padded_leather_blue,itm_horn_helmet_3,
       itm_rathos_spangenhelm_b_light,itm_sarranid_veiled_helmet,
       itm_talak_seax,itm_spear_3,itm_axehammer_2,itm_axehammer_1,
       itm_ad_viking_shield_round_02,itm_ad_viking_shield_round_03,itm_ad_viking_shield_round_04,
       itm_ad_viking_shield_round_05,itm_ad_viking_shield_round_06,itm_ad_viking_shield_round_07,
       itm_ad_viking_shield_round_08
     ],
     def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2
   ],

   [
     "sarranid_horseman","Gesith Jute (Lig. C.)","Gesithas Jutes",
     tf_mounted|tf_guarantee_all,0,0,fac_neutral,
     [
       itm_javelin,itm_javelin,itm_javelin,itm_javelin,
       itm_normal_horse30,itm_saddle_horse,itm_steppe_horse,itm_charger,
       itm_normal_horse21,itm_normal_horse22,itm_normal_horse27,
       itm_leather_gloves,
       itm_mail_boots,itm_decorated_leather_shoes_orange,
       itm_tattered_leather_armor_gr,itm_padded_leather_brown,itm_leather_armor_c,
       itm_leather_armor_c2,itm_byrnie,itm_mail_shirthre,itm_mail_shirtredwhite,itm_mail_shirt_1_trig,
       itm_nordic_fighter_helmet,itm_nordic_footman_helmet,itm_nordic_veteran_archer_helmet,
       itm_vendel14,itm_horn_helmet_3,itm_vendel14_2,
       itm_axe_hammer_long,itm_spear_8,itm_spear_4,itm_valssword,
       itm_saxon_adorno_14,itm_saxon_adorno_15,itm_tab_shield_small_round_c
     ],
     def_attrib3|level(27),wp(200),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2
   ],

   [
     "sarranid_mamluke","Ridwiga Jute (Hv. I.)","Ridwigas Jutes",
     tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,
     [
       itm_throwing_spears3,itm_light_throwing_axes,itm_throwing_axes,itm_throwing_spears4,itm_jarid,
       itm_leather_gloves,
       itm_decorated_leather_shoes_grey,itm_carbatinae_1_grey,itm_iron_greaves,
       itm_tattered_leather_armor_blu,itm_ad_viking_byrnie_01,itm_ad_viking_byrnie_02,
       itm_ad_viking_byrnie_03,itm_ad_viking_byrnie_04,itm_mail_shirt_9_trig,
       itm_vaegir_fur_helmet,itm_magyar_helmet_a,itm_flat_topped_helmet,itm_nordic_huscarl_helmet,
       itm_sarranid_mail_coif,itm_khergit_cavalry_helmet,
       itm_vikingaxeb,itm_vikingaxe,itm_le_richsword2,itm_saxon_richsword,itm_battle_axe,
       itm_ad_viking_shield_round_09,itm_saxon_adorno_15,itm_saxon_adorno_16,itm_saxon_adorno_17,
       itm_saxon_adorno_18,itm_saxon_adorno_19
     ],
     def_attrib3|level(27),wp(200),knows_warrior_veteran,vaegir_face_young_1, vaegir_face_older_2
   ],

   [
     "sarranid_archer","Duguth Jute (Hv. I.)","Duguthas Jutes",
     tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_neutral,
     [
       itm_throwing_spears3,itm_light_throwing_axes,itm_throwing_axes,itm_throwing_spears4,itm_jarid,
       itm_leather_gloves,
       itm_carbatinae_1_grey,itm_mail_boots,itm_decorated_leather_shoes_orange,
       itm_norman_helmet,itm_leather_steppe_cap_b,itm_sarranid_helmet1,itm_rath_spangenlord5,
       itm_noblemanshirt,itm_noblemanshirt_gaelic,itm_coat_of_plates6,itm_coat_of_plates8,itm_coat_of_plates9,
       itm_padded_jack_3_trig,itm_mail_shirt_8_trig,itm_mail_shirt_7_trig,itm_mail_shirt_6_trig,itm_mail_shirt_4_trig,
       itm_le_bamburghsword,itm_spear_2,itm_langseax,
       itm_norman_shield_4,itm_norman_shield_5,itm_norman_shield_6,itm_norman_shield_7,
       itm_norman_shield_8,itm_plate_covered_round_shield
     ],
     def_attrib3|level(27),wp(200),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2
   ],

   [
     "sarranid_master_archer","Hearthweru Jute (Elit. I.)","Hearthweruas Jutes",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,
     [
       itm_throwing_spears3,itm_light_throwing_axes,itm_throwing_spears4,itm_throwing_axes,itm_jarid,
       itm_leather_gloves,
       itm_light_leather_boots,itm_carbatinae_2_greaves_green,itm_carbatinae_1_greaves_blue,
       itm_carbatinae_2_greaves_orange,itm_splinted_leather_greaves,
       itm_vikinglamellar2yellow,itm_vikinglamellar2red,itm_vikinglamellar2blue,itm_wolf_coat1,
       itm_wolfpelt_mail_coat,itm_mail_shirt_grn,itm_mail_shirt_red,
       itm_segmented_helmet,itm_vaegir_fur_cap,itm_byzantion_helmet_a,
       itm_vaegir_mask,itm_nasal_helmet,itm_rus_helmet_a,itm_spiked_helmet,
       itm_spear_1,itm_spear_2,itm_axehammer_1,itm_le_richsword2,itm_valssword,itm_frankish_axe2,
       itm_tab_shield_round_c
     ],
     def_attrib3|level(32),wp(260),knows_warrior_elite,vaegir_face_young_1, vaegir_face_older_2
   ],

   [
     "sarranid_messenger","Horsweala Jute","Horswealas Jutes",
     tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
     [
       itm_javelin,itm_saddle_horse, itm_leather_gloves,
       itm_decorated_leather_shoes,itm_carbatinae_2,itm_decorated_leather_shoes_green,
       itm_decorated_leather_shoes_blue,itm_carbatinae_2_blue,
       itm_shirt,itm_roman_shirt,itm_fattiglinenskjortir,itm_wessex_tunic3,itm_bl_tunicsr02,
       itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsleather,
       itm_spear_6,itm_spear_3,itm_langseax,
       itm_norman_shield_4,itm_norman_shield_5,itm_norman_shield_6,itm_norman_shield_7,
       itm_norman_shield_8,itm_plate_covered_round_shield
     ],
     def_attrib3|agi_21|level(27),wp(200),knows_common|knows_riding_7|knows_power_throw_2,
     vaegir_face_young_1, vaegir_face_older_2
   ],

   [
     "sarranid_deserter","Jute Deserter","Jutes Deserters",
     tf_guarantee_shield|tf_guarantee_boots,0,0,fac_deserters,
     [
       itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
       itm_carbatinae_2,itm_carbatinae_2_blue,itm_carbatinae_2_grey,itm_carbatinae_1_green,
       itm_fattiglinenskjortir,itm_wessex_tunic3,itm_bl_tunicsr02,itm_mercia_tunic1,
       itm_blue_short_tunic,itm_bl_tunicsleather,
       itm_woolen_cap_newblu,itm_woolen_cap_newred,itm_woolen_cap_newwht,itm_woolen_cap,
       itm_bowl_helmet,itm_horn_helmet_2,itm_leather_warrior_cap,
       itm_vikingaxeb,itm_saxon_spear,itm_spear_3,itm_langseax,itm_falchion,itm_spear_3,
       itm_ad_viking_shield_round_01,itm_ad_viking_shield_round_02,itm_ad_viking_shield_round_03,
       itm_ad_viking_shield_round_04,itm_ad_viking_shield_round_05,itm_ad_viking_shield_round_06
     ],
     def_attrib2|str_10|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1, vaegir_face_older_2
   ],

   [
     "sarranid_prison_guard","Prison Guard","Prison Guards",
     tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_neutral,
     [
       itm_throwing_spears3,itm_leather_gloves,itm_decorated_leather_shoes,itm_woolen_cap_newblu,
       itm_woolen_cap_newred,itm_norman_helmet,itm_leather_cap,itm_bowl_helmet,
       itm_noblemanshirt,itm_noblemanshirt_gaelic,itm_leather_vest_red,itm_tattered_leather_armor_blk,
       itm_spear_2,itm_langseax,itm_plate_covered_round_shield
     ],
     def_attrib3|level(29),wp(200),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2
   ],

   [
     "sarranid_castle_guard","Castle Guard","Castle Guards",
     tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_throwing_spears3,itm_leather_gloves,itm_decorated_leather_shoes,itm_woolen_cap_newblu,
       itm_woolen_cap_newred,itm_norman_helmet,itm_leather_cap,itm_bowl_helmet,
       itm_noblemanshirt,itm_noblemanshirt_gaelic,itm_leather_vest_red,itm_tattered_leather_armor_blk,
       itm_spear_2,itm_langseax,itm_plate_covered_round_shield
     ],
     def_attrib3|level(29),wp(200),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2
   ],


#TEMPERED chief NEW TROOP LINE FOR RANGERS
  #arbol frisio frisios chief
   [
     "fresena","Fresena (Lig. I.)","Frisen",
     tf_guarantee_armor|tf_guarantee_boots,no_scene,reserved,fac_neutral,
     [
       itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,
       itm_ankle_boots,itm_wrapping_boots,
       itm_woolen_cap_newgrn,itm_woolen_cap_newblk,itm_woolen_cap_newwht,itm_woolen_cap,
       itm_shirt,itm_roman_shirt,itm_bl_tunicsr02,itm_bl_tunicsr01,itm_shirtb,itm_shirtc,
       itm_shirtd,itm_shirte,itm_fat_body,
       itm_knife,itm_pitch_fork,itm_cudgel,itm_quarter_staff,itm_sickle,itm_wooden_stick
     ],
     def_attrib|level(15),wp(110),knows_warrior_basic,nord_face_young_1, nord_face_older_2
   ],

   [
     "thene_saltan_fresena","Thene Saltan Fresena (Med. I.)","Thene Saltan Frisen",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,0,fac_neutral,
     [
       itm_javelin,itm_javelin,itm_javelin,itm_sniper_crossbow,itm_flintlock_pistol,
       itm_carbatinae_1_grey,itm_carbatinae_1_green,
       itm_woolen_cap_newgrn,itm_woolen_cap_newwht,
       itm_shirt,itm_roman_shirt,itm_shirtb,itm_shirtc,itm_shirtd,itm_shirte,
       itm_coat_of_plates6,itm_coat_of_plates1,itm_coat_of_plates8,itm_coat_of_plates11,
       itm_frisian_helmet_mesh,itm_horn_helmet_2,itm_leather_cap,
       itm_spear_6,itm_langseax,
       itm_ad_viking_shield_round_01,itm_ad_viking_shield_round_37,itm_ad_viking_shield_round_38,
       itm_ad_viking_shield_round_39,itm_ad_viking_shield_round_41
     ],
     def_attrib2|level(21),wp(150),knows_warrior_normal, nord_face_young_1, nord_face_older_2
   ],

   [
     "skel_fresena","Skel Fresena (Hv. I.)","Skel Frisen",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
     no_scene,reserved,fac_neutral,
     [
       itm_throwing_spears,itm_throwing_spears,itm_throwing_spears,
       itm_leather_gloves,
       itm_decorated_leather_shoes_blue,itm_mail_boots,itm_decorated_leather_shoes_orange,
       itm_blue_short_tunic2,itm_bluevikingshirt,itm_mercia_tunic10,itm_wessex_tunic4,
       itm_mail_shirt_ylw,itm_mail_shirt_blk,itm_mail_shirt_wht,itm_padded_jack_3_trig,
       itm_flat_topped_helmet,itm_kettle_hat,itm_nordic_footman_helmet,itm_nordic_fighter_helmet,
       itm_nasal_helmet,itm_vaegir_fur_helmet,
       itm_spear_6,itm_spear_3,itm_axehammer_2,itm_langseax,itm_axehammer1,itm_bl_sword01_03,itm_new_sword2,
       itm_tab_shield_round_c
     ],
     def_attrib3|level(27),wp(200),knows_warrior_veteran,nord_face_young_1, nord_face_older_2
   ],

   [
     "herem_fresena","Herem Fresena (Lig. C.)","Herem Frisen",
     tf_mounted|tf_guarantee_all,no_scene,reserved,fac_neutral,
     [
       itm_javelin,itm_javelin,itm_javelin,
       itm_normal_horse21,itm_normal_horse22,itm_normal_horse27,itm_normal_horse24,
       itm_normal_horse25,itm_normal_horse26,
       itm_carbatinae_2_blue,itm_carbatinae_2_grey,
       itm_shirtb,itm_shirtc,itm_shirtd,itm_shirte,itm_armor_27,itm_armor_26,
       itm_peasant_man_e,itm_peasant_man_f,itm_padded_jack_4_trig,itm_padded_jack_6_trig,
       itm_frisian_helmet_mesh,itm_footman_helmet,itm_sarranid_veiled_helmet,itm_horn_helmet_2,itm_leather_cap,
       itm_hunting_dagger,itm_spear_8,itm_spear_4,itm_leathershield_small_b,itm_woodenshield_small_d,
       itm_woodenshield_small,itm_leathershield_small_d
     ],
     def_attrib3|level(23),wp(170),knows_warrior_veteran,nord_face_young_1, nord_face_older_2
   ],
  #tempered acaba chief


#peasant - retainer - footman - man-at-arms -  knight - britones
   [
     "swadian_recruit","Aillt (Lig. I.)","Aillts",
     tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,
       itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
       itm_hood_newblk,itm_common_hood,
       itm_shirt,itm_roman_shirt,itm_bl_tunicsr01,itm_bl_tunicsr01_2,itm_bl_tunicsr02,
       itm_shirtb,itm_shirtc,itm_shirtd,itm_fattiglinenskjortir,
       itm_knife,itm_pitch_fork,itm_cudgel,itm_battle_fork,itm_club,itm_sickle
     ],
     def_attrib|level(15),wp(110),knows_common,swadian_face_younger_1, swadian_face_middle_2
   ],

   [
     "swadian_militia","Bonheddwr (Lig. I.)","Bonheddwyr",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,
     [
       itm_throwing_knives,itm_throwing_knives,itm_javelin,itm_sniper_crossbow,itm_flintlock_pistol,itm_heavy_crossbow,
       itm_carbatinae_2_bare,itm_carbatinae_1_bare,itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,
       itm_black_hood,itm_black_cloak,itm_white_cloak,itm_piel_coat05,
       itm_armor_8,itm_armor_9,itm_short_tunic,itm_red_tunic,itm_green_tunic,
       itm_leather_steppe_cap_a,itm_peasant_archer,itm_armor_26,
       itm_spiked_club,itm_club,itm_hand_axe,itm_sarranid_two_handed_axe_b,
       itm_wooden_shield,itm_nordic_shield,itm_ckler,itm_buckler28,itm_talak_buckler
     ],
     def_attrib2|level(19),wp(140),knows_warrior_basic,swadian_face_young_1, swadian_face_old_2
   ],

   [
     "swadian_footman","Pedyt (Med. I.)","Pedytes",
     tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
       itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
       itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
       itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,
       itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
       itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
       itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
       itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,
       itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29
     ],
     def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2
   ],

   [
     "swadian_crossbowman","Uchelwr (Hv. I.)","Uchelwyr",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,
     [
       itm_throwing_spears,itm_throwing_spears,
       itm_decorated_leather_shoes_blue,itm_decorated_leather_shoes_grey,itm_carbatinae_1_grey,itm_carbatinae_2,
       itm_shirt_red,itm_bl_tunic01,itm_bl_tunic04,itm_bl_tunic09,itm_linen_tunic,itm_bl_tunic10,
       itm_arena_tunicj_brown,itm_arena_tunicj_magenta,itm_arena_tunicj_violet,itm_mail_with_surcoat,
       itm_mail_shirt_3,itm_lamellar_armor,itm_cuir_bouilli,itm_mamluke_mail,itm_padded_jack_6_trig,
       itm_hasta,itm_roman_spear_1,itm_broadsword,itm_saxonsword1, itm_arming_cap,itm_padded_coif,
       itm_ad_viking_shield_round_22,itm_ad_viking_shield_round_23,itm_ad_viking_shield_round_24,
       itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26
     ],
     def_attrib3|level(27),wp(200),knows_warrior_veteran,swadian_face_young_1, swadian_face_old_2
   ],

   [
     "briton_portaestandarte","Gwas Ys Tafell","Gwas Ys Tafell",
     tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_carbatinae_2_blue,itm_carbatinae_2_grey,itm_carbatinae_1_grey,itm_carbatinae_1_green,
       itm_piel_coat02,itm_piel_coat03,
       itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,
       itm_shirt_blk,itm_bl_tunic02,itm_woolen_hood,itm_leather_steppe_cap_a,
       itm_wessexbanner9,itm_wessexbanner4,itm_personalbanner,itm_trophy_b,
       itm_long_mail_coat,itm_cloaked_tunic,itm_tattered_leather_armor_blk,
       itm_tattered_leather_armor_wht,itm_leather_gloves,itm_helm_captaina
     ],
     def_attrib2|level(23),wp(165),knows_warrior_normal,vaegir_face_young_1, vaegir_face_old_2
   ],

   [
     "briton_sacerdote","Briton Cleric","Britons Clerics",
     tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_blue_gambeson,itm_sarranid_leather_armor,
       itm_stones,itm_staff
     ],
     def_attrib|level(23),wp(165),knows_cleric,sac_face_1, sac_face_2
   ],

   [
     "swadian_infantry","Gwrda (Skrm.)","Gwrdas",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,
     [
       itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
       itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,
       itm_white_cloak,itm_irishcloak,itm_piel_coat07,
       itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,
       itm_vae_thick_coat2,itm_vae_thick_coat3,
       itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
       itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,
       itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15
     ],
     def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2
   ],

   [
     "swadian_sergeant","Cadwr (Hv. I.)","Cadwyr",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_neutral,
     [
       itm_throwing_spears,itm_throwing_spears,itm_throwing_spears,
       itm_leather_gloves,
       itm_decorated_leather_shoes_green,itm_decorated_leather_shoes_blue,itm_carbatinae_2_blue,
       itm_nordiclightarmor10,itm_nordiclightarmor11,itm_nordiclightarmor12,itm_padded_jack_6_trig,
       itm_light_leather,itm_mail_with_surcoat,itm_coat_of_plates,itm_swadian_mail_hauberk,itm_byrnie5,
       itm_rathos_spangenhelm_a_light,itm_rathos_spangenhelm_b_light,itm_briton_helm,
       itm_rathos_bowl_helmet, itm_arming_cap, itm_padded_coif,
       itm_hasta,itm_roman_spear_1,itm_saxonsword1,itm_nordic_sword,itm_broadsword,itm_le_pictishsword6,
       itm_shield_1,itm_shield_2,itm_shield_3,itm_shield_4,itm_shield_5,itm_shield_6,itm_shield_7,itm_shield_10
     ],
     def_attrib3|level(27),wp(190),knows_warrior_veteran,swadian_face_middle_1, swadian_face_older_2
   ],

   [
     "campeon","Campgwr (Elit. I.)","Campgwyr",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_neutral,
     [
       itm_throwing_spears,itm_throwing_spears,itm_throwing_spears,
       itm_leather_gloves,
       itm_carbatinae_1_greaves_green,itm_carbatinae_1_greaves_blue,itm_carbatinae_2_greaves_blue,
       itm_carbatinae_1_greaves_grey,
       itm_wei_xiadi_sar_hauberk,itm_swadian_mail_hauberk,itm_byrnie4,
       itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_spangenhelm_yellow_plum,
       itm_romanelitehelm,itm_rathos_spangenhelm_b,itm_briton_helm2,itm_briton_helm3,itm_briton_helm5,itm_steppe_cap,
       itm_roman_spear_1,itm_bamburghsword2,itm_celticsword,itm_saxonsword1,itm_broadsword,itm_le_bamburghsword,
       itm_celticsaxon_adorno_8,itm_celticsaxon_adorno_9,itm_shield_16,itm_shield_17,itm_tab_shield_round_c
     ],
     def_attrib3|level(29),wp(220),knows_warrior_veteran,swadian_face_middle_1, swadian_face_older_2
   ],

   [
     "swadian_skirmisher","Bweydd (Missile)","Bweydds",
     tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
       itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
       itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
       itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,
       itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
       itm_wooden_stick,itm_hand_axe,itm_cudgel
     ],
     basic_ranged_attrib|level(19),wp(60)|wp_archery(140),
     knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2
   ],

   [
     "swadian_sharpshooter","Saethydd (Missile)","Saethydds",
     tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_arrows,itm_long_bow,itm_long_bow,itm_long_bow,itm_long_bow,itm_long_bow,
       itm_carbatinae_2_green,itm_carbatinae_1_blue,itm_carbatinae_2_blue,itm_carbatinae_2_grey,
       itm_hood_newwht,itm_black_hood,itm_head_wrappings,itm_common_hood,
       itm_shirt,itm_fattiglinenskjortir,itm_shirt_blu,itm_shirt_grn,itm_shirt_ylw,
       itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_peasant_archer,itm_armor_26,
       itm_scianshortbone,itm_scianshort,itm_hand_axe,itm_lui_waronehandedaxec
     ],
     veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),
     knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2
   ],

   [
     "swadian_man_at_arms","Marchoc (Lig. C.)","Marcach",
     tf_mounted|tf_guarantee_all,0,0,fac_neutral,
     [
       itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
       itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,
       itm_normal_horse15,itm_normal_horse16,
       itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
       itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,
       itm_mail_shirt_1,itm_mail_shirt_2,
       itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,
       itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
       itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
       itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,
       itm_shield_round_07,itm_shield_round_01
     ],
     def_attrib3|level(27),wp(200),knows_warrior_veteran,swadian_face_young_1, swadian_face_old_2
   ],

   [
     "swadian_knight","Teulu (Elit. C.)","Teulus",
     tf_mounted|tf_guarantee_all,0,0,fac_neutral,
     [
       itm_javelin,
       itm_arabian_horse_b,itm_courser,itm_arabian_horse_a3,itm_arabian_horse_b3,
       itm_arabian_horse_a4,itm_arabian_horse_b4,itm_courser4,
       itm_leather_gloves,itm_carbatinae_2_greaves_green,itm_carbatinae_1_greaves_green,
       itm_carbatinae_2_greaves_grey,itm_splinted_leather_greaves,
       itm_mail_shirt_reddragon,itm_swadian_mail_hauberk,itm_wei_xiadi_sar_hauberk,
       itm_banded_armor,itm_coat_of_plates_red,itm_plate_armor,itm_mail_hauberk,
       itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_briton_helm,itm_dux_ridge_helm,
       itm_barf_helm,itm_spangenhelm_a_ornate,itm_vaegir_war_helmet,itm_briton_helm4,itm_spangenhelm_a_trim,itm_steppe_cap,
       itm_sarranid_axe_b,itm_saxonsword1,itm_celticsword,itm_le_pictishsword2,itm_broadsword,
       itm_tab_shield_small_round_c,itm_shield_round_08,itm_norman_shield_5,itm_ad_viking_shield_round_11
     ],
     def_attrib3|level(29),wp(230),knows_warrior_elite,swadian_face_middle_1, swadian_face_older_2
   ],

   [
     "swadian_messenger","Briton Messenger","Britons Messengers",
     tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
     [
       itm_leather_gloves,itm_leather_gloves,itm_javelin,itm_arabian_horse_b,
       itm_decorated_leather_shoes,itm_carbatinae_2,itm_decorated_leather_shoes_green,
       itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,
       itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,
       itm_sarranid_axe_b,itm_sarranid_axe_b,itm_scianlong,itm_scianlongbone,
       itm_scythe,itm_nordic_sword,itm_broadsword,
       itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,
       itm_shield_round_06,itm_shield_round_07,itm_shield_round_01
     ],
     def_attrib3|agi_21|level(29),wp(230),
     knows_common|knows_riding_7|knows_power_draw_3|knows_horse_archery_5,swadian_face_young_1, swadian_face_old_2
   ],

   [
     "swadian_deserter","Briton Deserter","Britons Deserters",
     tf_guarantee_boots|tf_guarantee_shield,0,0,fac_deserters,
     [
       itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
       itm_carbatinae_1,itm_carbatinae_2,itm_carbatinae_2_green,
       itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_shirt_blk,itm_bl_tunic02,
       itm_shirt,itm_shirt_grn,itm_shirt_ylw,itm_bl_tunic02,
       itm_leather_cap,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,itm_leather_steppe_cap_c,
       itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_langseax,itm_scianshort,
       itm_ad_viking_shield_round_24,itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,
       itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29
     ],
     def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2\
   ],

   [
     "swadian_prison_guard","Prison Guard","Prison Guards",
     tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_neutral,
     [
       itm_throwing_spears,
       itm_leather_gloves,
       itm_iron_greaves,
       itm_linen_tunic,itm_bl_tunic10,itm_swadian_mail_hauberk,itm_byrnie5,itm_rathos_spangenhelm_b_light,
       itm_rathos_spangenhelm_yellow_plum,
       itm_roman_spear_1,itm_scianshort,itm_shield_17
     ],
     def_attrib3|level(29),wp(230),
     knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2
   ],

   [
     "swadian_castle_guard","Castle Guard","Castle Guards",
     tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_throwing_spears,
       itm_leather_gloves,itm_iron_greaves,
       itm_linen_tunic,itm_bl_tunic10,itm_swadian_mail_hauberk,itm_byrnie5,
       itm_rathos_spangenhelm_b_light,itm_rathos_spangenhelm_yellow_plum,
       itm_roman_spear_1,itm_scianshort,itm_shield_17
     ],
     def_attrib3|level(29),wp(230),
     knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2
   ],

# Vaegir watchman? Saxons
   [
     "vaegir_recruit","Gebur Seaxe (Lig. I.)","Geburas Seaxna",
     tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,
       itm_ankle_boots,itm_wrapping_boots,
       itm_woolen_cap_newgrn,itm_woolen_cap_newblk,itm_woolen_cap_newwht,itm_woolen_cap,
       itm_shirt,itm_roman_shirt,itm_fattiglinenskjortir,itm_bl_tunicsr01_2,itm_bl_tunicsr02,
       itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsr01,itm_fattiglinenskjortir,
       itm_knife,itm_battle_fork,itm_club,itm_quarter_staff,itm_sickle,itm_hatchet,itm_wooden_stick
     ],
     def_attrib|level(15),wp(110),knows_warrior_basic, vaegir_face_younger_1, vaegir_face_middle_2
   ],

   [
     "vaegir_footman","Kotsetla Seaxe (Lig. I.)","Kotsetlas Seaxna",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,
     [
       itm_javelin,itm_javelin,itm_javelin,itm_sniper_crossbow,itm_flintlock_pistol,itm_heavy_crossbow,
       itm_ankle_boots,itm_wrapping_boots,
       itm_woolen_cap_newred,itm_woolen_cap_newgrn,itm_woolen_cap_newblk,
       itm_piel_coat02,itm_piel_coat03,itm_piel_coat04,
       itm_roman_shirt,itm_fattiglinenskjortir,itm_peasant_man_c,itm_armor_27,itm_peasant_man_e,
       itm_woolen_hood,itm_idi_furjacket1,itm_idi_furjacket2,itm_idi_furjacket5,
       itm_palka2,itm_palka3,itm_scimitar,itm_sarranid_axe_a,
       itm_buckler10,itm_buckler11,itm_buckler12,itm_buckler13,itm_buckler14
     ],
     def_attrib2|level(19),wp(140),knows_warrior_basic, vaegir_face_young_1, vaegir_face_middle_2
   ],

   [
     "vaegir_skirmisher","Sceotand Seaxe (Missile)","Sceotandas Seaxna",
     tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
     [
       itm_arrows,itm_short_bow,itm_short_bow,itm_short_bow,itm_hunting_bow,
       itm_bare_legs_blue,itm_ankle_boots,itm_wrapping_boots,
       itm_woolen_cap_newblu,itm_woolen_cap_newred,itm_woolen_cap_newgrn,itm_woolen_cap,
       itm_shirt,itm_roman_shirt,itm_fattiglinenskjortir,itm_bl_tunicsr01_2,itm_bl_tunicsr02,
       itm_mercia_tunic1,itm_bl_tunicsr01,
       itm_cudgel,itm_dagger,itm_saxon_axe
     ],
     basic_ranged_attrib|level(15),wp(40)|wp_archery(110),
     knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2
   ],

   [
     "saxon_portaestandarte","Tacnberend","Tacnberend",
     tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_carbatinae_1,itm_carbatinae_2,itm_piel_coat02,itm_piel_coat05,itm_piel_coat07,
       itm_shirt,itm_roman_shirt,itm_fattiglinenskjortir,itm_wessex_tunic3,itm_blue_short_tunic,itm_bl_tunicsleather,
       itm_goat_cap,itm_felt_steppe_cap,itm_boar_helmet,
       itm_wessexbanner1,itm_personalbanner,itm_trophy_b,
       itm_leather_gloves
     ],
     def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1, vaegir_face_old_2
   ],

   [
     "todos_cuerno","Hornman","Hornmen",
     tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_bare_legs_blue,itm_ankle_boots,itm_wrapping_boots,itm_piel_coat02,itm_piel_coat05,itm_piel_coat07,
       itm_roman_shirt,itm_fattiglinenskjortir,itm_wessex_tunic3,itm_bl_tunicsr02,
       itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsleather,
       itm_horn,itm_trophy_a,itm_buckler11,itm_stones,itm_falchion
     ],
     def_attrib2|level(15),wp(115),knows_warrior_normal,vaegir_face_young_1, vaegir_face_old_2
   ],

   [
     "saxon_sacerdote","Cleric Seaxe","Clerics Seaxna",
     tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_decorated_leather_shoes,itm_carbatinae_2,itm_decorated_leather_shoes_green,
       itm_decorated_leather_shoes_blue,itm_carbatinae_2_blue,
       itm_blue_gambeson,itm_skirmisher_armor,
       itm_stones,itm_staff
     ],
     def_attrib|level(23),wp(170),knows_cleric,sac_face_1, sac_face_2
   ],

   [
     "vaegir_veteran","Geneata Seaxe (Med. I.)","Geneatas Seaxna",
     tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
       itm_carbatinae_1_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,itm_carbatinae_2_orange,
       itm_blue_short_tunic2,itm_bluevikingshirt,itm_mercia_tunic10,
       itm_coat_of_plates8,itm_leather_vest_red,itm_pelt_coat2,itm_idi_furjacket6,
       itm_vikingaxeb,itm_saxon_spear,itm_spear_3,itm_lance,itm_langseax,itm_falchion,itm_spear_3,
       itm_ad_viking_shield_round_10,itm_ad_viking_shield_round_11,itm_ad_viking_shield_round_12,
       itm_ad_viking_shield_round_13,itm_ad_viking_shield_round_16,itm_ad_viking_shield_round_17,
       itm_ad_viking_shield_round_18
     ],
     def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1, vaegir_face_old_2
   ],

   [
     "vaegir_infantry","Geoguth Seaxe (Med. I.)","Geoguthas Seaxna",
     tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
       itm_carbatinae_1_grey,itm_carbatinae_1_green,itm_carbatinae_2_orange,
       itm_woolen_cap_newblk,itm_woolen_cap_newwht,itm_rathos_bowl_helmet,
       itm_bl_tunicsleather,itm_bl_tunicsleather_2,
       itm_leather_vest_green,itm_coat_of_plates1,itm_leather_vest_blue,itm_coat_of_plates3,itm_coat_of_plates5,
       itm_spear_6,itm_spear_3,itm_langseax,
       itm_nomad_shield,itm_leather_covered_round_shield,itm_hide_covered_round_shield,itm_shield_heater_c,
       itm_bl_roundshields_a,itm_norman_shield_1,itm_norman_shield_2,itm_norman_shield_3
     ],
     def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1, vaegir_face_older_2
   ],

   [
     "vaegir_guard","Beadu rinc Seaxe (Med. I.)","Beadu rincas Seaxna",
     tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_neutral,
     [
       itm_throwing_spears3,itm_javelin,itm_throwing_spears4,
       itm_leather_gloves,itm_carbatinae_2,itm_carbatinae_2_green,
       itm_piel_coat01,itm_piel_coat03,itm_piel_coat06,
       itm_bl_tunic03,itm_bluevikingshirt,itm_redvikingshirt,itm_leather_armor_c2,itm_leather_armor_c,
       itm_padded_leather_brown,itm_vae_thick_coat3,
       itm_sarranid_helmet1,itm_horn_helmet_3,itm_rathos_bowl_helmet,itm_rathos_spangenhelm_b_light,
       itm_langseax,itm_spear_3,itm_lui_waronehandedaxec,itm_axe_2,itm_lui_battleaxetwoh,
       itm_ad_viking_shield_round_13,itm_ad_viking_shield_round_16,itm_ad_viking_shield_round_17,
       itm_ad_viking_shield_round_18,itm_ad_viking_shield_round_19,itm_ad_viking_shield_round_20,
       itm_ad_viking_shield_round_21
     ],
     def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2
   ],

   [
     "vaegir_horseman","Gesith Seaxe (Lig. C.)","Gesithas Seaxna",
     tf_mounted|tf_guarantee_all,0,0,fac_neutral,
     [
       itm_javelin,itm_javelin,
       itm_normal_horse30,itm_saddle_horse,itm_normal_horse21,itm_normal_horse22,itm_normal_horse27,
       itm_normal_horse24,itm_normal_horse25,itm_normal_horse26,
       itm_carbatinae_2_blue,itm_decorated_leather_shoes_grey,itm_mail_boots,itm_decorated_leather_shoes_orange,
       itm_tattered_leather_armor_gr,itm_padded_leather_blue,itm_byrnie,itm_mail_shirthre,
       itm_mail_shirtredwhite,itm_mail_shirt_1_trig,
       itm_rathos_spangenhelm_b,itm_nordic_fighter_helmet,itm_spangenhelm_helm,itm_rathos_spangenhelm_a_yellow2,
       itm_horn_helmet_2,itm_horn_helmet,itm_horn_helmet_3,
       itm_hunting_dagger,itm_axehammer_2,itm_spear_8,itm_spear_4,itm_saxonsword,itm_le_richsword1,
       itm_saxon_adorno_6,itm_saxon_adorno_7,itm_tab_shield_small_round_c
     ],
     def_attrib3|level(27),wp(200),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2
   ],

   [
     "vaegir_knight","Ridwiga Seaxe (Hv. I.)","Ridwigas Seaxna",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_neutral,
     [
       itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
       itm_leather_gloves,
       itm_decorated_leather_shoes,itm_carbatinae_2,itm_decorated_leather_shoes_green,
       itm_tattered_leather_armor_red,itm_tattered_leather_armor_blk,itm_ad_viking_byrnie_01,
       itm_ad_viking_byrnie_05,itm_ad_viking_byrnie_06,itm_mail_shirt_2_trig,itm_mail_shirt_3_trig,
       itm_rathos_spangenhelm_yellow_plum,itm_rathos_spangenhelm_a,itm_nordic_huscarl_helmet,
       itm_kettle_hat,itm_briton_helm,itm_gaul_helmet,itm_vendel14,
       itm_ornate_seax,itm_frankish_axe2,itm_battle_axe,itm_war_axe,itm_saxonsword,itm_le_richsword1,
       itm_norman_shield_3,itm_saxon_adorno_8,itm_saxon_adorno_9,itm_saxon_adorno_10,
       itm_saxon_adorno_11,itm_saxon_adorno_12,itm_saxon_adorno_13
     ],
     def_attrib3|level(27),wp(200),knows_warrior_veteran,vaegir_face_young_1, vaegir_face_older_2
   ],

   [
     "vaegir_archer","Duguth Seaxe (Hv. I.)","Duguthas Seaxna",
     tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_neutral,
     [
       itm_throwing_spears3,itm_throwing_spears4,itm_throwing_spears4,itm_jarid,
       itm_leather_gloves,
       itm_decorated_leather_shoes,itm_mail_boots,itm_iron_greaves,
       itm_coat_of_plates6,itm_leather_vest_red,itm_padded_jack_6_trig,itm_tattered_leather_armor_blk,
       itm_mail_shirt_8_trig,itm_mail_shirt_4_trig,
       itm_woolen_cap_newblu,itm_woolen_cap_newred,itm_woolen_cap_newwht,itm_woolen_cap,
       itm_norman_helmet,itm_leather_cap,itm_fur_hat,itm_leather_cap,itm_leather_steppe_cap_b,
       itm_le_bamburghsword,itm_spear_2,itm_langseax,
       itm_nomad_shield,itm_leather_covered_round_shield,itm_hide_covered_round_shield,itm_shield_heater_c,
       itm_bl_roundshields_a,itm_norman_shield_1,itm_norman_shield_2
     ],
     def_attrib3|level(27),wp(200),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2
   ],

   [
     "vaegir_marksman","Hearthweru Seaxe (Elit. I.)","Hearthweruas Seaxna",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,
     [
       itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
       itm_leather_gloves,
       itm_carbatinae_1_greaves_orange,itm_splinted_leather_greaves,
       itm_byrnie_e_new,itm_hauberk6,itm_mail_shirt_1_trig,itm_byrnie5,itm_wolfpelt_mail_coat,
       itm_mail_shirt_grn,itm_mail_shirt_red,itm_nowa,itm_byrnie_b_new,itm_byrnie_e_new,itm_ad_viking_byrnie_06,itm_byrnie2,
       itm_vendel14_2,itm_vendel14,itm_vaegir_mask,itm_gaul_helmet,itm_spangenhelm_helm,itm_rathos_spangenhelm_b,itm_fur_hat,
       itm_spear_1,itm_spear_2,itm_saxonsword,itm_saxon_richsword,itm_le_pictishsword3,
       itm_tab_shield_round_c,itm_viking_shield_round_27,itm_shield_round_01,itm_shield_round_05
     ],
     def_attrib3|level(32),wp(260),knows_warrior_elite,vaegir_face_young_1, vaegir_face_older_2
   ],

   [
     "vaegir_messenger","Horsweala Seaxe","Horswealas Seaxna",
     tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
     [
       itm_leather_gloves,itm_javelin,itm_saddle_horse,
       itm_decorated_leather_shoes_grey,itm_carbatinae_1_grey,itm_mail_boots,itm_decorated_leather_shoes_orange,itm_iron_greaves,
       itm_shirt,itm_roman_shirt,itm_fattiglinenskjortir,itm_wessex_tunic3,itm_bl_tunicsr02,
       itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsleather,
       itm_spear_6,itm_spear_3,itm_langseax,
       itm_shield_heater_c,itm_bl_roundshields_a,itm_norman_shield_1,itm_norman_shield_2,itm_norman_shield_3
     ],
     def_attrib3|agi_21|level(29),wp(200),knows_common|knows_riding_7|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2
   ],

   [
     "vaegir_deserter","Deserter Seaxe","Deserters Seaxna",
     tf_guarantee_shield|tf_guarantee_boots,0,0,fac_deserters,
     [
       itm_javelin,itm_javelin,itm_javelin,itm_javelin,
       itm_carbatinae_1,itm_carbatinae_1_blue,itm_carbatinae_1_grey,
       itm_shirt,itm_roman_shirt,itm_fattiglinenskjortir,itm_wessex_tunic3,itm_bl_tunicsr02,
       itm_woolen_cap_newblu,itm_woolen_cap_newred,itm_woolen_cap_newwht,itm_woolen_cap,
       itm_norman_helmet,itm_leather_cap,itm_bowl_helmet,itm_horn_helmet_2,itm_leather_cap,
       itm_vikingaxeb,itm_saxon_spear,itm_spear_3,itm_lance,itm_langseax,itm_falchion,itm_spear_3,
       itm_ad_viking_shield_round_18,itm_ad_viking_shield_round_19,itm_ad_viking_shield_round_20,
       itm_leathershield_medium_d,itm_leathershield_medium_y,itm_leathershield_medium_b,itm_woodenshield_medium_d
     ],
     def_attrib2|str_10|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1, vaegir_face_older_2
   ],

   [
     "vaegir_prison_guard","Prison Guard","Prison Guards",
     tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_neutral,
     [
       itm_throwing_spears3,itm_leather_gloves,itm_iron_greaves,itm_coat_of_plates9,
       itm_padded_jack_3_trig,itm_padded_jack_6_trig,itm_woolen_cap_newwht,itm_woolen_cap,
       itm_bowl_helmet,itm_horn_helmet_2,itm_leather_cap,itm_spear_1,itm_langseax,itm_shield_heater_c
     ],
     def_attrib3|level(29),wp(200),
     knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2
   ],

   [
     "vaegir_castle_guard","Castle Guard","Castle Guards",
     tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_throwing_spears3,itm_leather_gloves,itm_iron_greaves,itm_coat_of_plates9,
       itm_padded_jack_3_trig,itm_padded_jack_6_trig,itm_woolen_cap_newwht,itm_woolen_cap,
       itm_bowl_helmet,itm_horn_helmet_2,itm_leather_warrior_cap,itm_spear_1,itm_langseax,itm_shield_heater_c
     ],
     def_attrib3|level(29),wp(200),
     knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2
   ],

# pictos
   [
     "khergit_tribesman","Petta (Lig. I.)","Pettas",
     tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
     [
       itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,
       itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
       itm_pictish_hood,itm_head_wrappings,
       itm_koszula_gaelicka,itm_armor_26,itm_shirt,itm_bl_tunicsr01,itm_bl_tunicsr02_2,itm_fattiglinenskjortir,
       itm_bl_tunicsr03_2,itm_shirtb,itm_bl_tunicsr02,
       itm_knife,itm_cudgel,itm_stones,itm_club,itm_quarter_staff,itm_sickle,itm_wooden_stick
     ],
     def_attrib|level(15),wp(110),knows_common,khergit_face_younger_1, khergit_face_old_2
   ],

   [
     "pict_woman","Sept woman (Lig. I.)","Sept women",
     tf_female|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
     [
       itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_sniper_crossbow,itm_flintlock_pistol,
       itm_bare_legs_blue,
       itm_picta_1,itm_picta_2,itm_picta_3,itm_picta_4,itm_picta_5,itm_picta_6,itm_picta_7,itm_picta_8,itm_picta_9,itm_picta_10,
       itm_pictish_hatchet,itm_boar_spear,itm_buckler29,itm_buckler17,itm_buckler18,itm_buckler19,itm_vae_h_shield12,itm_vae_h_shield9
     ],
     def_attrib|level(23),wp(170),knows_warrior_normal|knows_ironflesh_3,khergit_woman_face_1, khergit_woman_face_6
   ],

   [
     "khergit_skirmisher","Saiogdear Picti (Missile)","Saiogdears Picti",
     tf_guarantee_ranged|tf_guarantee_boots,0,0,fac_neutral,
     [
       itm_arrows,itm_bolts,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,itm_hunting_crossbow,
       itm_bare_legs_blue,itm_carbatinae_1_bare,itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,
       itm_vaelicus_tunic_12,itm_vaelicus_tunic_11,itm_vaelicus_tunic_10,itm_vaelicus_tunic_7,itm_vaelicus_tunic_5,
       itm_vaelicus_tunic_4,itm_vaelicus_tunic_1,itm_vaelicus_tunic_9,itm_thick_coat,itm_coat_with_cape,
       itm_pictish_hatchet,itm_cudgel,itm_scianshort,itm_scianshortbone
     ],
     basic_ranged_attrib|level(19),wp(60)|wp_archery(140)|wp_crossbow(140),
     knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,khergit_face_younger_1, khergit_face_old_2
   ],

   [
     "khergit_horseman","Boaire (Lig. I.)","Boaires",
     tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_neutral,
     [
       #itm_throwing_knives,itm_throwing_knives,
       itm_javelin,itm_sniper_crossbow,itm_flintlock_pistol,
       itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
       itm_pictish_hood,itm_head_wrappings,itm_common_hood,
       itm_pict_tunic7,itm_pict_tunic6,itm_dane_tunic1,itm_green_tunic,itm_vaelicus_tunic_1,itm_tunic_b,
       itm_vaelicus_tunic_2,itm_bl_tunicsr03,itm_koszula_gaelicka,
       itm_pictish_hatchet,itm_boar_spear,itm_vae_h_shield10,itm_vae_h_shield11,itm_vae_cuadrado_15,
       itm_buckler27,itm_buckler26,itm_buckler2,itm_buckler3,itm_buckler4,itm_buckler5
     ],
     def_attrib2|level(19),wp(140),
     knows_warrior_basic|knows_ironflesh_2|knows_power_strike_2,khergit_face_young_1, khergit_face_older_4
   ],

   [
     "khergit_horse_archer","Fuidir (Skrm.)","Fuidirs",
     tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_boots,0,0,fac_neutral,
     [
       itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
       itm_sniper_crossbow,itm_flintlock_pistol,itm_heavy_crossbow,
       itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
       itm_war_paint_two,itm_long_mail_coat,itm_mail_with_tunic_red,itm_hide_coat,itm_linen_shirt,itm_wool_coat,
       itm_dress,itm_picto_gordo1,itm_war_paint_two_5,itm_pelt_coat,
       itm_pictish_hatchet,itm_boar_spear,itm_scianshortbone,itm_scianshort,
       itm_vae_cuadrado_18,itm_vae_h_shield7,itm_vae_h_shield6,itm_vae_h_shield12,
       itm_vae_cuadrado_10,itm_vae_cuadrado_11,itm_vae_cuadrado_12
     ],
     def_attrib2|level(20),wp(140)|wp_throwing(170),
     knows_warrior_normal|knows_ironflesh_4|knows_power_strike_4,khergit_face_young_1, khergit_face_older_4
   ],

   [
     "fuidir_elite","Eite Fuidir (Elit. Skrm.)","Elite Fuidirs",
     tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_neutral,
     [
       itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
       itm_carbatinae_2_bare,itm_carbatinae_1_bare,
       itm_head_wrappings,itm_common_hood,
       itm_war_paint_two,itm_long_mail_coat,itm_mail_with_tunic_red,itm_hide_coat,itm_linen_shirt,itm_wool_coat,
       itm_dress,itm_picto_gordo1,itm_war_paint_two_5,itm_war_paint_two_2,
       itm_irish_sword,itm_scianshortbone,itm_scianshort,itm_scianlong,itm_scianlongbone,
       itm_vae_cuadrado_19,itm_vae_cuadrado_20,itm_vae_cuadrado_21,itm_vae_cuadrado_3,itm_vae_cuadrado_4,itm_vae_cuadrado_5,
       itm_h_shield,itm_vae_h_shield1,itm_vae_h_shield2,itm_vae_h_shield3
     ],
     def_attrib2|level(25),wp(185)|wp_throwing(230),
     knows_warrior_veteran|knows_ironflesh_4|knows_power_strike_4,khergit_face_young_1, khergit_face_older_4
   ],

   [
     "picto_portaestandarte","Samhladh","Samhladh",
     tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
       itm_war_paintus,itm_1celtbody,itm_2celtbody,itm_3celtbody,itm_5celtbody,itm_6celtbody,itm_mail_with_tunic_red,itm_war_paint_two_2,
       itm_wessexbanner6,itm_personalbanner,
       itm_war_paint_two,itm_war_paintus,itm_trophy_b
     ],
     def_attrib2|level(23),wp(165),knows_warrior_normal,khergit_face_young_1, khergit_face_older_4
   ],

   [
     "picto_cuerno","Hornman","Hornmen",
     tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
       itm_war_paintus_2,itm_war_paintus_3,itm_war_paintus_4,itm_war_paintus_5,itm_war_paintus_6,itm_war_paintus_7,itm_war_paintus_8,
       itm_horn,itm_buckler27,itm_buckler26,itm_buckler29,itm_buckler2,itm_buckler3,itm_buckler4,itm_buckler5,itm_trophy_a
     ],
     def_attrib2|level(15),wp(110),knows_warrior_normal,khergit_face_young_1, khergit_face_older_4
   ],

   [
     "picto_sacerdote","Cleric","Clergy",
     tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
     [
       itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
       itm_blue_gambeson,itm_sarranid_cavalry_robe,itm_stones,itm_staff
     ],
     def_attrib|level(23),wp(165),knows_cleric,khergit_face_young_1, khergit_face_older_4
   ],

   [
     "khergit_veteran_horse_archer","Creach Sluagh (Med. I.)","Creach Sluagh",
     tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_boots,0,0,fac_neutral,
     [
       itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
       itm_carbatinae_2_bare,itm_carbatinae_1_bare,
       itm_pelt_coat2,itm_blue_dress,itm_tabard,itm_merchant_outfit,itm_homespun_dress,
       itm_thick_coat,itm_mail_with_tunic_green,itm_picto_gordo3,itm_war_paintus_10,itm_war_paintus_11,itm_war_paintus_12,
       itm_war_spear,itm_spear,itm_twohand_spear,itm_scianshortbone,itm_scianshort,itm_scianlong,
       itm_shield_small_round,itm_vae_cuadrado_13,itm_vae_cuadrado_14,itm_vae_cuadrado_16,itm_vae_h_shield4,
       itm_vae_h_shield5,itm_vae_h_shield6,itm_vae_h_shield7,
       itm_celtic_shield_small_round_a,itm_celtic_shield_small_round_b,itm_vae_escudo_picto12
     ],
     def_attrib2|level(23),wp(170),
     knows_warrior_normal|knows_ironflesh_4|knows_power_strike_4,khergit_face_middle_1, khergit_face_older_4
   ],

   [
     "khergit_lancer","Diuberr (Hv. I.)","Diuberrs",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,
     [
       itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
       itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
       itm_tribal_warrior_outfit,itm_nomad_robe,itm_nordic_outfit,itm_vaelicus_tunic_10,itm_nordic_outfit2,itm_braz,itm_czerwony,
       itm_vaelicus_t_19,itm_lamellar_vest_khergit,itm_padded_jack_3_trig,
       itm_leather_steppe_cap_b,itm_leather_steppe_cap_c,itm_rathos_bowl_helmet,itm_bowl_helmet,
       itm_spear_7,itm_club_with_spike_head,itm_spear,itm_twohand_spear,itm_irish_sword,itm_scianshort,itm_war_spear,
       itm_vae_cuadrado_17,itm_vae_cuadrado_27,itm_tarcze_celtyckie,itm_pict_shield_a,itm_tab_shield_round_c,
       itm_celtic_vae_shield6,itm_vae_h_shield8,itm_vae_h_shield9,itm_celtic_shield_small_round_d,itm_celtic_shield_small_round_e
     ],
     def_attrib3|level(27),wp(200),
     knows_warrior_veteran|knows_ironflesh_5|knows_power_strike_5,khergit_face_middle_1, khergit_face_older_4
   ],

   [
     "picti_bruide","Bruide (Hv. I.)","Bruides",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_neutral,
     [
       itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
       itm_leather_gloves,itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
       itm_heraldric_armor,itm_studded_leather_coat,itm_sleeveless_tunic,itm_gairlom,itm_tuniczka,
       itm_padded_jack_4_trig,itm_padded_jack_6_trig,itm_heraldic_mail_with_tabard,
       itm_skull_cap_new_c,itm_leather_steppe_cap_b,itm_bowl_helmet_nasal,itm_bowl_helmet,
       itm_irish_sword,itm_le_pictishsword6,itm_le_pictishsword5,itm_scianshortbone,
       itm_tab_shield_round_c,itm_vae_cuadrado_22,itm_vae_cuadrado_23,itm_vae_cuadrado_24,
       itm_vae_cuadrado_25,itm_vae_cuadrado_26,itm_celtic_vae_shield7,itm_celtic_vae_shield8,
       itm_celtic_shield_small_round_f,itm_celtic_shield_small_round_e,itm_vae_cuadrado_28
     ],
     def_attrib3|level(27),wp(200),
     knows_warrior_veteran|knows_ironflesh_5|knows_power_strike_5,khergit_face_young_1, khergit_face_older_4
   ],

   [
     "picti_gaisgidh","Gaisgidh (Elit. I.)","Gaisgidhs",
     tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,
     [
       itm_throwing_spears,itm_throwing_spears,itm_throwing_spears,
       itm_leather_gloves,itm_carbatinae_2_greaves_orange,itm_splinted_leather_greaves,
       itm_mail_shirt_grn,itm_mail_shirt_wht,itm_hauberk5,itm_mail_shirtbluewhite,itm_byrnie8,
       itm_lamellar_vest,itm_lamellar_vest_khergit,itm_mail_shirt_redhorses,itm_mail_shirt_red,
       itm_briton_helm,itm_vaegir_war_helmet,itm_briton_helm3,itm_szpadelhelmet3,itm_szpadelhelmet4,itm_szpadelhelmet5,
       itm_pictish_longsword,itm_celticshort1_1,itm_celticshort1_2,itm_scianshort,itm_vae_caledonian_shield6,
       itm_vae_caledonian_shield7,itm_vae_caledonian_shield8,itm_vae_cuadrado_6,itm_celtic_shield_small_round_a,
       itm_celtic_shield_small_round_b,itm_celtic_shield_small_round_c,itm_celtic_shield_small_round_d,itm_celtic_vae_shield9,
       itm_celtic_vae_shield10
     ],
     def_attrib3|level(29),wp(230),
     knows_warrior_elite|knows_ironflesh_7|knows_power_strike_7,khergit_face_young_1, khergit_face_older_4
   ],

   [
     "picti_each","Each Raidh (Lig. C.","Each Raidhs",
     tf_mounted|tf_guarantee_all,0,0,fac_neutral,
     [
       itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
       itm_sumpter_horse,itm_warhorse_sarranid3,itm_arabian_horse_a,itm_steppe_horse,itm_charger,
       itm_saddle_horse,itm_normal_horse29,itm_normal_horse31,
       itm_bare_legs_blue,itm_decorated_leather_shoes_bare,
       itm_mail_with_tunic_green,itm_picto_gordo2,itm_vae_thick_coat10,itm_vae_thick_coat6,itm_vae_thick_coat3,
       itm_vae_thick_coat2,itm_vae_thick_coat1,itm_pelt_coat,itm_pelt_coat2,
       itm_scythe,itm_sarranid_axe_b,itm_scianshortbone,itm_scianlongbone,itm_hand_axe,itm_irish_long_sword,
       itm_celtic_vae_shield5,itm_celtic_vae_shield7, itm_h_shield,itm_vae_h_shield1,itm_vae_h_shield2,
       itm_vae_h_shield3,itm_vae_h_shield4,itm_vae_h_shield5,itm_vae_caledonian_shield12
     ],
     def_attrib2|level(23),wp(170),
     knows_warrior_normal|knows_ironflesh_4|knows_power_strike_4,khergit_face_young_1, khergit_face_older_4
   ],

   [
     "picti_airig","Airig (Hv. C.)","Arras",
     tf_mounted|tf_guarantee_all,0,0,fac_neutral,
     [
       itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
       itm_hunter,itm_warhorse,itm_warhorse_sarranid3,itm_arabian_horse_a,itm_steppe_horse,itm_saddle_horse,itm_normal_horse29,
       itm_bare_legs_blue,itm_carbatinae_2_bare,itm_yellow2,itm_yellow1,itm_vaelicus_t_9,itm_courtly_outfit,itm_arabian_armor_b,
       itm_lamellar_vest_khergit,itm_mail_shirtbluewhite,
       itm_rathos_bowl_helmet,itm_briton_helm5,itm_szpadelhelmet2,itm_vaegir_war_helmet, itm_scythe,itm_scianshort,
       itm_celticshort1_1,itm_irish_long_sword,
       itm_vae_h_shield11,itm_vae_h_shield12,itm_vae_cuadrado_7,itm_caledonian_shield,itm_caledonian_shield_dog,
       itm_caledonian_shield_raven,itm_square_shield,itm_vae_caledonian_shield1,itm_vae_caledonian_shield2,
       itm_vae_caledonian_shield3,itm_vae_caledonian_shield4,itm_vae_caledonian_shield5
     ],
     def_attrib3|level(27),wp(200),
     knows_warrior_veteran|knows_riding_5|knows_ironflesh_5|knows_power_strike_5,khergit_face_young_1, khergit_face_older_4
   ],

   [
     "khergit_messenger","Picti Messenger","Picti Messengers",
     tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
     [
       itm_hunter,itm_javelin,itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
       itm_linen_shirt,itm_wool_coat,itm_dress,itm_blue_dress,itm_tabard,itm_long_mail_coat,itm_mail_with_tunic_red,
       itm_sarranid_axe_b,itm_scianshortbone,itm_scianshort,itm_scianlong,
       itm_vae_cuadrado_8,itm_vae_cuadrado_9,itm_vae_cuadrado_10,itm_vae_cuadrado_11,itm_vae_cuadrado_12,itm_vae_cuadrado_13
     ],
     def_attrib3|agi_21|level(29),wp(170),
     knows_common|knows_riding_7|knows_power_draw_3|knows_horse_archery_5,khergit_face_young_1, khergit_face_older_4
   ],

   [
     "khergit_deserter","Picti Deserter","Picti Deserters",
     tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_deserters,
     [
       itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
       itm_carbatinae_2_bare,itm_carbatinae_1_bare,
       itm_vaelicus_tunic_11,itm_vaelicus_tunic_7,itm_war_paint_two,itm_picto_gordo3,itm_mail_with_tunic_green,
       itm_hide_coat,itm_merchant_outfit,itm_homespun_dress,
       itm_norman_helmet,itm_rathos_bowl_helmet,itm_bowl_helmet_nasal,
       itm_club_with_spike_head,itm_spear,itm_twohand_spear,itm_scianshortbone,itm_scianshort,
       itm_vae_caledonian_shield9,itm_vae_caledonian_shield10,itm_vae_caledonian_shield11,itm_vae_escudo_picto10,
       itm_vae_escudo_picto12,itm_vae_cuadrado_8,itm_vae_cuadrado_9,itm_vae_cuadrado_10,itm_vae_cuadrado_11,itm_vae_cuadrado_12
     ],
     def_attrib2|level(23),wp(170),
     knows_warrior_normal|knows_ironflesh_5|knows_power_strike_5,khergit_face_young_1, khergit_face_older_4
   ],

   [
     "khergit_prison_guard","Prison Guard","Prison Guards",
     tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_neutral,
     [
       itm_javelin,itm_leather_gloves,itm_bare_legs_blue,itm_nordic_outfit,itm_gairlom,itm_tuniczka,
       itm_padded_jack_6_trig,itm_bowl_helmet,itm_irish_sword,itm_scianshort,itm_vae_cuadrado_3,
       itm_vae_caledonian_shield9,itm_vae_caledonian_shield10,itm_vae_caledonian_shield11
     ],
     def_attrib3|level(29),wp(200),
     knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,khergit_face_middle_1, khergit_face_older_4
   ],

  [
    "khergit_castle_guard","Castle Guard","Castle Guards",
    tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
    [
      itm_javelin,itm_leather_gloves,itm_bare_legs_blue,itm_nordic_outfit,itm_gairlom,itm_tuniczka,
      itm_padded_jack_6_trig,itm_bowl_helmet,itm_irish_sword,itm_scianshort,itm_vae_cuadrado_3,itm_vae_cuadrado_4,
      itm_vae_cuadrado_5,itm_vae_cuadrado_6,itm_vae_cuadrado_7
    ],
    def_attrib3|level(29),wp(200),
    knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,khergit_face_middle_1, khergit_face_older_4
  ],

   # Anglos
  [
    "nord_recruit","Gebur Engle (Lig. I.)","Geburas Engles",
    tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
    [
      itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,
      itm_ankle_boots,itm_wrapping_boots,
      itm_woolen_cap_newred,itm_woolen_cap_newgrn,itm_woolen_cap_newblk,itm_woolen_cap,
      itm_shirt,itm_roman_shirt,itm_fattiglinenskjortir,itm_bl_tunicsr01_2,itm_bl_tunicsr02,
      itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsr01,itm_fat_body,
      itm_knife,itm_pitch_fork,itm_battle_fork,itm_quarter_staff,itm_sickle,itm_hatchet
    ],
    def_attrib|level(15),wp(110),knows_warrior_basic, nord_face_young_1, nord_face_old_2
  ],

  [
    "nord_footman","Kotsetla Engle (Lig. I.)","Kotsetlas Engles",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_sniper_crossbow,itm_flintlock_pistol,itm_heavy_crossbow,
      itm_ankle_boots,itm_wrapping_boots,
      itm_woolen_cap_newblu,itm_woolen_cap_newgrn,
      itm_piel_coat01,itm_piel_coat06,itm_piel_coat03,
      itm_shirt,itm_wessex_tunic3,itm_mercia_tunic1,itm_peasant_man_f,itm_leather_jerkin,
      itm_idi_furjacket1,itm_idi_furjacket2,itm_idi_furjacket3,
      itm_palka3,itm_palka4,itm_cudgel,itm_axefaradon2,
      itm_buckler15,itm_buckler16,itm_buckler28,itm_buckler32,itm_buckler42
    ],
    def_attrib2|level(19),wp(140),knows_warrior_basic, nord_face_young_1, nord_face_old_2
  ],

  [
    "nord_trained_footman","Geneata Engle (Med. I.)","Geneatas Engles",
    tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_neutral,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_carbatinae_1,itm_carbatinae_2,itm_carbatinae_2_green,itm_carbatinae_1_orange,
      itm_blue_short_tunic2,itm_bluevikingshirt,itm_mercia_tunic10,itm_wessex_tunic4,
      itm_coat_of_plates9,itm_leather_vest_red,itm_pelt_coat2,itm_idi_furjacket5,itm_idi_furjacket6,
      itm_lui_battleaxetwoh,itm_saxon_spear,itm_spear_3,itm_langseax,itm_falchion,itm_spear_3,
      itm_ad_viking_shield_round_35,itm_ad_viking_shield_round_36,itm_ad_viking_shield_round_37,
      itm_ad_viking_shield_round_38,itm_ad_viking_shield_round_39,itm_ad_viking_shield_round_40,
      itm_ad_viking_shield_round_41,itm_ad_viking_shield_round_42
    ],
    def_attrib2|level(23),wp(170),knows_warrior_normal,nord_face_young_1, nord_face_old_2
  ],

  [
    "nord_warrior","Geoguth Engle (Med. I.)","Geoguthas Engles",
    tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_carbatinae_2_green,itm_carbatinae_1_blue,itm_carbatinae_2_orange,
      itm_bl_tunicsleather_3,itm_bl_tunicsleather,itm_bl_tunicsleather_2,
      itm_leather_vest_green,itm_coat_of_plates1,itm_leather_vest_blue,itm_coat_of_plates3,itm_coat_of_plates5,
      itm_spear_6,itm_spear_3,itm_langseax,
      itm_viking_shield_round_27,itm_viking_shield_round_28,itm_viking_shield_round_17,itm_viking_shield_round_33,
      itm_viking_shield_round_26,itm_viking_shield_round_34,itm_shield_ocho,itm_steel_shield
    ],
    def_attrib2|level(23),wp(170),knows_warrior_normal,nord_face_young_1, nord_face_old_2
  ],

  [
    "anglo_portaestandarte","Tacnberend","Tacnberend",
    tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
    [
      itm_carbatinae_1_grey,itm_carbatinae_1_green,itm_carbatinae_1_orange,itm_carbatinae_2_orange,
      itm_piel_coat02,itm_piel_coat04,itm_piel_coat05,
      itm_roman_shirt,itm_fattiglinenskjortir,itm_wessex_tunic3,itm_bl_tunicsr02,
      itm_mercia_tunic1,itm_blue_short_tunic,
      itm_goat_cap,itm_felt_steppe_cap,itm_boar_helmet,itm_nomad_cap,
      itm_wessexbanner2,itm_personalbanner,itm_wessexbanner3,itm_trophy_b,itm_leather_gloves,itm_helm_captaina
    ],
    def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1, vaegir_face_old_2
  ],

  [
    "anglo_sacerdote","Cleric Engle","Cleric Engles",
    tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
    [
      itm_decorated_leather_shoes,itm_carbatinae_2,itm_decorated_leather_shoes_green,
      itm_decorated_leather_shoes_blue,itm_carbatinae_2_blue,
      itm_blue_gambeson,itm_skirmisher_armor,
      itm_stones,itm_staff
    ],
    def_attrib|level(23),wp(165),knows_cleric,sac_face_1, sac_face_2
  ],

  [
    "anglo_pagano","Woden Priest","Woden Priests",
    tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_neutral,
    [
      itm_carbatinae_2_blue,itm_decorated_leather_shoes_grey,itm_carbatinae_1_grey,
      itm_goat_cap,itm_felt_steppe_cap,itm_boar_helmet,
      itm_sarranid_cloth_robe,itm_robe,
      itm_stones,itm_staff
    ],
    def_attrib|level(23),wp(165),knows_cleric,sac_face_1, sac_face_2
  ],

  [
    "nord_veteran","Beadu rinc Engle (Med. I.)","Beadu rincas Engles",
    tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_neutral,
    [
      itm_throwing_spears3,itm_javelin,itm_throwing_spears4,itm_javelin,
      itm_carbatinae_2_blue,itm_carbatinae_2_grey,
      itm_piel_coat01,itm_piel_coat03,itm_bl_boar_fur,
      itm_bl_tunic03,itm_redvikingshirt,itm_redtunic,itm_bl_tunic03,itm_leather_armor_c2,
      itm_leather_armor_c,itm_vae_thick_coat2,itm_vae_thick_coat3,itm_tattered_leather_armor_gr,
      itm_rathos_bowl_helmet,itm_bowl_helmet,itm_sarranid_helmet1,itm_horn_helmet_3,itm_khergit_cavalry_helmet,
      itm_dagger,itm_saxon_axe,itm_axe,itm_spear_3,itm_spear_2,itm_lui_battleaxetwoh,
      itm_ad_viking_shield_round_31,itm_ad_viking_shield_round_32,itm_ad_viking_shield_round_43,
      itm_ad_viking_shield_round_34,itm_ad_viking_shield_round_36,itm_ad_viking_shield_round_37,
      itm_ad_viking_shield_round_38,itm_ad_viking_shield_round_39
    ],
    def_attrib3|level(25),wp(185),knows_warrior_veteran,nord_face_young_1, nord_face_old_2
  ],

  [
    "nord_champion","Gesith Engle (Lig. C.)","Gesithas Engles",
    tf_mounted|tf_guarantee_all,0,0,fac_neutral,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_saddle_horse,itm_steppe_horse,itm_charger,itm_normal_horse24,itm_normal_horse25,itm_normal_horse26,
      itm_decorated_leather_shoes_green,itm_decorated_leather_shoes_blue,itm_carbatinae_2_blue,
      itm_padded_leather_blue,itm_padded_leather_brown,itm_byrnie,itm_mail_shirthre,itm_mail_shirtredwhite,itm_mail_shirt_1_trig,
      itm_vaegir_war_helmet,itm_briton_helm,itm_briton_helm2,itm_magyar_helmet_a,itm_vaegir_mask,itm_talak_spangenhelm,
      itm_horn_helmet,itm_horn_helmet_3,
      itm_hunting_dagger,itm_new_sword3,itm_spear_8,itm_spear_4,
      itm_saxon_adorno_20,itm_saxon_adorno_1,itm_saxon_adorno_2,itm_tab_shield_small_round_c
    ],
    def_attrib3|level(27),wp(200),knows_warrior_veteran,nord_face_young_1, nord_face_old_2
  ],

  [
    "nord_huntsman","Sceotand Engle (Missile)","Sceotandas Engles",
    tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
    [
      itm_arrows,itm_short_bow,itm_short_bow,itm_short_bow,itm_hunting_bow,
      itm_ankle_boots,itm_wrapping_boots,
      itm_leather_steppe_cap_a,itm_roman_shirt,itm_fattiglinenskjortir,itm_bl_tunicsr01_2,itm_bl_tunicsr02,
      itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsr01,
      itm_cudgel,itm_dagger,itm_axe
    ],
    basic_ranged_attrib|str_10|level(15),wp(40)|wp_archery(110),
    knows_ironflesh_1|knows_power_draw_2|knows_power_throw_1,nord_face_young_1, nord_face_old_2
  ],

  [
    "nord_archer","Rigwiga Engle (Hv. I.)","Ridwigas Engles",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_neutral,
    [
      itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
      itm_leather_gloves,itm_decorated_leather_shoes_grey,itm_iron_greaves,
      itm_tattered_leather_armor_ylw,itm_padded_leather_blue,itm_ad_viking_byrnie_02,itm_ad_viking_byrnie_04,
      itm_ad_viking_byrnie_06,itm_mail_shirt_9_trig,itm_mail_shirt_2_trig,
      itm_horn_helmet,itm_horn_helmet_2,itm_spangenhelm_helm,itm_vendel_helmet2,itm_briton_helm4,itm_briton_helm3,
      itm_nordic_veteran_archer_helmet,itm_footman_helmet,
      itm_scimitar,itm_new_sword3,itm_le_pictishsword3,itm_saxonsword,itm_le_richsword1,
      itm_ad_viking_shield_round_15,itm_ad_viking_shield_round_30,itm_saxon_adorno_20,itm_saxon_adorno_1,
      itm_saxon_adorno_2,itm_saxon_adorno_3,itm_saxon_adorno_4,itm_saxon_adorno_5
    ],
    def_attrib3|level(27),wp(200),knows_warrior_veteran,nord_face_young_1, nord_face_old_2
  ],

  [
    "nord_veteran_archer","Duguth Engle (Hv. I.)","Duguthas Engles",
    tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_neutral,
    [
      itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
      itm_decorated_leather_shoes_blue,itm_carbatinae_2_blue,itm_mail_boots,
      itm_noblemanshirt_gaelic,itm_noblemanshirt_pictish,
      itm_leather_vest_red,itm_coat_of_plates8,itm_coat_of_plates9,itm_padded_jack_3_trig,itm_tattered_leather_armor_blk,
      itm_mail_shirt_8_trig,itm_mail_shirt_7_trig,itm_mail_shirt_4_trig,
      itm_woolen_cap_newwht,itm_woolen_cap,
      itm_norman_helmet,itm_rathos_bowl_helmet,itm_leather_cap,itm_leather_steppe_cap_b,
      itm_spear_1,itm_le_bamburghsword,itm_langseax,
      itm_viking_shield_round_27,itm_viking_shield_round_28,itm_viking_shield_round_17,itm_viking_shield_round_33,
      itm_viking_shield_round_26,itm_viking_shield_round_34,itm_shield_ocho,itm_steel_shield
    ],
    def_attrib3|level(27),wp(200),knows_warrior_veteran,nord_face_young_1, nord_face_old_2
  ],

  [
    "engle_hearth","Hearthweru Engle (Elit. I.)","Hearthweruas Engles",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,
    [
      itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
      itm_leather_gloves,
      itm_carbatinae_1_greaves_blue,itm_decorated_leather_shoes_grey,itm_splinted_leather_greaves,
      itm_padded_jack_8_trig,itm_heraldic_mail_with_tunic,itm_mail_coat_2_trig,itm_mail_shirtdeer,
      itm_mail_shirt_grn,itm_mail_shirt_red,itm_byrnie_e_new,itm_byrnie2,
      itm_vaegir_war_helmet,itm_briton_helm,itm_briton_helm5,itm_flat_topped_helmet,itm_talak_spangenhelm,
      itm_vaegir_mask,itm_briton_helm4,itm_bascinet_3,
      itm_spear_1,itm_spear_2,itm_new_sword4,itm_new_sword3,itm_le_richsword1,
      itm_tab_shield_round_c
    ],
    def_attrib3|level(32),wp(260),knows_warrior_elite,nord_face_young_1, nord_face_old_2
  ],

  [
    "nord_messenger","Horsweala Engle","Horswealas Engles",
    tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
    [
      itm_leather_gloves,itm_normal_horse30,
      itm_decorated_leather_shoes,itm_carbatinae_2,itm_decorated_leather_shoes_green,
      itm_decorated_leather_shoes_grey,itm_decorated_leather_shoes_orange,
      itm_wessex_tunic3,itm_bl_tunicsr02,itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsleather,
      itm_spear_6,itm_spear_3,itm_langseax,
      itm_viking_shield_round_26,itm_viking_shield_round_34,itm_shield_ocho,itm_steel_shield
    ],
    def_attrib3|agi_21|level(29),wp(215),knows_common|knows_riding_7|knows_power_throw_2,nord_face_young_1, nord_face_old_2
  ],

  [
    "nord_deserter","Deserter Engle","Deserters Engles",
    tf_guarantee_shield|tf_guarantee_boots,0,0,fac_deserters,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_carbatinae_2_grey,itm_carbatinae_1_grey,
      itm_wessex_tunic3,itm_bl_tunicsr02,itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsleather,
      itm_woolen_cap_newblu,itm_woolen_cap_newred,itm_woolen_cap_newwht,itm_woolen_cap,
      itm_bowl_helmet,itm_horn_helmet_2,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
      itm_lui_battleaxetwoh,itm_saxon_spear,itm_spear_3,itm_lance,itm_langseax,itm_falchion,itm_spear_3,
      itm_ad_viking_shield_round_38,itm_ad_viking_shield_round_39,itm_ad_viking_shield_round_40,
      itm_ad_viking_shield_round_41,itm_ad_viking_shield_round_42,itm_ad_viking_shield_round_43
    ],
    def_attrib2|str_10|level(23),wp(170),knows_warrior_normal,nord_face_young_1, nord_face_old_2
  ],

  [
    "nord_prison_guard","Prison Guard","Prison Guards",
    tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_neutral,
    [
      itm_throwing_spears3,itm_leather_gloves,itm_decorated_leather_shoes_green,itm_noblemanshirt_pictish,
      itm_padded_jack_3_trig,itm_padded_jack_6_trig,itm_woolen_cap_newred,
      itm_norman_helmet,itm_leather_steppe_cap_b,itm_spear_1,itm_langseax,itm_viking_shield_round_27
    ],
    def_attrib3|level(29),wp(200),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2
  ],

  [
    "nord_castle_guard","Castle Guard","Castle Guards",
    tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
    [
      itm_throwing_spears3,itm_leather_gloves,itm_decorated_leather_shoes_green,itm_noblemanshirt_pictish,
      itm_padded_jack_3_trig,itm_padded_jack_6_trig,itm_woolen_cap_newred,
      itm_norman_helmet,itm_leather_steppe_cap_b,itm_spear_1,itm_langseax,itm_viking_shield_round_27
    ],
    def_attrib3|level(29),wp(200),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2
  ],

   # irlandeses
  [
    "rhodok_tribesman","Bothach (Lig. I.)","Bothach",
    tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
    [
      itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
      itm_hood_newwht,itm_black_hood,
      itm_roman_shirt,itm_tunic_a,itm_koszula_gaelicka,itm_shirtc,itm_koszula_gaelicka,
      itm_shirtd,itm_bl_tunicsr01,itm_fat_body,
      itm_knife,itm_pitch_fork,itm_cudgel,itm_battle_fork,itm_quarter_staff,itm_sickle
    ],
    def_attrib|level(15),wp(110),knows_common,rhodok_face_younger_1, rhodok_face_old_2
  ],

  [
    "rhodok_crossbowman","Saiogdear Goidel (Missile)","Saiogdears Goidels",
    tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
    [
      itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
      itm_carbatinae_2_bare,itm_carbatinae_1_bare,
      itm_hood_newwht,itm_black_hood,itm_head_wrappings,itm_common_hood,
      itm_leather_vest,itm_steppe_armor,itm_gambeson,itm_tunic_a,itm_koszula_gaelicka,
      itm_bl_tunicsr03,itm_bl_tunicsr03_2,itm_bl_tunicsr01,itm_vaelicus_tunic_3,itm_tunic_c,
      itm_club,itm_scianshort,itm_scianshortbone
    ],
    basic_ranged_attrib|level(19),wp(60)|wp_archery(140),
    knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2
  ],

  [
    "rhodok_spearman","Ceither (Lig. I.)","Ceithers",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,
    [
      #itm_darts,itm_darts,itm_throwing_knives,itm_throwing_knives,
      itm_sniper_crossbow,itm_flintlock_pistol,
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
      itm_black_hood,itm_common_hood,itm_celta_capa1,itm_celta_capa2,itm_red_cloak,
      itm_armor_9,itm_shirtb,itm_shirte,itm_koszula_gaelicka,itm_leather_coat,itm_mail_coat,
      itm_vaelicus_tunic_6,itm_vaelicus_tunic_8,itm_vaelicus_tunic_9,
      itm_scianshortbone,itm_scianshort,itm_cudgel,itm_buckler20,itm_buckler21,itm_buckler22,
      itm_buckler23,itm_buckler24,itm_tarcza_harfa_vae_20
    ],
    def_attrib2|level(19),wp(140),
    knows_warrior_basic|knows_ironflesh_3|knows_power_strike_3,rhodok_face_young_1, rhodok_face_old_2
  ],

  [
    "rhodok_trained_spearman","Cliarthaire (Med. I.)","Cliarthaires",
    tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_neutral,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_carbatinae_2_bare,itm_decorated_leather_shoes_bare,
      itm_courtly_outfit,itm_nomad_armor,itm_nomad_vest,itm_leather_jacket,itm_pict_tunic5,
      itm_vaelicus_tunic_6,itm_koszula_gaelicka,itm_bl_tunic08,itm_bl_tunic11,itm_bl_tunic05,
      itm_scianshortbone,itm_one_handed_war_axe_a,itm_military_fork,itm_sarranid_two_handed_axe_a,itm_club_with_spike_head,
      itm_vae_escudo_picto7,itm_vae_escudo_picto8,itm_vae_escudo_picto9,itm_vae_escudo_picto10,itm_tarcza_harfa_vae_21,
      itm_vae_escudo_picto12,itm_vae_escudo_picto13,itm_vae_escudo_picto27,itm_vae_escudo_picto28,itm_shield_ip
    ],
    def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2
  ],

  [
    "gael_portaestandarte","Meirgeach","Meirgeach",
    tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
    [
      itm_bare_legs_blue,itm_decorated_leather_shoes_bare,
      itm_celta_capa1,itm_celta_capa2,
      itm_nobleman_outfit,itm_ragged_outfit,itm_pict_tunic7,itm_pict_tunic6,itm_pict_tunic7,
      itm_vaelicus_t_35,itm_vaelicus_t_36,
      itm_wessexbanner7,itm_wessexbanner8,itm_personalbanner,itm_trophy_b
    ],
    def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1, vaegir_face_old_2
  ],

  [
    "gael_sacerdote","Cleric Goidel","Cleric Goidels",
    tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
    [
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
      itm_blue_gambeson,itm_archers_vest,
      itm_stones,itm_knife
    ],
    def_attrib|level(23),wp(165),knows_cleric,sac_face_1, sac_face_2
  ],

  [
    "rhodok_veteran_spearman","Fian (Skrm.)","Fianna",
    tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_neutral,
    [
      itm_darts,itm_throwing_knives,itm_javelin_jinetes,
      itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
      itm_nomad_vest,itm_ragged_outfit,itm_nordic_armor,itm_hide_armor,itm_bl_tunic07,itm_bl_tunic11,
      itm_bl_tunic06,itm_vae_thick_coat1,itm_gatheredcloaks4,itm_vaelicus_t_25,
      itm_leather_cap,itm_skull_cap_new_c,itm_head_wrappings,
      itm_scianshort,itm_one_handed_war_axe_a,itm_war_spear,
      itm_tab_shield_round_c,itm_celtic_shield_small_round_a,itm_buckler25,itm_vae_escudo_picto11,
      itm_tarcza_harfa_vae_9,itm_tarcza_harfa_vae_10,itm_tarcza_harfa_vae_11,itm_tarcza_harfa_vae_12
    ],
    def_attrib2|level(23),wp(170)|wp_throwing(200),
    knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2
  ],

  [
    "gael_deaisbard","Deaisbard (Elit. Skrm.)","Deaisbards",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,
    [
      itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
      itm_carbatinae_2_bare,itm_carbatinae_1_bare,
      itm_nobleman_outfit,itm_fur_coat,itm_vaelicus_t_25,itm_vaelicus_t_27,itm_sarranid_elite_armor,
      itm_vaegir_elite_armor,itm_brigandine_red,itm_mail_with_surcoat,itm_surcoat_over_mail,
      itm_skull_cap_new_c,itm_leather_steppe_cap_c,itm_celtycka_lebka,itm_celtycka_iron,
      itm_scianshortbone,itm_celticv2_1,itm_celticv2_2,itm_irishword2,itm_celtic1,
      itm_tab_shield_round_c,itm_tarcza_harfa_vae_13,itm_tarcza_harfa_vae_14,itm_tarcza_harfa_vae_15,
      itm_scyld8,itm_scyld9,itm_tarcza_harfa_vae_18,itm_tarcza_harfa_vae_19
    ],
    def_attrib3|level(27),wp(200)|wp_throwing(260),
    knows_warrior_veteran,rhodok_face_young_1, rhodok_face_older_2
  ],

  [
    "rhodok_trained_crossbowman","Ocaire (Med. I.)","Ocaires",
    tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_carbatinae_2_bare,itm_carbatinae_1_bare,
      itm_nordiclightarmor4,itm_nordiclightarmor5,itm_nordiclightarmor6,itm_nordiclightarmor7,
      itm_nordiclightarmor8,itm_gatheredcloaks1,itm_gatheredcloaks2,itm_gatheredcloaks3,itm_gatheredcloaks5,
      itm_skull_cap_new_c,itm_leather_cap,itm_bowl_helmet,
      itm_scianshortbone,itm_war_spear,itm_spear,itm_celtic1,
      itm_vae_escudo_picto,itm_vae_escudo_picto2,itm_vae_escudo_picto3,itm_vae_escudo_picto4,
      itm_vae_escudo_picto5,itm_vae_escudo_picto6,itm_vae_escudo_picto7,itm_vae_escudo_picto8,itm_vae_escudo_picto9
    ],
    def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2
  ],

  [
    "rhodok_sergeant","Airig (Hv. I.)","Arras",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_neutral,
    [
      itm_throwing_spears,itm_throwing_spears,itm_throwing_spears,itm_throwing_spears,
      itm_leather_gloves,itm_bare_legs_blue,itm_carbatinae_2_bare,
      itm_padded_jack_4_trig,itm_scale_armor,itm_goatist_tunic,itm_haubergeon,itm_byrnie151,itm_byrnie3,itm_padded_jack_6_trig,
      itm_szpadelhelmet,itm_szpadelhelmet2,itm_szpadelhelmet3,itm_szpadelhelmet4,itm_szpadelhelmet5,itm_red_cloak_hood,
      itm_scianshort,itm_celticv2_1,itm_celticv2_2,itm_celticshort1_1,itm_celticshort1_2,itm_celticsword2,itm_war_spear,
      itm_celticsaxon_adorno_1,itm_celticsaxon_adorno_2,itm_celticsaxon_adorno_3,itm_celticsaxon_adorno_4,
      itm_celticsaxon_adorno_5,itm_celticsaxon_adorno_6,itm_celticsaxon_adorno_7,itm_gaelic_shield_j,itm_scyld10,
      itm_scyld,itm_celticsaxon_adorno_10
    ],
    def_attrib3|level(27),wp(200),knows_warrior_veteran,rhodok_face_middle_1, rhodok_face_older_2
  ],

  [
    "rhodok_veteran_crossbowman","Marcach (Lig. C.)","Marcachs",
    tf_mounted|tf_guarantee_all,0,0,fac_neutral,
    [
      itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
      itm_saddle_horse,itm_steppe_horse,itm_charger,itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,
      itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
      itm_gatheredcloaks1,itm_vaelicus_t_21,itm_vaelicus_t_26,itm_vaelicus_t_27,itm_vaelicus_t_35,
      itm_padded_jack_3_trig,itm_padded_jack_6_trig,itm_padded_jack_7_trig,itm_padded_jack_9_trig,
      itm_helm_captaina,itm_leather_cap,itm_celtycka_lebka,itm_celtycka_iron,itm_blue_cloak_hood,
      itm_scianlongbone,itm_celticv2_1,itm_spear_8,itm_sarranid_axe_b,
      itm_tab_shield_round_c,itm_celtic_shield_small_round_b,itm_celtic_shield_small_round_e,itm_celtic_vae_shield5,
      itm_scyld5,itm_scyld6,itm_scyld7,itm_tarcza_harfa_vae_16,itm_tarcza_harfa_vae_17,itm_gaelic_shield_h,itm_gaelic_shield_i
    ],
    def_attrib3|level(27),wp(200),knows_warrior_veteran,rhodok_face_middle_1, rhodok_face_older_2
  ],

  [
    "rhodok_sharpshooter","Curraidh (Elit. C.)","Curraidhs",
    tf_mounted|tf_guarantee_all,0,0,fac_neutral,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_normal_horse17,itm_normal_horse18,itm_normal_horse19,itm_normal_horse20,itm_normal_horse23,
      itm_normal_horse28,itm_courser4,itm_courser5,
      itm_carbatinae_1_greaves_grey,itm_decorated_leather_shoes_blue,itm_decorated_leather_shoes_bare,
      itm_scale_armor,itm_lamellar_vest,itm_idi_scale14,itm_brigandine_red,itm_lorika,itm_mail_shirtred,
      itm_celta_capa1,itm_celta_capa2,itm_spangenhelm_a_trim,itm_romanelitehelm,itm_szpadelhelmet,itm_szpadelhelmet3,itm_green_cloak,
      itm_kirkburn,itm_pict_sword,itm_celticshort1_1,itm_spear_8,
      itm_tab_shield_round_c,itm_celtic_shield_small_round_d,itm_celtic_vae_shield7,itm_celtic_shield_small_round_a,
      itm_gaelic_shield_d,itm_gaelic_shield_e,itm_gaelic_shield_f,itm_gaelic_shield_g,itm_scyld10,itm_scyld,
      itm_vae_escudo_picto14,itm_vae_escudo_picto15
    ],
    def_attrib3|level(29),wp(230),knows_warrior_elite,rhodok_face_middle_1, rhodok_face_older_2
  ],

  [
    "rhodok_messenger","Gael Messenger","Gaels Messengers",
    tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
    [
      itm_leather_gloves,itm_javelin,itm_sumpter_horse,
      itm_bare_legs_blue,itm_carbatinae_2_bare,
      itm_nobleman_outfit,itm_ragged_outfit,itm_pict_tunic7,itm_pict_tunic6,itm_pict_tunic7,itm_vaelicus_t_35,itm_vaelicus_t_36,
      itm_scianshort,itm_scianshortbone,itm_one_handed_war_axe_a,itm_war_spear,itm_spear,
      itm_tarcza_harfa_vae_17,itm_tarcza_harfa_vae_18,itm_tarcza_harfa_vae_19,itm_tarcza_harfa_vae_20,itm_tarcza_harfa_vae_21
    ],
    def_attrib3|agi_21|level(29),wp(200),knows_common|knows_riding_7|knows_power_draw_3,rhodok_face_middle_1, rhodok_face_older_2
  ],

  [
    "rhodok_deserter","Goidels Deserter","Goidels Deserters",
    tf_guarantee_boots|tf_guarantee_shield,0,0,fac_deserters,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
      itm_bl_tunicsr03,itm_bl_tunicsr03_2,itm_bl_tunicsr01,itm_vaelicus_tunic_3,itm_tunic_c,itm_pict_tunic5,itm_pict_tunic6,
      itm_skull_cap_new_c,itm_leather_steppe_cap_b,itm_celtycka_lebka,
      itm_scianshortbone,itm_one_handed_war_axe_a,itm_war_spear,itm_spear,
      itm_tarcza_harfa_vae_1,itm_tarcza_harfa_vae_2,itm_tarcza_harfa_vae_3,itm_tarcza_harfa_vae_4,itm_tarcza_harfa_vae_5,
      itm_tarcza_harfa_vae_6,itm_tarcza_harfa_vae_7,itm_tarcza_harfa_vae_8
    ],
    def_attrib2|level(23),wp(170),knows_warrior_normal, rhodok_face_older_2
  ],

  [
    "rhodok_prison_guard","Prison Guard","Prison Guards",
    tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_neutral,
    [
      itm_javelin,itm_bare_legs_blue,itm_nordiclightarmor7,itm_nordiclightarmor8,itm_fur_coat,itm_leather_cap,
      itm_rathos_bowl_helmet,itm_scianshortbone,itm_spear,itm_shield_17
    ],
    def_attrib3|level(29),wp(200),
    knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,rhodok_face_middle_1, rhodok_face_older_2
  ],

  [
    "rhodok_castle_guard","Castle Guard","Castle Guards",
    tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
    [
      itm_javelin,itm_bare_legs_blue,itm_nordiclightarmor7,itm_nordiclightarmor8,itm_fur_coat,
      itm_leather_cap,itm_rathos_bowl_helmet,itm_scianshortbone,itm_spear,itm_shield_17
    ],
    def_attrib3|level(29),wp(200),
    knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,rhodok_face_middle_1, rhodok_face_older_2
  ],


   # Ryan BEGIN
  [
    "looter","Theow","Theows",
    0,0,0,fac_outlaws,
    [
      itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,
      itm_ankle_boots,itm_wrapping_boots,
      itm_woolen_cap_newblu,itm_woolen_cap_newgrn,itm_head_wrappings,
      itm_shirt,itm_bl_tunicsr01,itm_shirtb,itm_bl_tunicsr01_2,itm_shirte,itm_fat_body,
      itm_knife,itm_cudgel,itm_club,itm_sickle,itm_hatchet,itm_wooden_stick,itm_hand_axe
    ],
    def_attrib|level(15),wp(110),knows_common,bandit_face1, bandit_face2
  ],
  # Ryan END

  [
    "bandit","Bagauda","Bagaudas",
    tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_outlaws,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
      itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
      itm_shirt,itm_roman_shirt,itm_bl_tunicsr02,itm_bl_tunicsr01,itm_shirtb,itm_shirtc,itm_shirtd,itm_shirte,
      itm_knife,itm_cudgel,itm_club,itm_sickle,itm_hand_axe,itm_spear_2
    ],
    def_attrib2|level(19),wp(140),knows_warrior_basic,bandit_face1, bandit_face2
  ],

  [
    "brigand","Wylisc","Wylisc",
    tf_guarantee_boots|tf_guarantee_shield,0,0,fac_outlaws,
    [
      itm_javelin,itm_javelin,itm_shirtc,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_carbatinae_1_green,itm_carbatinae_1_orange,itm_carbatinae_2_orange,
      itm_head_wrappings,itm_common_hood,
      itm_fattiglinenskjortir,itm_wessex_tunic3,itm_bl_tunicsr02,itm_mercia_tunic1,itm_blue_short_tunic,
      itm_spear_6,itm_hunting_dagger,itm_woodenshield_small
    ],
    def_attrib2|level(23),wp(170),knows_warrior_normal,bandit_face1, bandit_face2
  ],

  [
    "mountain_bandit","Morth","Morths",
    tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_outlaws,
    [
      itm_sniper_crossbow,itm_sniper_lead,itm_flintlock_pistol,itm_hunting_bow,itm_arrows,
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,itm_ankle_boots,itm_wrapping_boots,
      itm_shirt,itm_roman_shirt,itm_bl_tunicsleather,
      itm_hunting_dagger
    ],
    basic_ranged_attrib|str_14|level(15),wp(60)|wp_archery(100),
    knows_warrior_normal|knows_power_draw_2,rhodok_face_young_1, rhodok_face_old_2
  ],

  [
    "forest_bandit","Unright","Unrights",
    tf_guarantee_boots,0,0,fac_outlaws,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_arrows,itm_short_bow,itm_hunting_bow,
      itm_carbatinae_2_bare,itm_carbatinae_1_bare,itm_ankle_boots,
      itm_peasant_archer,itm_peasant_man_d,itm_peasant_man_c,itm_armor_27,itm_armor_26,
      itm_peasant_man_e,itm_peasant_man_f,itm_leather_jerkin,
      itm_hand_axe,itm_hatchet,itm_axe_2,itm_knife,itm_cudgel
    ],
    def_attrib2|level(23),wp(140)|wp_archery(160),knows_warrior_basic,swadian_face_young_1, swadian_face_old_2
  ],

  [
    "sea_raider","Frank","Frankish",
    tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_outlaws,
    [
      itm_light_throwing_axes,itm_jarid,itm_throwing_axes,itm_throwing_spears3,itm_javelin,itm_throwing_spears4,
      itm_decorated_leather_shoes,itm_decorated_leather_shoes_green,
      itm_vikinglamellar3red,itm_vikinglamellar3green,itm_vikinglamellar3blue,itm_mail_shirt_3,
      itm_ad_viking_byrnie_01,itm_mamluke_mail,itm_hauberk_a_new,itm_mail_shirt_brown,
      itm_rathos_spangenhelm_b,itm_rathos_spangenhelm_a_yellow2,itm_norman_helmet,itm_padded_coif,itm_arming_cap,itm_steppe_cap,
      itm_spatha,itm_spear_3,itm_frankish_axe2,itm_vikingaxeb,itm_axehammer_1,itm_le_pictishsword2,
      itm_leathershield_medium_d,itm_leathershield_medium
    ],
    def_attrib3|level(27),wp(200),knows_warrior_elite,nord_face_younger_1, nord_face_old_2
  ],

  [
    "steppe_bandit","Scotos","Scoti",
    tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_outlaws,
    [
      itm_darts,itm_javelin,itm_throwing_knives,itm_javelin,itm_throwing_knives,itm_sniper_crossbow,itm_flintlock_pistol,
      itm_carbatinae_1_grey,itm_carbatinae_1_green,
      itm_padded_jack_6_trig,itm_bl_tunicsr03_2,itm_bl_tunicsr01,itm_vaelicus_tunic_3,itm_tunic_c,
      itm_pict_tunic5,itm_shirtb,itm_shirte,itm_pelt_coat,itm_light_leather,itm_mail_with_surcoat,itm_military_cleaver_b,
      itm_celtycka_lebka,itm_celtycka_iron,itm_leather_cap,
      itm_irish_sword,itm_spear,itm_boar_spear,itm_sarranid_two_handed_axe_a,itm_celticv2_1,itm_scianshort,
      itm_leathershield_small_d,itm_vae_cuadrado_8,itm_vae_cuadrado_9,itm_leathershield_medium,itm_vae_cuadrado_1,
      itm_vae_cuadrado_2,itm_scyld1,itm_scyld2,itm_scyld3,itm_scyld4,
      itm_gaelic_shield_a,itm_gaelic_shield_b,itm_gaelic_shield_c
    ],
    def_attrib2|level(25),wp(185),knows_warrior_normal,khergit_face_young_1, khergit_face_old_2
  ],

  [
    "taiga_bandit","Outlaw Warrior","Outlaw Warriors",
    tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_outlaws,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_carbatinae_1,itm_carbatinae_2,itm_carbatinae_2_green,itm_carbatinae_1_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
      itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_peasant_archer,itm_armor_26,itm_military_cleaver_c,
      itm_broadsword,itm_hatchet,itm_lance,itm_lance,itm_lance,itm_lance,
      itm_leathershield_medium_y
    ],
    def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1, vaegir_face_old_2
  ],

  [
    "desert_bandit","Bandit","Bandits",
    tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_outlaws,
    [
      itm_arrows,itm_short_bow,itm_short_bow,itm_short_bow,itm_hunting_bow,
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,itm_ankle_boots,
      itm_black_hood,itm_head_wrappings,itm_common_hood,
      itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,
      itm_peasant_archer,itm_armor_26,itm_knife
    ],
    basic_ranged_attrib|str_14|level(19),wp(100)|wp_archery(130),
    knows_warrior_normal|knows_power_draw_2,khergit_face_young_1, khergit_face_old_2
  ],

  [
    "black_khergit_horseman","Dena Pirate","Dena Pirates",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_black_khergits,
    [
      itm_throwing_spears3,itm_throwing_spears3,itm_throwing_spears4,itm_throwing_spears3,
      itm_leather_gloves,
      itm_carbatinae_1_grey,itm_mail_boots,itm_iron_greaves,
      itm_mail_shirt_ylw,itm_mail_shirt_blk,itm_mail_shirt_wht,itm_mail_shirt_grn,itm_hauberk_a_new,itm_mail_shirt_whiteaxes,
      itm_nordic_veteran_archer_helmet,itm_rus_helmet_a,itm_kettle_hat,itm_sarranid_mail_coif,itm_nordic_huscarl_helmet,
      itm_flat_topped_helmet,itm_footman_helmet,
      itm_bl_sword01_02,itm_hunting_dagger,itm_lui_waronehandedaxec,itm_war_axe,itm_spear_1,itm_spear_2,
      itm_leathershield_medium_b,itm_leathershield_small_b
    ],
    def_attrib3|level(29),wp(230),knows_warrior_elite,bandit_face1, bandit_face2
  ],

  #lideres bandidos chief
  [
    "sea_raider_leader2","Ship Captain","Captains",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_outlaws,
    [
      itm_throwing_spears3,itm_leather_gloves,
      itm_carbatinae_2_greaves_green,itm_carbatinae_1_greaves_green,
      itm_mail_shirt_wht,itm_byrnie_f_new,itm_mail_shirt_grn,itm_heraldic_mail_with_tunic,
      itm_nordic_warlord_helmet,itm_full_helm,itm_spangenhelm_helm,
      itm_great_helmet,itm_winged_great_helmet,itm_valssword,itm_bl_sword01_03,
      itm_hunting_dagger,itm_war_axe,itm_woodenshield_medium_d
    ],
    def_attrib3|level(32),wp(260),
    knows_warrior_elite|knows_wound_treatment_8|knows_surgery_8,
    0x00000007a6002194125b6db6cb6db6db00000000001db6c30000000000000000, nord_face_old_2
  ],

  [
    "looter_leader2","Bandit Leader","Bandit Leaders",
    tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,
    [
      itm_javelin,itm_javelin,itm_javelin,
      itm_leather_gloves,itm_decorated_leather_shoes_green,itm_decorated_leather_shoes_blue,
      itm_mail_shirt_ylw,itm_mail_shirt_blk,itm_mail_shirt_wht,itm_bowl_helmet,itm_spangenhelm_a_trim,
      itm_spangenhelm_helm,itm_sarranid_helmet1,itm_nomad_cap,itm_military_cleaver_c, itm_military_cleaver_b,itm_military_sickle_a,
      itm_new_sword1,itm_new_sword2,itm_hunting_dagger,itm_war_axe,itm_arrows,itm_strong_bow,itm_leathershield_small_d
    ],
    def_attrib3|level(27),wp(200),
    knows_warrior_elite|knows_wound_treatment_8|knows_surgery_8,
    0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2
  ],
  #lideres bandidos acaban

  [
    "manhunter","Young Warrior","Young Band",
    tf_guarantee_boots|tf_guarantee_shield,0,0,fac_manhunters,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_carbatinae_1_grey,itm_carbatinae_1_green,itm_carbatinae_1_orange,
      itm_roman_shirt,itm_armor_8,itm_armor_9,itm_short_tunic,itm_green_tunic,itm_blue_tunic,itm_coat_of_plates11,
      itm_coat_of_plates10,itm_coat_of_plates9,itm_military_sickle_a,
      itm_leather_cap,itm_leather_cap,
      itm_spear_1,itm_knife,itm_spear_3,itm_woodenshield_small_d
    ],
    def_attrib2|level(23),wp(170),knows_warrior_basic,bandit_face1, bandit_face2
  ],

  ##  ["deserter","Deserter","Deserters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_swadian_deserters,
  ##   [itm_arrows,itm_spear,itm_fighting_pick,itm_short_bow,itm_sword,itm_voulge,itm_nordic_shield,itm_round_shield,itm_kettle_hat,itm_leather_cap,itm_padded_cloth,itm_leather_armor,itm_scale_armor,itm_saddle_horse],
  ##   def_attrib|level(12),wp(60),knows_common,bandit_face1, bandit_face2],

   #fac_slavers
  ##  ["slave_keeper","Slave Keeper","Slave Keepers",tf_guarantee_armor,0,0,fac_slavers,
  ##   [itm_cudgel,itm_club,itm_woolen_cap,itm_leather_vest_green,itm_coarse_tunic,itm_leather_armor_c,itm_nordic_shield,itm_ankle_boots,itm_wrapping_boots,itm_sumpter_horse],
  ##   def_attrib|level(10),wp(60),knows_common,bandit_face1, bandit_face2],

  [
    "slave_driver","Slave Driver","Slave Drivers",
    tf_guarantee_boots|tf_guarantee_shield,0,0,fac_slavers,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_carbatinae_2_green,itm_carbatinae_1_blue,itm_carbatinae_2_blue,itm_carbatinae_2_grey,itm_carbatinae_1_grey,
      itm_hood_newwht,itm_black_hood,itm_head_wrappings,itm_common_hood,
      itm_shirt,itm_roman_shirt,itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_shirtd,
      itm_spear_1,itm_spear_2,itm_spear_3,itm_woodenshield_small
    ],
    def_attrib2|level(20),wp(155),knows_warrior_basic,bandit_face1, bandit_face2
  ],

  [
    "slave_hunter","Slave Hunter","Slave Hunters",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_slavers,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_decorated_leather_shoes,itm_carbatinae_2,itm_decorated_leather_shoes_green,
      itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_green_tunic,itm_red_tunic,itm_blue_tunic,
      itm_padded_jack_3_trig,itm_padded_jack_4_trig,
      itm_bowl_helmet,itm_spangenhelm_helm,itm_horn_helmet_2,
      itm_spear_1,itm_spear_2,itm_spear_3,itm_woodenshield_medium
    ],
    def_attrib3|level(25),wp(180),knows_warrior_veteran,bandit_face1, bandit_face2
  ],

  [
    "slave_crusher","Veteran Slave Hunter","Veteran Slave Hunters",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_slavers,
    [
      itm_throwing_spears,itm_throwing_spears,itm_throwing_spears,itm_throwing_spears,
      itm_leather_gloves,
      itm_decorated_leather_shoes_blue,itm_carbatinae_2_blue,
      itm_mail_shirt_ylw,itm_mail_shirt_blk,itm_mail_shirt_wht,itm_padded_jack_3_trig,itm_padded_jack_4_trig,itm_padded_jack_6_trig,
      itm_spangenhelm_helm,itm_horn_helmet_2,itm_sarranid_helmet1,itm_nomad_cap,itm_padded_coif,itm_arming_cap,itm_steppe_cap,
      itm_new_sword1,itm_bl_sword01_03,itm_woodenshield_medium
    ],
    def_attrib3|level(27),wp(200),knows_warrior_elite,bandit_face1, bandit_face2
  ],

  [
    "slaver_chief","Slaver Chief","Slaver Chiefs",
    tf_mounted|tf_guarantee_all,0,0,fac_slavers,
    [
      itm_javelin,
      itm_leather_gloves,
      itm_saddle_horse,itm_steppe_horse,
      itm_carbatinae_2_greaves_orange,itm_splinted_leather_greaves,
      itm_padded_jack_3_trig,itm_padded_jack_4_trig,itm_padded_jack_6_trig,itm_war_bow,itm_arrows,
      itm_spangenhelm_a_trim,itm_spangenhelm_helm,itm_steppe_cap,
      itm_new_sword2,itm_bl_sword01_03,itm_woodenshield_medium
    ],
    def_attrib3|level(29),wp(230),knows_warrior_elite,bandit_face1, bandit_face2
  ],

#Rhodok tribal, Hunter, warrior, veteran, warchief

#  ["undead_walker","undead_walker","undead_walkers",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
  #   [],
  #   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
  #  ["undead_horseman","undead_horseman","undead_horsemen",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_undeads,
  #   [],
  #   def_attrib|level(19),wp(100),knows_common,undead_face1, undead_face2],
  #  ["undead_nomad","undead_nomad","undead_nomads",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
  #   [],
  #   def_attrib|level(21),wp(100),knows_common|knows_riding_4,khergit_face1, khergit_face2],
  #  ["undead","undead","undead",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
  #   [],
  #   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
  #  ["hell_knight","hell_knight","hell_knights",tf_undead|tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_undeads,
  #   [],
  #   def_attrib|level(23),wp(100),knows_common|knows_riding_3,undead_face1, undead_face2],



  [
    "follower_woman","Camp Woman","Camp Women",
    tf_female|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
    [
      itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,itm_stones,itm_stones,itm_stones,
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
      itm_wimple_a,itm_wimple_with_veil,
      itm_blue_tunic2,itm_peasant_dress_b_new,itm_pict_long_tunic2,itm_pict_long_tunic3,itm_pict_long_tunic4,
      itm_lady_dress_green,itm_lady_dress_blue,
      itm_knife,itm_club,itm_hand_axe
    ],
    def_attrib|level(15),wp(110)|wp_archery(110),knows_common,refugee_face1,refugee_face2
  ],

  [
    "hunter_woman","Camp Follower","Camp Follower",
    tf_female|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
    [
      itm_sniper_crossbow,itm_flintlock_pistol,itm_stones,itm_arrows,itm_short_bow,
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
      itm_wimple_a,itm_wimple_with_veil,
      itm_blue_tunic_long,itm_lady_dress_ruby,itm_woolen_dress,itm_blue_tunic2,itm_pict_long_tunic1,
      itm_peasant_dress_b_new,itm_pict_long_tunic3,
      itm_knife,itm_club,itm_hand_axe
    ],
    def_attrib|level(17),wp(125)|wp_archery(125),knows_common|knows_power_draw_2,refugee_face1,refugee_face2
  ],

  [
    "fighter_woman","Soldier's Wife","Wives of Soldiers",
    tf_female|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
    [
      itm_sniper_crossbow,itm_flintlock_pistol,itm_arrows,itm_hunting_bow,
      itm_carbatinae_2_grey,itm_carbatinae_1_grey,itm_carbatinae_1_green,
      itm_sarranid_head_cloth,itm_veil_b,itm_veil_d,itm_veil_c,itm_veil_e,itm_veil_f,itm_veil_g,
      itm_blue_tunic_long,itm_lady_dress_ruby,itm_woolen_dress,itm_blue_tunic2,itm_peasant_dress_b_new,
      itm_pict_long_tunic4,itm_lady_dress_green,itm_lady_dress_blue,
      itm_knife,itm_club,itm_hand_axe
    ],
    def_attrib|level(20),wp(145)|wp_archery(145),
    knows_common|knows_athletics_2|knows_ironflesh_1|knows_power_draw_3,refugee_face1,refugee_face2
  ],

  [
    "sword_sister","Camp Defender","Camp Defenders",
    tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_commoners,
    [
      itm_arrows,itm_short_bow,
      itm_carbatinae_1,itm_carbatinae_2_blue,itm_carbatinae_2_grey,itm_carbatinae_1_grey,
      itm_veil_b,itm_veil_d,itm_veil_c,itm_veil_e,itm_veil_f,itm_veil_g,
      itm_lady_dress_ruby,itm_woolen_dress,itm_blue_tunic2,itm_pict_long_tunic1,itm_peasant_dress_b_new,
      itm_lady_dress_green,itm_lady_dress_blue,
      itm_knife,itm_club,itm_hand_axe
    ],
    def_attrib|level(24),wp(160)|wp_archery(160),
    knows_common|knows_athletics_3|knows_ironflesh_2|knows_shield_2|knows_power_draw_3,refugee_face1,refugee_face2
  ],

  [
    "refugee","Refugee","Refugees",
    tf_female|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
    [
      itm_stones,
      itm_bare_legs_blue,
      itm_wimple_a,itm_wimple_with_veil,itm_peasant_dress_b_new,itm_blue_tunic_long,itm_lady_dress_ruby,itm_woolen_dress,
      itm_knife,itm_club
    ],
    def_attrib|level(1),wp(20),knows_common,refugee_face1,refugee_face2
  ],

  [
    "peasant_woman","Peasant Woman","Peasant Women",
    tf_female|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_stones,
      itm_bare_legs_blue,
      itm_wimple_a,itm_wimple_with_veil,itm_peasant_dress_b_new,itm_blue_tunic_long,itm_lady_dress_ruby,itm_woolen_dress,
      itm_knife,itm_club
    ],
    def_attrib|level(1),wp(20),knows_common,refugee_face1,refugee_face2
  ],

  #para dungeon chief
  [
    "refugeeromanruins","Refugee","Refugees",
    tf_female|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
    [
      itm_stones,
      itm_bare_legs_blue,
      itm_wimple_a,itm_wimple_with_veil,itm_peasant_dress_b_new,itm_blue_tunic_long,itm_lady_dress_ruby,itm_woolen_dress,
      itm_knife,itm_club
    ],
    def_attrib|level(15),wp(60),knows_common,refugee_face1,refugee_face2
  ],

  [
    "peasant_womanromanruins","Peasant Woman","Peasant Women",
    tf_female|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_stones,
      itm_bare_legs_blue,
      itm_wimple_a,itm_wimple_with_veil,itm_peasant_dress_b_new,itm_blue_tunic_long,itm_lady_dress_ruby,itm_woolen_dress,
      itm_knife,itm_club
    ],
    def_attrib|level(15),wp(60),knows_common,refugee_face1,refugee_face2
  ],

  [
    "refugeedruid","Refugee","Refugees",
    tf_female|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
    [
      itm_stones,
      itm_bare_legs_blue,
      itm_wimple_a,itm_wimple_with_veil,itm_peasant_dress_b_new,itm_blue_tunic_long,itm_lady_dress_ruby,itm_woolen_dress,
      itm_knife,itm_club
    ],
    def_attrib|level(15),wp(60),knows_common,refugee_face1,refugee_face2
  ],

  [
    "peasant_womandruid","Peasant Woman","Peasant Women",
    tf_female|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_stones,
      itm_bare_legs_blue,
      itm_wimple_a,itm_wimple_with_veil,itm_peasant_dress_b_new,itm_blue_tunic_long,itm_lady_dress_ruby,itm_woolen_dress,
      itm_knife,itm_club
    ],
    def_attrib|level(15),wp(60),knows_common,refugee_face1,refugee_face2
  ],

  [
    "farmerdruid","Farmer","Farmers",
    tf_guarantee_boots|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
    [
      itm_stones, itm_stones, itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,
      itm_warhorse_steppe,
      itm_ankle_boots,itm_wrapping_boots,
      itm_woolen_cap_newblk,itm_woolen_cap_newwht,itm_woolen_cap,
      itm_shirt,itm_roman_shirt,itm_bl_tunicsr01_2,itm_bl_tunicsr02,
      itm_bl_tunicsr01,itm_shirtb,itm_shirtc,itm_shirtd,itm_shirte,
      itm_fat_body,itm_knife,itm_pitch_fork,itm_cudgel,itm_stones,
      itm_battle_fork,itm_staff,itm_quarter_staff,itm_sickle
    ],
    def_attrib|level(15),wp(110),knows_common,man_face_middle_1, man_face_old_2
  ],

  [
    "manhunterdruid","Young Warrior","Young Band",
    tf_guarantee_boots|tf_guarantee_shield,0,0,fac_manhunters,
    [
      itm_javelin,itm_javelin,itm_javelin,
      itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
      itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_green_tunic,
      itm_coat_of_plates11,itm_coat_of_plates10,itm_coat_of_plates9,
      itm_leather_cap,itm_leather_warrior_cap,
      itm_spear_2,itm_spear_3,itm_woodenshield_small_d
    ],
    def_attrib2|level(15),wp(125),knows_warrior_basic,bandit_face1, bandit_face2
  ],

  [
    "prisionerdruid","Prisoner","Prisoners",
    tf_bajo|tf_guarantee_boots|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
    [],
    def_attrib|level(5),wp(70),knows_common,man_face_middle_1, man_face_old_2
  ],

  [
    "quarry_trabajador","Quarry Worker","Quarry Workers",
    tf_randomize_face,no_scene,reserved,fac_commoners,
    [
      itm_bare_legs_blue,itm_carbatinae_2_bare,
      itm_woolen_cap_newblu,itm_woolen_cap_newred,itm_woolen_cap_newgrn,itm_woolen_cap_newblk,
      itm_shirt,itm_roman_shirt,itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_bl_tunicsr01,
      itm_shirtb,itm_shirtc,itm_shirtd,itm_shirte,
      itm_knife,itm_sickle
    ],
    def_attrib|level(5),wp(70),knows_common,man_face_middle_1, man_face_old_2
  ],

  [
    "quarry_capataz","Quarry Foreman","Quarry Foremen",
    tf_alto|tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
    [
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,itm_ankle_boots,itm_wrapping_boots,
      itm_woolen_cap_newblk,itm_woolen_cap_newwht,itm_woolen_cap,
      itm_shirt,itm_roman_shirt,itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_bl_tunicsr01,
      itm_shirtb,itm_shirtc,itm_shirtd,itm_shirte,
      itm_knife,itm_staff,itm_quarter_staff,itm_sickle,itm_hatchet
    ],
    def_attrib|level(5),wp(70),knows_common,man_face_middle_1, man_face_old_2
  ],

  [
    "abad","Abbot","Abbot",
    tf_guarantee_armor|tf_guarantee_boots, no_scene,0, fac_commoners,
    [
      itm_blue_gambeson,itm_ankle_boots,itm_staff
    ],
    def_attrib|level(5),wp(90),knows_common,sac_face_1, sac_face_2
  ],

  [
    "monjes","Monk","Monks",
    tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_knife,itm_robe,itm_ankle_boots,itm_staff
    ],
    def_attrib|level(4),wp(80),knows_common,sac_face_1, sac_face_2
  ],
  ###chief acaba

  [
    "caravan_master","Caravan Master","Caravan Masters",
    tf_mounted|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
    [
      itm_javelin,itm_saddle_horse,
      itm_carbatinae_2_green,itm_carbatinae_1_blue,itm_carbatinae_1_green,itm_carbatinae_1_orange,
      itm_carbatinae_2_orange,itm_mail_shirt_ylw,itm_mail_shirt_blk,itm_mail_shirt_wht,
      itm_padded_jack_3_trig,itm_padded_jack_4_trig,itm_padded_jack_6_trig,
      itm_new_sword1,itm_new_sword2,itm_bl_sword01_03,itm_ad_viking_shield_round_43
    ],
    def_attrib2|level(22),wp(165),knows_warrior_normal|knows_trade_4,mercenary_face_1, mercenary_face_2
  ],

  [
    "kidnapped_girl","Kidnapped Girl","Kidnapped Girls",
    tf_hero|tf_female|tf_randomize_face|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
    [
      itm_blue_tunic_long,itm_ankle_boots
    ],
    def_attrib|level(2),wp(30),knows_common|knows_riding_2,woman_face_1, woman_face_2
  ],

#This troop is the troop marked as soldiers_end and town_walkers_begin
  #briton
  [
    "town_walker_1","Townsman","Townsmen",
    tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_shirt_blu, itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,
      itm_nordiclightarmor10,itm_blue_gambeson,
      itm_roman_shirt,itm_bl_tunicsr01_2, itm_shirtb, itm_shirtd, itm_shirte, itm_armor_9,
      itm_peasant_archer, itm_armor_26,itm_bl_tunicsr02,
      itm_bare_legs_blue, itm_carbatinae_2_bare, itm_carbatinae_1_bare, itm_hood_newblu, itm_hood_newred
    ],
    def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2
  ],

  [
    "town_walker_2","Townswoman","Townswomen",
    tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_blue_tunic_long,itm_lady_dress_ruby,itm_woolen_dress, itm_peasant_dress_b_new,
      itm_veil_c,itm_veil_e,itm_veil_f,itm_wimple_a,itm_wimple_with_veil,
      itm_red_dress,itm_brown_dress,itm_green_dress, itm_carbatinae_1_bare
    ],
    def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2
  ],

  #picto e irlandes
  [
    "town_walker_3","Townsman","Townsmen",
    tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_studded_leather_coat, itm_sarranid_jellaba_blue,itm_dane_tunic1,itm_wessex_tunic1,
      itm_pict_tunic5,itm_pict_tunic6,itm_pict_tunic7,itm_bl_tunicsr02_2,itm_bl_tunicsr03,
      itm_bl_tunicsr03_2,itm_shirt,itm_bl_tunicsr01,itm_shirtb, itm_shirtc,itm_armor_8,
      itm_bare_legs_blue, itm_carbatinae_2_bare, itm_carbatinae_1_bare, itm_hood_newblu, itm_hood_newred
    ],
    def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2
  ],

  [
    "town_walker_4","Townswoman","Townswomen",
    tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_blue_tunic2,itm_pictishdressverde,itm_woolen_dress, itm_veil_d, itm_veil_c,
      itm_veil_e,itm_veil_f,itm_wimple_a,itm_wimple_with_veil,
      itm_pict_long_tunic1,itm_sarranid_dress_b,itm_pict_long_tunic2,itm_peasant_dress_b_new,
      itm_pict_long_tunic4, itm_carbatinae_1_bare
    ],
    def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2
  ],

  #sajon
  [
    "town_walker_5","Townsman","Townsmen",
    tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_coarse_tunic1, itm_fattiglinenskjortir,itm_mercia_tunic1,itm_blue_short_tunic,
      itm_wessex_tunic3,itm_bl_tunicsleather,itm_bl_tunicsleather_3,itm_bluevikingshirt,
      itm_mercia_tunic10,itm_wessex_tunic4,
      itm_bare_legs_blue, itm_carbatinae_2_bare, itm_carbatinae_1_bare, itm_woolen_cap_newgrn,
      itm_woolen_cap_newblk, itm_woolen_cap_newblu, itm_woolen_cap_newwht
    ],
    def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2
  ],

  [
    "town_walker_6","Townswoman","Townswomen",
    tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_blue_tunic_long,itm_lady_dress_ruby,itm_woolen_dress, itm_veil_d, itm_peasant_dress_b_new,
      itm_veil_e,itm_veil_f,itm_wimple_a,itm_wimple_with_veil,
      itm_kenttunik, itm_carbatinae_1_bare
    ],
    def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2
  ],

  #ninos
  [
    "nino_varon","Child","Childs",
    tf_undead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
    [
      itm_shirt,itm_roman_shirt,itm_shirtb, itm_shirtc, itm_shirtd, itm_shirte,
      itm_bare_legs_blue, itm_carbatinae_2_bare, itm_carbatinae_1_bare,
      itm_hood_newblu, itm_woolen_cap_newblu, itm_woolen_cap_newwht
    ],
    def_attrib|level(4),wp(60),knows_common,man_face_younger_1, man_face_young_1
  ],

## ["nina_chica","Child","Childs",tf_nina|tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
  ##   [itm_blue_tunic_long,itm_lady_dress_ruby,itm_woolen_dress, itm_carbatinae_1_bare],
  ##   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

# ["khergit_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
  #   [itm_sarranid_woolen_cap_newwht,itm_turban,itm_wrapping_boots,itm_sarranid_cloth_robe, itm_arena_tunic_white],
  #   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
  # ["khergit_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
  #   [itm_brown_dress, itm_blue_tunic_long, itm_lady_dress_ruby, itm_lady_dress_ruby, itm_wrapping_boots, itm_carbatinae_2_blue, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
  #   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
  # ["sarranid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
  #   [itm_sarranid_woolen_cap_newwht,itm_turban,itm_wrapping_boots,itm_sarranid_cloth_robe, itm_arena_tunic_white],
  ##   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
  # ["sarranid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
  #   [itm_sarranid_common_dress, itm_sarranid_common_dress_b, itm_sarranid_felt_head_cloth, itm_sarranid_felt_head_cloth_b],
  #   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as town_walkers_end and village_walkers_begin
  [
    "village_walker_1","Villager","Villagers",
    tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_warhorse_steppe,itm_shirt_blu, itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
      itm_bl_tunic02,itm_nordiclightarmor10,itm_blue_gambeson,
      itm_roman_shirt,itm_bl_tunicsr01_2, itm_shirtb, itm_shirtd, itm_shirte, itm_armor_9,
      itm_peasant_archer, itm_armor_26,itm_bl_tunicsr02,
      itm_bare_legs_blue, itm_carbatinae_2_bare, itm_carbatinae_1_bare, itm_hood_newblu, itm_hood_newred
    ],
    def_attrib|level(4),wp(60),knows_common,man_face_younger_1, man_face_older_2
  ],

  [
    "village_walker_2","Villager","Villagers",
    tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_blue_tunic_long,itm_lady_dress_ruby,itm_woolen_dress, itm_veil_d, itm_veil_c,itm_veil_e,
      itm_veil_f,itm_wimple_a,itm_peasant_dress_b_new,
      itm_red_dress,itm_brown_dress,itm_green_dress, itm_carbatinae_1_bare
    ],
    def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2
  ],

  [
    "village_walker_3","Villager","Villager",
    tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_mule,itm_studded_leather_coat, itm_sarranid_jellaba_blue,itm_dane_tunic1,itm_wessex_tunic1,
      itm_pict_tunic5,itm_pict_tunic6,itm_pict_tunic7,itm_bl_tunicsr02_2,itm_bl_tunicsr03,itm_bl_tunicsr03_2,
      itm_shirt,itm_bl_tunicsr01,itm_shirtb, itm_shirtc,itm_armor_8,
      itm_bare_legs_blue, itm_carbatinae_2_bare, itm_carbatinae_1_bare, itm_hood_newblu, itm_hood_newred
    ],
    def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2
  ],

  [
    "village_walker_4","Villager","Villager",
    tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_blue_tunic2,itm_pictishdressverde,itm_woolen_dress, itm_veil_d, itm_veil_c,
      itm_veil_e,itm_veil_f,itm_wimple_a,itm_wimple_with_veil,
      itm_pict_long_tunic1,itm_sarranid_dress_b,itm_pict_long_tunic2,itm_pict_long_tunic3,
      itm_peasant_dress_b_new, itm_carbatinae_1_bare
    ],
    def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2
  ],

  [
    "village_walker_5","Villager","Villager",
    tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_donkey_mount,itm_coarse_tunic1, itm_fattiglinenskjortir,itm_mercia_tunic1,
      itm_blue_short_tunic,itm_wessex_tunic3,itm_bl_tunicsleather,itm_bl_tunicsleather_3,
      itm_bluevikingshirt,itm_mercia_tunic10,itm_wessex_tunic4,
      itm_bare_legs_blue, itm_carbatinae_2_bare, itm_carbatinae_1_bare, itm_woolen_cap_newgrn,
      itm_woolen_cap_newblk, itm_woolen_cap_newblu, itm_woolen_cap_newwht
    ],
    def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2
  ],

  [
    "village_walker_6","Villager","Villager",
    tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_blue_tunic_long,itm_lady_dress_ruby,itm_woolen_dress,
      itm_veil_d, itm_veil_c,itm_veil_e,itm_veil_f,itm_peasant_dress_b_new,itm_wimple_with_veil,
      itm_kenttunik, itm_carbatinae_1_bare
    ],
    def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2
  ],

## ["nino_varon2","Child","Childs",tf_nino|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
  ##   [ itm_shirt,itm_roman_shirt,itm_bl_tunicsr01,itm_bl_tunicsr01_2,itm_bl_tunicsr02, itm_shirtb, itm_shirtc, itm_shirtd, itm_shirte, itm_armor_8, itm_armor_9,itm_armor_26,
  ##    itm_bare_legs_blue, itm_carbatinae_2_bare, itm_carbatinae_1_bare, itm_hood_newblu, itm_hood_newred],
  ##   def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_young_2],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
  [
    "spy_walker_1","Townsman","Townsmen",
    tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_shirt,itm_roman_shirt,itm_bl_tunicsr02, itm_shirtb,
      itm_shirtc, itm_shirtd, itm_peasant_archer, itm_armor_26,
      itm_bare_legs_blue, itm_carbatinae_2_bare, itm_carbatinae_1_bare
    ],
    def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2
  ],

  [
    "spy_walker_2","Townswoman","Townswomen",
    tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_blue_tunic_long,itm_lady_dress_ruby,itm_woolen_dress, itm_veil_d, itm_veil_c,
      itm_veil_e,itm_veil_f,itm_wimple_a,itm_wimple_with_veil,
      itm_carbatinae_1_bare
    ],
    def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2
  ],
  # Ryan END

  # This troop is the troop marked as spy_walkers_end
  # Zendar
  ["tournament_master","Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_coarse_tunic1,itm_carbatinae_1_bare],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["trainer","Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_armor_8,itm_carbatinae_1_bare],def_attrib|level(2),wp(20),knows_common,0x00000000000430c701ea98836781647f],
  ["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_padded_jack_3_trig,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,0x00000000000c41c001fb15234eb6dd3f],

  # Ryan BEGIN
  ["Ramun_the_slave_trader","Aethelmaer, the Slave Trader","Aethelmaer, the Slave Trader",tf_bajo|tf_hero, no_scene,reserved, fac_commoners,[itm_noblemanshirt,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

  ["guide","Ulric","Ulric",tf_hero, no_scene,0,  fac_commoners,[itm_coarse_tunic3,itm_carbatinae_1_bare],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x0000000e0e08c284389373be918dc60b00000000001269230000000000000000],
  # Ryan END

  ["Xerina","Anchoret the Pict","Anchoret",tf_hero|tf_female, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_padded_jack_3_trig,itm_carbatinae_2_bare],def_attrib|str_15|agi_15|level(39),wp(312),knows_power_strike_9|knows_ironflesh_9|knows_riding_6|knows_power_draw_4|knows_athletics_9|knows_shield_3,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["Dranton","Niall the Briton","Niall",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_padded_jack_4_trig,itm_ankle_boots],def_attrib|str_15|agi_14|level(42),wp(324),knows_power_strike_9|knows_ironflesh_9|knows_riding_4|knows_power_draw_4|knows_athletics_6|knows_shield_3,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["Kradus","Uthred the Saxon","Kradus",tf_oso|tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_padded_jack_6_trig,itm_carbatinae_1_blue],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_9|knows_ironflesh_9|knows_riding_4|knows_power_draw_4|knows_athletics_6|knows_shield_3,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],


  #Tutorial
  ["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac_commoners,[itm_robe,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_padded_jack_4_trig,itm_padded_jack_3_trig,itm_padded_jack_6_trig,itm_ankle_boots,itm_leather_cap,itm_arena_helmet_yellow],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_padded_jack_4_trig,itm_padded_jack_6_trig,itm_padded_jack_6_trig,itm_ankle_boots,itm_leather_cap,itm_arena_helmet_yellow],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_padded_jack_6_trig,itm_padded_jack_4_trig,itm_padded_jack_3_trig,itm_ankle_boots,itm_leather_cap,itm_arena_helmet_yellow],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_padded_jack_6_trig,itm_padded_jack_4_trig,itm_padded_jack_3_trig,itm_ankle_boots,itm_leather_cap,itm_arena_helmet_yellow],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],

#Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
  ["Galeas","Balin","Balin",tf_hero, 0, reserved, fac_commoners,[itm_peasant_man_e,itm_decorated_leather_shoes],def_attrib|level(5),wp(20),0x0000000ebe0c224a6ce565c71b4ca8da00000000001de46e0000000000000000],

#Dhorak keep

  ["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_linen_tunic,itm_coarse_tunic1,itm_shirt,itm_ankle_boots,itm_carbatinae_1_bare],
   def_attrib|level(5),wp(70),knows_common,man_face_middle_1, man_face_older_2],

  ["trainer_1","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_carbatinae_1_bare],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_leather_armor_c,itm_carbatinae_1_bare],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_padded_jack_3_trig,itm_carbatinae_1_bare],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_carbatinae_1_bare],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_sarranid_cavalry_robe,itm_carbatinae_1_bare],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers.
  ["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_linen_tunic,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_bajo|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_padded_leather_blue,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_armor_c,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_padded_leather_brown,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_arena_tunic_green,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_oso|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_shirt_ylw,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_shirtc,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_bajo|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_courtly_outfit,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_dane_tunic1,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_arena_tunic_blue,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_11","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_linen_tunic,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_12","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_padded_leather_blue,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_13","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_nomad_vest,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_14","Ransom_Broker","Ransom_Broker",tf_alto|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_padded_leather_brown,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_15","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_arena_tunic_green,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_16","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_shirt_ylw,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_17","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_shirtc,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_18","Ransom_Broker","Ransom_Broker",tf_bajo|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_tunic,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_19","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_dane_tunic1,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_20","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_arena_tunic_blue,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_arena_tunic_blue,itm_carbatinae_1_bare,itm_black_cloak],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_padded_leather_brown,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_alto|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_shirt_ylw,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_padded_cloth,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_5","Traveller","Traveller",tf_alto|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_arena_tunic_blue,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_linen_tunic,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jerkin,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_nobleman_outfit,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_bajo|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_padded_leather_blue,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jerkin,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_11","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_arena_tunic_blue,itm_carbatinae_1_bare,itm_black_cloak],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_12","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_padded_leather_brown,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_13","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_shirt_ylw,itm_carbatinae_1_bare,itm_black_cloak],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_14","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_armor_c,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_15","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_padded_cloth,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_16","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ragged_outfit,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_17","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jerkin,itm_carbatinae_1_bare,itm_black_cloak],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_18","Conchobor","Conchobor",tf_bajo|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_dane_tunic1,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,0x0000000ff508d2c91da5ad32d3695ae500000000001d335c0000000000000000],
  ["tavern_traveler_19","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_padded_leather_blue,itm_red_cloak_hood,itm_carbatinae_1_bare],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_20","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jerkin,itm_carbatinae_1_bare,itm_black_cloak],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_coarse_tunic_red,itm_carbatinae_2,
                                                                                                                               itm_book_tactics, itm_book_persuasion, itm_book_wound_treatment_reference, itm_book_leadership,
                                                                                                                               itm_book_intelligence, itm_book_training_reference, itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_bajo|tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_coarse_tunic_blu,itm_carbatinae_2,
                                                                                                                                       itm_book_wound_treatment_reference, itm_book_leadership, itm_book_intelligence, itm_book_trade,
                                                                                                                                       itm_book_engineering, itm_book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],

# Tavern minstrel.
  ["tavern_minstrel_1","Wandering Bard","Minstrel",tf_alto|tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_dane_tunic1, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute
  ["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_tunic_with_green_cape, itm_bare_legs_blue, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],  #early harp/lyre
  ["tavern_minstrel_3","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_tunic_c, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute/oud or rebab
  ["tavern_minstrel_4","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_armor_9, itm_bare_legs_blue, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #No instrument or lyre
  ["tavern_minstrel_5","Wandering Bard","Minstrel",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_mercia_tunic1,itm_mercia_tunic10, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #Lute or Byzantine/Occitan lyra

#cortesanos y similares Chief
  # Bardos chief
  ["bardo_1","Kingdom Bard","Bard",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_28_castle|entry(10), reserved, fac_commoners,[itm_shirt_blu, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_2","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_19_castle|entry(10), reserved, fac_commoners,[itm_shirt_grn, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_3","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_3_castle|entry(10), reserved, fac_commoners,[itm_noblemanshirt, itm_bare_legs_blue, itm_lyre],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_4","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_13_castle|entry(10), reserved, fac_commoners,[itm_redvikingshirt, itm_bare_legs_blue, itm_lyre],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_5","Owain map Mordred","Owain",tf_oso|tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_1_castle|entry(10), reserved, fac_commoners,[itm_mail_with_tunic_green, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_6","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_2_castle|entry(10), reserved, fac_commoners,[itm_shirt_grn, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_7","Kingdom Bard","Bard",tf_alto|tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_12_castle|entry(10), reserved, fac_commoners,[itm_shirt_blu, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_8","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_14_castle|entry(10), reserved, fac_commoners,[itm_shirt_grn, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_9","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_16_castle|entry(10), reserved, fac_commoners,[itm_shirt_blu, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_10","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_41_castle|entry(10), reserved, fac_commoners,[itm_shirt_grn, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_11","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_42_castle|entry(10), reserved, fac_commoners,[itm_shirt_blu, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_12","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_17_castle|entry(10), reserved, fac_commoners,[itm_shirt_grn, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_13","Kingdom Bard","Bard",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_23_castle|entry(10), reserved, fac_commoners,[itm_noblemanshirt, itm_bare_legs_blue, itm_lyre],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_14","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_27_castle|entry(10), reserved, fac_commoners,[itm_redvikingshirt, itm_bare_legs_blue, itm_lyre],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_15","Kingdom Bard","Bard",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_24_castle|entry(10), reserved, fac_commoners,[itm_shirt_blu, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_16","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_7_castle|entry(10), reserved, fac_commoners,[itm_shirt_grn, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_17","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_5_castle|entry(10), reserved, fac_commoners,[itm_shirt_blu, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_18","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_30_castle|entry(10), reserved, fac_commoners,[itm_shirt_grn, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_19","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_6_castle|entry(10), reserved, fac_commoners,[itm_shirt_blu, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_20","Kingdom Bard","Bard",tf_alto|tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_39_castle|entry(10), reserved, fac_commoners,[itm_shirt_grn,itm_red_cloak_hood, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_21","Kingdom Bard","Bard",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_25_castle|entry(10), reserved, fac_commoners,[itm_shirt_blu, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_22","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_22_castle|entry(10), reserved, fac_commoners,[itm_shirt_grn, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_23","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_29_castle|entry(10), reserved, fac_commoners,[itm_noblemanshirt, itm_bare_legs_blue, itm_lyre],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_24","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_26_castle|entry(10), reserved, fac_commoners,[itm_redvikingshirt, itm_bare_legs_blue, itm_lyre],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_25","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_9_castle|entry(10), reserved, fac_commoners,[itm_shirt_blu, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_26","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_21_castle|entry(10), reserved, fac_commoners,[itm_shirt_grn, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_27","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_36_castle|entry(10), reserved, fac_commoners,[itm_shirt_blu, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_28","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_32_castle|entry(10), reserved, fac_commoners,[itm_shirt_grn, itm_irishcloak,itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_29","Kingdom Bard","Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_33_castle|entry(10), reserved, fac_commoners,[itm_shirt_blu, itm_piel_coat01,itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,man_face_young_1, man_face_old_2],
  ["bardo_30","Kingdom Bard","Bard",tf_bajo|tf_hero|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_40_castle|entry(10), reserved, fac_commoners,[itm_shirt_grn, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,0x000000028e0854c9472ab256954dc6e400000000001f37a50000000000000000],
  ["bardo_31","Ailen","Bard",tf_hero|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, 0, fac_neutral,[itm_shirt_grn, itm_bare_legs_blue, itm_lute],def_attrib|level(5),wp(20),knows_common,0x000000032a0c200f259b4f3aee72275a00000000001ec5900000000000000000],

# chief sacerdotes, obispos y abades, quest especial derfel Cadarn
  ["sacerdote_1","Abbot Felix of Dommoc","sacerdote",tf_bajo|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_14_castle|entry(11), reserved, fac_kingdom_4,[itm_blue_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000be90ce5d226a971b31e54c8f400000000001e56990000000000000000],
  ["sacerdote_2","Abbot Fursey","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_40_castle|entry(11), reserved, fac_kingdom_31,[itm_robe, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000e821043404864c59b0c92352400000000001d56580000000000000000],
  ["sacerdote_3","Bishop Paulinus","sacerdote",tf_bajo|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_1_castle|entry(11), reserved, fac_kingdom_1,[itm_red_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000fef04e44e28e265e2d46d454200000000001dc8eb0000000000000000],
  ["sacerdote_4","Bishop Honorius","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_2_castle|entry(11), reserved, fac_kingdom_2,[itm_red_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000ff810e2931864a41b3432c91c00000000001da6230000000000000000],
  ["sacerdote_5","Abbot Boisil","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_12_castle|entry(11), reserved, fac_kingdom_3,[itm_blue_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x00000009e20c458e251572bb5c38b71c00000000001e3cdc0000000000000000],
  ["sacerdote_6","Abbot Aidan","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_27_castle|entry(11), reserved, fac_kingdom_13,[itm_blue_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x00000009ff04e00e3ab34a3ad54956a300000000001cb2d80000000000000000],
  ["sacerdote_7","Bishop Binarus","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_16_castle|entry(11), reserved, fac_kingdom_5,[itm_red_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x000000083300e34e18acb0c495d0b73600000000001f5c930000000000000000],
  ["sacerdote_8","Abbot Saxulf","sacerdote",tf_alto|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_4_castle|entry(11), reserved, fac_kingdom_9,[itm_blue_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000ec40c111342b676b8a415c8e100000000001d642e0000000000000000],
  ["sacerdote_9","Bishop Oudeceus","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_9_castle|entry(11), reserved, fac_kingdom_26,[itm_red_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000d940050ce58aba6ad0c6e5a9d00000000001dc6a20000000000000000],
  ["sacerdote_10","Abbot Dona ap Selyffan","sacerdote",tf_bajo|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_22_castle|entry(11), reserved, fac_kingdom_22,[itm_robe, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000d8008e14e235289b6629238e200000000001e26e40000000000000000],
  ["sacerdote_11","Bishop Felix","sacerdote",tf_bajo|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_13_castle|entry(11), reserved, fac_kingdom_23,[itm_red_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000fee003300329eb63ba64f4a8200000000001e8b2b0000000000000000],
  ["sacerdote_12","Bishop Rhun ap Urbgen","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_7_castle|entry(11), reserved, fac_kingdom_15,[itm_red_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000fc80c528e4cda72551877586500000000001e3ce30000000000000000],
  ["sacerdote_13","Bishop Mochonna","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_6_castle|entry(11), reserved, fac_kingdom_18,[itm_red_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000cac08e3ce365b7158a3439a9300000000001e165a0000000000000000],
  ["sacerdote_14","Abbot Cuminian","sacerdote",tf_bajo|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_30_castle|entry(11), reserved, fac_kingdom_17,[itm_robe, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000c9f0061401cc9664bc48f34d100000000001cb2930000000000000000],
  ["sacerdote_15","Abbot Colman mac Duach","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_36_castle|entry(11), reserved, fac_kingdom_28,[itm_blue_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x00000009d408154e26b3a4c34c9534cb00000000000dba530000000000000000],
  ["sacerdote_16","Abbot Riderch","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_33_castle|entry(11), reserved, fac_kingdom_30,[itm_blue_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000ff90c6552299c3524f4ca5b2200000000001f38b50000000000000000],
  ["sacerdote_17","Abbot Molaise","sacerdote",tf_bajo|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_21_castle|entry(11), reserved, fac_kingdom_27,[itm_blue_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000c9a0464ce2725553aeb7138d400000000001df91b0000000000000000],
  ["sacerdote_18","Abbot Aedh Dubh","sacerdote",tf_bajo|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_19_castle|entry(11), reserved, fac_kingdom_19,[itm_blue_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000c820c545346ddae431e79b6a400000000001e34680000000000000000],
  ["sacerdote_19","Abbot Aileran","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_32_castle|entry(11), reserved, fac_kingdom_29,[itm_blue_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000cb60801d258dc49257ab1d9a300000000001e89950000000000000000],

  ["sacerdote_20","Abbot Foillan","sacerdote",tf_bajo|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_41_castle|entry(11), reserved, fac_kingdom_6,[itm_robe, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000c8610110e491b69d5714a290c00000000001e33070000000000000000],
  ["sacerdote_21","Abbot Finian","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_42_castle|entry(11), reserved, fac_kingdom_7,[itm_blue_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000fcc0cc18e2892249c9cc9293200000000001e1ade0000000000000000],
  ["sacerdote_22","Abbot Petroc","sacerdote",tf_alto|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_17_castle|entry(11), reserved, fac_kingdom_8,[itm_blue_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000eb304c5524313aac88b84cd1300000000001cc35d0000000000000000],
  ["sacerdote_23","Bishop Inabwy","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_26_castle|entry(11), reserved, fac_kingdom_25,[itm_red_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000eb00005531f6c7249649b36e500000000001dd4a40000000000000000],
  ["sacerdote_24","Bishop Euddogwy","sacerdote",tf_alto|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_28_castle|entry(11), reserved, fac_kingdom_11,[itm_red_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000ad700034039640f5b94aea29200000000001e331c0000000000000000],
  ["sacerdote_25","Abbot Peius","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_3_castle|entry(11), reserved, fac_kingdom_12,[itm_blue_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000ad50c35ce449cc5c653a22cee00000000001e395a0000000000000000],
  ["sacerdote_26","Bishop Fechin","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_24_castle|entry(11), reserved, fac_kingdom_14,[itm_red_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000fd200e0d35b6476289f1acc9400000000001d6cde0000000000000000],
  ["sacerdote_27","Bishop Aebbe","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_5_castle|entry(11), reserved, fac_kingdom_16,[itm_red_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000ff10095d3312c6dc0abc946e200000000001e36550000000000000000],
  ["sacerdote_28","Abbot Ultan","sacerdote",tf_bajo|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_39_castle|entry(11), reserved, fac_kingdom_20,[itm_robe, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000a5d04334e454b9a511b29b09e00000000001db4e60000000000000000],
  ["sacerdote_29","Bishop Dywel","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_26_castle|entry(11), reserved, fac_kingdom_21,[itm_red_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000a530854ce66d36db8dc66156300000000001e152a0000000000000000],
  ["sacerdote_30","Abbot Oengus","sacerdote",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_29_castle|entry(11), reserved, fac_kingdom_24,[itm_blue_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000fe704c240465354b6dc50dd5e00000000001e62e30000000000000000],
  #sacerdotes chief acaba

#damas de compania en tabernas
  ["quastuosa_1","Hore","quastuosa",tf_female|tf_hero|tf_randomize_face, scn_town_1_tavern|entry(5), 0, fac_commoners,[itm_lady_dress_blue, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,quastuosa_woman_face_1,quastuosa_woman_face_6],
  ["quastuosa_2","Hore","quastuosa",tf_female|tf_hero|tf_randomize_face, scn_town_6_tavern|entry(5), 0, fac_commoners,[itm_lady_dress_blue, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,quastuosa_woman_face_1,quastuosa_woman_face_6],
  ["quastuosa_3","Hore","quastuosa",tf_osa|tf_female|tf_hero|tf_randomize_face, scn_town_12_tavern|entry(5), 0, fac_commoners,[itm_blue_tunic_long, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,quastuosa_woman_face_1,quastuosa_woman_face_6],
  ["quastuosa_4","Hore","quastuosa",tf_female|tf_hero|tf_randomize_face, scn_town_15_tavern|entry(5), 0, fac_commoners,[itm_pict_long_tunic3, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,quastuosa_woman_face_1,quastuosa_woman_face_6],
  ["quastuosa_5","Hore","quastuosa",tf_female|tf_hero|tf_randomize_face, scn_town_30_tavern|entry(5), 0, fac_commoners,[itm_pict_long_tunic1, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,quastuosa_woman_face_1,quastuosa_woman_face_6],
  ["quastuosa_6","Hore","quastuosa",tf_female|tf_hero|tf_randomize_face, scn_town_33_tavern|entry(5), 0, fac_commoners,[itm_pict_long_tunic3, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,quastuosa_woman_face_1,quastuosa_woman_face_6],
  ["quastuosa_7","Hore","quastuosa",tf_female|tf_hero|tf_randomize_face, scn_town_11_tavern|entry(5), 0, fac_commoners,[itm_pict_long_tunic1, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,quastuosa_woman_face_1,quastuosa_woman_face_6],
  #damas de compania acaba chief

  #Especiales npcs, aparecen en sitios concretos
  ["especiales_1","Hermit Derfel Gadarn","especiales",tf_alto|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_castle_25_interior|entry(1), reserved, fac_commoners,[itm_robe, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000fcd04d2802cdc4ca6692e3c9500000000001eb90b0000000000000000],
  ["especiales_2","Abbot Constantine map Riderch","especiales",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_castle_9_interior|entry(1), reserved, fac_commoners,[itm_blue_gambeson, itm_bare_legs_blue],def_attrib|level(5),wp(20),knows_common,0x0000000ff308910e26679119657ae21b00000000001cd9230000000000000000],
  ["especiales_3","Dryhten Eadfrith Cearling","especiales",tf_alto|tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_5_castle|entry(1), reserved, fac_commoners,[itm_mail_shirt_1,itm_ad_viking_shield_round_01,itm_spatha, itm_ankle_boots], def_attrib3|level(26),wp(185),knows_warrior_elite,0x00000003fc041144245396b72cb5db6e00000000001ea9560000000000000000], #es NacroxNicke
  ["especiales_4","Guledic Geraint map Erbin","especiales",tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_castle_16_interior|entry(1), reserved, fac_commoners,[itm_mail_shirt_3,itm_ad_viking_shield_round_02,itm_spatha, itm_ankle_boots], def_attrib3|level(26),wp(185),knows_warrior_elite, 0x0000000eff0c420a279231a7666eb98a00000000001dc8d20000000000000000], # morcant
  ["especiales_5","Great Bard Aneirin","Bard",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_3_castle|entry(1), reserved, fac_commoners,[itm_noblemanshirt, itm_bare_legs_blue, itm_lyre],def_attrib|level(5),wp(20), knows_common,man_face_young_1, man_face_old_2],
  ["especiales_6","Great Bard Afan Ferddig","Bard",tf_bajo|tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, scn_town_13_castle|entry(1), reserved, fac_commoners,[itm_redvikingshirt,itm_richbluecoat, itm_bare_legs_blue, itm_lyre],def_attrib|level(5),wp(20), knows_common,man_face_young_1, man_face_old_2],

#NPC system changes begin
  #Companions
  ["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

  [
    "npc1","Osmund","Osmund",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
    [
      itm_bluevikingshirt,itm_ankle_boots,itm_knife
    ],
    str_10|agi_9|int_9|cha_6|level(1),wp(50),
    knows_tracking_4|knows_ironflesh_2|knows_weapon_master_2|
    knows_power_throw_2|knows_inventory_management_2|knows_pathfinding_2|
    knows_athletics_3|knows_spotting_3|knows_riding_1, #skills 2/3 player at that level
    0x0000000b8004344b324a95da9965ac5600000000001cf4ee0000000000000000
  ], #chief acabado

  [
    "npc2","Aleifr","Aleifr",
    tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
    [
      itm_linen_tunic,itm_carbatinae_1_bare,itm_club
    ],
    str_7|agi_6|int_9|cha_12|level(1),wp(40),
    knows_ironflesh_2|knows_weapon_master_2|knows_trade_7|
    knows_inventory_management_7|knows_athletics_2|knows_riding_1,
    0x000000094a1013c24756d14224b347af00000000001c36db0000000000000000
  ], #chief acabado

  [
    "npc3","Eithne","Eithene",
    tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
    [
      itm_blue_tunic_long,itm_carbatinae_2,itm_knife
    ],
    str_6|agi_6|int_11|cha_11|level(1),wp(30),
    knows_wound_treatment_5|knows_trade_3|knows_first_aid_5|knows_surgery_2|
    knows_inventory_management_2|knows_athletics_2|knows_riding_1|knows_leadership_2,
    0x000000019f0c8004472355def396431e00000000000f5da30000000000000000
  ], #chief acabado

  [
    "npc4","Athrwys ap Gwawrddur","Arthur",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_leather_jerkin,itm_ankle_boots, itm_spear_2
    ],
    str_10|agi_8|int_8|cha_8|level(1),wpe(70,60,50,40),
    knows_weapon_master_3|knows_power_strike_2|knows_inventory_management_1|
    knows_ironflesh_2|knows_riding_1|knows_athletics_2|knows_power_draw_2|
    knows_shield_2|knows_tactics_4|knows_leadership_2,
    0x00000001a404621064d58e3ae2356e9a00000000001d175d0000000000000000
  ], #chief acabado

  [
    "npc5","Frioc","Frioc",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_linen_tunic,itm_ankle_boots, itm_spear_2
    ],
    str_9|agi_7|int_8|cha_10|level(1),wp(70),
    knows_riding_1|knows_power_strike_3|knows_ironflesh_3|knows_power_throw_2|
    knows_shield_2|knows_leadership_5|knows_weapon_master_2|knows_athletics_2,
    0x000000018310e1c44691ad2333b0acdc00000000001e99230000000000000000
  ], #chief acabado

  [
    "npc6","Bodero","Bodero",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_shirt,itm_ankle_boots,itm_javelin, itm_spear_3
    ],
    str_10|agi_10|int_6|cha_8|level(17),wp(120),
    knows_power_throw_4|knows_weapon_master_2|knows_power_strike_2|knows_ironflesh_2|
    knows_athletics_2|knows_shield_2|knows_trainer_2|knows_leadership_5,
    0x00000001bc08e5c9631e6e279c4d9cdb00000000001d4b720000000000000000
  ], #chief acabado

  [
    "npc7","Bridei","Bridei",
    tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
    [
      itm_picta_4,itm_carbatinae_2_bare, itm_hunting_bow, itm_arrows, itm_knife
    ],
    str_7|agi_11|int_10|cha_6|level(1),wp(60),
    knows_ironflesh_1|knows_inventory_management_2|knows_pathfinding_2|knows_riding_1|
    knows_tracking_5|knows_athletics_2|knows_spotting_2|knows_power_throw_2|
    knows_weapon_master_2|knows_shield_2,
    0x0000000a320cd0014b5388a4da92bb1a00000000001eb96d0000000000000000
  ], #chief acabado

  [
    "npc8","Siwi","Siwi",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_woolen_cap_newwht,itm_shirt,itm_carbatinae_2_bare, itm_spear_3
    ],
    str_10|agi_8|int_6|cha_10|level(1),wp(70),
    knows_weapon_master_3|knows_persuasion_2|knows_power_strike_2|
    knows_ironflesh_2|knows_athletics_3|knows_shield_2|knows_leadership_3|
    knows_entertain_2|knows_inventory_management_2,
    0x0000000afb00e44b4658b263229e34d500000000001d36910000000000000000
  ], #chief acabado

  [
    "npc9","Lothar","Lothar",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_arena_tunic_blue,itm_carbatinae_1_grey, itm_spear_1
    ],
    str_9|agi_10|int_6|cha_9|level(1),wp(70),
    knows_weapon_master_2|knows_persuasion_2|knows_riding_1|knows_athletics_2|
    knows_leadership_1|knows_tactics_2|knows_power_throw_2|knows_power_strike_2|
    knows_ironflesh_2|knows_shield_2,
    0x00000002511002077a9d8e489b8b18af00000000001e26990000000000000000
  ], #chief acabado

  [
    "npc10","Ceawlin","Ceawlin",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_shirt,itm_carbatinae_1_grey, itm_spear_2, itm_talak_seax
    ],
    str_13|agi_10|int_5|cha_6|level(17),wp(100),
    knows_weapon_master_3|knows_trainer_2|knows_leadership_4|knows_ironflesh_5|
    knows_athletics_2|knows_shield_2|knows_power_strike_2|knows_inventory_management_2,
    0x000000015e105004570cae574c6e48fd00000000001f2c9a0000000000000000
  ], #chief acabado

  [
    "npc11","Gwenllian","Gwenllian",
    tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_shirt, itm_ankle_boots, itm_shepherds_crook
    ],
    str_8|agi_11|int_7|cha_8|level(1),wp(70),
    knows_persuasion_3|knows_weapon_master_2|knows_power_strike_2|knows_shield_1|
    knows_first_aid_1|knows_pathfinding_1|knows_inventory_management_2|knows_athletics_2|
    knows_entertain_3|knows_spotting_1|knows_trade_3,
    0x000000019f0c8004472355def396431e00000000000f5da30000000000000000
  ], #chief acabado

  [
    "npc12","Orosio","Orosio",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_sarranid_cavalry_robe,itm_ankle_boots, itm_staff
    ],
    str_10|agi_5|int_13|cha_6|level(1),wp(70),
    knows_ironflesh_2|knows_riding_1|knows_weapon_master_2|knows_athletics_1|
    knows_leadership_1|knows_inventory_management_2|knows_surgery_5|
    knows_wound_treatment_4|knows_first_aid_4,
    0x00000001bf0ce446133331b2a14e26e500000000001ec86b0000000000000000
  ], #chief acabado

  [
    "npc13","Liuva","Liuva",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_arena_tunic_white,itm_carbatinae_1_grey, itm_spear_2
    ],
    str_9|agi_7|int_11|cha_7|level(19),wp(80),
    knows_trainer_4|knows_leadership_1|knows_athletics_2|knows_ironflesh_3|
    knows_power_strike_3|knows_power_throw_2|knows_shield_2|knows_weapon_master_2,
    0x000000079f08520a494d564b6b65b89b00000000001da51e0000000000000000
  ], #chief acabado

  [
    "npc14","Brian","Brian",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_fattiglinenskjortir,itm_carbatinae_1_grey, itm_spear_1
    ],
    str_8|agi_8|int_8|cha_10|level(21),wp(70),
    knows_riding_1|knows_leadership_1|knows_athletics_2|knows_ironflesh_2|
    knows_trainer_3|knows_power_strike_2|knows_power_throw_1|knows_shield_2|
    knows_weapon_master_3|knows_entertain_2,
    0x000000078010120f26c432b56d6948db00000000001da59a0000000000000000
  ], #chief acabado

  [
    "npc15","Agasicles","Agasicles",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_arena_tunic_white,itm_carbatinae_1_grey, itm_spear_5
    ],
    str_8|agi_8|int_12|cha_6|level(1),wp(50),
    knows_tactics_2|knows_engineer_4|knows_trade_1|knows_athletics_2|
    knows_power_throw_2|knows_shield_2|knows_tracking_1|knows_spotting_1,
    0x0000000f5110e45308ec865716aa35ab00000000001d2b8d0000000000000000
  ], #chief acabado

  [
    "npc16","Aedh","Aedh",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_shirt,itm_carbatinae_1_grey, itm_knife,itm_donkey_mount
    ],
    str_9|agi_9|int_6|cha_10|level(1),wp(40),
    knows_ironflesh_3|knows_persuasion_2|knows_weapon_master_2|knows_athletics_2|
    knows_shield_2|knows_surgery_1|knows_wound_treatment_4|knows_first_aid_3,
    0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000
  ], #chief acabado

##########chief mas companions
  [
    "npc_basher","Ciniod","Ciniod",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_war_paint_two, itm_knife, itm_spear_2
    ],
    str_12|agi_6|int_6|cha_4|level(1),wp(70),
    knows_weapon_master_2|knows_power_throw_2|knows_power_strike_2|
    knows_inventory_management_2|knows_looting_2|knows_ironflesh_4|
    knows_athletics_2|knows_shield_2|knows_leadership_3|knows_tactics_2,
    0x000000018400d3c734f6353d5169cad200000000001d2ada0000000000000000
  ], #terminado chief

  [
    "npc_sange","Onuist","Onuist",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_spear_2, itm_war_paintus
    ],
    str_12|agi_13|int_6|cha_5|level(1),wp(70),
    knows_weapon_master_2|knows_power_throw_2|knows_power_strike_2|
    knows_ironflesh_3|knows_athletics_2|knows_shield_2|knows_leadership_3|
    knows_inventory_management_2|knows_looting_3,
    0x00000001bf04b1cd25656dd49d4e691c00000000001e44a40000000000000000
  ], #terminado chief

  ##--
  [
    "npc_paintrain","Eadwine","Eadwine",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_spear_2, itm_shirt, itm_ankle_boots
    ],
    str_9|agi_10|int_9|cha_6|level(1),wpe(50,50,80,70),
    knows_ironflesh_2|knows_wound_treatment_2|knows_weapon_master_2|
    knows_power_draw_2|knows_pathfinding_3|knows_athletics_2|
    knows_tracking_3|knows_spotting_3|knows_riding_1|knows_inventory_management_1, #skills 2/3 player at that level
    0x00000009e710040b2715963724923d0e00000000001dd72e0000000000000000
  ], #explorador

  [
    "npc_hammertime","Mihael ap Cadwalladr","Mihael",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_shirt,itm_carbatinae_1_grey, itm_knife
    ],
    str_7|agi_7|int_9|cha_11|level(1),wp(50),
    knows_weapon_master_2| knows_power_throw_2|knows_pathfinding_4|knows_athletics_1|
    knows_tracking_1|knows_spotting_4|knows_riding_1|knows_inventory_management_2|knows_trade_4, #skills 2/3 player at that level
    0x00000009f408928c24acb238d3692aeb00000000001dbd220000000000000000
  ], #chief acabado

  #starts with short sword
  [
    "npc_tank","Ultan","Ultan",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_staff, itm_robe
    ],
    str_12|agi_6|int_11|cha_5|level(1),wp(30),
    knows_ironflesh_2|knows_persuasion_2|knows_weapon_master_3|knows_power_strike_3|
    knows_athletics_1|knows_inventory_management_2|knows_surgery_1|knows_wound_treatment_4|knows_first_aid_4,
    0x00000009dc0812c6392288c05579cd13000000000012a2d30000000000000000
  ], #druid chief

  [
    "npc_backwoodsharry","Inka","Inka",
    tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_short_bow, itm_arrows, itm_shirt, itm_woolen_dress,itm_knife
    ],
    str_9|agi_12|int_7|cha_6|level(1),wpe(30,70,80,70),
    knows_power_draw_2|knows_weapon_master_2|knows_wound_treatment_1|
    knows_trade_3|knows_power_throw_1|knows_leadership_2|knows_first_aid_1|
    knows_surgery_1|knows_inventory_management_2|knows_athletics_3|knows_riding_1|knows_looting_2,
    0x000000024400100338a1d1d2ecaed44c00000000001536a50000000000000000
  ], #mujer frisia abandonada por su marido chief se lia con eadfrith

  [
    "npc_deadeye","Eadfrith","Eadfrith",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
    [
      itm_black_hood, itm_hand_axe, itm_ankle_boots
    ],
    str_11|agi_10|int_9|cha_4|level(1),wpe(50,70,60,70),
    knows_power_strike_1|knows_weapon_master_1|knows_ironflesh_2|knows_power_throw_2|
    knows_power_draw_2|knows_athletics_2|knows_tracking_3|knows_spotting_3|
    knows_riding_1|knows_inventory_management_1, #skills 2/3 player at that level
    0x00000009d90002ca22d2b2369d8ad4b300000000001e692d0000000000000000
  ],

  [
    "npc_probulator","Matui Turthail","Matui",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_shortened_spear, itm_javelin, itm_shirtc, itm_ankle_boots
    ],
    str_10|agi_6|int_10|cha_8|level(1),wp(50),
    knows_pathfinding_3|knows_tracking_1|knows_spotting_3|knows_leadership_2|
    knows_athletics_1|knows_ironflesh_2|knows_persuasion_2|knows_power_throw_2|
    knows_shield_2|knows_inventory_management_2|knows_weapon_master_1, #skills 2/3 player at that level
    0x00000009c00873014751b0da68ad28e500000000001e151c0000000000000000
  ],

  #starts w/ military scythe
  [
    "npc_grim","Clovis","Clovis",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_shortened_spear, itm_black_hood, itm_robe, itm_ankle_boots
    ],
    str_9|agi_8|int_10|cha_7|level(19),wp(60),
    knows_power_strike_2|knows_weapon_master_2|knows_riding_1|
    knows_ironflesh_2|knows_tactics_3|knows_engineer_3|knows_trade_1|
    knows_athletics_2|knows_power_throw_1|knows_shield_2|knows_trainer_3|
    knows_inventory_management_2,
    0x00000001800462133914b187a2b89b8b00000000001dd8e40000000000000000
  ], #franco

  [
    "npc_enchantress","Connor mac Odhrain","Connor",
    tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
    [
      itm_short_bow, itm_arrows, itm_knife, itm_armor_9, itm_ankle_boots
    ],
    str_10|agi_6|int_6|cha_12|level(1),wpe(40,70,70,70),
    knows_riding_2|knows_power_draw_2|knows_leadership_4|knows_athletics_1|
    knows_ironflesh_2|knows_power_strike_2|knows_power_throw_3|knows_shield_2|
    knows_weapon_master_2|knows_inventory_management_2,
    0x00000009ff0cf414295c45dccc6dc2ec00000000001d34ea0000000000000000
  ], #irlandes
  ##########chief mas companions termina

#NPC system changes end

#governers olgrel rasevas                                                                                              Horse          Bodywear                Footwear_in                              Footwear_out                              Armor                                 Weapon                  Shield                  Headwaer
  ["kingdom_1_lord",  "Cyning Eadbald Aethelberhting",  "Kingdom 1 Lord",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_warhorse_sarranid,   itm_nordiclightarmor1,        itm_decorated_leather_shoes_red,     itm_decorated_leather_shoes_greaves_grey,  itm_vikinglamellar2blue,          itm_leather_gloves,    itm_scimitar_b,      itm_tab_shield_round_c,       itm_vendel14_3, itm_trophy_c],          knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000],
  ["kingdom_2_lord",  "Cyning Cuthwulf Cuthwining",  "Kingdom 2 Lord",  tf_hero, 0,reserved,  fac_kingdom_2,[itm_arabian_horse_a,    itm_nordiclightarmor2,      itm_decorated_leather_shoes,              itm_carbatinae_2_greaves_green,              itm_byrnie_b_new, itm_leather_gloves,      itm_arming_sword,      itm_tab_shield_round_c,      itm_valsgarde_new, itm_trophy_c],    knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000ec50001490a2269f919dee11700000000001cc57d0000000000000000],
  ["kingdom_3_lord",  "Cyning Sigeberht Parvus Saewarding",  "Kingdom 3 Lord",  tf_bajo|tf_hero, 0,reserved,  fac_kingdom_3,[itm_courser,   itm_nordiclightarmor3,            itm_decorated_leather_shoes,              itm_carbatinae_2_greaves_grey,           itm_byrnie_e_new,  itm_leather_gloves,       itm_shortened_spear,              itm_tab_shield_round_c,       itm_vaegir_lamellar_helmet, itm_trophy_c],      knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000ccd0051c8457e2d14d370c65c00000000001ed6d70000000000000000],
  ["kingdom_4_lord",  "Cyning Annan Ening",  "Kingdom 4 Lord",  tf_hero, 0,reserved,  fac_kingdom_4,[itm_arabian_horse_a,    itm_noblemanshirt,    itm_decorated_leather_shoes_orange,              itm_splinted_leather_greaves,                 itm_wolfpelt_mail_coat,  itm_leather_gloves,    itm_suttonhooswordking,           itm_tab_shield_round_c,    itm_talak_sutton_hoo, itm_trophy_c],            knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000],
  ["kingdom_5_lord",  "Cyning Cynegils Ceolricing",  "Kingdom 5 Lord",  tf_hero, 0,reserved,  fac_kingdom_5,[itm_courser,  itm_blue_tunic,             itm_carbatinae_1_green,              itm_decorated_leather_shoes_greaves_grey,   itm_mail_coat_5,  itm_leather_gloves,         itm_arabian_sword_a,         itm_tab_shield_round_c,        itm_spangenhelm_a_ornate, itm_trophy_c],         knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000efc04118125848dac5d50d62400000000001d48b80000000000000000],
  ["kingdom_6_lord",  "Dryhten Eanhere",  "Kingdom 6 Lord",  tf_alto|tf_hero, 0,reserved,  fac_kingdom_6,[itm_steppe_outfit,             itm_carbatinae_1_green,              itm_mail_chausses,   itm_mail_coat_6,  itm_leather_gloves,         itm_woden_fury,        itm_spangenhelm_a_trim, itm_trophy_c],         knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x0000000abf0c21924de54f34ad61ffff00000000001e7b670000000000000000], #yeyo chief
  ["kingdom_7_lord",  "Ri Morfael map Cyndrwyn Glas",  "Kingdom 7 Lord",  tf_hero, 0,reserved,  fac_kingdom_7,[itm_warhorses4,   itm_romantunic_purple,      itm_carbatinae_1_green,     itm_carbatinae_2_red,  itm_mail_coat_1_trig,          itm_leather_gloves,    itm_siren_song,      itm_tab_shield_round_c,       itm_rathos_spangenhelm_a_gold_decorated, itm_trophy_c],          knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x00000007260c52051914673b52a6d91300000000001f57190000000000000000], #cara real rey chief
  ["kingdom_8_lord",  "Ri Petroc Baladrddellt map Clement",  "Kingdom 8 Lord",  tf_hero, 0,reserved,  fac_kingdom_8,[itm_warhorses4,    itm_cloaked_tunic,      itm_carbatinae_1_green,              itm_carbatinae_2_greaves_orange,              itm_mail_coat_2, itm_leather_gloves,      itm_arabian_sword_d,      itm_tab_shield_round_c,      itm_dux_ridge_helm_gold, itm_trophy_c],    knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000c981013c40add69b4a591b92300000000001e2b630000000000000000], #cara real rey chief
  ["kingdom_9_lord",  "Cyning Penda Pybbing",  "Kingdom 9 Lord",  tf_oso|tf_hero, 0,reserved,  fac_kingdom_9,[itm_charger,   itm_shirt_red,        itm_decorated_leather_shoes_orange,     itm_decorated_leather_shoes_greaves_grey,  itm_wolf_coat1,          itm_leather_gloves,    itm_one_handed_battle_axe_c,      itm_tab_shield_round_c,       itm_briton_helm6, itm_trophy_c],          knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x00000008aa08d1cf3a9952c8e17a32de00000000001dd71c0000000000000000], #cara real rey chief
  ["kingdom_10_lord",  "Ri Allech map Tudwal",  "Kingdom 10 Lord",  tf_hero, 0,reserved,  fac_kingdom_10,[itm_arabian_horse_b,   itm_sleeveless_leather_tunic,             itm_decorated_leather_shoes_green,              itm_mail_chausses,           itm_byrnie_c_new,  itm_leather_gloves,       itm_nomad_sabre,              itm_tab_shield_round_c,       itm_dux_ridge_helm_gold, itm_trophy_c],      knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x000000089e002091186493392265c8e400000000001e96220000000000000000], #cara real rey chief
  ["kingdom_11_lord",  "Ri Cynddylan map Cyndrwyn Glas",  "Kingdom 11 Lord",  tf_alto|tf_hero, 0,reserved,  fac_kingdom_11,[itm_arabian_horse_a,    itm_shirt_red,    itm_decorated_leather_shoes_green,              itm_decorated_leather_shoes_greaves_grey,                 itm_mail_coat_1,  itm_leather_gloves,    itm_bastard_sword_a,           itm_tab_shield_round_c, itm_sib_couronne, itm_trophy_c],            knight_attrib_5,wp(250),knight_skills_5|knows_trainer_5, 0x00000003fc041144245396b72cb5db6e00000000001ea9560000000000000000], #cara real rey chief
  ["kingdom_12_lord",  "Ri Mynyddog Mwynfawr map Cunbelin",  "Kingdom 12 Lord",  tf_hero, 0,reserved,  fac_kingdom_12,[itm_arabian_horse_b,  itm_bl_tunic01,             itm_carbatinae_2_red,              itm_carbatinae_2_greaves_green,   itm_mail_hauberk,  itm_leather_gloves,         itm_one_handed_battle_axe_b,         itm_tab_shield_round_c,        itm_rathos_spangenhelm_a_gold_decorated, itm_trophy_c],         knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000fc60c544732e4923b558d38f500000000001db7260000000000000000],  #cara real rey chief
  ["kingdom_13_lord",  "Brytenwalda Oswald Aethelfrithing",  "Kingdom 13 Lord",  tf_hero, 0,reserved,  fac_kingdom_13,[itm_courser,  itm_bl_tunic01,             itm_carbatinae_2_red,              itm_carbatinae_2_greaves_blue,   itm_mail_coat_6,  itm_leather_gloves,         itm_sword,         itm_tab_shield_round_c,        itm_sib_lombardy, itm_trophy_c],         knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x00000008811003c812db8b3c9bc526dc00000000001e5b240000000000000000], #cara real rey chief
  ["kingdom_14_lord",  "Cyning Eanferth Biscoping",  "Kingdom 14 Lord",  tf_hero, 0,reserved,  fac_kingdom_14,[itm_arabian_horse_a,    itm_bl_tunic09,    itm_carbatinae_2_green,              itm_splinted_leather_greaves,                 itm_mail_coat_5,  itm_leather_gloves,    itm_sarranid_cavalry_sword,           itm_tab_shield_round_c,    itm_felt_steppe_cap, itm_trophy_c],            knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000e010441533699513c5b6e94f200000000001da6ac0000000000000000],
  ["kingdom_15_lord",  "Ri Rhoedd map Rhun",  "Kingdom 15 Lord",  tf_hero, 0,reserved,  fac_kingdom_15,[itm_courser,  itm_bl_tunic10,             itm_carbatinae_2_green,              itm_decorated_leather_shoes_greaves_grey,   itm_mail_coat_1,  itm_leather_gloves,         itm_long_spiked_club,         itm_tab_shield_round_c,        itm_rathos_spangenhelm_b_gold_decorated, itm_trophy_c],         knight_attrib_5,wp(250),knight_skills_5|knows_trainer_5, 0x00000008a108704528d395c7a28f34cb00000000001d88e40000000000000000], #cara real rey chief
  ["kingdom_16_lord",  "Gwdelic Dwywg map Llywarch",  "Kingdom 16 Lord",  tf_hero, 0,reserved,  fac_kingdom_16,[itm_romantunic_purple,             itm_carbatinae_2_green,              itm_mail_chausses,   itm_wei_xiadi_sar_hauberk,  itm_leather_gloves,         itm_thunder,        itm_briton_helm7, itm_trophy_c],         knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x00000008910815864ae4f532eb4a48ce00000000001eca250000000000000000], #cara real rey chief
  ["kingdom_17_lord",  "Ruire Rogallach mac Matach",  "Kingdom 17 Lord",  tf_hero, 0,reserved,  fac_kingdom_17,[itm_warhorse,    itm_nobleman_outfit,      itm_decorated_leather_shoes_bare,              itm_carbatinae_2_greaves_green,              itm_mail_shirt_8_trig, itm_leather_gloves,      itm_sword_viking_2,      itm_tab_shield_round_c,      itm_szpadelhelmet_gold, itm_trophy_c],    knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x000000088a086547246d88b8d92cc55b00000000001d596a0000000000000000], #cara real rey chief
  ["kingdom_18_lord",  "Ri Bili map Neithon",  "Kingdom 18 Lord",  tf_hero, 0,reserved,  fac_kingdom_18,[itm_courser,    itm_nordiclightarmor10,      itm_carbatinae_2_red,              itm_carbatinae_2_greaves_orange,              itm_byrnie_g_new, itm_leather_gloves,      itm_sword_viking_1,      itm_tab_shield_round_c,      itm_dux_ridge_helm_gold, itm_trophy_c],    knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000fe21072801b2357ccc56a426400000000001f6b760000000000000000], #cara real rey chief
  ["kingdom_19_lord",  "Ruire Domnall Brecc mac Echach",  "Kingdom 19 Lord",  tf_hero, 0,reserved,  fac_kingdom_19,[itm_warhorse,   itm_courtly_outfit,        itm_decorated_leather_shoes_bare,     itm_decorated_leather_shoes_greaves_grey,  itm_haubergeon,          itm_leather_gloves,    itm_sword_of_war,      itm_tab_shield_round_c,       itm_szpadelhelmet_gold, itm_trophy_c],          knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x000000065205920736a269baa652572900000000001dd8ae0000000000000000], #cara real rey chief
  ["kingdom_20_lord",  "Ri Gartnait map Gwid",  "Kingdom 20 Lord",  tf_hero, 0,reserved,  fac_kingdom_20,[itm_hunter,   itm_tribal_warrior_outfit,             itm_decorated_leather_shoes_bare,              itm_mail_chausses,           itm_haubergeon,  itm_leather_gloves,       itm_sword_viking_3,              itm_tab_shield_round_c,       itm_szpadelhelmet_gold, itm_trophy_c],      knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000a74116356591c8a266c92c96200000000001e3aa50000000000000000], #cara real rey chief
  ["kingdom_21_lord",  "Ri Clydog map Arthlwys",  "Kingdom 21 Lord",  tf_hero, 0,reserved,  fac_kingdom_21,[itm_warhorse_sarranid,    itm_romantunic_purple,    itm_decorated_leather_shoes_blue,              itm_decorated_leather_shoes_greaves_grey,                 itm_idi_scale14,  itm_leather_gloves,    itm_sword_medieval_c_long,           itm_tab_shield_round_c, itm_briton_helm6, itm_trophy_c],            knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000e0b103342779bc95727b1c8ed00000000001e295a0000000000000000],
  ["kingdom_22_lord",  "Ri Eluan map Cyndrwyn Glas",  "Kingdom 22 Lord",  tf_hero, 0,reserved,  fac_kingdom_22,[itm_courser,  itm_nordiclightarmor11,             itm_decorated_leather_shoes_blue,              itm_carbatinae_2_greaves_green,   itm_byrnie_c_new,  itm_leather_gloves,         itm_shortened_spear,         itm_tab_shield_round_c,        itm_briton_helm7, itm_trophy_c],         knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000efc04118125848dac5d50d62400000000001d48b80000000000000000],
  ["kingdom_23_lord",  "Ri Cadfael Cadomedd map Cynfeddw",  "Kingdom 23 Lord",  tf_hero, 0,reserved,  fac_kingdom_23,[itm_charger,  itm_nordiclightarmor12,             itm_decorated_leather_shoes_grey,              itm_carbatinae_2_greaves_blue,   itm_byrnie_d_new,  itm_leather_gloves,         itm_sword_medieval_c,         itm_tab_shield_round_c,        itm_rathos_spangenhelm_a_gold_decorated, itm_trophy_c],         knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x000000080c0c5040554d8547226db6a400000000001d36e90000000000000000], #cara real rey chief
  ["kingdom_24_lord",  "Ri Nowy Hen map Arthur",  "Kingdom 24 Lord",  tf_hero, 0,reserved,  fac_kingdom_24,[itm_warhorse_sarranid,    itm_nordiclightarmor10,    itm_decorated_leather_shoes_grey,              itm_splinted_leather_greaves,                 itm_mail_shirt_8_trig,  itm_leather_gloves,    itm_sword_medieval_a,           itm_tab_shield_round_c,    itm_rathos_spangenhelm_b_gold_decorated, itm_trophy_c],            knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000fc80833d334ed8627656dc32e00000000001d98e10000000000000000], #cara real rey chief
  ["kingdom_25_lord",  "Ri Rhiwallon map Idwallon",  "Kingdom 25 Lord", tf_hero, 0,reserved,  fac_kingdom_25,[itm_courser,  itm_nordiclightarmor11,             itm_carbatinae_1_red,              itm_decorated_leather_shoes_greaves_grey,   itm_byrnie4,  itm_leather_gloves,         itm_sword_medieval_b,         itm_tab_shield_round_c,        itm_rathos_spangenhelm_a_gold_decorated, itm_trophy_c],         knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000eff10c1110b192f2b1c91b35c00000000001e47700000000000000000],
  ["kingdom_26_lord",  "Ri Meurig map Tewrig",  "Kingdom 26 Lord",  tf_hero, 0,reserved,  fac_kingdom_26,[itm_warhorse_sarranid,  itm_nordiclightarmor12,             itm_carbatinae_1_red,              itm_mail_chausses,   itm_mail_hauberk,  itm_leather_gloves,         itm_long_hafted_knobbed_mace,         itm_tab_shield_round_c,        itm_szpadelhelmet6, itm_trophy_c],         knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000b660c20064754af28f3d248e400000000001ed74b0000000000000000], #cara real rey chief
  ["kingdom_27_lord",  "Ruire Faelan mac Colmain Mair",  "Kingdom 27 Lord",  tf_hero, 0,reserved,  fac_kingdom_27,[itm_hunter,   itm_nomad_armor,        itm_decorated_leather_shoes_bare,     itm_decorated_leather_shoes_greaves_green,  itm_mail_coat_3,          itm_leather_gloves,    itm_long_hafted_spiked_mace,      itm_tab_shield_round_c,       itm_szpadelhelmet6, itm_trophy_c],          knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x000000005000234432e2aa392aadc71100000000001dd8690000000000000000], #cara real rey chief
  ["kingdom_28_lord",  "Ruire Failbhe Flann mac Aedho",  "Kingdom 28 Lord",  tf_hero, 0,reserved,  fac_kingdom_28,[itm_warhorse,    itm_nordic_outfit2,      itm_decorated_leather_shoes_bare,              itm_carbatinae_2_greaves_orange,              itm_mail_shirt_8_trig, itm_leather_gloves,      itm_shortened_spear,      itm_tab_shield_round_c,      itm_szpadelhelmet_gold, itm_trophy_c],    knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x000000094b1011c85976514960992d2300000000001e58d90000000000000000], #cara real rey chief
  ["kingdom_29_lord",  "Ruire Congal Caech mac Scandal Sciathlethan",  "Kingdom 29 Lord",  tf_bajo|tf_hero, 0,reserved,  fac_kingdom_29,[itm_khergit_armor,        itm_decorated_leather_shoes_bare,     itm_decorated_leather_shoes_greaves_grey,  itm_mail_shirt_8_trig,          itm_leather_gloves,    itm_sword_khergit_1,      itm_tab_shield_round_c,       itm_szpadelhelmet_gold, itm_trophy_c],          knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x000000097b1004474519550522693a9c00000000001e369a0000000000000000], #cara real rey chief
  ["kingdom_30_lord",  "Ard Ruire Domnaill mac Aedho",  "Kingdom 30 Lord", tf_hero, 0,reserved,  fac_kingdom_30,[itm_hunter,   itm_hide_armor,             itm_decorated_leather_shoes_bare,              itm_carbatinae_2_greaves_grey,           itm_mail_coat_2,  itm_leather_gloves,       itm_sword_medieval_b_small,              itm_tab_shield_round_c,       itm_szpadelhelmet6, itm_trophy_c],      knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000ead00328f354e91972451d8ac00000000001d56d90000000000000000], #cara real rey chief
  ["kingdom_31_lord",  "Ruire Mael Odhar Caech mac Feradaig",  "Kingdom 31 Lord",  tf_hero, 0,reserved,  fac_kingdom_31,[itm_hunter,   itm_nordic_armor,        itm_decorated_leather_shoes_bare,     itm_decorated_leather_shoes_greaves_grey,  itm_mail_shirt_8_trig,          itm_leather_gloves,    itm_sword_of_war,      itm_tab_shield_round_c,       itm_szpadelhelmet6, itm_trophy_c],          knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000fab0022c355596d379e6dab5d00000000001f6ba10000000000000000], #cara real rey chief


#    Imbrea   Belinda Ruby Qaelmas Rose    Willow
  #  Alin  Ganzo            Zelka Rabugti
  #  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina
  # Dunga        Agatha     Dibus Crahask

#                                                                                                              Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
  #Swadian civilian clothes: itm_bluevikingshirt itm_leather_jerkin itm_padded_jack_4_trig itm_padded_jack_4_trig itm_nobleman_outfit itm_rich_outfit itm_short_tunic itm_tabard
  #Older knights with higher skills moved to top
  ["knight_1_1", "Aetheling Eormenred Eadbalding", "Aetheling Eormenred Eadbalding", tf_hero, 0, reserved,  fac_kingdom_1, [itm_arabian_horse_a,itm_bl_tunic09,      itm_mail_coat_1_trig,   itm_decorated_leather_shoes, itm_splinted_leather_greaves,       itm_vaegir_spiked_helmet,           itm_valssword,  itm_leather_gloves,         itm_tab_shield_round_c],   knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x00000007a6002194125b6db6cb6db6db00000000001db6c30000000000000000], #adorno chief
  ["knight_1_2", "Aetheling Eorcenberht Eadbalding", "Aetheling Eorcenberht Eadbalding", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse_sarranid,itm_noblemanshirt_gaelic,      itm_vikinglamellar2blue,   itm_decorated_leather_shoes_red, itm_splinted_leather_greaves,       itm_vendel14_2,           itm_valssword,  itm_leather_gloves,         itm_tab_shield_round_c],    knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x00000001bd00258736db6db6db6db6db00000000001db6db0000000000000000], #rad chief
  ["knight_1_3", "Ealdorman Aethelwald", "Ealdorman Aethelwald", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_noblemanshirt_pictish,     itm_vikinglamellar2red,                 itm_carbatinae_2_blue,              itm_decorated_leather_shoes_greaves_green,                      itm_sarranid_felt_hat,  itm_leather_gloves,     itm_axehammer_1,   itm_tab_shield_round_c],   knight_attrib_1|knows_trainer_1,wp(200),knight_skills_1, 0x000000099c00020958dc6e2484b6a11b00000000001d4cde0000000000000000],

  ["knight_2_1", "Aetheling Ceowald Cuthwulfing", "Aetheling Ceowald Cuthwulfing", tf_hero, 0, reserved,  fac_kingdom_2, [itm_courser,itm_redvikingshirt,      itm_mail_coat_2_trig,   itm_decorated_leather_shoes, itm_splinted_leather_greaves,       itm_bascinet,           itm_frankish_axe2,  itm_leather_gloves,         itm_tab_shield_round_c],       knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x00000001ad0c620628ab4c688b2ddb1b0000000000113caa0000000000000000],
  ["knight_2_2", "Ealdorman Ceadda Cuthwining", "Ealdorman Ceadda Cuthwining", tf_hero, 0, reserved,  fac_kingdom_2, [itm_arabian_horse_a,      itm_noblemanshirt_pictish,     itm_vikinglamellar2yellow,                 itm_carbatinae_1_green,              itm_decorated_leather_shoes_greaves_green,                      itm_sipahi_helmet_a,  itm_leather_gloves,     itm_bl_shsword,   itm_tab_shield_round_c],  knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000d800c30c3099126a49c71c8eb00000000001d859c0000000000000000],
  ["knight_2_3", "Ealdorman Cynebald Cuthwining", "Ealdorman Cynebald Cuthwining", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse_sarranid,      itm_mail_shirt_wht,   itm_mail_shirt_wht,                 itm_carbatinae_2_blue,              itm_decorated_leather_shoes_greaves_green,                      itm_black_helmet,  itm_leather_gloves,     itm_bl_shsword,   itm_tab_shield_round_c],    knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x0000000da70825d0449c71b94cb1b51200000000000e38e30000000000000000],

  ["knight_3_1", "Ealdorman Saebbi Seaxreding", "Ealdorman Saebbi Seaxreding", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,      itm_mail_shirtdeer,     itm_mail_shirtdeer,                 itm_decorated_leather_shoes,              itm_decorated_leather_shoes_greaves_green,                      itm_khergit_helmet,  itm_leather_gloves,     itm_suttonhoosword,   itm_tab_shield_round_c],   knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x00000001b200248956e4ad471d95e77400000000000d25240000000000000000],
  ["knight_3_2", "Ealdorman Swithhelm Seaxbalding", "Ealdorman Swithhelm Seaxbalding", tf_hero, 0, reserved,  fac_kingdom_3, [itm_arabian_horse_a,      itm_mail_shirt_ylw,     itm_mail_shirt_ylw,                 itm_carbatinae_1_green,              itm_decorated_leather_shoes_greaves_green,                      itm_desert_turban,  itm_leather_gloves,     itm_bl_shsword,   itm_tab_shield_round_c],    knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000d0410528f5ba295b49438dc5c00000000001daad40000000000000000],
  ["knight_3_3", "Ealdorman Swithfrith Seaxbalding", "Ealdorman Swithfrith Seaxbalding", tf_hero, 0, reserved,  fac_kingdom_3, [  itm_mail_shirt_blk,  itm_mail_shirt_blk,   itm_carbatinae_2_blue,  itm_decorated_leather_shoes_greaves_green,   itm_valsgarde_new, itm_leather_gloves, itm_bl_shsword,  itm_tab_shield_round_c, itm_light_throwing_axes],      knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x0000000d030812002c92aa3c94ca18a300000000001e36b50000000000000000],

  ["knight_4_1", "Aetheling Eormin Annaning", "Aetheling Eormin Annaning", tf_hero, 0, reserved,  fac_kingdom_4, [itm_charger,itm_redvikingshirt,      itm_nowa,   itm_decorated_leather_shoes, itm_splinted_leather_greaves,       itm_vaegir_war_helmet,           itm_suttonhoosword,  itm_leather_gloves,         itm_tab_shield_round_c], knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000c800c42c44a6590c96ab1c91d00000000001e470c0000000000000000],
  ["knight_4_2", "Ealdorman Aethelhere Ening", "Ealdorman Aethelhere Ening", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse_sarranid,      itm_byrnie_b_new,     itm_byrnie_b_new,                 itm_carbatinae_2_blue,              itm_decorated_leather_shoes_greaves_blue,                      itm_spangenhelm_helm,  itm_leather_gloves,     itm_suttonhoosword,   itm_tab_shield_round_c],   knight_attrib_4,wp(240),knight_skills_4, 0x00000009810803ca476ab0a336b2175400000000001da9d40000000000000000],
  ["knight_4_3", "Ealdorman Aethelric Ening", "Ealdorman Aethelric Ening", tf_hero, 0, reserved,  fac_kingdom_4, [itm_arabian_horse_a,      itm_byrnie2,     itm_byrnie2,                 itm_carbatinae_1_red,              itm_decorated_leather_shoes_greaves_blue,                      itm_talak_sutton_hoo,  itm_leather_gloves,     itm_new_sword4,   itm_tab_shield_round_c],    knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x0000000dc20092894913a9390c6a4ddb00000000001e594b0000000000000000],
  ["knight_4_4", "Ealdorman Aethelwald Ening", "Ealdorman Aethelwald Ening", tf_hero, 0, reserved,  fac_kingdom_4, [itm_courser,      itm_mail_shirt_red,     itm_mail_shirt_red,                 itm_carbatinae_1_green,              itm_decorated_leather_shoes_greaves_blue,                      itm_spangenhelm_helm,  itm_leather_gloves,     itm_new_sword4,   itm_tab_shield_round_c],   knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x000000000000030015dd45db236dd6db00000000001ea6b80000000000000000], # verbeek chief
  ["knight_4_5", "Ealdorman Tondberct", "Ealdorman Tondberct", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_mail_shirt_grn,  itm_mail_shirt_grn,   itm_carbatinae_2_blue,  itm_decorated_leather_shoes_greaves_blue,   itm_rath_spangenlord5, itm_leather_gloves, itm_le_pictishsword7,  itm_tab_shield_round_c, itm_light_throwing_axes],       knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000a400010c9350ba5c99222d59c00000000001f43230000000000000000],
  ["knight_4_6", "Dryhten Ealdwulf Aethelricing", "Dryhten Ealdwulf Aethelricing", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_mail_shirtdeer,        itm_mail_shirtdeer,                   itm_carbatinae_1_orange,            itm_decorated_leather_shoes_orange,                   itm_vendel_helmet2,    itm_leather_gloves,    itm_talak_bearded_axe,        itm_tab_shield_round_c],  knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x0000000a5e0022c9175c5226686ac75100000000001ee7180000000000000000],

  ["knight_5_1", "Ealdorman Cwichelm Ceolricing", "Ealdorman Cwichelm Ceolricing", tf_hero, 0, reserved,  fac_kingdom_5, [itm_charger,      itm_byrnie_e_new,     itm_byrnie_e_new,                 itm_decorated_leather_shoes,              itm_decorated_leather_shoes_greaves_blue,                      itm_vendel_helmet,  itm_leather_gloves, itm_bl_shsword,   itm_tab_shield_round_c],    knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x000000001c0011c7292dc6659b88c57600000000001e4b7a0000000000000000], #BrustwarzenLenny chief
  ["knight_5_2", "Aetheling Cenwalh Cynegilsing", "Aetheling Cenwalh Cynegilsing", tf_hero, 0, reserved,  fac_kingdom_5, [itm_arabian_horse_b,itm_byrnie_f_new,      itm_byrnie_f_new,   itm_carbatinae_1_red, itm_splinted_leather_greaves,       itm_gaul_helmet,           itm_bl_shsword,  itm_leather_gloves,         itm_tab_shield_round_c],   knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x00000005c00c518a266255c725da32cb00000000001cb3640000000000000000],
  ["knight_5_3", "Aetheling Ethelwine Cynegilsing", "Aetheling Ethelwine Cynegilsing", tf_hero, 0, reserved,  fac_kingdom_5, [itm_courser,itm_byrnie2,      itm_byrnie2,   itm_carbatinae_1_orange, itm_splinted_leather_greaves,       itm_spangenhelm_a_ornate,           itm_le_richsword2,  itm_leather_gloves,         itm_tab_shield_round_c, itm_had_seax],    knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x0000000e4004028516949549946b149300000000001e18450000000000000000],
  ["knight_5_4", "Aetheling Centwine Cynegilsing", "Aetheling Centwine Cynegilsing", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_sarranid,itm_vikinglamellar3,      itm_vikinglamellar3,   itm_decorated_leather_shoes_red, itm_splinted_leather_greaves,       itm_spangenhelm_a_ornate,        itm_leather_gloves,   itm_talak_bearded_axe,       itm_tab_shield_round_c],      knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x000000098008134d0a6d4dab2596429b00000000001f3a990000000000000000],
  ["knight_5_5", "Ealdorman Cuthgils Ceolwulfing", "Ealdorman Cuthgils Ceolwulfing", tf_hero, 0, reserved,  fac_kingdom_5, [itm_mercia_tunic1,itm_tattered_leather_armor_red,     itm_mail_coat_1_trig,                 itm_carbatinae_1_orange,              itm_decorated_leather_shoes_greaves_blue,                      itm_spangenhelm_a_trim,  itm_leather_gloves,     itm_le_richsword2,   itm_tab_shield_round_c], knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x000000098004038a28cb2a24927b2d1900000000001e64930000000000000000],
  ["knight_5_6", "Dryhten Cuthred Cwichelming", "Dryhten Cuthred Cwichelming", tf_hero, 0, reserved,  fac_kingdom_5, [  itm_tattered_leather_armor_blu,        itm_byrnie_c_new,                   itm_carbatinae_2_blue,            itm_decorated_leather_shoes_orange,                   itm_rath_spangenlord5,    itm_leather_gloves,    itm_le_richsword2,        itm_tab_shield_round_c],    knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x00000009801040c928d38afb348d436300000000001dc31b0000000000000000],
  ["knight_5_7", "Dryhten Cenfert Cuthgilsing", "Dryhten Cenfert Cuthgilsing", tf_hero, 0, reserved,  fac_kingdom_5, [  itm_tattered_leather_armor_ylw,        itm_mail_shirtdeer,                   itm_carbatinae_2_blue,            itm_decorated_leather_shoes_orange,                   itm_vendel_helmet2,    itm_leather_gloves,    itm_talak_nordic_axe,        itm_tab_shield_round_c],    knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x00000009a6046291452099b8d96e64140000000000194da30000000000000000],

  ["knight_6_1", "Dryhten Eanfrith", "Dryhten Eanfrith", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,            itm_swadian_mail_hauberk,        itm_swadian_mail_hauberk,                   itm_decorated_leather_shoes,            itm_decorated_leather_shoes_orange,                   itm_gaul_helmet,    itm_leather_gloves,    itm_new_sword2,        itm_tab_shield_round_c],     knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000c131031c546a38a2765b4c86000000000001e58d30000000000000000, vaegir_face_older_2],
  ["knight_6_2", "Ecgwald", "Ecgwald", tf_hero, 0, reserved,  fac_kingdom_6, [  itm_mail_shirt_bluehorses,      itm_mail_shirt_bluehorses,               itm_carbatinae_1_orange,            itm_decorated_leather_shoes_greaves_orange,                    itm_khergit_lady_hat,   itm_leather_gloves,       itm_sarranid_axe_b,    itm_tab_shield_round_c],    knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x0000000c2f0832c748f272540d8ab65900000000001d34e60000000000000000, vaegir_face_older_2],

  ["knight_7_1", "Mael Morcant Glas map Morfael", "Edling Morgan Glas ap Morfael", tf_hero, 0, reserved,  fac_kingdom_7, [itm_courser,itm_wei_xiadi_sar_hauberk,      itm_wei_xiadi_sar_hauberk,   itm_decorated_leather_shoes, itm_splinted_leather_greaves,       itm_dux_ridge_helm_gold,           itm_le_pictishsword2,  itm_leather_gloves,         itm_tab_shield_round_c, itm_javelin],   knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x00000001870862c13a928a44ec5012f200000000001d57120000000000000000],

  ["knight_8_1", "Mael Culmin map Petroc", "Edling Cwlfyn ap Petroc", tf_hero, 0, reserved,  fac_kingdom_8, [itm_arabian_horse_a,itm_coat_of_plates,      itm_coat_of_plates,   itm_decorated_leather_shoes, itm_splinted_leather_greaves,       itm_briton_helm7,           itm_new_sword2,  itm_leather_gloves,         itm_tab_shield_round_c, itm_javelin],     knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x00000004530c440637928a38cc6de2a400000000001dcaa50000000000000000], #cara real rey chief
  ["knight_8_2", "Guledic Bleddyn map Bledric", "Tywysog Bleddyn ap Bledric", tf_hero, 0, reserved,  fac_kingdom_8, [itm_courser, itm_mail_shirt_blk, itm_mail_shirt_blk, itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_rathos_spangenhelm_b_gold,  itm_leather_gloves, itm_new_sword1, itm_tab_shield_round_c, itm_javelin], knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x0000000199002148439a774513a93aeb00000000001c23220000000000000000], #Palestine
  ["knight_8_3", "Guledic Brochwel map Petroc", "Tywysog Brochwel ap Petroc", tf_hero, 0, reserved,  fac_kingdom_8, [itm_charger, itm_heraldic_mail_with_tunic, itm_mail_shirt_a_copy, itm_carbatinae_1_orange, itm_decorated_leather_shoes_greaves_grey, itm_briton_helm3, itm_leather_gloves, itm_spatha, itm_tab_shield_round_c, itm_javelin],    knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x00000007130c300436d28a24cc6dc8a300000000001ecb250000000000000000], #cara real rey chief
  ["knight_8_4", "Tiern Tewdwr map Peredur", "Udd Tewdwr ap Peredur", tf_hero, 0, reserved,  fac_kingdom_8, [  itm_mail_shirt_whiteaxes, itm_mail_shirt_whiteaxes,  itm_carbatinae_2_orange, itm_carbatinae_2_greaves_green, itm_briton_helm4,    itm_leather_gloves,    itm_new_sword2, itm_shield_round_07, itm_javelin],    knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000c0f04024b2509d5d53944c6a300000000001d5b320000000000000000, vaegir_face_old_2],
  ["knight_8_5", "Tiern Ednowain map Bleddyn", "Udd Ednowain ap Bleddyn", tf_hero, 0, reserved,  fac_kingdom_8, [itm_arabian_horse_b, itm_mail_shirt_green,     itm_mail_shirt_green, itm_carbatinae_2_blue, itm_decorated_leather_shoes_greaves_grey, itm_rathos_spangenhelm_yellow_plum,  itm_leather_gloves,     itm_new_sword1, itm_tab_shield_round_c, itm_javelin],    knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000c1d0821d236acd6991b74d69d00000000001e476c0000000000000000, vaegir_face_middle_2],
  ["knight_8_6", "Tiern Dywel map Bledric", "Udd Dywel ap Bledric", tf_hero, 0, reserved,  fac_kingdom_8, [itm_mail_shirt_brown,     itm_mail_shirt_brown, itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_barf_helm, itm_leather_gloves, itm_sarranid_axe_b, itm_tab_shield_round_c, itm_javelin],      knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x0000000f7c00520e66b76edd5cd5eb6e00000000001f691e0000000000000000, vaegir_face_older_2],

  ["knight_9_1", "Aetheling Peada Pending", "Aetheling Peada Pending", tf_hero, 0, reserved,  fac_kingdom_9, [itm_arabian_horse_a,itm_wolfpelt_mail_coat,      itm_wolfpelt_mail_coat,   itm_decorated_leather_shoes, itm_splinted_leather_greaves,       itm_talak_spangenhelm,           itm_le_pictishsword7,  itm_leather_gloves,         itm_tab_shield_round_c],     knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x000000044900018832a696b4da8dc59300000000001d46b20000000000000000], #cara real rey chief
  ["knight_9_2", "Ealdorman Eowa Pybbing", "Ealdorman Eowa Pybbing", tf_hero, 0, reserved,  fac_kingdom_9, [itm_arabian_horse_b,      itm_mail_shirt_8_trig,     itm_mail_shirt_8_trig,                 itm_carbatinae_2_blue,              itm_decorated_leather_shoes_greaves_blue,                      itm_nordic_helmet,  itm_leather_gloves,     itm_new_sword4,   itm_tab_shield_round_c],    knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x0000000c27046000471bd2e93375b52c00000000001dd5220000000000000000, vaegir_face_older_2],
  ["knight_9_3", "Ealdorman Coenwalh Pybbing", "Ealdorman Coenwalh Pybbing", tf_hero, 0, reserved,  fac_kingdom_9, [itm_hauberk6,     itm_hauberk6,                 itm_carbatinae_1_orange,              itm_decorated_leather_shoes_greaves_blue,                      itm_nomad_cap_b,  itm_leather_gloves,     itm_talak_nordic_axe,   itm_tab_shield_round_c],       knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x000000038b0453492663827dce85569f00000000001cfaa30000000000000000], #Uruksoth chief clan cuervo
  ["knight_9_4", "Aetheling Wulfhere Pending", "Aetheling Wulfhere Pending", tf_hero, 0, reserved,  fac_kingdom_9, [itm_charger,itm_byrnie2,      itm_byrnie2,   itm_decorated_leather_shoes_red, itm_splinted_leather_greaves,       itm_talak_spangenhelm,  itm_leather_gloves,  itm_le_pictishsword7,        itm_tab_shield_round_c],   knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x00000004570c525456a269e99b6de71a00000000001cb7190000000000000000], #cara real rey chief
  ["knight_9_5", "Ealdorman Frithewalh", "Ealdorman Frithewalh", tf_hero, 0, reserved,  fac_kingdom_9, [itm_warhorse_sarranid,      itm_mail_shirtdeer,     itm_mail_shirtdeer,                 itm_carbatinae_2_blue,              itm_decorated_leather_shoes_greaves_blue,                      itm_nordic_helmet,  itm_leather_gloves,     itm_new_sword4,   itm_tab_shield_round_c],    knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000a070c4387374bd19addd2a4ab00000000001e32cc0000000000000000, vaegir_face_old_2],
  ["knight_9_6", "Ealdorman Beorhtferth", "Ealdorman Beorhtferth", tf_hero, 0, reserved,  fac_kingdom_9, [  itm_mail_coat_1_trig,itm_mail_coat_1_trig,   itm_carbatinae_2_blue,  itm_decorated_leather_shoes_greaves_grey,   itm_horn_helmet_3, itm_leather_gloves, itm_new_sword4,  itm_tab_shield_round_c, itm_light_throwing_axes],    knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000b670012c23d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_older_2],
  ["knight_9_7", "Dryhten Osmod Eowing", "Dryhten Osmod Eowing", tf_hero, 0, reserved,  fac_kingdom_9, [itm_courser,      itm_byrnie,        itm_byrnie,                   itm_carbatinae_2_blue,            itm_decorated_leather_shoes_orange,                   itm_horn_helmet_3,    itm_leather_gloves,    itm_new_sword4,        itm_tab_shield_round_c],    knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000e070050853b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],
  ["knight_9_8", "Dryhten Alwih Eowing", "Dryhten Alwih Eowing", tf_hero, 0, reserved,  fac_kingdom_9, [  itm_ad_viking_byrnie_02,        itm_ad_viking_byrnie_02,                   itm_decorated_leather_shoes_grey,            itm_decorated_leather_shoes_orange,                   itm_vendel_helmet,    itm_leather_gloves,    itm_le_richsword2,        itm_tab_shield_round_c],      knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000f800021c63b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],
  ["knight_9_9", "Dryhten Cundwalh Coenwalhing", "Dryhten Cundwalh Coenwalhing", tf_hero, 0, reserved,  fac_kingdom_9, [  itm_mail_shirt_1,        itm_mail_shirt_1,                   itm_decorated_leather_shoes_grey,            itm_decorated_leather_shoes_orange,                   itm_vaegir_war_helmet,    itm_leather_gloves,    itm_talak_jomsviking_axe,        itm_tab_shield_round_c],    knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x000000019504115c674d29b3512ca90c00000000000da4dd0000000000000000], #cara unica

  ["knight_10_1", "Mael Cynfyn map Allech", "Edling Cynfyn ap Allech", tf_hero, 0, reserved,  fac_kingdom_10, [itm_arabian_horse_a,itm_byrnie_g_new,      itm_byrnie_g_new,   itm_decorated_leather_shoes, itm_splinted_leather_greaves,       itm_dux_ridge_helm_gold,           itm_le_pictishsword2,  itm_leather_gloves,         itm_tab_shield_round_c, itm_javelin],  knight_attrib_1,wp(200),knight_skills_1|knows_trainer_3|knows_power_draw_4, 0x000000043000318b54b246b7094dc39c00000000001d31270000000000000000, khergit_face_middle_2],

  ["knight_11_1", "Mael Caranfael map Cynddylan", "Edling Caranfael ap Cynddylan", tf_hero, 0, reserved,  fac_kingdom_11, [itm_arabian_horse_a,itm_byrnie_d_new,      itm_byrnie_d_new,   itm_decorated_leather_shoes, itm_splinted_leather_greaves,       itm_rathos_spangenhelm_a_gold_decorated,           itm_le_pictishsword2,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],  knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x00000000ff012013286b9239335554d200000000001d48ea0000000000000000], #cara real rey chief
  ["knight_11_2", "Guledic Hygarfael map Cyndrwyn",  "Tywysog Hygarfael ap Cyndrwyn", tf_hero, 0, reserved,  fac_kingdom_11, [itm_warhorse_sarranid,      itm_byrnie_g_new,     itm_byrnie_g_new,  itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey,  itm_rathos_spangenhelm_b_gold,  itm_leather_gloves,     itm_le_pictishsword2, itm_tab_shield_round_c, itm_javelin],  knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x00000001a90523d338ab7238da46a2d100000000001ce69b0000000000000000], #cara real rey chief
  ["knight_11_3", "Guledic Cynwraith map Cyndrwyn", "Tywysog Cynwraith ap Cyndrwyn", tf_hero, 0, reserved,  fac_kingdom_11, [itm_courser,      itm_byrnie4,     itm_byrnie4,  itm_decorated_leather_shoes_grey, itm_decorated_leather_shoes_greaves_grey, itm_dux_ridge_helm,  itm_leather_gloves,     itm_long_hafted_knobbed_mace, itm_tab_shield_round_c, itm_javelin], knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x000000083210300424a2cd57a379536a00000000001d48930000000000000000], #cara real rey chief
  ["knight_11_4", "Guledic Cuawg map Cyndrwyn","Tywysog Cuawg ap Cyndrwyn", tf_hero, 0, reserved,  fac_kingdom_11, [itm_arabian_horse_b, itm_byrnie5,     itm_byrnie5, itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_briton_helm6,  itm_leather_gloves,     itm_new_sword1, itm_tab_shield_round_c, itm_javelin], knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000ed800c1864d334db8a941a6db00000000001eb9190000000000000000], #cara real rey chief
  ["knight_11_5", "Guledic Cynon map Cyndrwyn", "Tywysog Cynon ap Cyndrwyn", tf_hero, 0, reserved,  fac_kingdom_11, [itm_mail_hauberk,     itm_mail_hauberk,                 itm_carbatinae_2_orange, itm_decorated_leather_shoes_greaves_grey, itm_steppe_cap,  itm_leather_gloves,     itm_spatha, itm_tab_shield_round_c, itm_javelin],  knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000abc00518b5af4ab4b9c8e596400000000001dc76d0000000000000000, khergit_face_older_4],
  ["knight_11_6", "Guledic Gwion map Cyndrwyn","Tywysog Gwion ap Cyndrwyn", tf_hero, 0, reserved,  fac_kingdom_11, [itm_warhorse_sarranid, itm_arena_tunicj_brown,     itm_arena_tunicj_brown, itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_vaegir_war_helmet,  itm_leather_gloves,     itm_long_hafted_spiked_mace, itm_tab_shield_round_c, itm_javelin],  knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000a180441c921a30ea68b54971500000000001e54db0000000000000000, khergit_face_older_4],
  ["knight_11_7", "Guledic Madoc map Cadell","Tywysog Madoc map Cadell", tf_hero, 0, reserved,  fac_kingdom_11, [itm_saddle_horse, itm_mail_shirt_9,     itm_mail_shirt_9, itm_decorated_leather_shoes_orange, itm_decorated_leather_shoes_greaves_grey, itm_briton_helm2,  itm_leather_gloves,     itm_new_sword1, itm_tab_shield_round_c, itm_javelin], knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000], #Raymond chief fictionnal character, good name
  ["knight_11_8", "Tiern Caradoc map Riwall", "Udd Caradoc map Riwall", tf_hero, 0, reserved,  fac_kingdom_11, [  itm_mamluke_mail, itm_mamluke_mail,  itm_carbatinae_2_orange, itm_carbatinae_2_greaves_green, itm_briton_helm4,    itm_leather_gloves,    itm_sarranid_axe_b, itm_tab_shield_round_c, itm_javelin],  knight_attrib_1,wp(200),knight_skills_1|knows_trainer_2, 0x00000007d100534b44962d14d370c65c00000000001ed6df0000000000000000, khergit_face_middle_2], #chief fictionnal character, good name

  ["knight_12_1", "Mael Dumnagual map Mynyddog", "Edling Dumnagual ap Mynyddog", tf_hero, 0, reserved,  fac_kingdom_12, [itm_arabian_horse_a,itm_lamellar_vest_khergit,      itm_lamellar_vest_khergit,   itm_decorated_leather_shoes, itm_splinted_leather_greaves,       itm_briton_helm6,           itm_le_pictishsword2,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin], knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000b8d00240644ac323993d5c91b00000000001f3aad0000000000000000], #cara real chief
  ["knight_12_2", "Guledic Cynan map Clydno","Tywysog Cynan ap Clydno", tf_hero, 0, reserved,  fac_kingdom_12, [itm_courser, itm_mail_shirt_8,     itm_mail_shirt_8, itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_rathos_spangenhelm_b_gold,  itm_leather_gloves,     itm_spatha, itm_tab_shield_round_c, itm_javelin],  knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000bfd0061c65b6eb33b25d2591d00000000001f58eb0000000000000000, khergit_face_older_4],
  ["knight_12_3", "Guledic Brychan map Gwlyget",  "Tywysog Brychan ap Gwlyget", tf_hero, 0, reserved,  fac_kingdom_12, [itm_warhorse_sarranid,      itm_cuir_bouilli,     itm_cuir_bouilli,                 itm_decorated_leather_shoes_orange, itm_decorated_leather_shoes_greaves_grey, itm_barf_helm,  itm_leather_gloves,     itm_bamburghsword2, itm_tab_shield_round_c, itm_javelin],  knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x0000000b6900514144be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_older_4],

  ["knight_13_1", "Hlaford Oswiu Aethelberhting", "Hlaford Oswiu Aethelberhting", tf_hero, 0, reserved,  fac_kingdom_13, [itm_arabian_horse_a,itm_byrnie_e_new,      itm_byrnie_e_new,   itm_decorated_leather_shoes, itm_splinted_leather_greaves,       itm_spangenhelm_a_trim,           itm_suttonhoosword,  itm_leather_gloves,         itm_tab_shield_round_c],  knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000bba012107193495d6912e48d900000000001ecb150000000000000000], #cara real chief
  ["knight_13_2", "Ealdorman Osgudu Aethelfrithing","Ealdorman Osgudu Aethelfrithing", tf_hero, 0, reserved,  fac_kingdom_13, [itm_courser,      itm_mail_shirt_1_trig,     itm_mail_shirt_1_trig,                 itm_decorated_leather_shoes_orange,              itm_decorated_leather_shoes_greaves_grey,                      itm_spangenhelm_a_trim,  itm_leather_gloves,     itm_le_pictishsword7,   itm_tab_shield_round_c],  knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x0000000c350c418438ab85b75c61b8d300000000001d21530000000000000000, khergit_face_middle_2],
  ["knight_13_3", "Ealdorman Offa Aethelfrithing", "Ealdorman Offa Aethelfrithing", tf_hero, 0, reserved,  fac_kingdom_13, [itm_arabian_horse_b,      itm_mail_shirtredwhite,     itm_mail_shirtredwhite,                 itm_carbatinae_2_blue,              itm_decorated_leather_shoes_greaves_grey,                      itm_talak_spangenhelm,  itm_leather_gloves,     itm_talak_jomsviking_axe,   itm_tab_shield_round_c],  knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x0000000c350c418438ab85b75c61b8d300000000001d21530000000000000000, khergit_face_middle_2],
  ["knight_13_4", "Ealdorman Osguid Aethelfrithing", "Ealdorman Osguid Aethelfrithing", tf_hero, 0, reserved,  fac_kingdom_13, [itm_warhorse_sarranid,      itm_nowa,     itm_nowa,                 itm_carbatinae_2_red,              itm_decorated_leather_shoes_greaves_grey,                      itm_talak_spangenhelm,  itm_leather_gloves,     itm_le_pictishsword7,   itm_tab_shield_round_c, itm_had_seax], knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x000000043000318b54b246b7094dc39c00000000001d31270000000000000000, khergit_face_middle_2],
  ["knight_13_5", "Ealdorman Oslaf Aethelfrithing",  "Ealdorman Oslaf Aethelfrithing", tf_hero, 0, reserved,  fac_kingdom_13, [itm_byrnie_e_new,     itm_byrnie_e_new,                 itm_carbatinae_2_blue,              itm_decorated_leather_shoes_greaves_grey,                      itm_talak_spangenhelm,  itm_leather_gloves,     itm_suttonhoosword,   itm_tab_shield_round_c], knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000c280461004929b334ad632aa200000000001e05120000000000000000, khergit_face_old_2],
  ["knight_13_6", "Ealdorman Oslac Aethelfrithing",  "Ealdorman Oslac Aethelfrithing", tf_hero, 0, reserved,  fac_kingdom_13, [itm_warhorse_sarranid,      itm_byrnie_f_new,     itm_byrnie_f_new,                 itm_carbatinae_2_orange,              itm_decorated_leather_shoes_greaves_grey,                      itm_talak_spangenhelm,  itm_leather_gloves,     itm_talak_jomsviking_axe,   itm_tab_shield_round_c],  knight_attrib_3,wp(190),knight_skills_3|knows_trainer_5|knows_power_draw_4, 0x0000000e880062c53b0a6e4994ae272a00000000001db4e10000000000000000, khergit_face_older_4],
  ["knight_13_7", "Ealdorman Coelfrith", "Ealdorman Coelfrith", tf_hero, 0, reserved,  fac_kingdom_13, [  itm_mail_shirt_wht,  itm_mail_shirt_wht,   itm_carbatinae_2_blue,  itm_decorated_leather_shoes_greaves_grey,   itm_vendel_helmet, itm_leather_gloves, itm_sword_two_handed_b,  itm_tab_shield_round_c, itm_light_throwing_axes],   knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000f830051c53b026e4994ae272a00000000001db4e10000000000000000, nord_face_older_2],
  ["knight_13_8", "Dryhten Hunwold", "Dryhten Hunwold", tf_hero, 0, reserved,  fac_kingdom_13, [  itm_mail_shirt_grn,  itm_mail_shirt_grn,   itm_decorated_leather_shoes_orange,  itm_decorated_leather_shoes_greaves_grey,   itm_vaegir_war_helmet, itm_leather_gloves, itm_new_sword4,  itm_tab_shield_round_c],  knight_attrib_4,wp(220),knight_skills_2|knows_trainer_2, 0x0000000c230401c6349c2e9b2168eb1a00000000001eb0630000000000000000, nord_face_older_2],
  ["knight_13_9", "Dryhten Aethlewine", "Dryhten Aethlewine", tf_hero, 0, reserved,  fac_kingdom_13, [  itm_mail_shirt_green,  itm_mail_shirt_green,   itm_carbatinae_2_blue,  itm_decorated_leather_shoes_greaves_grey,   itm_spangenhelm_helm, itm_leather_gloves, itm_new_sword4,  itm_tab_shield_round_c, itm_javelin],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_6, 0x000000084b0002063d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_older_2],

  ["knight_14_1", "Aetheling Eatta Eanfrething", "Aetheling Eatta Eanfrething", tf_hero, 0, reserved,  fac_kingdom_14, [itm_mail_shirt_wht,      itm_mail_shirt_wht,   itm_decorated_leather_shoes, itm_splinted_leather_greaves,       itm_vaegir_war_helmet,           itm_sword_two_handed_a,  itm_leather_gloves,         itm_tab_shield_round_c],   knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000c0810500347ae7acd0d3ad74a00000000001e289a0000000000000000, khergit_face_older_4],
  ["knight_14_2", "Aetheling Aldfrith Eanfrething","Aetheling Aldfrith Eanfrething", tf_hero, 0, reserved,  fac_kingdom_14, [itm_warhorse_sarranid,itm_mail_shirt_grn,      itm_mail_shirt_grn,   itm_decorated_leather_shoes_red, itm_splinted_leather_greaves,       itm_briton_helm3,           itm_le_pictishsword7,  itm_leather_gloves,         itm_tab_shield_round_c],  knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000c1500510528f50d52d20b152300000000001d66db0000000000000000, khergit_face_older_4],
  ["knight_14_3", "Ealdorman Blaecca","Ealdorman Blaecca", tf_hero, 0, reserved,  fac_kingdom_14, [  itm_mail_shirt_green,  itm_mail_shirt_green,   itm_carbatinae_2_red,  itm_decorated_leather_shoes_greaves_grey,   itm_spangenhelm_helm, itm_leather_gloves, itm_new_sword4,  itm_tab_shield_round_c, itm_javelin],  knight_attrib_5,wp(240),knight_skills_1|knows_trainer_1, 0x0000000e0d1091413aabada93c8ac95b00000000001d42e10000000000000000],

  ["knight_15_1", "Guledic Eadwine map Owain", "Tywysog Edwin ap Owain", tf_hero, 0, reserved,  fac_kingdom_15, [itm_arabian_horse_a, itm_khergit_elite_armor,     itm_khergit_elite_armor,  itm_decorated_leather_shoes, itm_decorated_leather_shoes_greaves_grey, itm_rathos_spangenhelm_b_gold_decorated,  itm_leather_gloves, itm_bamburghsword2, itm_tab_shield_round_c, itm_javelin], knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x0000000b800803d348eb68a71b6956dc00000000001d399b0000000000000000], #cara real chief
  ["knight_15_2", "Guledic Pasgen map Owain", "Tywysog Pasgen ap Owain", tf_hero, 0, reserved,  fac_kingdom_15, [  itm_mail_shirt_6,     itm_mail_shirt_6,  itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_dux_ridge_helm,  itm_leather_gloves, itm_spatha, itm_tab_shield_round_c, itm_javelin],  knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x000000089b0c305312cb39b6dec5869a00000000001ed9340000000000000000], #cara real chief
  ["knight_15_3", "Guledic Gwaith map Elffin", "Tywysog Gwaith ap Elffin", tf_hero, 0, reserved,  fac_kingdom_15, [itm_warhorse_sarranid, itm_mail_hauberk,     itm_mail_hauberk,  itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_khergit_cavalry_helmet,  itm_leather_gloves, itm_le_bamburghsword, itm_tab_shield_round_c, itm_javelin],  knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x000000088a08d25356d64946ec722c9c000000000012692c0000000000000000], #cara real chief
  ["knight_15_4", "Tiern Cynan map Pasgen", "Udd Cynan ap Pasgen", tf_hero, 0, reserved,  fac_kingdom_15, [itm_hunter,   itm_lamellar_armor, itm_lamellar_armor,  itm_carbatinae_2_orange, itm_carbatinae_2_greaves_green, itm_rathos_spangenhelm_a_yellow2,    itm_leather_gloves,    itm_sarranid_axe_b, itm_tab_shield_round_c, itm_javelin],  knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x00000001bf00100326ad8413929040cf00000000001eb9640000000000000000], #chief Rathmor

  ["knight_16_1", "Tiern Caid map Dwywg", "Udd Caid ap Dwywg", tf_hero, 0, reserved,  fac_kingdom_16, [  itm_byrnie5, itm_byrnie5,  itm_decorated_leather_shoes, itm_carbatinae_2_greaves_green, itm_rathos_spangenhelm_b_gold_decorated,    itm_leather_gloves,    itm_le_bamburghsword, itm_tab_shield_round_c, itm_javelin], knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000ff508330546dc4a59422d450c00000000001e51340000000000000000, nord_face_older_2],
  ["knight_16_2", "Tiern Madogion map Sanddle", "Upp Madogion ap Sanddle", tf_hero, 0, reserved,  fac_kingdom_16, [   itm_light_leather, itm_light_leather,  itm_carbatinae_2_orange, itm_carbatinae_2_greaves_green, itm_rathos_spangenhelm_a_yellow2,    itm_leather_gloves,    itm_spatha, itm_tab_shield_round_c, itm_javelin],   knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x00000005b00011813d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_middle_2],
  ["knight_16_3", "Tiern Cwyar map Dwywg", "Udd Cwyar ap Dwywg", tf_hero, 0, reserved,  fac_kingdom_16, [  itm_mail_shirt_6, itm_mail_shirt_6,  itm_carbatinae_2_green, itm_carbatinae_2_greaves_green, itm_rathos_spangenhelm_a_gold,    itm_leather_gloves,    itm_le_bamburghsword, itm_tab_shield_round_c, itm_javelin],   knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x00000006690002873d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_old_2],

  ["knight_17_1", "Ard Tiarna Cathal mac Rogallaig", "Ard Tiarna Cathal mac Rogallaig", tf_hero, 0, reserved,  fac_kingdom_17, [itm_courser,itm_hauberk5, itm_hauberk5, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet_gold,           itm_pict_sword,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],     knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000ab90872001b1a76d51bb22ce600000000001e4b6b0000000000000000], #cara real chief
  ["knight_17_2", "Ard Tiarna Laidgnen mac Colmain", "Ard Tiarna Laidgnen mac Colmain", tf_hero, 0, reserved,  fac_kingdom_17, [itm_warhorse,itm_haubergeon, itm_haubergeon, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet6,           itm_kirkburn,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin], knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x0000000bbf0001013722a526a66cad0500000000001e4ade0000000000000000], #cara real chief
  ["knight_17_3", "Tiarna Guaire Aidne mac Colmain", "Tiarna Guaire Aidne mac Colmain", tf_hero, 0, reserved,  fac_kingdom_17, [itm_hunter,      itm_mail_shirt_4,     itm_mail_shirt_4, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_szpadelhelmet6,  itm_leather_gloves,     itm_pict_sword, itm_tab_shield_round_c, itm_javelin],    knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000bbf001198371aa526a46caf1d00000000001e4b1e0000000000000000], #cara real chief
  ["knight_17_4", "Tiarna Marcan mac Tommain", "Tiarna Marcan mac Tommain", tf_hero, 0, reserved,  fac_kingdom_17, [itm_hunter,      itm_nordiclightarmor6,     itm_heraldic_mail_with_surcoat, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_szpadelhelmet_gold,  itm_leather_gloves,     itm_celticshort1_2, itm_tab_shield_round_c, itm_javelin],     knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000c3a0455c443d46e4c8b91291a00000000001ca51b0000000000000000, rhodok_face_old_2],
  ["knight_17_5", "Tiarna Fergus mac Rogallig", "Tiarna Fergus mac Rogallig", tf_hero, 0, reserved,  fac_kingdom_17, [itm_warhorse,      itm_nordiclightarmor5,     itm_mail_shirt_ylw, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_szpadelhelmet5,  itm_leather_gloves,     itm_celticshort1_2, itm_tab_shield_round_c, itm_javelin],    knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000, rhodok_face_older_2],
  ["knight_17_6", "Tiarna Maenach mac Baeithin", "Tiarna Maenach mac Baeithin", tf_hero, 0, reserved,  fac_kingdom_17, [itm_sumpter_horse,      itm_nordiclightarmor4,     itm_coat_of_plates_red, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_szpadelhelmet4,  itm_leather_gloves,     itm_celticshort1_1, itm_tab_shield_round_c, itm_javelin],   knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000c130461054af448eb19cd40e400000000001d488a0000000000000000, rhodok_face_older_2],
  ["knight_17_7", "Tiarna Cellach mac Guairi", "Tiarna Cellach mac Guairi", tf_hero, 0, reserved,  fac_kingdom_17, [itm_bl_tunic11,     itm_arabian_armor_b, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_szpadelhelmet3,  itm_leather_gloves,     itm_celticshort1_1, itm_tab_shield_round_c, itm_javelin],  knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x00000008e20011063d9b6d4a92ada53500000000001cc1180000000000000000, rhodok_face_older_2],

  ["knight_18_1", "Mael Eugein map Bili", "Edling Eugein ap Bili", tf_alto|tf_hero, 0, reserved,  fac_kingdom_18, [itm_charger,itm_byrnie4, itm_byrnie4, itm_decorated_leather_shoes, itm_splinted_leather_greaves,   itm_romanelitehelm,  itm_le_pictishsword2,  itm_leather_gloves, itm_tab_shield_round_c], knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x00000008221023012b23774ccd72492400000000001f6b5c0000000000000000], #cara real chief
  ["knight_18_2", "Guledic Brude map Bili", "Tywysog Brude ap Bili", tf_hero, 0, reserved,  fac_kingdom_18, [  itm_mail_hauberk,     itm_mail_hauberk,  itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_dux_ridge_helm,  itm_leather_gloves, itm_long_hafted_spiked_mace, itm_tab_shield_round_c, itm_javelin],  knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x000000067810000443231663add158e400000000001dc69a0000000000000000], #cara real chief
  ["knight_18_3", "Guledic Guret map Neithon", "Tywysog Guret ap Neithon", tf_hero, 0, reserved,  fac_kingdom_18, [itm_warhorse_sarranid, itm_mail_shirt_7,     itm_mail_shirt_7,  itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_spangenhelm_a_ornate,  itm_leather_gloves, itm_spatha, itm_tab_shield_round_c],  knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x00000008b40110415d22d2b89d5aa4db00000000001e6c550000000000000000], #cara real chief
  ["knight_18_4", "Tiern Mordaf Hael map Serwan", "Udd Mordaf Hael ap Serwan", tf_hero, 0, reserved,  fac_kingdom_18, [  itm_mail_shirt_2, itm_mail_shirt_2,  itm_carbatinae_2_orange, itm_carbatinae_2_greaves_green, itm_rathos_spangenhelm_a_gold_decorated,    itm_leather_gloves,    itm_le_pictishsword2, itm_tab_shield_round_c, itm_javelin],   knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000000003189275b523689ac38e100000000001e39660000000000000000], #piipe chief
  ["knight_18_5", "Tiern Dingat map Nudd", "Udd Dingat ap Nudd", tf_hero, 0, reserved,  fac_kingdom_18, [  itm_byrnie3, itm_byrnie3,  itm_carbatinae_2_blue, itm_carbatinae_2_greaves_green, itm_briton_helm5,    itm_leather_gloves,    itm_bl_sword01_03, itm_tab_shield_round_c, itm_javelin],  knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000c0d00118866e22e3d9735a72600000000001eacad0000000000000000, nord_face_older_2],
  ["knight_18_6", "Tiern Angharad Tonfelen map Riderch Hael", "Udd Angharad Tonfelen ap Riderch Hael", tf_hero, 0, reserved,  fac_kingdom_18, [   itm_mail_and_plate, itm_mail_and_plate,  itm_carbatinae_2_orange, itm_carbatinae_2_greaves_green, itm_rathos_spangenhelm_yellow_plum,    itm_leather_gloves,    itm_bl_sword01_03, itm_tab_shield_round_c, itm_javelin],   knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000f570000514763954d1b34a69500000000001e56a20000000000000000], #cara real chief
  ["knight_18_7", "Tiern Brwydr Ddriaid map  Riderch Hael", "Udd Brwydr Ddriaid ap  Riderch Hael", tf_hero, 0, reserved,  fac_kingdom_18, [itm_hunter,   itm_mail_shirt_whiteraven, itm_mail_shirt_whiteraven,  itm_carbatinae_2_orange, itm_carbatinae_2_greaves_green, itm_barf_helm,    itm_leather_gloves,    itm_spatha, itm_tab_shield_round_c, itm_javelin], knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x000000016410001843231663adc8d8e200000000001d469b0000000000000000], #cara real chief

  ["knight_19_1", "Ard Tiarna Fecher mac Conall Cerr", "Ard Tiarna Fecher mac Conall Cerr", tf_hero, 0, reserved,  fac_kingdom_19, [itm_warhorse,itm_haubergeon,  itm_haubergeon, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet_gold,  itm_pict_sword,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],  knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x00000001ab0c02115d318e452d726b6300000000000dc96b0000000000000000], #devilshepi chief
  ["knight_19_2", "Ard Tiarna Garnait mac Donuel", "Ard Tiarna Garnait mac Donuel", tf_hero, 0, reserved,  fac_kingdom_19, [itm_hunter,itm_hauberk5,      itm_hauberk5,   itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet6,           itm_kirkburn,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],  knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x0000000f630052813b6bb36de5d6eb7400000000001dd72c0000000000000000, nord_face_older_2],
  ["knight_19_3", "Tiarna Drust mac Donuel", "Tiarna Drust mac Donuel", tf_hero, 0, reserved,  fac_kingdom_19, [itm_warhorse_sarranid,      itm_bl_tunic07,     itm_sarranid_elite_armor, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_szpadelhelmet_gold,  itm_leather_gloves,     itm_pict_sword, itm_tab_shield_round_c, itm_javelin],     knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000a4e01419316a6b1e6527950e400000000001cb6a20000000000000000], #cara hecha por morcant
  ["knight_19_4", "Tiarna Derile mac Donuel", "Tiarna Derile mac Donuel", tf_hero, 0, reserved,  fac_kingdom_19, [itm_hunter,      itm_bl_tunic06,     itm_scale_armor, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_szpadelhelmet4,  itm_leather_gloves,     itm_celticshort1_2, itm_tab_shield_round_c, itm_javelin],     knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000a560971d52123a74b2224d36100000000001f39940000000000000000], #cara hecha por morcant
  ["knight_19_5", "Tiarna Conall Crandomna mac Echach", "Tiarna Conall Crandomna mac Echach", tf_hero, 0, reserved,  fac_kingdom_19, [itm_bl_tunic05,     itm_vaegir_elite_armor, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_szpadelhelmet5,  itm_leather_gloves,     itm_celticshort1_1, itm_tab_shield_round_c, itm_javelin],    knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],

  ["knight_20_1", "Tannist Brude map Gwid", "Tannist Brude maqq Gwid", tf_hero, 0, reserved,  fac_kingdom_20, [itm_arabian_horse_b,itm_heraldric_armor, itm_hauberk5, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet_gold, itm_kirkburn,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],   knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000a7411820f491c8a271c4ae96300000000001e39240000000000000000], #cara real chief
  ["knight_20_2", "Tannist Tarloc map Gwid", "Tannist Tarloc maqq Gwid", tf_hero, 0, reserved,  fac_kingdom_20, [itm_warhorse,itm_studded_leather_coat, itm_coat_of_plates_red, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_romanelitehelm, itm_pict_sword,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],  knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x0000000a74117448491c8a264c4aa76300000000001e38a40000000000000000], #cara real chief
  ["knight_20_3", "Tannist Talorcan map Eanfrith", "Tannist Talorcan maqq Eanfrith", tf_hero, 0, reserved,  fac_kingdom_20, [itm_hunter,itm_hauberk5, itm_hauberk5, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_briton_helm4, itm_pict_sword,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],     knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x000000040b04c2c624db4537239174cb00000000001c39730000000000000000], #cara real chief
  ["knight_20_4", "Toiseach Ynyr Frafdrwch map Gwyddno", "Tannist Ynyr Frafdrwch maqq Gwyddno", tf_hero, 0, reserved,  fac_kingdom_20, [itm_hunter,itm_mail_shirtbluewhite, itm_mail_shirtbluewhite, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet4, itm_pict_sword,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],    knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000bb704c34755115dc8e0acb54d00000000001d69b30000000000000000], #cara real chief
  ["knight_20_5", "Toiseach Idris Arw map Clydno", "Tannist Idris Arw maqq Clydno", tf_hero, 0, reserved,  fac_kingdom_20, [itm_hunter,itm_tuniczka, itm_byrnie6, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet2, itm_pict_sword,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],   knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000e9411051a051176aae165d4db00000000001ddb6b0000000000000000], #cara real chief
  ["knight_20_6", "Toiseach Domlech", "Tannist Domlech", tf_hero, 0, reserved,  fac_kingdom_20, [itm_arabian_horse_a,itm_gairlom, itm_byrnie8, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet_gold, itm_celticshort1_2,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],  knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000f2d11034d44e3bb575da9bd5900000000001e59740000000000000000], #cara real chief
  ["knight_20_7", "Tiern Entifidach", "Tannist Entifidach", tf_hero, 0, reserved,  fac_kingdom_20, [itm_steppe_horse,itm_nomad_robe, itm_haubergeon, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_briton_helm2, itm_celticshort1_2,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],     knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000e7f0c5107361c8a7bd6cdbbba00000000001edade0000000000000000], #angel clan cuervo chief
  ["knight_20_8", "Tiern Clydno map Ynyr Farfdrwch", "Tannist Clydno maqq Ynyr Farfdrwch", tf_hero, 0, reserved,  fac_kingdom_20, [itm_sumpter_horse,itm_czerwony, itm_ad_viking_byrnie_04, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_briton_helm, itm_celticshort1_1,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],    knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x00000001800111c63975061a9d8c58e00000000000065c6d0000000000000000], #me encanta esta cara chief
  ["knight_20_9", "Tiern Lugthreni", "Tannist Lugthreni", tf_hero, 0, reserved,  fac_kingdom_20, [itm_braz, itm_surcoat_over_mail, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet6, itm_celticshort1_1,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],    knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x0000000aff001014351a7230d2826b1500000000001d89230000000000000000], #motomataru chief

  ["knight_21_1", "Brenin Morwd map Elaed", "Brenin Morwd ap Elaed", tf_hero, 0, reserved,  fac_kingdom_21, [itm_charger,     itm_mail_and_plate,  itm_mail_and_plate,     itm_decorated_leather_shoes,    itm_decorated_leather_shoes_greaves_blue,    itm_romanelitehelm, itm_leather_gloves,       itm_le_pictishsword2,  itm_tab_shield_round_c, itm_javelin], knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000, rhodok_face_older_2],

  ["knight_22_1", "Mael Beli map Eluan", "Edling Beli ap Eluan", tf_hero, 0, reserved,  fac_kingdom_22, [itm_courser, itm_lamellar_vest, itm_lamellar_vest, itm_decorated_leather_shoes, itm_splinted_leather_greaves, itm_dux_ridge_helm_gold, itm_bl_sword01_02, itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],    knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000dbe0014432ceca99d1555d6e100000000001ddb5c0000000000000000], #cara real chief
  ["knight_22_2", "Guledic Gwydr Drum map Gwedrog", "Tywysog Gwydr Drum ap Gwedrog", tf_hero, 0, reserved,  fac_kingdom_22, [itm_warhorse_sarranid, itm_khergit_guard_armor,     itm_khergit_guard_armor,  itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_steppe_cap,  itm_leather_gloves, itm_spatha, itm_tab_shield_round_c, itm_javelin],     knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000c081001d3465c89a6a452356300000000001cda550000000000000000, rhodok_face_old_2],
  ["knight_22_3", "Tiern Mascuid map Hueil", "Udd Mascuid map Hueil", tf_hero, 0, reserved,  fac_kingdom_22, [itm_arabian_horse_a, itm_arena_tunicj_violet,     itm_arena_tunicj_violet,    itm_decorated_leather_shoes,      itm_decorated_leather_shoes_greaves_grey,    itm_romanelitehelm, itm_leather_gloves,       itm_sarranid_axe_b,   itm_tab_shield_round_c],    knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x0000000a3d0c13c3452aa967276dc95c00000000001dad350000000000000000, rhodok_face_older_2], #chief fictionnal character, good name

  ["knight_23_1", "Guledic Gweddeint", "Tywysog Gweddeint", tf_hero, 0, reserved,  fac_kingdom_23, [itm_courser, itm_lamellar_vest_khergit,     itm_lamellar_vest_khergit,  itm_decorated_leather_shoes, itm_decorated_leather_shoes_greaves_grey, itm_briton_helm5,  itm_leather_gloves, itm_bl_sword01_02, itm_tab_shield_round_c, itm_javelin],    knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x0000000020003147495c6d26d369d8e200000000001dc6e30000000000000000], #makute
  ["knight_23_2", "Guledic Swalda map Idris", "Tywysog Swalda ap Idris", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_a, itm_arena_tunicj_magenta,     itm_arena_tunicj_magenta,  itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_rathos_spangenhelm_a_light_gold,  itm_leather_gloves, itm_bl_sword01_01, itm_tab_shield_round_c, itm_javelin],     knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000d6e10445039334a2754b1d4bb00000000001e58c90000000000000000], #cara real chief
  ["knight_23_3", "Tiern Brochael map Swalda", "Udd Brochael ap Swalda", tf_hero, 0, reserved,  fac_kingdom_23, [itm_warhorse_sarranid, itm_arena_tunicj_brown,     itm_arena_tunicj_brown,    itm_decorated_leather_shoes,      itm_splinted_leather_greaves,    itm_helmet_with_neckguard, itm_leather_gloves,       itm_new_sword2,   itm_tab_shield_round_c, itm_javelin],    knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x00000000190034d3445bba489031b91500000000001ea65b0000000000000000], #cara real chief
  ["knight_23_4", "Tiern Catihern map Peibio", "Udd Catihern map Peibio", tf_hero, 0, reserved,  fac_kingdom_23, [itm_banded_armor,     itm_banded_armor,   itm_carbatinae_2_red,    itm_splinted_leather_greaves,       itm_barf_helm, itm_splinted_leather_greaves,   itm_long_hafted_knobbed_mace,  itm_javelin, itm_tab_shield_round_c],   knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x0000000c3f08038245545e3b236a68de00000000001e37230000000000000000, rhodok_face_older_2], #chief fictionnal character, good name

  ["knight_24_1", "Mael Gwlyddien map Nowy", "Edling Gwlyddien ap Nowy", tf_hero, 0, reserved,  fac_kingdom_24, [itm_courser,itm_lamellar_vest, itm_lamellar_vest, itm_decorated_leather_shoes, itm_splinted_leather_greaves, itm_dux_ridge_helm_gold, itm_bl_sword01_01, itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],     knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x00000005ac0833c634ed8d27646dc92b00000000001db8e30000000000000000], #cara real chief
  ["knight_24_2", "Guledic Congar map Brioc", "Tywysog Congar map Brioc", tf_hero, 0, reserved,  fac_kingdom_24, [itm_arabian_horse_a, itm_brigandine_red,     itm_brigandine_red,  itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_rathos_spangenhelm_a_light_gold,  itm_leather_gloves, itm_new_sword2, itm_tab_shield_round_c, itm_javelin],    knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000, rhodok_face_older_2], #chief fictionnal character, good name
  ["knight_24_3", "Guledic Withenoc map Teilo", "Tywysog Withenoc map Teilo", tf_hero, 0, reserved,  fac_kingdom_24, [itm_warhorse_sarranid, itm_padded_jack_9_trig,     itm_padded_jack_9_trig,  itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_steppe_cap,  itm_leather_gloves, itm_new_sword1, itm_tab_shield_round_c, itm_javelin],    knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000, rhodok_face_older_2], #chief fictionnal character, good name

  ["knight_25_1", "Guledic Ysgorda Fychen map Ysgorda", "Tywysog Ysgorda Fychen ap Ysgorda", tf_hero, 0, reserved,  fac_kingdom_25, [itm_warhorse_sarranid, itm_idi_scale14,     itm_idi_scale14,  itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_romanelitehelm,  itm_leather_gloves, itm_sarranid_axe_b, itm_tab_shield_round_c, itm_javelin],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_6, 0x0000000d8a00514544be2d14d370c65c00000000001ed6df0000000000000000, rhodok_face_older_2],

  ["knight_26_1", "Guledic Llywarch map Tewdwr", "Tywysog Llywarch ap Tewdwr", tf_hero, 0, reserved,  fac_kingdom_26, [itm_courser, itm_mail_hauberk,     itm_mail_hauberk,  itm_decorated_leather_shoes, itm_decorated_leather_shoes_greaves_grey, itm_rathos_spangenhelm_a_light_gold,  itm_leather_gloves, itm_new_sword1, itm_tab_shield_round_c, itm_javelin],     knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000d3f08e1080b29d7b515acb33c00000000001d2a020000000000000000], #educalle chief
  ["knight_26_2", "Guledic Gwrgant Fawr map Cynfyn", "Tywysog Gwrgant Fawr ap Cynfyn", tf_hero, 0, reserved,  fac_kingdom_26, [itm_warhorse_sarranid, itm_mail_shirt_7,     itm_mail_shirt_7,  itm_carbatinae_2_red, itm_decorated_leather_shoes_greaves_grey, itm_rathos_spangenhelm_a_gold_decorated,  itm_leather_gloves, itm_axehammer1, itm_tab_shield_round_c, itm_javelin],    knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x000000065a0cd280291a72ad36d25bae00000000001f5d660000000000000000], #cara real chief
  ["knight_26_3", "Mael Athrwys map Meurig", "Edling Athrwys ap Meurig", tf_hero, 0, reserved,  fac_kingdom_26, [itm_charger,itm_padded_jack_3_trig, itm_padded_jack_3_trig, itm_decorated_leather_shoes_blue, itm_splinted_leather_greaves, itm_romanelitehelm, itm_long_spiked_club, itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],    knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x00000000590821454ade66456ac9d6dc00000000001e45650000000000000000], #cara real chief

  ["knight_27_1", "Ard Tiarna Conall mac Faelain", "Ard Tiarna Conall mac Faelain", tf_hero, 0, reserved,  fac_kingdom_27, [itm_warhorse,itm_khergit_armor, itm_byrnie_c_new, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet6,           itm_kirkburn,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],     knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x000000088b08325879149ba755d5397200000000001dd5730000000000000000],
  ["knight_27_2", "Ard Tiarna Crundmael mac Ronain", "Ard Tiarna Crundmael mac Ronain", tf_hero, 0, reserved,  fac_kingdom_27, [itm_hunter,itm_nordiclightarmor7, itm_mail_shirt_3, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet1,           itm_pict_sword,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],    knight_attrib_2,wp(200),knight_skills_2, 0x00000006471125c72646963a99d2b71c00000000001d36ea0000000000000000],
  ["knight_27_3", "Tiarna Fiannamail mac Mael Tuile", "Tiarna Fiannamail mac Mael Tuile", tf_hero, 0, reserved,  fac_kingdom_27, [itm_gairlom,itm_scale_armor,    itm_byrnie4, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_celtycka_iron,  itm_leather_gloves,     itm_celticshort1_1, itm_tab_shield_round_c, itm_javelin],    knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x00000008a504d0493aab2936cd95b6eb00000000001dba9b0000000000000000],

  ["knight_28_1", "Ard Tiarna Cuan mac Amalgaid", "Ard Tiarna Cuan mac Amalgaid", tf_hero, 0, reserved,  fac_kingdom_28, [itm_hunter,itm_nomad_armor, itm_hauberk5, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet_gold,           itm_pict_sword,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],   knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x00000001b80402da478c6ae6daa9c75c00000000001d3d660000000000000000],
  ["knight_28_2", "Ard Tiarna Mael Duin mac Aedh", "Ard Tiarna Mael Duin mac Aedh", tf_hero, 0, reserved,  fac_kingdom_28, [itm_hunter,itm_nordiclightarmor4, itm_byrnie3, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet6,           itm_kirkburn,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin], knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x000000067f101308371d79bf9175e81300000000001dbb240000000000000000],
  ["knight_28_3", "Ard Tiarna Cathal CuCenMathair mac Cathail", "Ard Tiarna Cathal CuCenMathair mac Cathail", tf_hero, 0, reserved,  fac_kingdom_28, [itm_warhorse,itm_vaelicus_t_36, itm_lorika, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet6,           itm_pict_sword,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],    knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000e3f001287158b89b71271b86500000000001cb9040000000000000000],
  ["knight_28_4", "Tiarna Maenach mac Fingin", "Tiarna Maenach mac Fingin", tf_hero, 0, reserved,  fac_kingdom_28, [itm_hunter,      itm_vaelicus_t_35,     itm_mail_coat_2_trig, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_szpadelhelmet1,  itm_leather_gloves,     itm_celticshort1_2, itm_tab_shield_round_c, itm_javelin],     knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x00000004261003c856acba399e6aa6de00000000001de50a0000000000000000],
  ["knight_28_5", "Tiarna Ronan Righfhlaith mac Colmain Mair", "Tiarna Ronan Righfhlaith mac Colmain Mair", tf_hero, 0, reserved,  fac_kingdom_28, [itm_vaelicus_t_27,     itm_byrnie_c_new, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_szpadelhelmet1,  itm_leather_gloves,     itm_celticsword2, itm_javelin],    knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x00000008b80830403729b2a14e719c8b00000000001de45c0000000000000000],
  ["knight_28_6", "Tiarna Mael Umai mac Cuan", "Tiarna Mael Umai mac Cuan", tf_hero, 0, reserved,  fac_kingdom_28, [itm_vaelicus_t_26,     itm_mail_shirt_whiteaxes, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_celtycka_iron,  itm_leather_gloves,     itm_celticsword2, itm_tab_shield_round_c, itm_javelin],   knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x00000003b50124d8274bae26e9d2649a00000000001e468e0000000000000000],
  ["knight_28_7", "Tiarna Aillil mac Maenach", "Tiarna Aillil mac Maenach", tf_hero, 0, reserved,  fac_kingdom_28, [itm_vaelicus_t_25,     itm_scale_armor, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_celtycka_iron,  itm_leather_gloves,     itm_celticshort1_1, itm_tab_shield_round_c, itm_javelin],  knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x000000087d04704a524d86bb2391e8a900000000001e63550000000000000000],

  ["knight_29_1", "Ard Tiarna Dunchad mac Fiachnai", "Ard Tiarna Dunchad mac Fiachnai", tf_hero, 0, reserved,  fac_kingdom_29, [itm_hunter,itm_vaelicus_t_21, itm_byrnie1, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet6,           itm_kirkburn,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],     knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x000000066e0821da0b1ba9c7a0d72f7400000000001ec88b0000000000000000],
  ["knight_29_2", "Tiarna Airmetach Caech mac Conaill", "Tiarna Airmetach Caech mac Conaill", tf_hero, 0, reserved,  fac_kingdom_29, [itm_warhorse,      itm_vaelicus_t_19,     itm_mail_shirt_2, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_szpadelhelmet1,  itm_leather_gloves,     itm_pict_sword, itm_tab_shield_round_c, itm_javelin],    knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x000000065905234a355e4f272b6da95d00000000001f4b260000000000000000],
  ["knight_29_3", "Tiarna Faelchu mac Airmetach", "Tiarna Faelchu mac Airmetach", tf_hero, 0, reserved,  fac_kingdom_29, [itm_vaelicus_t_16,     itm_vaegir_elite_armor, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_celtycka_iron,  itm_leather_gloves,     itm_celticshort1_1, itm_tab_shield_round_c, itm_javelin],    knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x00000006620c55543d6a6628abcddca300000000001dc6eb0000000000000000], #betatester chief Wilsonrtf

  ["knight_30_1", "Ard Tiarna Fecher mac Conaill Cerr", "Ard Tiarna Fecher mac Conaill Cerr", tf_hero, 0, reserved,  fac_kingdom_30, [itm_hunter,itm_nobleman_outfit,itm_hauberk5, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet_gold,           itm_pict_sword,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],    knight_attrib_5,wp(280),knight_skills_5|knows_trainer_5, 0x0000000657003353371ca5b6dcadc49100000000001dd9230000000000000000], #cara real chief
  ["knight_30_2", "Ard Tiarna Diarmaid mac Aedh Slaine", "Ard Tiarna Diarmaid mac Aedh Slaine", tf_hero, 0, reserved,  fac_kingdom_30, [itm_warhorse,itm_bl_tunic08, itm_byrnie151, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet6,           itm_kirkburn,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin], knight_attrib_4,wp(240),knight_skills_4|knows_trainer_4, 0x000000066f003298371ca5d91c69c49400000000001dd8cb0000000000000000], #cara real chief
  ["knight_30_3", "Ard Tiarna Mael Doid mac Suibni", "Ard Tiarna Mael Doid mac Suibni", tf_hero, 0, reserved,  fac_kingdom_30, [itm_hunter,itm_bl_tunic07, itm_mail_shirtred, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet6,           itm_pict_sword,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],    knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x000000067e00705117118ad5634aec9d00000000001f35330000000000000000], #cara real chief
  ["knight_30_4", "Ard Tiarna Oengus mac Domnaill", "Ard Tiarna Oengus mac Domnaill", tf_hero, 0, reserved,  fac_kingdom_30, [itm_warhorse,itm_bl_tunic06, itm_byrnie1, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet1,           itm_celticshort1_2,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],     knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000d7f05229334d28d4c912d5b6300000000001f396c0000000000000000], #cara real chief
  ["knight_30_5", "Tiarna Cellach mac Maele Cobo", "Tiarna Cellach mac Maele Cobo", tf_hero, 0, reserved,  fac_kingdom_30, [itm_bl_tunic05,     itm_mail_with_surcoat, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_szpadelhelmet1,  itm_leather_gloves,     itm_celticsword2, itm_tab_shield_round_c, itm_javelin],    knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x000000085309214358e28ecd8b6b22a100000000001d746d0000000000000000], #cara real chief
  ["knight_30_6", "Tiarna Conall Cael mac Maele Cobo", "Tiarna Conall Cael mac Maele Cobo", tf_hero, 0, reserved,  fac_kingdom_30, [itm_nordiclightarmor8,     itm_arena_tunicj_violet, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_celtycka_iron,  itm_leather_gloves,     itm_celticsword2, itm_javelin],   knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x0000000676052040352a6f26d268caa300000000001f29950000000000000000], #cara real chief
  ["knight_30_7", "Tiarna Fergus Fanat mac Domnaill", "Tiarna Fergus Fanat mac Domnaill", tf_hero, 0, reserved,  fac_kingdom_30, [itm_nordiclightarmor7,     itm_sarranid_elite_armor, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_celtycka_iron,  itm_leather_gloves,     itm_celticshort1_1, itm_tab_shield_round_c, itm_javelin],  knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x0000000feb0423c122546b11537104ec00000000001ec49a0000000000000000], #cara real chief

  ["knight_31_1", "Ard Tiarna Cuanu mac Cailcin", "Ard Tiarna Cuanu mac Cailcin", tf_hero, 0, reserved,  fac_kingdom_31, [itm_warhorse,itm_courtly_outfit, itm_byrnie2, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet6,           itm_kirkburn,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],     knight_attrib_3,wp(240),knight_skills_3|knows_trainer_3, 0x0000000d520ce0922ad376351bd0e2cd00000000001db6920000000000000000], #cara real chief
  ["knight_31_2", "Ard Tiarna Mael Duin mac Furudran", "Ard Tiarna Mael Duin mac Furudran", tf_hero, 0, reserved,  fac_kingdom_31, [itm_hunter,itm_nordiclightarmor5, itm_nordiclightarmor2, itm_bare_legs_blue, itm_decorated_leather_shoes_greaves_blue, itm_szpadelhelmet1,           itm_pict_sword,  itm_leather_gloves, itm_tab_shield_round_c, itm_javelin],    knight_attrib_2,wp(220),knight_skills_2|knows_trainer_2, 0x00000008bf0840583adcecb70c4746dc00000000001e295c0000000000000000], #cara real chief
  ["knight_31_3", "Tiarna Cumascach mac Oiliolla", "Tiarna Cumascach mac Oiliolla", tf_hero, 0, reserved,  fac_kingdom_31, [itm_nordiclightarmor4,     itm_arabian_armor_b, itm_decorated_leather_shoes_bare,  itm_mail_chausses, itm_celtycka_iron,  itm_leather_gloves,     itm_celticsword2, itm_tab_shield_round_c, itm_javelin],    knight_attrib_1,wp(200),knight_skills_1|knows_trainer_1, 0x000000088e04440714e371c93a4acadb0000000000054a1a0000000000000000], #cara real chief
  ###finaliza caballeros  chief de facciones####


###pretendientes####
  ["kingdom_1_pretender",  "Mael Erfig map Gwrfoddw",       "Edling Erfig ap Gwrfoddw",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_26,[itm_saddle_horse,   itm_swadian_mail_hauberk,  itm_ankle_boots,      itm_splinted_leather_greaves,         itm_swadian_mail_hauberk,      itm_spatha,      itm_shield_round_06,       itm_skull_cap_new_c],          lord_attrib,wp(220),knight_skills_5, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
  #claims pre-salic descent

  ["kingdom_2_pretender",  "Ard Tiarna Dungal mac Fergusa", "Tywysog Dungal mac Fergusa",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_19,[itm_saddle_horse,   itm_mail_shirt_8_trig,      itm_ankle_boots,              itm_splinted_leather_greaves,              itm_mail_shirt_8_trig,       itm_spatha,      itm_shield_round_05,      itm_leather_steppe_cap_c],    lord_attrib,wp(220),knight_skills_5, 0x0000000b3c084547575e30a9293736a100000000001cd5130000000000000000],
  #had his patrimony falsified

  ["kingdom_3_pretender",  "Mael Manwgan map Selyfan",               "Edling Manwgan ap Selyfan",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_22,[itm_saddle_horse,   itm_wei_xiadi_sar_hauberk,             itm_ankle_boots,              itm_splinted_leather_greaves,           itm_wei_xiadi_sar_hauberk,         itm_spatha,              itm_shield_round_02,       itm_horn_helmet],      lord_attrib,wp(220),knight_skills_5, 0x0000000b2f081190370c6aeedcb1b0a200000000001e669c0000000000000000],
  #of the family

  ["kingdom_4_pretender",  "Aetheling Oswine  Orsicing",   "Aetheling Oswine  Orsicing",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_13,[itm_saddle_horse,   itm_nowa,    itm_ankle_boots,              itm_splinted_leather_greaves,                 itm_nowa,           itm_spatha,           itm_shield_round_03,    itm_helm_captaina],            lord_attrib,wp(220),knight_skills_5, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
  #dispossessed and wronged

  ["kingdom_5_pretender",  "Aetheling Osfrith Ceorling",  "Aetheling Osfrith Ceorling",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_9,[itm_saddle_horse,  itm_byrnie_f_new,             itm_ankle_boots,              itm_splinted_leather_greaves,   itm_byrnie_f_new,           itm_spatha,         itm_shield_round_04,        itm_horn_helmet],         lord_attrib,wp(220),knight_skills_5, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
  #republican

  ["kingdom_6_pretender",  "Issa map Finmail",       "Issa map Finmail",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_6,[itm_saddle_horse,  itm_byrnie5,             itm_ankle_boots,              itm_splinted_leather_greaves,   itm_byrnie5,           itm_spatha,      itm_tab_shield_small_round_c],          lord_attrib,wp(220),knight_skills_5, 0x0000000ca100304432d49b54539a24a300000000001cd6dc0000000000000000],

  ["kingdom_7_pretender",  "Aetheling Berthrold",       "Aetheling Berthrold",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,  itm_byrnie4,             itm_ankle_boots,              itm_splinted_leather_greaves,   itm_byrnie4,           itm_spatha,      itm_tab_shield_small_round_c],          lord_attrib,wp(220),knight_skills_5, 0x0000000b0500058d581d69551335d6f300000000001ee7a30000000000000000],

  ["kingdom_8_pretender",  "Cunbelin map Dunaut",       "Cunbelin map Dunaut",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_16,[itm_saddle_horse,  itm_byrnie5,             itm_ankle_boots,              itm_splinted_leather_greaves,   itm_byrnie5,           itm_spatha,      itm_tab_shield_small_round_c],          lord_attrib,wp(220),knight_skills_5, 0x0000000c9f0001041b5c95e9e346cb1a00000000001d285d0000000000000000],

  ["kingdom_9_pretender",  "Cystennin map Riderch Hael",       "Cystennin map Riderch Hael",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_18,[itm_blue_gambeson, itm_bare_legs_blue, itm_spatha,      itm_tab_shield_small_round_c],          lord_attrib,wp(220),knight_skills_5, 0x0000000fff003151396376cb1c91b89a00000000001dbc4a0000000000000000],

  ["kingdom_10_pretender",  "Tanist Brude map Bili",       "Tanist Brude map Bili",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_20,[itm_saddle_horse,  itm_mail_coat_1,             itm_ankle_boots,              itm_splinted_leather_greaves,   itm_mail_coat_1,           itm_spatha,      itm_tab_shield_small_round_c],          lord_attrib,wp(220),knight_skills_5, 0x0000000324092353552375c4e14ec57300000000001c3b490000000000000000],

  ["kingdom_11_pretender",  "Cadwaladr map Cadwallon",       "Cadwaladr map Cadwallon",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_23,[itm_saddle_horse,  itm_byrnie4,             itm_ankle_boots,              itm_splinted_leather_greaves,   itm_byrnie4,           itm_spatha,      itm_tab_shield_small_round_c],          lord_attrib,wp(220),knight_skills_5, 0x0000000324092353552375c4e14ec57300000000001c3b490000000000000000],

##  ["kingdom_1_lord_a", "Kingdom 1 Lord A", "Kingdom 1 Lord A", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
  ##  ["kingdom_1_lord_b", "Kingdom 1 Lord B", "Kingdom 1 Lord B", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
  ##  ["kingdom_1_lord_c", "Kingdom 1 Lord C", "Kingdom 1 Lord C", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
  ##  ["kingdom_1_lord_d", "Kingdom 1 Lord D", "Kingdom 1 Lord D", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
  ##  ["kingdom_1_lord_e", "Kingdom 1 Lord E", "Kingdom 1 Lord E", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
  ##  ["kingdom_1_lord_f", "Kingdom 1 Lord F", "Kingdom 1 Lord F", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
  ##  ["kingdom_1_lord_g", "Kingdom 1 Lord G", "Kingdom 1 Lord G", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
  ##  ["kingdom_1_lord_h", "Kingdom 1 Lord H", "Kingdom 1 Lord H", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
  ##  ["kingdom_1_lord_i", "Kingdom 1 Lord I", "Kingdom 1 Lord I", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
  ##  ["kingdom_1_lord_j", "Kingdom 1 Lord J", "Kingdom 1 Lord J", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
  ##  ["kingdom_1_lord_k", "Kingdom 1 Lord K", "Kingdom 1 Lord K", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
  ##  ["kingdom_1_lord_l", "Kingdom 1 Lord L", "Kingdom 1 Lord L", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
  ##  ["kingdom_1_lord_m", "Kingdom 1 Lord M", "Kingdom 1 Lord M", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
  ##  ["kingdom_1_lord_n", "Kingdom 1 Lord N", "Kingdom 1 Lord N", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],



#  ["town_1_ruler_a", "King Harlaus",  "King Harlaus",  tf_hero, scn_town_1_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_bluevikingshirt,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010908101e36db44b75b6dd],
  #  ["town_2_ruler_a", "Duke Taugard",  "Duke Taugard",  tf_hero, scn_town_2_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_bluevikingshirt,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000310401e06db86375f6da],
  #  ["town_3_ruler_a", "Count Grimar",  "Count Grimar",  tf_hero, scn_town_3_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004430301e46136eb75bc0a],
  #  ["town_4_ruler_a", "Count Haxalye", "Count Haxalye", tf_hero, scn_town_4_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010918701e77136e905bc0e
  #  ["town_5_ruler_a", "Count Belicha", "Count Belicha", tf_hero, scn_town_5_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000421c801e7713729c5b8ce],
  #  ["town_6_ruler_a", "Count Nourbis", "Count Nourbis", tf_hero, scn_town_6_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c640501e371b72bcdb724],
  #  ["town_7_ruler_a", "Count Rhudolg", "Count Rhudolg", tf_hero, scn_town_7_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c710201fa51b7286db721],

#  ["town_8_ruler_b", "King Yaroglek", "King_yaroglek", tf_hero, scn_town_8_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000128801f294ca6d66d555],
  #  ["town_9_ruler_b", "Count Aolbrug", "Count_Aolbrug", tf_hero, scn_town_9_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004234401f26a271c8d38ea],
  #  ["town_10_ruler_b","Count Rasevas", "Count_Rasevas", tf_hero, scn_town_10_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000001032c201f38e269372471c],
  #  ["town_11_ruler_b","Count Leomir",  "Count_Leomir",  tf_hero, scn_town_11_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c538001f55148936d3895],
  #  ["town_12_ruler_b","Count Haelbrad","Count_Haelbrad",tf_hero, scn_town_12_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000410c701f38598ac8aaaab],
  #  ["town_13_ruler_b","Count Mira",    "Count_Mira",    tf_hero, scn_town_13_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004204401f390c515555594],
  #  ["town_14_ruler_b","Count Camechaw","Count_Camechaw",tf_hero, scn_town_14_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],

##  ["kingdom_2_lord_a", "Kingdom 2 Lord A", "Kingdom 2 Lord A", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
  ##  ["kingdom_2_lord_b", "Kingdom 2 Lord B", "Kingdom 2 Lord B", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
  ##  ["kingdom_2_lord_c", "Kingdom 2 Lord C", "Kingdom 2 Lord C", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
  ##  ["kingdom_2_lord_d", "Kingdom 2 Lord D", "Kingdom 2 Lord D", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
  ##  ["kingdom_2_lord_e", "Kingdom 2 Lord E", "Kingdom 2 Lord E", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
  ##  ["kingdom_2_lord_f", "Kingdom 2 Lord F", "Kingdom 2 Lord F", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
  ##  ["kingdom_2_lord_g", "Kingdom 2 Lord G", "Kingdom 2 Lord G", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
  ##  ["kingdom_2_lord_h", "Kingdom 2 Lord H", "Kingdom 2 Lord H", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
  ##  ["kingdom_2_lord_i", "Kingdom 2 Lord I", "Kingdom 2 Lord I", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
  ##  ["kingdom_2_lord_j", "Kingdom 2 Lord J", "Kingdom 2 Lord J", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
  ##  ["kingdom_2_lord_k", "Kingdom 2 Lord K", "Kingdom 2 Lord K", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
  ##  ["kingdom_2_lord_l", "Kingdom 2 Lord L", "Kingdom 2 Lord L", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
  ##  ["kingdom_2_lord_m", "Kingdom 2 Lord M", "Kingdom 2 Lord M", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
  ##  ["kingdom_2_lord_n", "Kingdom 2 Lord N", "Kingdom 2 Lord N", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],



#Royal family members

  ["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [itm_shirt ,   itm_veil_g,    itm_ankle_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

  #Swadian ladies - eight mothers, eight daughters, four sisters
  ["kingdom_1_lady_1","Oslafa","Oslafa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [    itm_common_veil_b, itm_kenttunik,      itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_1_lady_2","Eanswith","Eanswith",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [    itm_red_dress,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_1_lady_3","Eanflaed","Eanflaed",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_lady_dress_ruby,   itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],

  ["kingdom_2_lady_1","Aethelburh","Elina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_common_veil_b, itm_tunikwjac1,   itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_2_lady_2","Ymme","Ymme",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [   itm_red_dress,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000004530000060512213341a24ace00000000001eef430000000000000000], #chief mujer de edu del clan cuervo
  ["kingdom_2_lady_3","Seaxburh","Seaxburh",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [  itm_lady_dress_ruby,     itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],

  ["kingdom_3_lady_1","Aebbe","Aebbe",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [     itm_kenttunik,itm_common_veil_d,    itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_3_lady_2","Eilfgiva","Eilfgiva",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [ itm_lady_dress_ruby,     itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003f008004778a23d387447fff00000000001eab110000000000000000], #onneca clan cuervo chief
  ["kingdom_3_lady_3","Aelfgyf","Aelfgyf",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_woolen_dress, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],

  ["kingdom_4_lady_1","Saewara","Saewara",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [  itm_common_veil_d ,itm_kenttunik,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_4_lady_2","Saethryth","Saethryth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [   itm_woolen_dress,    itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_4_lady_3","Eadgyd","Eadgyd",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [  itm_lady_dress_ruby,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_4_lady_4","Hereswith","Hereswith",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [ itm_common_veil_b,  itm_lady_dress_ruby,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_4_lady_5","Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [    itm_woolen_dress,    itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_4_lady_6","Aelftrudis","Aelftrudis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [    itm_lady_dress_ruby,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],

  ["kingdom_5_lady_1","Ethelgifu","Ethelgifu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [     itm_common_veil_d,itm_kenttunik, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_5_lady_2","Coenthryth Pybbing","Coenthryth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [   itm_common_veil_b,itm_tunikwjac1,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_5_lady_3","Edith","Edith",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [    itm_red_dress,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_5_lady_4","Egburh","Egburh",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [     itm_lady_dress_ruby,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
  ["kingdom_5_lady_5","Cynegyth","Cynegyth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [    itm_lady_dress_ruby,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_5_lady_6","Eormengyth","Eormengyth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [  itm_common_veil_b,itm_tunikwjac1,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_5_lady_7","Aelfwynne","Aelfwynne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [  itm_common_veil_e,itm_tunikwjac1, itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],

  ["kingdom_6_lady_1","Adelburga","Adelburga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [    itm_common_veil_e,itm_kenttunik,itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_6_lady_2","Edburge","Edburge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [    itm_red_dress,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],

  ["kingdom_7_lady_1","Gwledyr","Gwledyr",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [   itm_lady_dress_ruby,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],

  ["kingdom_8_lady_1","Verch Guitoli","Verch Guitoli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [  itm_common_veil_b,itm_sarranid_common_dress,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_8_lady_2","Gwenddwyn","Gwenddwyn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [   itm_common_veil_c,itm_lady_dress_ruby, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_8_lady_3","Verch Tewdwr","Verch Tewdwr",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [   itm_red_dress,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_8_lady_4","Ceingar","Ceingar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [  itm_sarranid_felt_head_cloth,itm_sarranid_common_dress_b,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_8_lady_5","Lleigy","Lleigy",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_red_dress,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_8_lady_6","Elen","Elen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [   itm_lady_dress_ruby,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],

  ["kingdom_9_lady_1","Cynewise","Cynewise",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [   itm_common_veil_d,itm_kenttunik,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_9_lady_2","Wilteburh","Wilteburh",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [   itm_common_veil_e,itm_kenttunik,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_9_lady_3","Cyneburh","Cyneburh",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [    itm_woolen_dress,   itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_9_lady_4","Cyneswith","Cyneswith",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [     itm_red_dress, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_9_lady_5","Alwith Eowing","Alwith",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [ itm_lady_dress_ruby, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_9_lady_6","Aedelfled","Aedelfled",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [ itm_common_veil_b,itm_tunikwjac1, itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_9_lady_7","Aepelhilde","Aepelhilde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [ itm_common_veil_c,itm_tunikwjac1,itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_9_lady_8","Aepelswip","Aepelswip",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [  itm_lady_dress_ruby,           itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_9_lady_9","Aette","Aette",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [   itm_red_dress,    itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],

  ["kingdom_10_lady_1","Onbrawst","Onbrawst",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [  itm_sarranid_felt_head_cloth,itm_sarranid_common_dress_b,        itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],

  ["kingdom_11_lady_1","Meisyr","Meisyr",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [    itm_red_dress,      itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_11_lady_2","Heledd","Heledd",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [   itm_lady_dress_ruby,      itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_11_lady_3","Ffever","Ffever",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [     itm_red_dress, itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_11_lady_4","Medlan","Medlan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [      itm_lady_dress_ruby,    itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_11_lady_5","Rhiain Ceinfrid","Ceinfrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [    itm_common_veil_b,itm_brown_dress,     itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_11_lady_6","Meddwyl","Meddwyl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [  itm_red_dress,     itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_11_lady_7","Gwladus","Gwladus",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [     itm_lady_dress_ruby,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],

  ["kingdom_12_lady_1","Morvydd verch Urien","Morvydd",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [      itm_common_veil_c,itm_brown_dress,      itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_12_lady_2","Eurneid verch Clydno","Eurneid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,  [      itm_red_dress,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_12_lady_3","Euronwy verch Clydno","Euronwy",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,  [     itm_lady_dress_ruby,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
  ["kingdom_12_lady_4","Menedoc verch Constantine","Menedoc",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,  [   itm_sarranid_felt_head_cloth,itm_sarranid_common_dress_b,    itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],

  ["kingdom_13_lady_1","Fin ingen Colman Rimid", "Verch Colman",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13, [    itm_common_veil_d,itm_kenttunik,      itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
  ["kingdom_13_lady_2","Beorhtwne","Beorhtwne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13, [       itm_common_veil_e,itm_tunikwjac1,    itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_13_lady_3","Bertanae","Bertanae",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13,  [    itm_woolen_dress, itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_13_lady_4","Bucgan","Bucgan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13,  [  itm_lady_dress_ruby,    itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_13_lady_5","Bergevilde","Bergevilde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13, [   itm_common_veil_b,itm_kenttunik,      itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_13_lady_6","Ceolburga","Ceolburga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13, [      itm_brown_dress,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_13_lady_7","Celfled","Celfled",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13,  [   itm_lady_dress_ruby, itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_13_lady_8","Cutsuidae","Cutsuidae",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13,  [   itm_lady_dress_ruby,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],

  ["kingdom_14_lady_1","Cwen","Cwen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,  [   itm_sarranid_felt_head_cloth,itm_kenttunik,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_14_lady_2","Cwenburh","Cwenburh",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,  [itm_lady_dress_ruby,    itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],

  ["kingdom_15_lady_1","Morfudd","Morfudd",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15, [    itm_lady_dress_ruby,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_15_lady_2","Rhiainfelt","Rhiainfelt",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15,  [ itm_brown_dress,    itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_15_lady_3","Seren","Seren",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15,  [  itm_common_veil_c,itm_brown_dress, itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_15_lady_4","Euronwy","Euronwy",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15,  [ itm_sarranid_felt_head_cloth,itm_sarranid_common_dress_b,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],

  ["kingdom_16_lady_1","Danhadlwen","Danhadlwen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16, [   itm_lady_dress_ruby,     itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_16_lady_2","Gwawl","Gwawl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16,  [  itm_red_dress, itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],

  ["kingdom_17_lady_1","Muireann","Muireann",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17, [    itm_common_veil_d,itm_pictishdressverde,     itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_17_lady_2","Ingen Rogallaig","Ingen Rogallaig",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17, [    itm_pictishdress,    itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_17_lady_3","Medb","Medb",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17,  [   itm_wimple_with_veil,itm_pictishdress1,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_17_lady_4","Creide","Creide",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17,  [ itm_sarranid_felt_head_cloth,itm_pictishdress3,   itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_17_lady_5","Derbforgaill","Derbforgaill",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17, [      itm_sarranid_dress_a,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_17_lady_6","Mor","Mor",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17,  [  itm_sarranid_dress_b,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],


  ["kingdom_18_lady_1","Verch Bili","Verch Bili",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18, [   itm_brown_dress,     itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_18_lady_2","Tenos","Tenos",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18, [     itm_sarranid_felt_head_cloth,itm_green_dress,     itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_18_lady_3","Gwenddydd","Gwenddydd",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18,  [    itm_common_veil_e,itm_sarranid_common_dress,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_18_lady_4","Tanglwst","Tanglwst",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18,  [    itm_brown_dress, itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_18_lady_5","Sannan","Sannan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18, [     itm_lady_dress_ruby,    itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_18_lady_6","Nesta","Nesta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18, [ itm_red_dress, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000bf0400035913aa236b4d975a00000000001eb69c0000000000000000],

  ["kingdom_19_lady_1","Ingen Gwid","Ingen Gwid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19,  [ itm_pictishdressverde,     itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_19_lady_2","Etain","Etain",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19, [  itm_pictishdress1,       itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_19_lady_3","Aine","Aine",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19, [  itm_pictishdress3,     itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],

  ["kingdom_20_lady_1","Ingen Gwid","Ingen Gwid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20, [     itm_pictishdress,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_20_lady_2","Ingen Eanfrith","Ingen Eanfrith",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20, [  itm_pictishdressverde,    itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_20_lady_3","Ingen Brude","Ingen Brude",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20,  [ itm_sarranid_felt_head_cloth,itm_pictishdress1, itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_20_lady_4","Ingen Domlech","Ingen Domlech",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20,  [ itm_pictishdress3, itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_20_lady_5","Ingen Gwydd","Ingen Gwydd",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20, [   itm_sarranid_dress_a,      itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_20_lady_6","Bridei","Bridei",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20, [     itm_picta_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_20_lady_7","Eithne","Eithne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20,  [  itm_common_veil_b,itm_sarranid_dress_b], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],

  ["kingdom_21_lady_1","Ninnoc","Ninnoc",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21,  [    itm_lady_dress_ruby,itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],

  ["kingdom_22_lady_1","Efeilian","Efeilian",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [ itm_sarranid_felt_head_cloth,itm_sarranid_common_dress_b,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_22_lady_2","Wenna","Wenna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [  itm_brown_dress,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_22_lady_3","Aourken","Aourken",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [  itm_brown_dress,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],

  ["kingdom_23_lady_1","Perwyr","Eurowy",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [   itm_red_dress,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_23_lady_2","Eurowy","Eurowy",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [  itm_sarranid_felt_head_cloth,itm_sarranid_common_dress_b,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_23_lady_3","Maud","Maud",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [    itm_green_dress, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_23_lady_4","Morwyl","Morwyl",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [ itm_lady_dress_ruby, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],

  ["kingdom_24_lady_1","Sanan","Sanan",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [  itm_brown_dress,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_24_lady_2","Morgawse","Morgawse",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_lady_dress_ruby,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],

  ["kingdom_25_lady_1","Nesta","Nesta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25, [  itm_common_veil_b,itm_brown_dress,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_25_lady_2","Ceindrych","Ceindrych",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25, [ itm_green_dress, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],

  ["kingdom_26_lady_1","Brifael","Brifael",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [  itm_red_dress,itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_26_lady_2","Marwenna","Marwenna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [ itm_brown_dress,itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_26_lady_3","Anna","Anna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [  itm_lady_dress_ruby, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_26_lady_4","Gwenonwy","Gwenonwy",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [   itm_green_dress, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_26_lady_5","Gweneddlon","Gweneddlon",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [ itm_sarranid_felt_head_cloth,itm_brown_dress, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],

  ["kingdom_27_lady_1","Condadil","Condadil",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [  itm_common_veil_c,itm_sarranid_dress_a,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_27_lady_2","Uaisle","Uaisle",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [  itm_common_veil_d,itm_pictishdressverde,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_27_lady_3","Fedelm","Fedelm",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [  itm_pictishdress3,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],

  ["kingdom_28_lady_1","Almu","Almu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_28, [   itm_sarranid_felt_head_cloth,itm_sarranid_dress_a,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_28_lady_2","Aodhnait","Aodhnait",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_28, [ itm_sarranid_felt_head_cloth, itm_sarranid_dress_b,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
  ["kingdom_28_lady_3","Aoibheann","Aoibheann",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_28, [  itm_common_veil_e,     itm_pictishdress1,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_28_lady_4","Binne","Binne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_28, [ itm_common_veil_b,itm_pictishdressverde,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_28_lady_5","Briana","Briana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_28,  [ itm_pictishdress3, itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_28_lady_6","Caelfind","Caelfind",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_28,  [itm_pictishdress1,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],

  ["kingdom_29_lady_1","Delbchaem","Delbchaem",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_29, [ itm_sarranid_felt_head_cloth,itm_pictishdress1,    itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_29_lady_2","Doirend","Doirend",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_29, [  itm_pictishdress, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_29_lady_3","Eva","Eva",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_29, [  itm_sarranid_dress_a,   itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],

  ["kingdom_30_lady_1","Duinseach","Duinseach",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_30, [ itm_pictishdress1,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_30_lady_2","Lassair","Lassair",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_30, [    itm_pictishdressverde,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_30_lady_3","Cath ingen Cellach","Cath",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_30, [  itm_pictishdress, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_30_lady_4","Land","Land",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_30, [ itm_common_veil_c,  itm_pictishdress3,      itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_30_lady_5","Flannesda","Flannesda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_30, [  itm_sarranid_felt_head_cloth,itm_sarranid_dress_a,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_30_lady_6","lassa","lassa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_30,  [  itm_common_veil_d,itm_sarranid_dress_b,  itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],

  ["kingdom_31_lady_1","Teglaig ingen Odhar","Teglaig",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_31, [ itm_sarranid_dress_b, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_31_lady_2","Mall","Mall",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_31, [   itm_common_veil_e,itm_sarranid_dress_a,  itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_31_lady_3","Mhari","Mhari",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_31, [ itm_sarranid_felt_head_cloth,itm_pictishdress3, itm_decorated_leather_shoes_red],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],


#  ["kingdom_11_lord_daughter","kingdom_11_lord_daughter","kingdom_11_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008300701c08d34a450ce43],
  #  ["kingdom_13_lord_daughter","kingdom_13_lord_daughter","kingdom_13_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_green,   itm_turret_hat_green,   itm_decorated_leather_shoes_red], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008000401db10a45b41d6d8],
  ##  ["kingdom_1_lady_a","kingdom_1_lady_a","kingdom_1_lady_a",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_ankle_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],
  ##  ["kingdom_1_lady_b","kingdom_1_lady_b","kingdom_1_lady_b",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_ankle_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000101c3ae68e0e944ac],
  ##  ["kingdom_2_lady_a","Kingdom 2 Lady a","Kingdom 2 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_green,   itm_turret_hat_green,   itm_ankle_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008100501d8ad93708e4694],
  ##  ["kingdom_2_lady_b","Kingdom 2 Lady b","Kingdom 2 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_ankle_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000401d8ad93708e4694],
  ##  ["kingdom_3_lady_a","Kingdom 3 Lady a","Kingdom 3 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_3, [               itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_ankle_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500301d8ad93708e4694],
  ##
  ##  ["kingdom_3_lady_b","Kingdom 3 Lady b","Kingdom 3 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_3,  [                         itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_ankle_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100601d8b08d76d14a24],
  ##  ["kingdom_4_lady_a","Kingdom 4 Lady a","Kingdom 4 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_green,   itm_turret_hat_green,   itm_ankle_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500601d8ad93708e4694],
  ##  ["kingdom_4_lady_b","Kingdom 4 Lady b","Kingdom 4 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_ankle_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse,itm_leather_jerkin,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],
  #Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
  ##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_kingdom_1,[itm_courser,            itm_fighting_axe,       itm_leather_jerkin,         itm_ankle_boots,          itm_veil_g],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008200201e54c137a940c91],
  ##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_kingdom_2,[itm_saddle_horse,       itm_arming_sword,       itm_light_leather,          itm_wrapping_boots,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000000601db6db6db6db6db],
  ##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_kingdom_3,[itm_courser,            itm_nordic_sword,       itm_leather_jerkin,         itm_wrapping_boots,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008100701db6db6db6db6db],
  ##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_kingdom_4,[itm_saddle_horse,       itm_falchion,           itm_light_leather,          itm_carbatinae_2_blue,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401e54c137a945c91],
  ##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_kingdom_5,[itm_saddle_horse,       itm_sword,              itm_ragged_outfit,          itm_ankle_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008038001e54c135a945c91],
  ##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_kingdom_1,[itm_saddle_horse,      itm_scimitar,           itm_leather_jerkin,         itm_ankle_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000248e01e54c1b5a945c91],
  ##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_kingdom_2,[itm_hunter,            itm_arming_sword,       itm_padded_jack_3_trig,         itm_carbatinae_2_blue,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004200601c98ad39c97557a],
  ##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_kingdom_3,[itm_saddle_horse,      itm_nordic_sword,       itm_light_leather,          itm_ankle_boots,          itm_woolen_hood],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001095ce01d6aad3a497557a],
  ##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_kingdom_4,[itm_saddle_horse,      itm_sword,              itm_padded_jack_3_trig,         itm_ankle_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010519601ec26ae99898697],
  ##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_wrapping_boots,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000884c401f6837d3294e28a],
  ##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jerkin,         itm_wrapping_boots,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c450501e289dd2c692694],
  ##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_falchion,           itm_leather_jerkin,         itm_ankle_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c660a01e5af3cb2763401],
  ##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[itm_sumpter_horse,      itm_nordic_sword,       itm_padded_jack_3_trig,         itm_ankle_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001001d601ec912a89e4d534],
  ##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[itm_courser,            itm_bastard_sword,      itm_light_leather,          itm_ankle_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004335601ea2c04a8b6a394],
  ##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_padded_jack_3_trig,         itm_wrapping_boots,            itm_woolen_cap_newred],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008358e01dbf27b6436089d],
  ##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_ankle_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c300101db0b9921494add],
  ##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jerkin,         itm_carbatinae_2_blue,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008740f01e945c360976a0a],
  ##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_nordic_sword,       itm_padded_jack_3_trig,         itm_ankle_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008020c01fc2db3b4c97685],
  ##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_falchion,           itm_leather_jerkin,         itm_wrapping_boots,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008118301f02af91892725b],
  ##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_courser,            itm_arming_sword,       itm_padded_jack_3_trig,         itm_ankle_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401f6837d27688212],
  #LAZERAS MODIFIED  {Top Tier Troops Recruit} chief
  ###########################################################################
["hero1","Briton Elite Companion","Briton Elite Companion",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],str_9|agi_5|int_12|cha_9|level(3),wp(60),knows_tracker_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2,swadian_face_middle_1,swadian_face_older_2],
  ["hero2","Saxon Elite Companion","Saxon Elite Companion",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],str_9|agi_5|int_12|cha_9|level(3),wp(60),knows_tracker_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2,swadian_face_middle_1,swadian_face_older_2],
  ["hero3","Pictish Elite Companion","Pictish Elite Companion",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],str_20|agi_5|int_12|cha_9|level(3),wp(60),knows_tracker_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2,swadian_face_middle_1,swadian_face_older_2],
  ["hero4","Anglo Elite Companion","Anglo Elite Companion",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],str_9|agi_15|int_12|cha_9|level(3),wp(60),knows_tracker_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2,swadian_face_middle_1,swadian_face_older_2],
  ["hero5","Godelic Elite Companion","Godelic Elite Companion",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],str_9|agi_5|int_12|cha_9|level(3),wp(60),knows_tracker_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2,swadian_face_middle_1,swadian_face_older_2],
  ["hero6","Jute Elite Companion","Jute Elite Companion",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],str_9|agi_5|int_12|cha_9|level(3),wp(60),knows_tracker_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2,swadian_face_middle_1,swadian_face_older_2],
  ["hero7","Pirate Elite Companion","Pirate Elite Companion",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],str_9|agi_5|int_12|cha_9|level(3),wp(60),knows_tracker_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2,swadian_face_middle_1,swadian_face_older_2],
  ["hero8","Outlaw Elite Companion","Outlaw Elite Companion",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],str_9|agi_5|int_12|cha_9|level(3),wp(60),knows_tracker_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2,swadian_face_middle_1,swadian_face_older_2],
  ["hero9","Slaver Elite Companion","Slaver Elite Companion",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],str_9|agi_5|int_12|cha_9|level(3),wp(60),knows_tracker_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2,swadian_face_middle_1,swadian_face_older_2],
  ["hero10","Frisen Elite Companion","Frisen Elite Companion",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],str_9|agi_5|int_12|cha_9|level(3),wp(60),knows_tracker_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2,swadian_face_middle_1,swadian_face_older_2],
  ["hero11","Mercenary Elite Companion","Mercenary Elite Companion",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],str_9|agi_5|int_12|cha_9|level(3),wp(60),knows_tracker_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2,swadian_face_middle_1,swadian_face_older_2],
  ["hero12","Cantabrian Elite Warrior","Cantabrian Elite Warrior",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],str_9|agi_5|int_12|cha_9|level(3),wp(60),knows_tracker_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2,swadian_face_middle_1,swadian_face_older_2],
  ###########################################################################

#LAZERAS MODIFIED  {Top Tier Troops Recruit}

#Seneschals
  ["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic5,       itm_decorated_leather_shoes_blue], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_jack_3_trig,     itm_carbatinae_1_red],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic5,       itm_decorated_leather_shoes_blue], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_carbatinae_1_red],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather_brown,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_carbatinae_1_red],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather_brown,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic5,       itm_decorated_leather_shoes_blue], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,     itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic5,       itm_decorated_leather_shoes_blue], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_khergit_armor,     itm_carbatinae_1_red],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_khergit_armor,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_khergit_armor,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_23_seneschal", "{!}Town 23 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic5,       itm_decorated_leather_shoes_blue], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_24_seneschal", "{!}Town 24 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_25_seneschal", "{!}Town 25 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_carbatinae_1_red],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_26_seneschal", "{!}Town 26 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather_brown,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_27_seneschal", "{!}Town 27 Seneschal", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_carbatinae_1_red],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_28_seneschal", "{!}Town 28 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather_brown,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_29_seneschal", "{!}Town 29 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic5,       itm_decorated_leather_shoes_blue], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_30_seneschal", "{!}Town 30 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_31_seneschal", "{!}Town 31 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,     itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_32_seneschal", "{!}Town 32 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic5,       itm_decorated_leather_shoes_blue], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_33_seneschal", "{!}Town 33 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_carbatinae_1_red],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_34_seneschal", "{!}Town 34 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_35_seneschal", "{!}Town 35 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_36_seneschal", "{!}Town 36 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_37_seneschal", "{!}Town 37 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_38_seneschal", "{!}Town 38 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_39_seneschal", "{!}Town 39 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_40_seneschal", "{!}Town 40 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_41_seneschal", "{!}Town 41 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_42_seneschal", "{!}Town 42 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_padded_leather_brown,      itm_carbatinae_1_green],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],

  ["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic5,          itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_armor_c,           itm_carbatinae_1_red],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,        itm_decorated_leather_shoes_blue], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_khergit_armor,           itm_carbatinae_1_red],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic5,          itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,         itm_carbatinae_1_green],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,        itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_armor_c,        itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_armor_c,           itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,        itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_khergit_armor,        itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_4_trig,         itm_carbatinae_2_blue],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,        itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_armor_c,           itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,        itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_4_trig,         itm_carbatinae_2_blue],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,        itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_armor_c,           itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,        itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,        itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_4_trig,         itm_carbatinae_2_blue],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,        itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_41_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_42_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_43_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_44_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_45_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_46_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_khergit_armor,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_47_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_48_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_49_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_50_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_51_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_52_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_armor_c,           itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_53_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,        itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_54_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_55_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_56_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_57_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_4_trig,         itm_carbatinae_2_blue],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_58_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,        itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_59_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_60_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_61_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_62_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_armor_c,           itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_63_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,        itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_64_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_65_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_66_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_67_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_4_trig,         itm_carbatinae_2_blue],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_68_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,        itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_69_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_70_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_71_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_72_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_armor_c,           itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_73_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_jack_3_trig,        itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_74_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_75_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],

#Arena Masters
  ["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic2,      itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_2_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_3_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_leather_armor_c,       itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_4_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic4,      itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_5_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_6_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_leather_jerkin,    itm_ankle_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_8_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_nomad_armor,       itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_10_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_khergit_armor,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_leather_jerkin,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_robe,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_sarranid_cavalry_robe,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_20_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[itm_robe,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_21_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_22_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_22_arena|entry(52),reserved,  fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_23_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_23_arena|entry(52),reserved,   fac_commoners,[itm_leather_armor_c,       itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_24_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_24_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_25_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_25_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_26_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_26_arena|entry(52),reserved,   fac_commoners,[itm_leather_jerkin,    itm_ankle_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_27_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_27_arena|entry(52),reserved,   fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_28_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_28_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_29_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_29_arena|entry(52),reserved,   fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_30_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_30_arena|entry(52),reserved,  fac_commoners,[itm_leather_armor_c,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_31_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_31_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_32_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_32_arena|entry(52),reserved,  fac_commoners,[itm_leather_jerkin,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_33_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_33_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_34_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_34_arena|entry(52),reserved,  fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_35_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_35_arena|entry(52),reserved,  fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_36_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_36_arena|entry(52),reserved,  fac_commoners,[itm_robe,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_37_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_37_arena|entry(52),reserved,  fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_38_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_38_arena|entry(52),reserved,  fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_39_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_39_arena|entry(52),reserved,  fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_40_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_40_arena|entry(52),reserved,  fac_commoners,[itm_robe,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_41_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_41_arena|entry(52),reserved,  fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_42_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_42_arena|entry(52),reserved,  fac_commoners,[itm_padded_jack_3_trig,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],


# Underground

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_ankle_boots       ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
  ##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,    itm_turret_hat_ruby     ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
  ##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_apron,      itm_ankle_boots          ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
  ##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_ankle_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
  ##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[itm_padded_jack_4_trig,       itm_carbatinae_2_blue           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
  ##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_ankle_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
  ##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,       itm_woolen_hood         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
  ##
  ##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_jerkin,     itm_ankle_boots       ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
  ##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_ankle_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
  ##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_ankle_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
  ##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_brown_dress,        itm_wimple_with_veil    ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
  ##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_ankle_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
  ##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[itm_padded_jack_4_trig,     itm_ankle_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
  ##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_lady_dress_ruby,      itm_turret_hat_ruby     ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
  #arena_masters_end = zendar_armorer

  ["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_ankle_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_lady_dress_ruby,          itm_veil_g       ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,        itm_ankle_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_jack_4_trig,         itm_ankle_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,          itm_ankle_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_robe,       itm_ankle_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_nomad_armor,       itm_carbatinae_2_blue       ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_jack_3_trig,       itm_ankle_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_jack_4_trig,        itm_ankle_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_nobleman_outfit,       itm_ankle_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_robe,        itm_ankle_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_nobleman_outfit,         itm_ankle_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_khergit_armor,       itm_ankle_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_lady_dress_ruby,         itm_veil_g       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_jack_4_trig,        itm_ankle_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_robe,         itm_ankle_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_robe,       itm_ankle_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_lady_dress_ruby,         itm_veil_g       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_jack_4_trig,        itm_ankle_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_robe,         itm_ankle_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_robe,       itm_ankle_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_sarranid_common_dress,         itm_veil_g       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_23_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,        itm_ankle_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_24_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_jack_4_trig,         itm_ankle_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_25_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,          itm_ankle_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_26_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_robe,       itm_ankle_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_27_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_carbatinae_2_blue       ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_28_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_jack_3_trig,       itm_ankle_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_29_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_jack_4_trig,        itm_ankle_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_30_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_ankle_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_31_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_robe,        itm_ankle_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_32_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_jack_4_trig,         itm_ankle_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_33_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_ankle_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_34_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_lady_dress_ruby,         itm_veil_g       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_35_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_jack_4_trig,        itm_ankle_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_36_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_robe,         itm_ankle_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_37_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_robe,       itm_ankle_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_38_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_lady_dress_ruby,         itm_veil_g       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_39_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_tunic,        itm_ankle_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_40_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_robe,         itm_ankle_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_41_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_sarranid_cavalry_robe,       itm_ankle_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_42_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_lady_dress_ruby,         itm_veil_g       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],

# Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_ankle_boots,itm_veil_g],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,     itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_robe,   itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_courtly_outfit,            itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_nomad_armor,            itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_lady_dress_ruby,     itm_wrapping_boots,itm_veil_g],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_9_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_nobleman_outfit,  itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_nobleman_outfit,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,  itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_khergit_armor,           itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,  itm_carbatinae_2],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_carbatinae_2],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_carbatinae_2],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_carbatinae_2],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_23_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_robe,   itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_24_weaponsmith", "Harenbili the weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_25_weaponsmith", "Maonirn the weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_26_weaponsmith", "Uormuin the weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_27_weaponsmith", "Godgyfu the weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_28_weaponsmith", "Dounerth the weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_lady_dress_ruby,     itm_wrapping_boots,itm_veil_g],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_29_weaponsmith", "Aed the weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_30_weaponsmith","Fogartach the weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_31_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,  itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_32_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_33_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_34_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_blue,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_35_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,  itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_36_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_khergit_armor,           itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_37_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_38_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_39_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,  itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_40_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_41_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_42_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

#Tavern keepers

  ["town_1_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_2_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_3_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_4_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_5_tavernkeeper", "Horsa_Monolithus","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_6_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_6_tavern|entry(9),0,   fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_7_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots,      itm_veil_g],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_8_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,      itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_9_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_10_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_10_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_11_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_11_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_12_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_13_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots,     itm_veil_g],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_14_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,[itm_courtly_outfit,               itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_15_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_15_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_16_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_17_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots,     itm_veil_g],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_18_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_19_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_19_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cavalry_robe,        itm_carbatinae_2],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_20_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_20_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe,       itm_carbatinae_2],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_21_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_21_tavern|entry(9),0,  fac_commoners,[itm_sarranid_common_dress,        itm_carbatinae_2,     itm_veil_g],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_22_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,[itm_nobleman_outfit,               itm_carbatinae_2],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_23_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_23_tavern|entry(9),0,   fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_24_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_24_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_25_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_25_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_26_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_26_tavern|entry(9),0,   fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_27_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_27_tavern|entry(9),0,   fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots,      itm_veil_g],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],

  ["town_28_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_28_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,      itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_29_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_29_tavern|entry(9),0,   fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_30_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_30_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_31_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_31_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_32_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_32_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_33_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_33_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots,     itm_veil_g],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_34_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_34_tavern|entry(9),0,  fac_commoners,[itm_khergit_armor,               itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_35_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_35_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_36_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_36_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_37_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_37_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots,     itm_veil_g],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_38_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_38_tavern|entry(9),0,  fac_commoners,[itm_blue_tunic,               itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_39_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_39_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby, itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_40_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_40_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots,     itm_veil_g],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_41_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_41_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby, itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_42_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_osa|tf_hero|tf_randomize_face|tf_female, scn_town_42_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby,        itm_ankle_boots,     itm_veil_g],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],

#Goods Merchants

  ["town_1_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_coarse_tunic5,  itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_blue_tunic,         itm_ankle_boots,  itm_veil_g   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_4_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_nobleman_outfit,   itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_6_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_lady_dress_ruby,  itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_leather_jerkin,itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_leather_jerkin,itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_11_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [itm_lady_dress_ruby,  itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_13_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_blue_tunic,         itm_ankle_boots,  itm_veil_g   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_15_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_lady_dress_ruby,  itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_17_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_blue_tunic,         itm_ankle_boots,  itm_veil_g   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_18_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_sarranid_common_dress_b,  itm_carbatinae_2],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_21_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_sarranid_cloth_robe,         itm_carbatinae_2],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,    [itm_nobleman_outfit, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_23_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_23_store|entry(9),0, fac_commoners,     [itm_blue_tunic,         itm_ankle_boots,  itm_veil_g   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_24_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_24_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_25_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_25_store|entry(9),0, fac_commoners,     [itm_nomad_armor,   itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_26_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_26_store|entry(9),0, fac_commoners,     [itm_sarranid_cavalry_robe,  itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_27_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_27_store|entry(9),0, fac_commoners,     [itm_courtly_outfit,itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

  ["town_28_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_28_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_29_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_29_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_30_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_30_store|entry(9),0, fac_commoners,    [itm_leather_jerkin,itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_31_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_31_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_32_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_32_store|entry(9),0, fac_commoners,    [itm_lady_dress_ruby,  itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_33_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_33_store|entry(9),0, fac_commoners,    [itm_blue_tunic,         itm_ankle_boots,  itm_veil_g   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_34_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_34_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_35_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_35_store|entry(9),0, fac_commoners,    [itm_nomad_armor, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_36_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_36_store|entry(9),0, fac_commoners,    [itm_lady_dress_ruby,  itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_37_merchant","Ecne Cellach","{!}Merchant",tf_female|tf_hero|tf_is_merchant, scn_town_37_store|entry(9),0, fac_commoners,    [itm_sarranid_jellaba_white],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x0000000fd4102003216df93d74534d5000000000001d59660000000000000000], #PJ QUEST chief
  ["town_38_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_38_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_39_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_39_store|entry(9),0, fac_commoners,    [itm_khergit_armor, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_40_merchant","Merchant","{!}Merchant",tf_osa|tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_40_store|entry(9),0, fac_commoners,    [itm_lady_dress_ruby,  itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_41_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_41_store|entry(9),0, fac_commoners,    [itm_blue_tunic,         itm_ankle_boots,  itm_veil_g   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_42_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_42_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_ankle_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

  ["salt_mine_merchant","Aeron ap Gareth","Aeron ap Gareth",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_leather_apron, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x0000000ebe0911d166ad8db91390aa09000000000011b6bc0000000000000000],

# Horse Merchants

  ["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_brown_dress,           itm_carbatinae_2_blue,      itm_common_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_sarranid_leather_armor,          itm_ankle_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_armor_c,          itm_ankle_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_4_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_ankle_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_tunic,                itm_wrapping_boots,    itm_black_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_6_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_ankle_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_ankle_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_ankle_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_wrapping_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_brown_dress,          itm_carbatinae_2_blue,      itm_veil_g],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nobleman_outfit,         itm_ankle_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jerkin,      itm_ankle_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_ankle_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_lady_dress_ruby,       itm_carbatinae_2_blue,      itm_veil_g],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_armor_c,         itm_ankle_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jerkin,      itm_ankle_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_leather_armor,        itm_ankle_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_lady_dress_ruby,       itm_carbatinae_2_blue,      itm_veil_g],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_armor_c,         itm_carbatinae_2],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe,      itm_carbatinae_2],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_khergit_armor,        itm_carbatinae_2],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_sarranid_common_dress_b,       itm_carbatinae_2_blue,      itm_veil_g],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_23_horse_merchant","Horse Merchant","{!}Town 23 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_armor_c,          itm_ankle_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_24_horse_merchant","Horse Merchant","{!}Town 24 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_ankle_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_25_horse_merchant","Horse Merchant","{!}Town 25 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_tunic,                itm_wrapping_boots,    itm_black_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_26_horse_merchant","Horse Merchant","{!}Town 26 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_ankle_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_27_horse_merchant","Horse Merchant","{!}Town 27 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_ankle_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_28_horse_merchant","Horse Merchant","{!}Town 28 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_nobleman_outfit,         itm_ankle_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_29_horse_merchant","Horse Merchant","{!}Town 29 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_wrapping_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_30_horse_merchant","Horse Merchant","{!}Town 30 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_brown_dress,          itm_carbatinae_2_blue,      itm_veil_g],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_31_horse_merchant","Horse Merchant","{!}Town 31 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_ankle_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_32_horse_merchant","Horse Merchant","{!}Town 32 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,      itm_ankle_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_33_horse_merchant","Horse Merchant","{!}Town 33 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_courtly_outfit,        itm_ankle_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_34_horse_merchant","Horse Merchant","{!}Town 34 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_lady_dress_ruby,       itm_carbatinae_2_blue,      itm_veil_g],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_35_horse_merchant","Horse Merchant","{!}Town 35 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_armor_c,         itm_ankle_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_36_horse_merchant","Horse Merchant","{!}Town 36 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_blue_tunic,      itm_ankle_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_37_horse_merchant","Horse Merchant","{!}Town 37 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_ankle_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_38_horse_merchant","Horse Merchant","{!}Town 38 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_lady_dress_ruby,       itm_carbatinae_2_blue,      itm_veil_g],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_39_horse_merchant","Horse Merchant","{!}Town 39 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_armor_c,         itm_ankle_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_40_horse_merchant","Horse Merchant","{!}Town 40 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jerkin,      itm_ankle_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_41_horse_merchant","Horse Merchant","{!}Town 41 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_ankle_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_42_horse_merchant","Horse Merchant","{!}Town 42 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_lady_dress_ruby,       itm_carbatinae_2_blue,      itm_veil_g],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],


#Town Mayors    #itm_bluevikingshirt itm_leather_jerkin itm_padded_jack_4_trig itm_padded_jack_4_trig itm_nobleman_outfit itm_rich_outfit
  ["town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_nobleman_outfit, itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_sarranid_leather_armor,     itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_archers_vest,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_4_mayor", "Aelle_the_Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_skirmisher_armor,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,     itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_6_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_sarranid_leather_armor,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_blue_tunic,     itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_8_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_9_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_skirmisher_armor,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_khergit_armor,     itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_skirmisher_armor,     itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nomad_armor,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_khergit_armor,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_skirmisher_armor,     itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_robe,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_leather_armor,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,     itm_carbatinae_2],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,       itm_carbatinae_2], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,    itm_carbatinae_2],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_carbatinae_2],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_23_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_blue_gambeson,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_24_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_robe,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_25_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_skirmisher_armor,     itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_26_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_nomad_armor,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_27_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_blue_tunic,     itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_28_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_sarranid_leather_armor,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_29_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_bluevikingshirt,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_30_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,     itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_31_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,     itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_32_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_tunic,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_33_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_34_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,     itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_35_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,     itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_36_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_robe,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_37_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_38_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_tunic,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_39_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,     itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_40_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_robe,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_41_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_42_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_archers_vest,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],


#Village stores
  ["village_1_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic1, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_2_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_3_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic2, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_4_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic3, itm_ankle_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_5_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_6_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic5, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_7_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_8_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic1, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_9_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_skirmisher_armor, itm_ankle_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic3, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic4, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_skirmisher_armor, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic1, itm_ankle_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic2, itm_ankle_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_ankle_boots, itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic4, itm_ankle_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic5, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_leather_armor, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_28_elder","Godiva_the_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_leather_armor, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_skirmisher_armor, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic_grn, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic_grn, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_37_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_38_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic_grn, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_39_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic_red, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_40_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_41_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic_red, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_42_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_43_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_44_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic_red, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_45_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_skirmisher_armor, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_46_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_47_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_48_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic3, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_49_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_50_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_51_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_52_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic4, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_53_elder","Wigmund_the_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_54_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_55_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_56_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_57_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_nomad_armor, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_58_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_59_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic3, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_60_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_61_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_62_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic4, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_63_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_64_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_65_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_66_elder","Pyr_the_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_67_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_68_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_69_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_khergit_armor, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_70_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_71_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_72_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_73_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_74_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_75_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_76_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_77_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic1, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_78_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_79_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic2, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_80_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_81_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic3, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_82_elder","Aesc_the_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_83_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_leather_armor, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_84_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_85_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_86_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic5, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_87_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_88_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_89_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_khergit_armor, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_90_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_91_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_92_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_93_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_94_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_95_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_nobleman_outfit, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_96_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic1, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_97_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_98_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_99_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic2, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_100_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_padded_cloth, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_101_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_102_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_103_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_104_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_courtly_outfit, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_105_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_106_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_courtly_outfit, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_107_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_108_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_109_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_110_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_111_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic3, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_112_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_113_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_114_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_115_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_ankle_boots, itm_woolen_cap_newwht],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_116_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_courtly_outfit, itm_ankle_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_117_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_118_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_ankle_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_119_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_ankle_boots, itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_120_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_ankle_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_121_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_122_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_123_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_ankle_boots, itm_woolen_cap_newwht],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_124_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_125_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_126_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_127_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_woolen_cap_newwht],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_128_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_129_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_130_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_131_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_132_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_133_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_134_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic2, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_135_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_136_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic1, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_137_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_138_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_139_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_leather_armor, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_140_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_141_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_142_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_143_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_144_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_145_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_146_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_147_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_148_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_149_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_150_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_leather_armor, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_151_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_leather_armor, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_152_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic3, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_153_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic5, itm_ankle_boots, itm_woolen_cap_newwht],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_154_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_155_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic4, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_156_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_157_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_woolen_cap_newwht],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_158_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_159_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic4, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_160_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_161_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_162_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_163_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_ankle_boots, itm_woolen_cap_newwht],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_164_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_165_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_166_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_leather_armor, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_167_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic4, itm_wrapping_boots, itm_woolen_cap_newwht],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_168_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_archers_vest, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_169_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic4, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_170_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_171_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_172_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_archers_vest, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_173_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_ankle_boots, itm_woolen_cap_newwht],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_174_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_175_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_176_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_177_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots, itm_woolen_cap_newwht],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_178_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_179_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_180_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_181_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_182_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_183_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_184_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_ankle_boots,itm_woolen_cap_newred],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_185_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_186_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_187_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_188_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_189_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_190_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_191_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_ankle_boots, itm_woolen_cap_newwht],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_192_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_193_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_194_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_ankle_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_195_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic3, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_196_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic4, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_197_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_198_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic5, itm_wrapping_boots, itm_woolen_cap_newwht],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_199_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic1, itm_ankle_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_200_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_archers_vest, itm_ankle_boots, itm_woolen_cap_newwht],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_201_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic3, itm_ankle_boots, itm_woolen_cap_newwht],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_202_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_archers_vest, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_203_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic4, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_204_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_tunic, itm_ankle_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_205_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_206_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_207_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_208_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_woolen_cap_newwht],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_209_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_archers_vest, itm_ankle_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_210_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_211_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_212_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  #rigale brigand merchant. chief
  ["brigand_hideout_merchant","Bandit merchant", "Bandit merchants",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ###monasterios monje mercader
  ["monje_mercader","Monk merchant", "Monks merchants",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_blue_gambeson, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              sac_face_1, sac_face_2],
  ["especial_merchant","Mystic Merchant","Mystic Merchant",                tf_hero|tf_is_merchant, 0,0, fac_commoners, [itm_coarse_tunic, itm_ankle_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x0000000ebe0911d166ad8db91390aa09000000000011b6bc0000000000000000],

# Place extra merchants before this point
  ["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  #Used for player enterprises
  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_jack_3_trig,     itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,     itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_arena_tunic_white,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_arena_tunic_white,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
  ["town_23_master_craftsman", "{!}Town 23 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_24_master_craftsman", "{!}Town 24 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_jack_3_trig,     itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_25_master_craftsman", "{!}Town 25 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_26_master_craftsman", "{!}Town 26 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_27_master_craftsman", "{!}Town 27 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,     itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_28_master_craftsman", "{!}Town 28 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_29_master_craftsman", "{!}Town 29 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_30_master_craftsman", "{!}Town 30 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_31_master_craftsman", "{!}Town 31 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,     itm_ankle_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_32_master_craftsman", "{!}Town 32 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_33_master_craftsman", "{!}Town 33 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_34_master_craftsman", "{!}Town 34 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_nomad_armor,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_35_master_craftsman", "{!}Town 35 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_36_master_craftsman", "{!}Town 36 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_37_master_craftsman", "{!}Town 37 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_nomad_armor,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_38_master_craftsman", "{!}Town 38 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_39_master_craftsman", "{!}Town 39 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_40_master_craftsman", "{!}Town 40 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_arena_tunic_white,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_41_master_craftsman", "{!}Town 41 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_42_master_craftsman", "{!}Town 42 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_arena_tunic_white,      itm_carbatinae_2_blue],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],


# Chests
  ["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
   [],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_nowa,itm_suttonhooswordking],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_carbatinae_1_greaves_grey,itm_ad_viking_shield_round_15],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_vendel14_2,itm_talak_seax],def_attrib|level(18),wp(60),knows_common, 0],

  ["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],

# These are used as arrays in the scripts. CC chief cambia knows
  ["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ##cc chief acaba
  ["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
  ##   [itm_arrows,itm_nomad_sabre,itm_scimitar,itm_winged_mace,itm_lance,itm_khergit_bow,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_nomad_shield,itm_steppe_horse,itm_warhorse],
  ##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],


# Add Extra Quest NPCs below this point
  ##chief quest###
  [
    "npc17","Neko","Neko",
    tf_oso|tf_hero|tf_unmoveable_in_party_window, scn_town_41_tavern|entry(6),reserved, fac_neko,
    [
      itm_wessex_tunic4,itm_black_cloak,itm_cantabro_shield_2,itm_ankle_boots,itm_new_mace
    ],
    def_attrib3|level(27),wp(190),knows_warrior_elite,
    0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000
  ],

  [
    "npc18","Cado","Cado",
    tf_alto|tf_hero|tf_unmoveable_in_party_window, scn_town_17_tavern|entry(6),reserved, fac_neko,
    [
      itm_ad_viking_byrnie_01,itm_cantabro_shield_1,itm_ankle_boots,itm_new_sword
    ],
    def_attrib3|level(29),wp(260),knows_warrior_elite|knows_wound_treatment_8|knows_first_aid_8|knows_surgery_8,
    0x000000091b0030112723494893b1a91b00000000001d291e0000000000000000
  ], #chief idibil

  [
    "hareck","Cerdic","Cerdic",
    tf_bajo|tf_hero,scn_town_41_tavern|entry(5),reserved,fac_commoners,
    [
      itm_padded_cloth,itm_ankle_boots
    ],
    def_attrib|level(5),wp(20),knows_common,
    0x0000000dc40011490a1bccf7d98db6df00000000001e16f30000000000000000
  ],

  [
    "violet","Aelfwyn","Aelfwyn",
    tf_hero|tf_female|tf_guarantee_boots|tf_guarantee_armor,scn_town_2_tavern|entry(6),reserved,fac_commoners,
    [
      itm_lady_dress_ruby
    ],
    def_attrib|level(2),wp(40),knows_common,
    0x000000018c00b0061d64b5cb5c86468c00000000001c5add0000000000000000
  ],

  [
    "violet2","Lunete","Lunete",
    tf_alta|tf_hero|tf_female|tf_guarantee_boots|tf_guarantee_armor,scn_town_7_tavern|entry(6),reserved,fac_commoners,
    [
      itm_lady_dress_ruby
    ],
    def_attrib|level(2),wp(40),knows_common,
    0x000000019008100166e18d570c59cc5500000000001e45330000000000000000
  ],

  [
    "violet3","Ceara","Ceara",
    tf_baja|tf_hero|tf_female|tf_guarantee_boots|tf_guarantee_armor,scn_town_35_tavern|entry(6),reserved,fac_commoners,
    [
      itm_lady_dress_ruby
    ],
    def_attrib|level(2),wp(40),knows_common,
    0x000000018300900215b4925b4b8ed821000000000015975d0000000000000000
  ],

  [
    "pagano_19","Priest Leofdaeg","Leofdaeg",
    tf_hero|tf_guarantee_armor|tf_guarantee_boots, scn_town_23_castle|entry(11), reserved, fac_kingdom_9,
    [
      itm_goat_cap, itm_sarranid_jellaba_white, itm_bare_legs_blue
    ],
    def_attrib|level(5),wp(20),knows_common,
    0x0000000e5a0ce5d3190889284b6ed6d500000000001e68af0000000000000000
  ],

###chief quest###
  [
    "local_merchant","Local Merchant","Local Merchants",
    tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,
    [
      itm_leather_apron,itm_ankle_boots,itm_butchering_knife
    ],
    def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2
  ],

  [
    "tax_rebel","Peasant Rebel","Peasant Rebels",
    tf_guarantee_armor,0,reserved,fac_commoners,
    [
      itm_staff,itm_knife,itm_pitch_fork,itm_club,itm_stones,itm_leather_cap,
      itm_woolen_cap,itm_woolen_cap_newblu,itm_linen_tunic,itm_coarse_tunic,
      itm_ankle_boots,itm_wrapping_boots
    ],
    def_attrib|level(15),wp(110),knows_common,vaegir_face1, vaegir_face2
  ],

  [
    "trainee_peasant","Peasant","Peasants",
    tf_guarantee_armor,0,reserved,fac_commoners,
    [
      itm_staff,itm_knife,itm_pitch_fork,itm_club,itm_stones,itm_leather_cap,
      itm_woolen_cap,itm_woolen_cap_newblu,itm_linen_tunic,itm_coarse_tunic,
      itm_ankle_boots,itm_wrapping_boots
    ],
    def_attrib|level(15),wp(110),knows_common,vaegir_face1, vaegir_face2
  ],

  [
    "fugitive","Nervous Man","Nervous Men",
    tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_stones,
      itm_ankle_boots,itm_wrapping_boots,
      itm_woolen_cap_newwht,itm_woolen_cap,
      itm_shirt,itm_bl_tunicsr01,itm_shirtb,itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_shirte,itm_fat_body,
      itm_knife,itm_cudgel,itm_stones,itm_club,itm_sickle,itm_hatchet,itm_wooden_stick,itm_hand_axe
    ],
    def_attrib|str_24|agi_25|level(31),wp(220),
    knows_warrior_veteran|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1, man_face_old_2
  ],

#chief bounty empieza
  [
    "fugitive2","Nervous Woman","Nervous Women",
    tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_lady_dress_ruby, itm_lady_dress_green, itm_lady_dress_blue, itm_blue_dress,
      itm_wimple_a, itm_wimple_with_veil, itm_female_hood, itm_knife, itm_spear_2
    ],
    def_attrib2|str_28|agi_25|level(30),wp(220),
    knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1, man_face_old_2
  ],

  ###bounty chief
  [
    "bounty12","Boy","Boy",
    tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_outlaws,
    [
      itm_sniper_crossbow,itm_flintlock_pistol,itm_sniper_crossbow,itm_flintlock_pistol,
      itm_bare_legs_blue,itm_ankle_boots,itm_wrapping_boots,
      itm_woolen_cap_newblu,itm_woolen_cap_newred,itm_woolen_cap_newgrn,itm_woolen_cap_newblk,
      itm_shirt,itm_bl_tunicsr02,itm_shirte,itm_fat_body,
      itm_knife,itm_cudgel,itm_stones,itm_club,itm_sickle
    ],
    def_attrib2|level(17),wp(140),knows_warrior_basic,bandit_face1, bandit_face2
  ],

  [
    "bounty13","Retired Soldier","Retired Soldier",
    tf_guarantee_boots,0,0,fac_outlaws,
    [
      itm_javelin,itm_javelin,itm_shirtc,itm_javelin,itm_javelin,
      itm_carbatinae_1_grey,itm_carbatinae_1_green,
      itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,itm_head_wrappings,itm_common_hood,
      itm_fattiglinenskjortir,itm_wessex_tunic3,itm_bl_tunicsr02,itm_mercia_tunic1,itm_blue_short_tunic,
      itm_spear_6,itm_hunting_dagger,itm_woodenshield_small
    ],
    def_attrib2|level(17),wp(140),knows_warrior_basic,rhodok_face_young_1, rhodok_face_old_2
  ],

  [
    "bounty14","Vagabond","Vagabond",
    tf_guarantee_boots,0,0,fac_outlaws,
    [
      itm_javelin,
      itm_bare_legs_blue,itm_carbatinae_2_bare,
      itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
      itm_shirt,itm_roman_shirt,itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_bl_tunicsr01,itm_shirtb,itm_shirtc,
      itm_donkey_mount,itm_mule,
      itm_knife,itm_cudgel,itm_club,itm_sickle,itm_hand_axe,itm_spear_2
    ],
    def_attrib2|level(17),wp(140),knows_warrior_basic,swadian_face_young_1, swadian_face_old_2
  ],

  [
    "bounty1","Bagauda","Bagaudas",
    tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_outlaws,
    [
      itm_javelin,itm_javelin,itm_javelin,
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
      itm_hood_newblu,itm_black_hood,itm_head_wrappings,itm_common_hood,
      itm_shirt,itm_roman_shirt,itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_bl_tunicsr01,
      itm_shirtb,itm_shirtc,itm_shirtd,itm_shirte,itm_fat_body,
      itm_donkey_mount,itm_mule,
      itm_knife,itm_cudgel,itm_club,itm_sickle,itm_hand_axe,itm_spear_2
    ],
    def_attrib2|level(17),wp(140),knows_warrior_basic,bandit_face1, bandit_face2
  ],

  [
    "bounty3","Spearman","Spearmen",
    tf_guarantee_boots,0,0,fac_outlaws,
    [
      itm_javelin,itm_javelin,itm_shirtc,itm_javelin,itm_javelin,
      itm_carbatinae_1,itm_carbatinae_2,itm_carbatinae_2_green,itm_carbatinae_1_blue,
      itm_head_wrappings,itm_common_hood,itm_turret_hat_blue,itm_turret_hat_green,
      itm_fattiglinenskjortir,itm_wessex_tunic3,itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsleather,
      itm_spear_6,itm_hunting_dagger,itm_woodenshield_small
    ],
    def_attrib2|level(17),wp(140),knows_warrior_basic,rhodok_face_young_1, rhodok_face_old_2
  ],

  [
    "bounty4","Unright","Unrights",
    tf_guarantee_boots,0,0,fac_outlaws,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_arrows,itm_short_bow,itm_hunting_bow,
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
      itm_roman_shirt,itm_peasant_man_d,itm_peasant_man_c,itm_armor_27,itm_armor_26,
      itm_peasant_man_e,itm_peasant_man_f,itm_leather_jerkin,
      itm_hand_axe,itm_hatchet,itm_axe_2
    ],
    def_attrib2|level(17),wp(140),knows_warrior_basic,swadian_face_young_1, swadian_face_old_2
  ],

  [
    "bounty2","Fugitive","Fugitives",
    tf_guarantee_boots|tf_guarantee_shield,0,0,fac_outlaws,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_arrows,itm_short_bow,itm_hunting_bow,
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,itm_ankle_boots,itm_wrapping_boots,
      itm_peasant_archer,itm_roman_shirt,itm_peasant_man_d,itm_peasant_man_c,itm_armor_27,itm_armor_26,itm_peasant_man_e,
      itm_hand_axe,itm_hatchet,itm_axe_2,itm_battle_fork,itm_pitch_fork
    ],
    def_attrib2|level(22),wp(165),knows_warrior_normal,bandit_face1, bandit_face2
  ],

  [
    "bounty5","Frank","Frankish",
    tf_guarantee_boots|tf_guarantee_shield,0,0,fac_outlaws,
    [
      itm_light_throwing_axes,itm_jarid,itm_throwing_axes,itm_throwing_spears3,
      itm_leather_gloves,
      itm_decorated_leather_shoes,itm_carbatinae_2,itm_decorated_leather_shoes_grey,
      itm_vikinglamellar3blue,itm_vikinglamellar2blue,itm_vikinglamellar2red,
      itm_mail_shirt_3,itm_ad_viking_byrnie_01,itm_mamluke_mail,
      itm_spangenhelm_helm,itm_horn_helmet_2,itm_sarranid_helmet1,
      itm_spatha,itm_spear_3,itm_frankish_axe2,itm_vikingaxeb,itm_axe_hammer_long,
      itm_axehammer_1,itm_le_pictishsword2,
      itm_leathershield_medium_d,itm_leathershield_medium
    ],
    def_attrib3|level(27),wp(190),knows_warrior_elite,nord_face_younger_1, nord_face_old_2
  ],

  [
    "bounty6","Nonconformist","Nonconformist",
    tf_guarantee_boots|tf_guarantee_shield,0,0,fac_outlaws,
    [
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
      itm_woolen_cap_newblu,itm_woolen_cap_newwht,itm_woolen_cap,
      itm_shirt,itm_bl_tunicsr01,itm_shirtb,itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_shirte,
      itm_club,itm_sickle,itm_hatchet,itm_wooden_stick,itm_hand_axe
    ],
    def_attrib2|level(23),wp(175),knows_warrior_normal,khergit_face_young_1, khergit_face_old_2
  ],

  [
    "bounty7","Outlaw Warrior","Outlaw Warriors",
    tf_guarantee_boots|tf_guarantee_shield,0,0,fac_outlaws,
    [
      itm_javelin,itm_javelin,itm_javelin,itm_javelin,
      itm_carbatinae_2_orange,
      itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_peasant_archer,itm_armor_26,
      itm_broadsword,itm_hatchet,itm_lance,itm_lance,
      itm_leathershield_medium_y
    ],
    def_attrib2|level(22),wp(165),knows_warrior_normal,vaegir_face_young_1, vaegir_face_old_2
  ],

  [
    "bounty8","Bandit","Bandits",
    tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_outlaws,
    [
      itm_javelin,itm_javelin,itm_javelin,
      itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,itm_ankle_boots,itm_wrapping_boots,
      itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,itm_head_wrappings,itm_common_hood,
      itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_bl_tunicsr01,itm_shirtb,itm_shirtc,itm_shirtd,itm_shirte,itm_fat_body,
      itm_knife,itm_cudgel,itm_club,itm_sickle,itm_hand_axe,itm_spear_2
    ],
    basic_ranged_attrib|str_14|level(17),wp(60)|wp_archery(150),
    knows_warrior_normal|knows_power_draw_2,khergit_face_young_1, khergit_face_old_2
  ],

  [
    "bounty9","Deserter","Deserters",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_black_khergits,
    [
      itm_javelin,itm_javelin,itm_javelin,
      itm_carbatinae_1,itm_carbatinae_2,
      itm_shirt,itm_roman_shirt,itm_fattiglinenskjortir,itm_wessex_tunic3,
      itm_norman_helmet,itm_leather_cap,itm_bowl_helmet,itm_horn_helmet_2,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
      itm_lui_battleaxetwoh,itm_saxon_spear,itm_spear_3,itm_lance,itm_langseax,itm_falchion,itm_spear_3,
      itm_ad_viking_shield_round_40,itm_ad_viking_shield_round_41,itm_ad_viking_shield_round_42,itm_ad_viking_shield_round_43
    ],
    def_attrib3|level(29),wp(200),knows_warrior_elite,bandit_face1, bandit_face2
  ],

  [
    "bounty10","Old Captain","Old Captains",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
    [
      itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
      itm_leather_gloves,itm_leather_gloves,
      itm_carbatinae_1_greaves_blue,itm_decorated_leather_shoes_grey,itm_carbatinae_2_greaves_blue,
      itm_mail_shirt_blk,itm_mail_shirt_whiteaxes,itm_hauberk6,itm_mail_shirt_bluehorses,
      itm_nordic_warlord_helmet,itm_full_helm,itm_spangenhelm_helm,itm_valssword,
      itm_bl_sword01_03,itm_hunting_dagger,itm_war_axe,
      itm_woodenshield_medium_d
    ],
    def_attrib3|level(35),wp(260),knows_warrior_elite|knows_wound_treatment_8|knows_surgery_8,
    0x00000007a6002194125b6db6cb6db6db00000000001db6c30000000000000000, nord_face_old_2
  ],

  [
    "bounty11","Bandit Leader","Bandit Leaders",
    tf_guarantee_boots,0,0,fac_outlaws,
    [
      itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
      itm_carbatinae_2_greaves_green,itm_carbatinae_1_greaves_green,
      itm_mail_shirt_ylw,itm_mail_shirt_blk,itm_mail_shirt_whiteaxes,itm_hauberk6,itm_mail_shirt_bluehorses,
      itm_full_helm,itm_spangenhelm_helm,itm_great_helmet,itm_winged_great_helmet,
      itm_valssword,itm_bl_sword01_03,itm_hunting_dagger,itm_war_axe,
      itm_woodenshield_medium_d
    ],
    def_attrib3|level(30),wp(200),knows_warrior_elite|knows_wound_treatment_8|knows_surgery_8,
    0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2
  ],
  #bounty chief acaba
  #chief bounty termina

  [
    "belligerent_drunk","Belligerent Drunk","Belligerent Drunks",
    tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [
      itm_tunic_with_green_cape,
      itm_fattiglinenskjortir,itm_wessex_tunic3,itm_bl_tunicsr02,itm_mercia_tunic1,
      itm_blue_short_tunic,itm_bl_tunicsleather,
      itm_ankle_boots, itm_carbatinae_2_blue, itm_wrapping_boots,
      itm_head_wrappings, itm_leather_cap, itm_knife
    ],
    def_attrib|str_20|agi_8|level(15),wp(120),
    knows_common|knows_power_strike_2|knows_ironflesh_9,bandit_face1, bandit_face2
  ],

  ["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, #they look like belligerent drunks
   [itm_arena_tunic_white, itm_wrapping_boots, itm_ankle_boots, itm_carbatinae_2_blue, itm_langseax,itm_spear_2,itm_hand_axe,itm_talak_buckler],
   def_attrib|str_20|agi_16|level(30),wp(220),knows_warrior_veteran|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

  ["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_arena_tunic_blue,itm_linen_tunic,itm_coarse_tunic, itm_wrapping_boots, itm_ankle_boots, itm_carbatinae_2_blue, itm_wrapping_boots, itm_head_wrappings, itm_leather_cap, itm_spear_3],
   def_attrib|str_20|agi_16|level(30),wp(220),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],



  ["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_club,itm_leather_jerkin,itm_ankle_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1, man_face_older_2],

  ["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_club_one,itm_leather_jerkin,itm_ankle_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],

#Tempered   chief        rioter added for unrest sabotage mission
  ["rioter","Rioting Peasant","Rioting Peasants",tf_guarantee_armor,no_scene,reserved,fac_outlaws,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],

#TEMPERED chief LOOT WAGON STORAGE TROOPS BEGIN
	["loot_wagon_storage_1","Supply Wagon","Supply Wagon",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["camp_armory","Camp Armory","Camp Armory",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],


   ["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,
    [itm_robe, itm_head_wrappings, itm_wrapping_boots],
    def_attrib|level(4),wp(60),knows_common,woman_face_1, woman_face_2],
  ["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_blue_tunic, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],


##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
  ##   [itm_sword,itm_leather_jerkin,itm_ankle_boots,itm_hunter,itm_leather_gloves],
  ##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
  ##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
  ##   [itm_sword,itm_leather_jerkin,itm_ankle_boots,itm_hunter,itm_leather_gloves],
  ##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
  ##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
  ##   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_woolen_cap_newwht,itm_woolen_cap_newwht,itm_linen_tunic,itm_coarse_tunic,itm_ankle_boots,itm_wrapping_boots],
  ##   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
  ##   [itm_sword,itm_leather_jerkin,itm_ankle_boots, itm_saddle_horse, itm_leather_jerkin, itm_leather_cap],
  ##   def_attrib|level(9),wp(100),knows_common,swadian_face1, swadian_face2],
  ##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
  ##   [itm_knife,itm_dagger,itm_hunting_crossbow,itm_blue_tunic,itm_robe,itm_lady_dress_ruby, itm_veil_g, itm_woolen_hood, itm_wrapping_boots],
  ##   def_attrib|level(3),wp(45),knows_common,refugee_face1,refugee_face2],


  ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_linen_tunic,itm_ankle_boots, itm_splinted_leather_greaves, itm_leather_steppe_cap_b, itm_spear_4,  itm_short_bow, itm_arrows, itm_wooden_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops
  ["swadian_crossbowman_multiplayer_aino","Bonheddwr (Lig. I.)","Bonheddwyr",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
   [itm_throwing_knives,itm_wrapping_boots,itm_common_hood,itm_armor_26,itm_sarranid_two_handed_axe_b,itm_talak_buckler],
   def_attrib2|level(19),wp(140),knows_warrior_basic,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer_aino",  "Pedyt (Med. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
   [itm_javelin,itm_carbatinae_1,itm_hood_newwht,itm_bl_tunic02,itm_scianshort,itm_ad_viking_shield_round_29],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_aino","Uchelwr (Hv. I.)","Uchelwyr",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,
   [itm_throwing_spears,itm_leather_gloves,itm_iron_greaves,itm_bl_tunic10,itm_hasta,itm_ad_viking_shield_round_22],
   def_attrib3|level(27),wp(200),knows_warrior_veteran,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer_aino","Sceotand Seaxe (Missile)","Sceotandas Seaxna",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
   [itm_arrows,itm_short_bow,itm_bare_legs_blue,itm_woolen_cap,itm_bl_tunicsr01,itm_saxon_axe],
   basic_ranged_attrib|level(15),wp(40)|wp_archery(110),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["vaegir_spearman_multiplayer_aino","Geneata Seaxe (Med. I.)","Geneatas Seaxna",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_neutral,
   [itm_javelin,itm_carbatinae_2_orange,itm_woolen_cap_newgrn,itm_wessex_tunic4,itm_falchion,itm_woodenshield_medium_d],
   def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_horseman_multiplayer_aino","Gesith Seaxe (Lig. C.)","Gesithas Seaxna",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_neutral,
   [itm_javelin,itm_normal_horse22,itm_leather_gloves,itm_iron_greaves,itm_mail_shirthre,itm_sarranid_mail_coif,itm_hunting_dagger,itm_woodenshield_medium_d],
   def_attrib3|level(27),wp(200),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],
  ["khergit_dismounted_lancer_multiplayer_aino","Fuidir (Skrm.)","Fuidirs",tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,
   [itm_javelin_jinetes,itm_decorated_leather_shoes_bare,itm_turret_hat_green,itm_war_paint_two_2,itm_scianshort,itm_vae_cuadrado_16],
   def_attrib2|level(19),wp(140)|wp_throwing(170),knows_warrior_normal|knows_ironflesh_4|knows_power_strike_4,khergit_face_young_1, khergit_face_older_4],
  ["khergit_veteran_horse_archer_multiplayer_aino","Eite Fuidir (Elit. Skrm.)","Elite Fuidirs",tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,
   [itm_javelin_jinetes,itm_turret_hat_green,itm_war_paint_two_5,itm_scianlongbone,itm_vae_cuadrado_26],
   def_attrib2|level(25),wp(185)|wp_throwing(230),knows_warrior_veteran|knows_ironflesh_4|knows_power_strike_4,khergit_face_young_1, khergit_face_older_4],
  ["khergit_lancer_multiplayer_aino","Creach Sluagh (Med. I.)","Creach Sluagh",tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,
   [itm_javelin,itm_decorated_leather_shoes_bare,itm_turret_hat_green,itm_picto_gordo1,itm_scianlongbone,itm_vae_h_shield12],
   def_attrib2|level(23),wp(170),knows_warrior_normal|knows_ironflesh_4|knows_power_strike_4,khergit_face_middle_1, khergit_face_older_4],
  ["nord_veteran_multiplayer_aino","Geneata Engle (Med. I.)","Geneatas Engles",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_neutral,
   [itm_javelin,itm_carbatinae_1_orange,itm_woolen_cap,itm_wessex_tunic4,itm_falchion,itm_ad_viking_shield_round_43],
   def_attrib2|level(23),wp(170),knows_warrior_normal,nord_face_young_1, nord_face_old_2],
  ["nord_scout_multiplayer_aino","Gesith Engle (Lig. C.)","Gesithas Engles",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_neutral,
   [itm_javelin,itm_normal_horse30,itm_leather_gloves,itm_carbatinae_2_blue,itm_byrnie,itm_horn_helmet_3,itm_spear_4,itm_woodenshield_medium_d],
   def_attrib3|level(27),wp(200),knows_warrior_veteran,nord_face_young_1, nord_face_old_2],
  ["nord_archer_multiplayer_aino","Sceotand Engle (Missile)","Sceotandas Engles",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
   [itm_arrows,itm_short_bow,itm_wrapping_boots,itm_bl_tunicsr01,itm_axe],
   basic_ranged_attrib|str_10|level(15),wp(40)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_power_throw_1,nord_face_young_1, nord_face_old_2],
  ["rhodok_veteran_crossbowman_multiplayer_aino","Cliarthaire (Med. I.)","Cliarthaires",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_neutral,
   [itm_javelin,itm_decorated_leather_shoes_bare,itm_hood_newwht,itm_vaelicus_tunic_6,itm_club_with_spike_head,itm_vae_escudo_picto13],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_multiplayer_aino","Fian (Skrm.)","Fianna",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_neutral,
   [itm_darts,itm_decorated_leather_shoes_bare,itm_red_cloak_hood,itm_bl_tunic06,itm_vae_thick_coat1,itm_norman_helmet,itm_spear,itm_tarcza_harfa_vae_21],
   def_attrib2|level(23),wp(170)|wp_throwing(200),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_aino","Marcach (Lig. C.)","Marcachs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_neutral,
   [itm_javelin_jinetes,itm_normal_horse15,itm_leather_gloves,itm_decorated_leather_shoes_bare,itm_padded_jack_9_trig,itm_celtycka_iron,itm_sarranid_axe_b,itm_scyld],
   def_attrib3|level(27),wp(200),knows_warrior_veteran,rhodok_face_middle_1, rhodok_face_older_2],
  ["sarranid_infantry_multiplayer_aino","Beadu rinc Jute (Med. I.)","Beadu rincas Jutes",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
   [itm_throwing_spears3,itm_leather_gloves,itm_carbatinae_2_blue,itm_bl_tunic03,itm_sarranid_veiled_helmet,itm_axe_hammer_long,itm_ad_viking_shield_round_09],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],
  ["sarranid_archer_multiplayer_aino","Sceotand Jute (Missile)","Sceotandas Jutes",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
   [itm_arrows,itm_short_bow,itm_ankle_boots,itm_woolen_cap,itm_shirt,itm_frankish_axe2],
   basic_ranged_attrib|str_10|level(15),wp_one_handed(40)|wp_polearm (40) |wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_old_2],
  ["sarranid_horseman_multiplayer_aino","Gesith Jute (Lig. C.)","Gesithas Jutes",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_javelin,itm_normal_horse24,itm_iron_greaves,
    itm_tattered_leather_armor_gr,itm_frisian_helmet_mesh,itm_spear_4,itm_ad_viking_shield_round_09],
   def_attrib3|level(27),wp(200),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],



#Multiplayer troops (they must have the base items only, nothing else)
  ["swadian_crossbowman_multiplayerno","Bonheddwr (Lig. I.)","Bonheddwyr",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
   [itm_throwing_knives,itm_wrapping_boots,itm_common_hood,itm_armor_26,itm_sarranid_two_handed_axe_b,itm_talak_buckler],
   def_attrib_multiplayer|level(19),wpe(90,60,180,90),knows_common|knows_ironflesh_2|knows_athletics_5|knows_shield_5|knows_power_strike_2|knows_riding_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayerno",  "Pedyt (Med. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
   [itm_javelin,itm_carbatinae_1,itm_hood_newwht,itm_bl_tunic02,itm_scianshort,itm_ad_viking_shield_round_29],
   def_attrib_multiplayer|level(20),wpex(105,130,110,40,60,110),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_4|knows_power_throw_2|knows_athletics_6|knows_riding_1,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayerno","Uchelwr (Hv. I.)","Uchelwyr",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,
   [itm_throwing_spears,itm_leather_gloves,itm_iron_greaves,itm_bl_tunic10,itm_hasta,itm_ad_viking_shield_round_22],
   def_attrib_multiplayer|level(20),wp(110),knows_common|knows_riding_5|knows_ironflesh_3|knows_shield_2|knows_power_throw_2|knows_power_strike_3|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],
  #  ["swadian_mounted_crossbowman_multiplayer","Swadian Mounted Crossbowman","Swadian Mounted Crossbowmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
  #   [itm_bolts,itm_light_crossbow,itm_tab_shield_heater_cav_a,itm_bastard_sword_a,
  #    itm_red_shirt,itm_ankle_boots,itm_saddle_horse],
  #   def_attrib_multiplayer|level(20),wp(100)|wp_crossbow(120),knows_common|knows_riding_4|knows_shield_3|knows_ironflesh_3|knows_horse_archery_2|knows_power_strike_3|knows_athletics_2|knows_shield_2,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayerno","Prisoner","Prisoners",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_ankle_boots],
   def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_ironflesh_2|knows_power_draw_6|knows_athletics_4|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayerno","Geneata Seaxe (Med. I.)","Geneatas Seaxna",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_neutral,
   [itm_javelin,itm_carbatinae_2_orange,itm_woolen_cap_newgrn,itm_wessex_tunic4,itm_falchion,itm_woodenshield_medium_d],
   def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_3|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayerno","Gesith Seaxe (Lig. C.)","Gesithas Seaxna",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_neutral,
   [itm_javelin,itm_normal_horse22,itm_leather_gloves,itm_iron_greaves,itm_mail_shirthre,itm_sarranid_mail_coif,itm_hunting_dagger,itm_woodenshield_medium_d],
   def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_veteran_horse_archer_multiplayerno","Fuidir (Skrm.)","Fuidirs",tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,
   [itm_javelin_jinetes,itm_decorated_leather_shoes_bare,itm_turret_hat_green,itm_war_paint_two_2,itm_scianshort,itm_vae_cuadrado_16],
   def_attrib_multiplayer|level(21),wpe(80,150,60,100),knows_riding_6|knows_power_draw_5|knows_shield_2|knows_horse_archery_5|knows_athletics_3,khergit_face_middle_1, khergit_face_older_4],
  ["khergit_lancer_multiplayerno","Eite Fuidir (Elit. Skrm.)","Elite Fuidirs",tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,
   [itm_javelin_jinetes,itm_turret_hat_green,itm_war_paint_two_5,itm_scianlongbone,itm_vae_cuadrado_16],
   def_attrib_multiplayer|str_11|level(15),wpe(90,150,60,80),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1,nord_face_young_1, nord_face_old_2],
  ["khergit_lancer_multiplayer_aino","Creach Sluagh (Med. I.)","Creach Sluagh",tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,
   [itm_javelin,itm_decorated_leather_shoes_bare,itm_turret_hat_green,itm_picto_gordo1,itm_scianlongbone,itm_vae_h_shield12],
   def_attrib_multiplayer|level(21),wp(115),knows_riding_6|knows_ironflesh_3|knows_power_throw_3|knows_shield_2|knows_horse_archery_1|knows_power_strike_2|knows_athletics_5,khergit_face_middle_1, khergit_face_older_4],
  ["nord_archer_multiplayerno","Geneata Engle (Med. I.)","Geneatas Engles",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_neutral,
   [itm_javelin,itm_carbatinae_1_orange,itm_woolen_cap,itm_wessex_tunic4,itm_falchion,itm_ad_viking_shield_round_43],
   def_attrib_multiplayer|str_11|level(15),wpe(90,150,60,80),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_multiplayerno","Gesith Engle (Lig. C.)","Gesithas Engles",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_neutral,
   [itm_javelin,itm_normal_horse30,itm_leather_gloves,itm_carbatinae_2_blue,itm_byrnie,itm_horn_helmet_3,itm_spear_4,itm_woodenshield_medium_d],
   def_attrib_multiplayer|level(24),wpex(110,135,100,40,60,140),knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayerno","Sceotand Engle (Missile)","Sceotandas Engles",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
   [itm_arrows,itm_short_bow,itm_wrapping_boots,itm_bl_tunicsr01,itm_axe],
   def_attrib_multiplayer|level(19),wp(105),knows_riding_6|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
  ["rhodok_veteran_crossbowman_multiplayerno","Cliarthaire (Med. I.)","Cliarthaires",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_neutral,
   [itm_javelin,itm_decorated_leather_shoes_bare,itm_hood_newwht,itm_vaelicus_tunic_6,itm_club_with_spike_head,itm_vae_escudo_picto13],
   def_attrib_multiplayer|level(20),wpe(100,60,180,90),knows_common|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_5|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sergeant_multiplayerno","Fian (Skrm.)","Fianna",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_neutral,
   [itm_darts,itm_decorated_leather_shoes_bare,itm_red_cloak_hood,itm_bl_tunic06,itm_vae_thick_coat1,itm_norman_helmet,itm_spear,itm_tarcza_harfa_vae_21],
   def_attrib_multiplayer|level(20),wpex(110,100,140,30,50,110),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_4|knows_power_throw_1|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayerno","Marcach (Lig. C.)","Marcachs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_neutral,
   [itm_javelin_jinetes,itm_normal_horse15,itm_leather_gloves,itm_decorated_leather_shoes_bare,itm_padded_jack_9_trig,itm_celtycka_iron,itm_sarranid_axe_b,itm_scyld],
   def_attrib_multiplayer|level(20),wp(100),knows_riding_4|knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_power_throw_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["sarranid_archer_multiplayerno","Beadu rinc Jute (Med. I.)","Beadu rincas Jutes",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
   [itm_throwing_spears3,itm_leather_gloves,itm_carbatinae_2_blue,itm_bl_tunic03,itm_sarranid_veiled_helmet,itm_axe_hammer_long,itm_ad_viking_shield_round_09],
   def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_ironflesh_2|knows_power_draw_5|knows_athletics_5|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_footman_multiplayerno","Sceotand Jute (Missile)","Sceotandas Jutes",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
   [itm_arrows,itm_short_bow,itm_ankle_boots,itm_woolen_cap,itm_shirt,itm_frankish_axe2],
   def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_3|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_mamluke_multiplayerno","Gesith Jute (Lig. C.)","Gesithas Jutes",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_javelin,itm_normal_horse24,itm_iron_greaves,
    itm_tattered_leather_armor_gr,itm_frisian_helmet_mesh,itm_spear_4,itm_ad_viking_shield_round_09],
   def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],

  ["multiplayer_endno","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],


  #replacable troop, not used
  ["nurse","Nurse","{!}nurse",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_veil_g ,   itm_wimple_a,    itm_ankle_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  #erase later added to avoid errors
  #fire arrow chief
  ["global_value", "quick_battle_6_player", "quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_ankle_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_ankle_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_ankle_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_ankle_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_ankle_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_ankle_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_ankle_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_ankle_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_ankle_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

###fire arrow chief
    ["fire_arrows",   "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["x_coordinate",  "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["y_coordinate",  "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["z_coordinate",  "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["x_velocity",    "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["y_velocity",    "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["z_velocity",    "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["fire_arrows_tick_count",    "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["object_instance_no",    "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["object_durability", "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["frame_tick_count",  "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["x_frame_position",  "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["y_frame_position",  "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["z_frame_position",  "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["burning_object",    "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["scene_prop_id", "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["ship_colisions",    "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["ship_num_crew", "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["ship_speed",    "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["ship_behavior", "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ["ship_rudder", "Local Merchant","Local Merchant",tf_guarantee_boots, 0,0, fac_commoners,[],def_attrib,0,0, merchant_face_1, merchant_face_2],
  ###fire arrow acaba

  ["quick_battle_troop_1","Neko Cantabrian","Neko Cantabrian", tf_hero,0,0,fac_kingdom_1,
   [itm_javelin,itm_decorated_leather_shoes_bare,itm_hood_newwht,itm_vaelicus_tunic_6,itm_club_with_spike_head,itm_vae_escudo_picto13],
   str_9|agi_15|int_12|cha_12|level(15),wpex(109,33,132,15,32,100),knows_riding_3|knows_athletics_5|knows_shield_3|knows_weapon_master_3|knows_power_throw_3|knows_power_strike_2|knows_ironflesh_3,0x0000000e240070cd598bb02b9556428c00000000001eabce0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_2","Alarico","Alarico", tf_hero,0,0,fac_kingdom_1,
   [itm_javelin,itm_normal_horse24,itm_iron_greaves,
    itm_tattered_leather_armor_gr,itm_frisian_helmet_mesh,itm_spear_4,itm_ad_viking_shield_round_09],
   str_12|agi_14|int_11|cha_18|level(22),wpex(182,113,112,159,82,115),knows_horse_archery_2|knows_riding_3|knows_athletics_4|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_1|knows_power_strike_3|knows_ironflesh_4,0x000000007f004000719b69422165b71300000000001d5d1d0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_3","Eldrid","Eldrid", tf_hero,0,0,fac_kingdom_1,
   [itm_arrows,itm_short_bow,itm_ankle_boots,itm_woolen_cap,itm_shirt,itm_frankish_axe2],
   str_18|agi_16|int_12|cha_11|level(24),wpex(90,152,102,31,33,34),knows_riding_5|knows_athletics_5|knows_shield_3|knows_weapon_master_5|knows_power_strike_6|knows_ironflesh_6,0x000000018000324428db8a431491472400000000001e44a90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_4","Sven","Sven", tf_hero,0,0,fac_kingdom_1,
   [itm_throwing_spears3,itm_leather_gloves,itm_carbatinae_2_blue,itm_bl_tunic03,itm_sarranid_veiled_helmet,itm_axe_hammer_long,itm_ad_viking_shield_round_09],
   str_18|agi_15|int_12|cha_12|level(24),wpex(130,150,130,30,50,90),knows_riding_2|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_throw_3|knows_power_strike_6|knows_ironflesh_6,0x000000081700205434db6df4636db8e400000000001db6e30000000000000000, swadian_face_old_2],
  ["quick_battle_troop_5","Oswald","Oswald", tf_hero,0,0,fac_kingdom_1,
   [itm_javelin_jinetes,itm_normal_horse15,itm_leather_gloves,itm_decorated_leather_shoes_bare,itm_padded_jack_9_trig,itm_celtycka_iron,itm_sarranid_axe_b,itm_scyld],
   str_15|agi_15|int_12|cha_12|level(21),wpex(110,130,110,80,15,110),knows_riding_1|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_draw_2|knows_power_throw_4|knows_power_strike_5|knows_ironflesh_5,0x000000048a00024723134e24cb51c91b00000000001dc6aa0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_6","Uthred","Uthred", tf_hero,0,0,fac_kingdom_1,
   [itm_javelin,itm_normal_horse30,itm_leather_gloves,itm_carbatinae_2_blue,itm_byrnie,itm_horn_helmet_3,itm_spear_4,itm_woodenshield_medium_d],
   str_12|agi_15|int_15|cha_9|level(18),wpex(70,70,100,140,15,100),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_weapon_master_3|knows_power_draw_4|knows_power_throw_3|knows_power_strike_2|knows_ironflesh_2,0x000000089e00444415136e36e34dc8e400000000001d46d90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_7","Artorius","Artorius", tf_hero,0,0,fac_kingdom_1,
   [itm_javelin,itm_carbatinae_1_orange,itm_woolen_cap,itm_wessex_tunic4,itm_falchion,itm_ad_viking_shield_round_43],
   str_12|agi_15|int_15|cha_12|level(21),wpex(100,70,70,30,140,80),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_shield_3|knows_weapon_master_5|knows_power_throw_2|knows_power_strike_4|knows_ironflesh_4,0x0000000e1400659226e34dcaa46e36db00000000001e391b0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_8","Pict woman","Picto woman", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_throwing_spears,itm_leather_gloves,itm_iron_greaves,itm_hasta,itm_ad_viking_shield_round_22],
   str_12|agi_15|int_12|cha_12|level(18),wpex(100,40,100,85,15,130),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_4|knows_power_strike_2|knows_ironflesh_2,0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_9","Cynyn","Cynyn", tf_hero,0,0,fac_kingdom_1,
   [itm_javelin_jinetes,itm_decorated_leather_shoes_bare,itm_turret_hat_green,itm_war_paint_two_2,itm_scianshort,itm_vae_cuadrado_16],
   str_16|agi_21|int_12|cha_14|level(26),wpex(182,113,112,159,82,115),knows_horse_archery_2|knows_riding_2|knows_athletics_7|knows_shield_2|knows_weapon_master_4|knows_power_draw_7|knows_power_throw_3|knows_power_strike_3|knows_ironflesh_4,0x000000000000210536db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_10","Congal","Congal", tf_hero,0,0,fac_kingdom_1,
   [itm_throwing_spears,itm_leather_gloves,itm_iron_greaves,itm_bl_tunic10,itm_hasta,itm_ad_viking_shield_round_22],
   str_13|agi_18|int_15|cha_9|level(18),wpex(126,19,23,149,41,26),knows_horse_archery_6|knows_riding_6|knows_weapon_master_2|knows_power_draw_4|knows_power_throw_1|knows_power_strike_4|knows_ironflesh_1,0x0000000502003001471a6a24dc6594cb00000000001da4840000000000000000, swadian_face_old_2],
  ["quick_battle_troop_11","Oengus","Oengus", tf_hero,0,0,fac_kingdom_1,
   [itm_throwing_knives,itm_wrapping_boots,itm_common_hood,itm_armor_26,itm_sarranid_two_handed_axe_b,itm_talak_buckler],
   str_15|agi_12|int_14|cha_20|level(28),wpex(101,35,136,15,17,19),knows_riding_4|knows_athletics_2|knows_shield_4|knows_weapon_master_4|knows_power_strike_5|knows_ironflesh_5,0x0000000e800015125adb702de3459a9c00000000001ea6d00000000000000000, swadian_face_old_2],
  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_ankle_boots],
   def_attrib|level(1),wp(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_shirt,itm_ankle_boots],
   def_attrib|level(1),wp(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_shirt,itm_ankle_boots],
   def_attrib|level(9),wp(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_ankle_boots],
   def_attrib|level(16),wp(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, vaegir_face_older_2],
  ["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_leather_jerkin,itm_leather_armor_c,itm_ankle_boots,itm_arena_helmet_yellow,itm_norman_helmet,itm_leather_warrior_cap,itm_leather_steppe_cap_c],
   def_attrib|str_12|level(19),wp(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_ankle_boots],
   def_attrib|str_12|level(19),wp(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, vaegir_face_older_2],
  ["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_shirt,itm_sumpter_horse, itm_saddle_horse,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["tutorial_rider_2","Horsewealas","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_shirte,itm_bl_tunicsr01_2,itm_ankle_boots,itm_talak_buckler,itm_sumpter_horse, itm_javelin],
   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1, khergit_face_older_4],
  ["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_leather_jerkin,itm_ankle_boots],
   def_attrib|str_12|level(19),wp(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, vaegir_face_older_2],

#cambiado chief mercants
  ["swadian_merchant", "Merchant", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_18, [itm_knife, itm_shirt, itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, 0x00000001870921d8585376b574d2d891000000000011ac240000000000000000],
  ["vaegir_merchant", "Merchant", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_4, [itm_knife, itm_sarranid_jellaba_blue, itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["khergit_merchant", "Merchant", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_knife, itm_coarse_tunic_red, itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["nord_merchant", "Merchant", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_23, [itm_knife, itm_coarse_tunic5, itm_ankle_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["rhodok_merchant", "Merchant", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_31, [itm_knife, itm_armor_8, itm_carbatinae_2_blue], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["sarranid_merchant", "Merchant", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_28, [itm_knife, itm_armor_9, itm_carbatinae_2], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  [
    "sea_raider_leader","Old Hero","Old Heros",
    tf_alto|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_outlaws,
    [
      itm_javelin,itm_leather_gloves, itm_carbatinae_2_greaves_green,itm_swadian_mail_hauberk,
      itm_dux_ridge_helm_gold, itm_spear_7,itm_saxonsword1,itm_broadsword,itm_shield_round_02
    ],
    def_attrib3|level(60),wp(690),
    knows_ironflesh_10|knows_power_strike_10|knows_power_throw_10|knows_athletics_10|
    knows_shield_10|knows_wound_treatment_3|knows_surgery_8,
    0x00000007a6002194125b6db6cb6db6db00000000001db6c30000000000000000, nord_face_old_2
  ],

  [
    "looter_leader","Bandit Leader","Looters",
    tf_hero|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_outlaws,
    [
      itm_javelin,itm_javelin,itm_javelin,
      itm_leather_gloves,
      itm_carbatinae_1_grey,itm_mail_boots,itm_decorated_leather_shoes_orange,itm_iron_greaves,
      itm_mail_shirt_a_copy,itm_mail_shirt_whiteaxes,itm_hauberk6,itm_mail_shirt_bluehorses,
      itm_spangenhelm_helm,itm_horn_helmet_2,itm_sarranid_helmet1,
      itm_new_sword2,itm_hunting_dagger,itm_war_axe,itm_leathershield_small_d
    ],
    def_attrib3|level(10),wp(100),knows_common|knows_wound_treatment_8|knows_surgery_8,
    0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2
  ],

  [
    "bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",
    tf_hero, 0,0, fac_commoners,[],
    def_attrib|level(2),wp(20),knows_inventory_management_10,0
  ],

  ["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_ankle_boots],
   def_attrib|level(1),wp(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2, 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, mercenary_face_2],

  ["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],
  #####grueso chief empieza#############
  #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
  #-#-#-#Hunting chief Mod begin#-#-#-#
  #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
  ["deer","Deer","Deer",0,no_scene,reserved,fac_neutral, [], def_attrib|level(0),wp(60),0,swadian_face_younger_1, swadian_face_younger_1],
  ["boar","Boar","Boar",0,no_scene,reserved,fac_neutral, [], def_attrib|level(0),wp(80),0,swadian_face_younger_1, swadian_face_younger_1],
  ["wolf","Wolf","Wolf",0,no_scene,reserved,fac_neutral, [], def_attrib|level(0),wp(80),0,swadian_face_younger_1, swadian_face_younger_1],
  ["coat","Goat","Goat",0,no_scene,reserved,fac_neutral, [], def_attrib|level(0),wp(60),0,swadian_face_younger_1, swadian_face_younger_1],
  ["coat_b","Goat","Goat",0,no_scene,reserved,fac_neutral, [], def_attrib|level(0),wp(60),0,swadian_face_younger_1, swadian_face_younger_1],
  ["wilddonkey","Wild Donkey","Wild Donkey",0,no_scene,reserved,fac_neutral, [], def_attrib|level(0),wp(60),0,swadian_face_younger_1, swadian_face_younger_1],
  #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
  #-#-#-#Hunting chief Mod end#-#-#-#
  #-#-#-#-#-#-#-#-#-#-#-#-#-#
  #chief quest character
["antler","Ulcagnus","Ulcagnus",tf_hero|tf_randomize_face, scn_town_7_tavern|entry(3),reserved, fac_commoners,[itm_robe,itm_ankle_boots],def_attrib|level(2),wp(40),knows_common,man_face_younger_1, man_face_older_2],
  ["thyr","Icorigas","Icorigas",tf_hero|tf_unkillable|tf_guarantee_helmet, no_scene,0, fac_arrians,[itm_spatha,itm_blue_gambeson,itm_ad_viking_shield_round_06,itm_ankle_boots,itm_javelin,itm_khergit_guard_helmet],knight_attrib_3|level(32),wp(220),knows_common|knows_riding_3|knows_athletics_3|knows_ironflesh_2|knows_shield_3,0x000000018301a4ca172aab34e54723090000000000066ad90000000000000000],
  ["guardian","Arian","Arians",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_arrians,
   [itm_spear_2,itm_robe,itm_ankle_boots,itm_javelin,itm_ad_viking_shield_round_06],knight_attrib_2|level(30),wp(190),knows_common|knows_riding_1|knows_athletics_3|knows_ironflesh_2|knows_shield_2,man_face_younger_1, man_face_older_2],

#-## Outposts begin chief
 ["fort_walker","Patrol","Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_player_faction,
  [itm_carbatinae_2,itm_decorated_leather_shoes_green,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02],
  def_attrib|level(11),wp(75),knows_common,man_face_young_1, man_face_old_2],
  ["fort_rider","Patrol","Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_player_faction,
   [itm_saddle_horse,itm_ankle_boots,itm_shirt_blk,itm_spear_7,itm_sarranid_axe_b,itm_scianlongbone],
   def_attrib|level(11),wp(75),knows_common|knows_riding_2,man_face_young_1, man_face_old_2],
  ["fort_slave","Slave","Slaves",0,0,0,fac_commoners,
   [itm_shirt],
   def_attrib|level(4),wp(20),knows_common,man_face_young_1, man_face_old_2],

  ["fort_captain","Lair Captain","Lair Captains",tf_hero|tf_allways_fall_dead|tf_no_capture_alive, scn_fort_exterior|entry(11),reserved,  fac_commoners,[itm_mail_shirt_1, itm_ankle_boots],knight_attrib_5|level(40),wp(150),knows_common,0x0000000a1a00200336db6db6db6db6db00000000001db6db0000000000000000, 0x0000000a1a00200336db6db6db6db6db00000000001db6db0000000000000000],
  #-## Outposts end

  ##diplomacy  chief begin
  ["dplmc_chamberlain","Chamberlain Marcus", "Chamberlains",tf_hero|tf_male,0,0,fac_commoners,[itm_leather_armor_c,itm_ankle_boots], def_attrib|level(10), wp(40),knows_inventory_management_10,0x0000000dfc0c238838e571c8d469c91b00000000001e39230000000000000000],

  ["dplmc_constable","Constable Sextus","Constables",tf_hero|tf_male,0,0,fac_commoners,[itm_mail_shirt_1, itm_ankle_boots],
   knight_attrib_4,wp(200),knows_common|knows_trainer_9|knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_athletics_4,0x0000000b4b1015054b1b4d591cba28d300000000001e472b0000000000000000],

  ["dplmc_chancellor","Chancellor Caio","Chancellors",tf_hero|tf_male,0,0,fac_commoners,[itm_robe,itm_ankle_boots],def_attrib|level(10), wp(40),knows_inventory_management_10, 0x00000009a20c21cf491bad28a28628d400000000001e371a0000000000000000],

  ["dplmc_messenger","Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_leather_gloves,itm_leather_gloves,itm_javelin,itm_arabian_horse_b,
    itm_carbatinae_2,itm_decorated_leather_shoes_green,
    itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,
    itm_spear_7,itm_sarranid_axe_b,itm_scianlongbone,itm_broadsword,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,swadian_face_young_1, swadian_face_old_2],

  ["dplmc_scout","Scout","Scouts",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_leather_gloves,itm_leather_gloves,itm_javelin,itm_arabian_horse_b,
    itm_carbatinae_2,itm_decorated_leather_shoes_green,
    itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,
    itm_spear_7,itm_sarranid_axe_b,itm_scianlongbone,itm_broadsword,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,man_face_young_1,man_face_old_2],

# recruiter kit begin
  ["dplmc_recruiter","Recruiter","Recruiter",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_spatha,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,swadian_face_young_1, swadian_face_old_2],
  # recruiter kit end
  ##diplomacy chief end
  #Otros chief
      ["bishop","Bishop","Bishop",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
       [itm_staff,itm_red_gambeson,itm_wrapping_boots,itm_mule],
       def_attrib|level(9),wp(50),knows_common|knows_riding_2|knows_ironflesh_1,sac_face_young_1, sac_face_older_2],
  ["iniau","Iniau","Iniau",tf_alto|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_spatha,itm_spear_2,itm_ad_viking_shield_round_01,itm_javelin,itm_javelin,itm_sarranid_helmet1,itm_byrnie,itm_ankle_boots, itm_iniauhorn],
   def_attrib3|level(31),wp(220),knows_warrior_elite|knows_wound_treatment_8|knows_surgery_8,0x00000007a6002194125b6db6cb6db6db00000000001db6c30000000000000000, nord_face_old_2],

## bandit heroes chief commander usados para otras cosas ahora.
  ["mountain_bandit_hero","Old Hero","Old Hero",tf_oso|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_outlaws,
   [itm_throwing_spears,itm_tab_shield_round_c,itm_saxonsword,itm_hunting_dagger,
    itm_vaegir_war_helmet,itm_decorated_leather_shoes_greaves_orange,itm_mail_shirt_8],
   def_attrib|level(42),wp(380),knows_common|knows_power_strike_2|knows_power_draw_4|knows_tactics_4|knows_leadership_4,rhodok_face_young_1, rhodok_face_old_2],
  ["forest_bandit_hero","Druid","Druid",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,
   [itm_sarranid_jellaba_white,itm_ankle_boots],
   def_attrib|level(22),wp(180),knows_common|knows_power_strike_3|knows_power_draw_6|knows_tactics_4|knows_leadership_4,0x0000000ff908935328e3b5289b572d2c00000000001e37730000000000000000],
  ["sea_raider_hero","Old Roman","Old Roman",tf_hero|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,
   [itm_armor_8,itm_ankle_boots,itm_hunting_dagger],
   def_attrib|level(32),wp(220),knows_ironflesh_4|knows_power_strike_4|knows_power_draw_6|knows_power_throw_4|knows_riding_2|knows_athletics_4|knows_tactics_6|knows_leadership_6,0x0000000fe800328f4462195373492aa900000000001dd8cb0000000000000000],
  ["sea_raider_hero2","{!}Captain Hero","{!}Sea Raiders",tf_hero|tf_randomize_face,0,0,fac_outlaws,
   [itm_throwing_spears3,itm_throwing_spears3,itm_throwing_spears4,
    itm_decorated_leather_shoes_blue,itm_carbatinae_2_blue,
    itm_ad_viking_byrnie_02,itm_ad_viking_byrnie_03,itm_ad_viking_byrnie_06,itm_mail_shirt_9_trig,itm_mail_shirt_2_trig,
    itm_nordic_huscarl_helmet,itm_kettle_hat,itm_briton_helm,itm_gaul_helmet,itm_vendel14,itm_spangenhelm_a_trim,
    itm_ornate_seax,itm_frankish_axe2,itm_battle_axe,itm_war_axe,itm_saxonsword,itm_le_richsword1,
    itm_saxon_adorno_12,itm_saxon_adorno_13],
   def_attrib|level(32),wp(220),knows_ironflesh_4|knows_power_strike_4|knows_power_draw_6|knows_power_throw_4|knows_riding_2|knows_athletics_4|knows_tactics_6|knows_leadership_6,nord_face_young_1, nord_face_old_2],
  ["desert_bandit_hero","Bandit King","Bandits Kings",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_outlaws,
   [itm_throwing_spears,itm_suttonhoosword2,itm_hunting_dagger, itm_norman_helmet,
    itm_leather_gloves,
    itm_decorated_leather_shoes_green,itm_decorated_leather_shoes_blue,itm_ad_viking_byrnie_03,itm_ad_viking_byrnie_04,itm_ad_viking_byrnie_05,
    itm_saxon_adorno_6,itm_saxon_adorno_7,itm_saxon_adorno_8,itm_saxon_adorno_9],
   def_attrib3|level(40),wp(300),knows_warrior_elite|knows_riding_8|knows_horse_archery_6|knows_power_strike_9|knows_power_draw_9|knows_tactics_5|knows_leadership_5,khergit_face_young_1, khergit_face_old_2],
  ## CC
  #######grueso chief acaba
  #nuevas quest chief
  ["oim_trakai_ksendz", "Priest","Peasant Rebels",tf_guarantee_armor|tf_guarantee_boots,scn_castle_40_interior|entry(1),reserved,fac_commoners,
   [itm_ankle_boots, itm_robe],
   def_attrib|level(15),wp(90),knows_common, bandit_face1, bandit_face2],
  #Exa's OSP
  #Port in Scenes - Troop
["port_keeper", "Shipwright", "Shipwrights", tf_male|tf_hero|tf_is_merchant, 0, reserved, fac_neutral, [itm_carbatinae_2,itm_decorated_leather_shoes_green,
                                                                                                        itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02], def_attrib|level(2), wp(20), knows_common,swadian_face_younger_1,swadian_face_middle_2],
  ["port_recruiter", "Sea Raider Captain", "SR Captains", tf_hero, 0, reserved, fac_neutral,
   [itm_throwing_spears3,itm_throwing_spears3,
    itm_decorated_leather_shoes_blue,itm_carbatinae_2_blue,itm_ad_viking_byrnie_03,itm_ad_viking_byrnie_06,itm_mail_shirt_9_trig,
    itm_nordic_huscarl_helmet,itm_kettle_hat,itm_vendel14,itm_spangenhelm_a_trim,
    itm_ornate_seax,itm_war_axe,itm_saxonsword,itm_le_richsword1,itm_saxon_adorno_12,itm_saxon_adorno_13],
   def_attrib|level(24), wp(110), knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2, bandit_face1, bandit_face2 ],
  ["port_slave_trader", "Slave Trader", "Slave Traders", tf_hero|tf_randomize_face, 0, reserved, fac_commoners, [itm_leather_jerkin,itm_leather_boots], def_attrib|level(5), wp(20), knows_common,swadian_face_younger_1,swadian_face_middle_2],

#Multiplayer ai troops
  #centware
  ["sarranid_infantry_multiplayer_ai","Beadu rinc Jute (Hv. I.)","Beadu rincas Jutes",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_1,
   [itm_throwing_spears3,itm_throwing_spears4,itm_javelin,itm_jarid,itm_javelin,
    itm_carbatinae_1_grey,itm_carbatinae_1_green,itm_carbatinae_2_orange,
    itm_piel_coat02,itm_piel_coat07,itm_bl_boar_fur,
    itm_bl_tunic03,itm_bluevikingshirt,itm_redvikingshirt,itm_redtunic,itm_bl_tunic03,
    itm_leather_armor_c2,itm_leather_armor_c,itm_vae_thick_coat2,itm_vae_thick_coat3,itm_tattered_leather_armor_gr,itm_padded_leather_blue,
    itm_rathos_bowl_helmet,itm_bowl_helmet,itm_sarranid_helmet1,itm_horn_helmet_3,itm_rathos_spangenhelm_b_light,itm_sarranid_veiled_helmet,
    itm_talak_seax,itm_spear_3,itm_axehammer_2,itm_axehammer_1,
    itm_ad_viking_shield_round_02,itm_ad_viking_shield_round_03,itm_ad_viking_shield_round_04,itm_ad_viking_shield_round_05,itm_ad_viking_shield_round_06,itm_ad_viking_shield_round_07,itm_ad_viking_shield_round_08],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,vaegir_face_middle_1, vaegir_face_older_2],
  ["sarranid_archer_multiplayer_ai","Sceotand Jute (Missile)","Sceotandas Jutes",tf_guarantee_ranged|tf_guarantee_boots,0,0,fac_kingdom_1,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_short_bow,itm_hunting_bow,
    itm_carbatinae_1_bare,itm_ankle_boots,itm_wrapping_boots,
    itm_woolen_cap_newblk,itm_woolen_cap_newwht,itm_woolen_cap,
    itm_shirt,itm_roman_shirt,itm_woolen_hood,itm_bl_tunicsr01_2,itm_leather_steppe_cap_a,itm_mercia_tunic1,itm_blue_short_tunic,
    itm_cudgel,itm_dagger,itm_frankish_axe2],
   basic_ranged_attrib|str_10|level(17),wp_one_handed(45)|wp_polearm (45) |wp_archery(125),knows_ironflesh_1|knows_power_draw_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_old_2],
  ["sarranid_frank_multiplayer_ai","Frank","Frankish",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_light_throwing_axes,itm_jarid,itm_throwing_axes,itm_throwing_spears3,itm_javelin,itm_throwing_spears4,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_green,
    itm_vikinglamellar3red,itm_vikinglamellar3green,itm_vikinglamellar3blue,itm_mail_shirt_3,itm_ad_viking_byrnie_01,itm_mamluke_mail,itm_hauberk_a_new,itm_mail_shirt_brown,
    itm_rathos_spangenhelm_b,itm_rathos_spangenhelm_a_yellow2,itm_norman_helmet,itm_padded_coif,itm_arming_cap,itm_steppe_cap,
    itm_spatha,itm_spear_3,itm_frankish_axe2,itm_vikingaxeb,itm_axehammer_1,itm_le_pictishsword2,
    itm_leathershield_medium_d,itm_leathershield_medium],
   def_attrib3|level(28),wp(210),knows_warrior_elite|knows_athletics_3,nord_face_younger_1, nord_face_old_2],
  ["sarranid_horseman_multiplayer_ai","Gesith Jute (C.)","Gesithas Jutes",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_normal_horse30,itm_saddle_horse,itm_steppe_horse,itm_charger,itm_normal_horse21,itm_normal_horse22,itm_normal_horse27,
    itm_leather_gloves,
    itm_mail_boots,itm_decorated_leather_shoes_orange,
    itm_bl_tunic03,itm_bluevikingshirt,itm_redvikingshirt,itm_redtunic,itm_bl_tunic03,
    itm_padded_leather_brown,itm_leather_armor_c,itm_byrnie,itm_mail_shirthre,itm_mail_shirtredwhite,
    itm_nordic_fighter_helmet,itm_nordic_footman_helmet,itm_nordic_veteran_archer_helmet,itm_vendel14,itm_horn_helmet_3,itm_vendel14_2,
    itm_hunting_dagger,itm_axe_hammer_long,itm_spear_8,itm_spear_4,
    itm_saxon_adorno_14,itm_saxon_adorno_15,itm_tab_shield_small_round_c],
   def_attrib3|level(23),wp(160),knows_warrior_normal|knows_athletics_3,vaegir_face_middle_1, vaegir_face_older_2],
  ###
  ["vaegir_archer_multiplayer_ai","Sceotand Seaxe (Missile)","Sceotandas Seaxna",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_2,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_short_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_ankle_boots,itm_wrapping_boots,
    itm_woolen_cap_newblu,itm_woolen_cap_newred,itm_woolen_cap_newgrn,itm_woolen_cap,
    itm_shirt,itm_roman_shirt,itm_fattiglinenskjortir,itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_mercia_tunic1,itm_bl_tunicsr01,
    itm_cudgel,itm_dagger,itm_saxon_axe],
   basic_ranged_attrib|level(17),wp(45)|wp_archery(125),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["vaegir_spearman_multiplayer_ai","Beadu rinc Seaxe (Hv. I.)","Beadu rincas Seaxna",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_2,
   [itm_throwing_spears3,itm_javelin,itm_throwing_spears4,
    itm_leather_gloves,itm_carbatinae_2,itm_carbatinae_2_green,
    itm_piel_coat01,itm_piel_coat03,itm_piel_coat06,
    itm_bl_tunic03,itm_bluevikingshirt,itm_redvikingshirt,itm_leather_armor_c2,itm_leather_armor_c,itm_padded_leather_brown,itm_vae_thick_coat3,
    itm_sarranid_helmet1,itm_horn_helmet_3,itm_rathos_bowl_helmet,itm_rathos_spangenhelm_b_light,
    itm_langseax,itm_spear_3,itm_lui_waronehandedaxec,itm_axe_2,itm_lui_battleaxetwoh,
    itm_ad_viking_shield_round_13,itm_ad_viking_shield_round_16,itm_ad_viking_shield_round_17,itm_ad_viking_shield_round_18,itm_ad_viking_shield_round_19,itm_ad_viking_shield_round_20,itm_ad_viking_shield_round_21],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer_ai","Ridwiga Seaxe (El. I.)","Ridwigas Seaxna",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
    itm_leather_gloves,
    itm_decorated_leather_shoes,itm_carbatinae_2,itm_decorated_leather_shoes_green,
    itm_tattered_leather_armor_red,itm_tattered_leather_armor_blk,itm_ad_viking_byrnie_01,itm_ad_viking_byrnie_05,itm_ad_viking_byrnie_06,itm_mail_shirt_2_trig,itm_mail_shirt_3_trig,
    itm_rathos_spangenhelm_yellow_plum,itm_rathos_spangenhelm_a,itm_nordic_huscarl_helmet,itm_kettle_hat,itm_briton_helm,itm_gaul_helmet,itm_vendel14,
    itm_ornate_seax,itm_frankish_axe2,itm_battle_axe,itm_war_axe,itm_saxonsword,itm_le_richsword1,
    itm_norman_shield_3,itm_saxon_adorno_8,itm_saxon_adorno_9,itm_saxon_adorno_10,itm_saxon_adorno_11,itm_saxon_adorno_12,itm_saxon_adorno_13],
   def_attrib3|level(28),wp(210),knows_warrior_veteran|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_gesith_multiplayer_ai","Gesith Seaxe (Lig. C.)","Gesithas Seaxna",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_javelin,itm_javelin,
    itm_normal_horse30,itm_saddle_horse,itm_normal_horse21,itm_normal_horse22,itm_normal_horse27,itm_normal_horse24,itm_normal_horse25,itm_normal_horse26,
    itm_carbatinae_2_blue,itm_decorated_leather_shoes_grey,itm_mail_boots,itm_decorated_leather_shoes_orange,
    itm_bl_tunic03,itm_bluevikingshirt,itm_redvikingshirt,itm_redtunic,itm_bl_tunic03,
    itm_tattered_leather_armor_gr,itm_padded_leather_blue,itm_mail_shirthre,itm_mail_shirt_1_trig,
    itm_rathos_spangenhelm_b,itm_nordic_fighter_helmet,itm_spangenhelm_helm,itm_rathos_spangenhelm_a_yellow2,itm_horn_helmet_2,itm_horn_helmet,itm_horn_helmet_3,
    itm_hunting_dagger,itm_axehammer_2,itm_spear_8,itm_spear_4,itm_saxonsword,itm_le_richsword1,
    itm_saxon_adorno_6,itm_saxon_adorno_7,itm_tab_shield_small_round_c],
   def_attrib3|level(23),wp(160),knows_warrior_normal|knows_athletics_3,vaegir_face_middle_1, vaegir_face_older_2],
  ####
  ["vaegir_archer_multiplayer_ai2","Sceotand Seaxe (Missile)","Sceotandas Seaxna",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_3,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_short_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_ankle_boots,itm_wrapping_boots,
    itm_woolen_cap_newblu,itm_woolen_cap_newred,itm_woolen_cap_newgrn,itm_woolen_cap,
    itm_shirt,itm_roman_shirt,itm_fattiglinenskjortir,itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_mercia_tunic1,itm_bl_tunicsr01,
    itm_cudgel,itm_dagger,itm_saxon_axe],
   basic_ranged_attrib|level(17),wp(45)|wp_archery(125),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["vaegir_spearman_multiplayer_ai2","Beadu rinc Seaxe (Hv. I.)","Beadu rincas Seaxna",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_3,
   [itm_throwing_spears3,itm_javelin,itm_throwing_spears4,
    itm_leather_gloves,itm_carbatinae_2,itm_carbatinae_2_green,
    itm_piel_coat01,itm_piel_coat03,itm_piel_coat06,
    itm_bl_tunic03,itm_bluevikingshirt,itm_redvikingshirt,itm_leather_armor_c2,itm_leather_armor_c,itm_padded_leather_brown,itm_vae_thick_coat3,
    itm_sarranid_helmet1,itm_horn_helmet_3,itm_rathos_bowl_helmet,itm_rathos_spangenhelm_b_light,
    itm_langseax,itm_spear_3,itm_lui_waronehandedaxec,itm_axe_2,itm_lui_battleaxetwoh,
    itm_ad_viking_shield_round_13,itm_ad_viking_shield_round_16,itm_ad_viking_shield_round_17,itm_ad_viking_shield_round_18,itm_ad_viking_shield_round_19,itm_ad_viking_shield_round_20,itm_ad_viking_shield_round_21],
   def_attrib3|level(27),wp(185),knows_warrior_veteran|knows_athletics_4,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer_ai2","Ridwiga Seaxe (El. I.)","Ridwigas Seaxna",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
    itm_leather_gloves,
    itm_decorated_leather_shoes,itm_carbatinae_2,itm_decorated_leather_shoes_green,
    itm_tattered_leather_armor_red,itm_tattered_leather_armor_blk,itm_ad_viking_byrnie_01,itm_ad_viking_byrnie_05,itm_ad_viking_byrnie_06,itm_mail_shirt_2_trig,itm_mail_shirt_3_trig,
    itm_rathos_spangenhelm_yellow_plum,itm_rathos_spangenhelm_a,itm_nordic_huscarl_helmet,itm_kettle_hat,itm_briton_helm,itm_gaul_helmet,itm_vendel14,
    itm_ornate_seax,itm_frankish_axe2,itm_battle_axe,itm_war_axe,itm_saxonsword,itm_le_richsword1,
    itm_norman_shield_3,itm_saxon_adorno_8,itm_saxon_adorno_9,itm_saxon_adorno_10,itm_saxon_adorno_11,itm_saxon_adorno_12,itm_saxon_adorno_13],
   def_attrib3|level(28),wp(210),knows_warrior_veteran|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_gesith_multiplayer_ai2","Gesith Seaxe (Lig. C.)","Gesithas Seaxna",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_javelin,itm_javelin,
    itm_normal_horse30,itm_saddle_horse,itm_normal_horse21,itm_normal_horse22,itm_normal_horse27,itm_normal_horse24,itm_normal_horse25,itm_normal_horse26,
    itm_carbatinae_2_blue,itm_decorated_leather_shoes_grey,itm_mail_boots,itm_decorated_leather_shoes_orange,
    itm_bl_tunic03,itm_bluevikingshirt,itm_redvikingshirt,itm_leather_armor_c2,itm_leather_armor_c,itm_padded_leather_brown,itm_vae_thick_coat3,
    itm_padded_leather_blue,itm_byrnie,itm_mail_shirtredwhite,itm_mail_shirt_1_trig,
    itm_rathos_spangenhelm_b,itm_nordic_fighter_helmet,itm_spangenhelm_helm,itm_rathos_spangenhelm_a_yellow2,itm_horn_helmet_2,itm_horn_helmet,itm_horn_helmet_3,
    itm_hunting_dagger,itm_axehammer_2,itm_spear_8,itm_spear_4,itm_saxonsword,itm_le_richsword1,
    itm_saxon_adorno_6,itm_saxon_adorno_7,itm_tab_shield_small_round_c],
   def_attrib3|level(23),wp(160),knows_warrior_normal|knows_athletics_3,vaegir_face_middle_1, vaegir_face_older_2],
  ####
  ["nord_veteran_multiplayer_ai","Beadu rinc Engle (Med. I.)","Beadu rincas Engles",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_4,
   [itm_throwing_spears3,itm_javelin,itm_throwing_spears4,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_2_grey,
    itm_piel_coat01,itm_piel_coat03,itm_bl_boar_fur,
    itm_bl_tunic03,itm_redvikingshirt,itm_redtunic,itm_bl_tunic03,itm_leather_armor_c2,itm_leather_armor_c,itm_vae_thick_coat2,itm_vae_thick_coat3,itm_tattered_leather_armor_gr,
    itm_rathos_bowl_helmet,itm_bowl_helmet,itm_sarranid_helmet1,itm_horn_helmet_3,itm_khergit_cavalry_helmet,
    itm_dagger,itm_saxon_axe,itm_axe,itm_spear_3,itm_spear_2,itm_lui_battleaxetwoh,
    itm_ad_viking_shield_round_31,itm_ad_viking_shield_round_32,itm_ad_viking_shield_round_43,itm_ad_viking_shield_round_34,itm_ad_viking_shield_round_36,itm_ad_viking_shield_round_37,itm_ad_viking_shield_round_38,itm_ad_viking_shield_round_39],
   def_attrib3|level(25),wp(180),knows_warrior_normal|knows_athletics_4,nord_face_young_1, nord_face_old_2],
  ["nord_scout_multiplayer_ai","Rigwiga Engle (Hv. I.)","Ridwigas Engles",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_4,
   [itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
    itm_leather_gloves,itm_decorated_leather_shoes_grey,itm_iron_greaves,
    itm_tattered_leather_armor_ylw,itm_padded_leather_blue,itm_ad_viking_byrnie_02,itm_ad_viking_byrnie_04,itm_ad_viking_byrnie_06,itm_mail_shirt_9_trig,itm_mail_shirt_2_trig,
    itm_horn_helmet,itm_horn_helmet_2,itm_spangenhelm_helm,itm_vaegir_war_helmet,itm_briton_helm4,itm_briton_helm3,itm_nordic_veteran_archer_helmet,itm_footman_helmet,
    itm_scimitar,itm_new_sword3,itm_le_pictishsword3,itm_saxonsword,itm_le_richsword1,
    itm_ad_viking_shield_round_15,itm_ad_viking_shield_round_30,itm_saxon_adorno_20,itm_saxon_adorno_1,itm_saxon_adorno_2,itm_saxon_adorno_3,itm_saxon_adorno_4,itm_saxon_adorno_5],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  ["nord_archer_multiplayer_ai","Sceotand Engle (Missile)","Sceotandas Engles",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_4,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_short_bow,itm_hunting_bow,
    itm_ankle_boots,itm_wrapping_boots,
    itm_leather_steppe_cap_a,itm_roman_shirt,itm_fattiglinenskjortir,itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsr01,
    itm_cudgel,itm_dagger,itm_axe],
   basic_ranged_attrib|str_10|level(15),wp(45)|wp_archery(125),knows_ironflesh_1|knows_power_draw_2|knows_power_throw_1,nord_face_young_1, nord_face_old_2],
  ["sarranid_dena_multiplayer_ai","Dena Mercenary (El. I.)","Dena",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_4,
   [itm_throwing_spears3,itm_throwing_spears3,itm_throwing_spears4,itm_throwing_spears3,
    itm_leather_gloves,
    itm_carbatinae_1_grey,itm_mail_boots,itm_iron_greaves,
    itm_mail_shirt_ylw,itm_mail_shirt_blk,itm_mail_shirt_wht,itm_mail_shirt_grn,itm_hauberk_a_new,itm_mail_shirt_whiteaxes,
    itm_nordic_veteran_archer_helmet,itm_rus_helmet_a,itm_kettle_hat,itm_sarranid_mail_coif,itm_nordic_huscarl_helmet,itm_flat_topped_helmet,itm_footman_helmet,
    itm_bl_sword01_02,itm_hunting_dagger,itm_lui_waronehandedaxec,itm_war_axe,itm_spear_1,itm_spear_2,
    itm_leathershield_medium_b,itm_leathershield_small_b],
   def_attrib3|level(28),wp(210),knows_warrior_elite|knows_athletics_3,bandit_face1, bandit_face2],
  ###
  ["vaegir_archer_multiplayer_ai3","Sceotand Seaxe (Missile)","Sceotandas Seaxna",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_5,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_short_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_ankle_boots,itm_wrapping_boots,
    itm_woolen_cap_newblu,itm_woolen_cap_newred,itm_woolen_cap_newgrn,itm_woolen_cap,
    itm_shirt,itm_roman_shirt,itm_fattiglinenskjortir,itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_mercia_tunic1,itm_bl_tunicsr01,
    itm_cudgel,itm_dagger,itm_saxon_axe],
   basic_ranged_attrib|level(17),wp(45)|wp_archery(125),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["vaegir_spearman_multiplayer_ai3","Fresena (Lig. I.)","Frisen",tf_guarantee_armor,no_scene,reserved,fac_kingdom_5,
   [itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,itm_stones,itm_sniper_crossbow,itm_flintlock_pistol,
    itm_ankle_boots,itm_wrapping_boots,
    itm_woolen_cap_newgrn,itm_woolen_cap_newblk,itm_woolen_cap_newwht,itm_woolen_cap,
    itm_shirt,itm_roman_shirt,itm_bl_tunicsr02,itm_bl_tunicsr01,itm_shirtb,itm_shirtc,itm_shirtd,itm_shirte,itm_fat_body,
    itm_knife,itm_pitch_fork,itm_cudgel,itm_quarter_staff,itm_sickle,itm_wooden_stick],
   def_attrib|level(27),wp(200),knows_warrior_veteran,nord_face_young_1, nord_face_older_2],
  ["vaegir_horseman_multiplayer_ai3","Ridwiga Seaxe (El. I.)","Ridwigas Seaxna",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
    itm_leather_gloves,
    itm_decorated_leather_shoes,itm_carbatinae_2,itm_decorated_leather_shoes_green,
    itm_tattered_leather_armor_red,itm_tattered_leather_armor_blk,itm_ad_viking_byrnie_01,itm_ad_viking_byrnie_05,itm_ad_viking_byrnie_06,itm_mail_shirt_2_trig,itm_mail_shirt_3_trig,
    itm_rathos_spangenhelm_yellow_plum,itm_rathos_spangenhelm_a,itm_nordic_huscarl_helmet,itm_kettle_hat,itm_briton_helm,itm_gaul_helmet,itm_vendel14,
    itm_ornate_seax,itm_frankish_axe2,itm_battle_axe,itm_war_axe,itm_saxonsword,itm_le_richsword1,
    itm_norman_shield_3,itm_saxon_adorno_8,itm_saxon_adorno_9,itm_saxon_adorno_10,itm_saxon_adorno_11,itm_saxon_adorno_12,itm_saxon_adorno_13],
   def_attrib3|level(28),wp(210),knows_warrior_veteran|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_gesith_multiplayer_ai3","Gesith Seaxe (Lig. C.)","Gesithas Seaxna",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_javelin,itm_javelin,
    itm_normal_horse30,itm_saddle_horse,itm_normal_horse21,itm_normal_horse22,itm_normal_horse27,itm_normal_horse24,itm_normal_horse25,itm_normal_horse26,
    itm_carbatinae_2_blue,itm_decorated_leather_shoes_grey,itm_mail_boots,itm_decorated_leather_shoes_orange,
    itm_bl_tunicsr02,itm_bl_tunicsr01,itm_shirtb,itm_shirtc,itm_shirtd,itm_shirte,itm_fat_body,
    itm_padded_leather_blue,itm_tattered_leather_armor_red,itm_mail_shirtredwhite,itm_mail_shirt_1_trig,
    itm_rathos_spangenhelm_b,itm_nordic_fighter_helmet,itm_spangenhelm_helm,itm_rathos_spangenhelm_a_yellow2,itm_horn_helmet_2,itm_horn_helmet,itm_horn_helmet_3,
    itm_hunting_dagger,itm_axehammer_2,itm_spear_8,itm_spear_4,itm_saxonsword,itm_le_richsword1,
    itm_saxon_adorno_6,itm_saxon_adorno_7,itm_tab_shield_small_round_c],
   def_attrib3|level(23),wp(170),knows_warrior_normal|knows_athletics_3,vaegir_face_middle_1, vaegir_face_older_2],
  ####
  ["swadian_crossbowman_multiplayer_ai","Saethydd (Missile)","Saethydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(200),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["gwrdas_multiplayer_ai","Gwrda (Skrm.)","Gwrdas",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,itm_white_cloak,itm_irishcloak,itm_piel_coat07,
    itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_vae_thick_coat2,itm_vae_thick_coat3,
    itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
    itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],
  ####
  ["swadian_crossbowman_multiplayer_ai2","Saethydd (Missile)","Saethydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_7,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(200),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai2","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_7,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai2","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["gwrdas_multiplayer_ai2","Gwrda (Skrm.)","Gwrdas",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,itm_white_cloak,itm_irishcloak,itm_piel_coat07,
    itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_vae_thick_coat2,itm_vae_thick_coat3,
    itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
    itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],
  ##########
  ["swadian_crossbowman_multiplayer_ai3","Bweydd (Missile)","Bweydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(17),wp(45)|wp_archery(125),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai3","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_normal|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai3","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_8,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["cantaber_iuventus_multiplayer_ai","Cantaber Iuventus","Cantaber Iuventi",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_ranged,no_scene,reserved,fac_kingdom_8,
   [itm_javelin,
    itm_turret_hat_blue,itm_turret_hat_green,itm_bare_legs_blue,itm_carbatinae_2_bare,
    itm_roman_shirt,itm_shirtc,itm_shirtd,itm_shirte,itm_khergit_elite_armor,itm_hauberk6,itm_mail_shirt_a_copy,
    itm_rathos_spangenhelm_a,itm_bowl_helmet,itm_norman_helmet,itm_leather_cap,itm_spear_2,itm_spatha,itm_hunting_dagger,
    itm_cantabro_shield_1,itm_cantabro_shield_2,itm_cantabro_shield_3,itm_cantabro_shield_4,itm_cantabro_shield_5,itm_cantabro_shield_6,itm_cantabro_shield_7,itm_cantabro_shield_8,itm_cantabro_shield_9,itm_cantabro_shield_10],
   def_attrib3|level(25),wp(180),knows_warrior_elite,mercenary_face_1, mercenary_face_2], #chief cambiado
  #####
  ["nord_veteran_multiplayer_ai2","Beadu rinc Engle (Hv. I.)","Beadu rincas Engles",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_9,
   [itm_throwing_spears3,itm_javelin,itm_throwing_spears4,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_2_grey,
    itm_piel_coat01,itm_piel_coat03,itm_bl_boar_fur,
    itm_bl_tunic03,itm_redvikingshirt,itm_redtunic,itm_bl_tunic03,itm_leather_armor_c2,itm_leather_armor_c,itm_vae_thick_coat2,itm_vae_thick_coat3,itm_tattered_leather_armor_gr,
    itm_rathos_bowl_helmet,itm_bowl_helmet,itm_sarranid_helmet1,itm_horn_helmet_3,itm_khergit_cavalry_helmet,
    itm_dagger,itm_saxon_axe,itm_axe,itm_spear_3,itm_spear_2,itm_lui_battleaxetwoh,
    itm_ad_viking_shield_round_31,itm_ad_viking_shield_round_32,itm_ad_viking_shield_round_43,itm_ad_viking_shield_round_34,itm_ad_viking_shield_round_36,itm_ad_viking_shield_round_37,itm_ad_viking_shield_round_38,itm_ad_viking_shield_round_39],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,nord_face_young_1, nord_face_old_2],
  ["nord_scout_multiplayer_ai2","Rigwiga Engle (El. I.)","Ridwigas Engles",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_9,
   [itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
    itm_leather_gloves,itm_decorated_leather_shoes_grey,itm_iron_greaves,
    itm_tattered_leather_armor_ylw,itm_padded_leather_blue,itm_ad_viking_byrnie_02,itm_ad_viking_byrnie_04,itm_ad_viking_byrnie_06,itm_mail_shirt_9_trig,itm_mail_shirt_2_trig,
    itm_horn_helmet,itm_horn_helmet_2,itm_spangenhelm_helm,itm_vaegir_war_helmet,itm_briton_helm4,itm_briton_helm3,itm_nordic_veteran_archer_helmet,itm_footman_helmet,
    itm_scimitar,itm_new_sword3,itm_le_pictishsword3,itm_saxonsword,itm_le_richsword1,
    itm_ad_viking_shield_round_15,itm_ad_viking_shield_round_30,itm_saxon_adorno_20,itm_saxon_adorno_1,itm_saxon_adorno_2,itm_saxon_adorno_3,itm_saxon_adorno_4,itm_saxon_adorno_5],
   def_attrib3|level(28),wp(210),knows_warrior_veteran|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  ["nord_archer_multiplayer_ai2","Sceotand Engle (Missile)","Sceotandas Engles",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_9,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_short_bow,itm_hunting_bow,
    itm_ankle_boots,itm_wrapping_boots,
    itm_leather_steppe_cap_a,itm_roman_shirt,itm_fattiglinenskjortir,itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsr01,
    itm_cudgel,itm_dagger,itm_axe],
   basic_ranged_attrib|str_10|level(17),wp(45)|wp_archery(125),knows_ironflesh_1|knows_power_draw_2|knows_power_throw_1,nord_face_young_1, nord_face_old_2],
  ["nord_champion_multiplayer_ai","Gesith Engle (Lig. C.)","Gesithas Engles",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_9,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_saddle_horse,itm_steppe_horse,itm_charger,itm_normal_horse24,itm_normal_horse25,itm_normal_horse26,
    itm_decorated_leather_shoes_green,itm_decorated_leather_shoes_blue,itm_carbatinae_2_blue,
    itm_bl_tunic03,itm_redvikingshirt,itm_redtunic,itm_bl_tunic03,itm_leather_armor_c2,itm_leather_armor_c,itm_vae_thick_coat2,itm_vae_thick_coat3,itm_tattered_leather_armor_gr,
    itm_padded_leather_brown,itm_tattered_leather_armor_ylw,itm_mail_shirthre,itm_mail_shirtredwhite,
    itm_vaegir_war_helmet,itm_briton_helm,itm_briton_helm2,itm_magyar_helmet_a,itm_vaegir_mask,itm_talak_spangenhelm,itm_horn_helmet,itm_horn_helmet_3,
    itm_hunting_dagger,itm_new_sword3,itm_spear_8,itm_spear_4,
    itm_saxon_adorno_20,itm_saxon_adorno_1,itm_saxon_adorno_2,itm_tab_shield_small_round_c],
   def_attrib3|level(23),wp(170),knows_warrior_normal|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  ######

  ["swadian_crossbowman_multiplayer_ai4","Saethydd (Missile)","Saethydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_10,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(200),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai4","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_10,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai4","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_10,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["gwrdas_multiplayer_ai4","Gwrda (Skrm.)","Gwrdas",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_10,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,itm_white_cloak,itm_irishcloak,itm_piel_coat07,
    itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_vae_thick_coat2,itm_vae_thick_coat3,
    itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
    itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],
  ###
  ["swadian_crossbowman_multiplayer_ai5","Saethydd (Missile)","Saethydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_11,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(200),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai5","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_11,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai5","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_11,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["gwrdas_multiplayer_ai5","Gwrda (Skrm.)","Gwrdas",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_11,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,itm_white_cloak,itm_irishcloak,itm_piel_coat07,
    itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_vae_thick_coat2,itm_vae_thick_coat3,
    itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
    itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],
  ###
  ["swadian_crossbowman_multiplayer_ai6","Saethydd (Missile)","Saethydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_12,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(200),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai6","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_12,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai6","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_12,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["gwrdas_multiplayer_ai6","Gwrda (Skrm.)","Gwrdas",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_12,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,itm_white_cloak,itm_irishcloak,itm_piel_coat07,
    itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_vae_thick_coat2,itm_vae_thick_coat3,
    itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
    itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],
  ###
  ["nord_veteran_multiplayer_ai3","Beadu rinc Engle (Hv. I.)","Beadu rincas Engles",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_13,
   [itm_throwing_spears3,itm_javelin,itm_throwing_spears4,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_2_grey,
    itm_piel_coat01,itm_piel_coat03,itm_bl_boar_fur,
    itm_bl_tunic03,itm_redvikingshirt,itm_redtunic,itm_bl_tunic03,itm_leather_armor_c2,itm_leather_armor_c,itm_vae_thick_coat2,itm_vae_thick_coat3,itm_tattered_leather_armor_gr,
    itm_rathos_bowl_helmet,itm_bowl_helmet,itm_sarranid_helmet1,itm_horn_helmet_3,itm_khergit_cavalry_helmet,
    itm_dagger,itm_saxon_axe,itm_axe,itm_spear_3,itm_spear_2,itm_lui_battleaxetwoh,
    itm_ad_viking_shield_round_31,itm_ad_viking_shield_round_32,itm_ad_viking_shield_round_43,itm_ad_viking_shield_round_34,itm_ad_viking_shield_round_36,itm_ad_viking_shield_round_37,itm_ad_viking_shield_round_38,itm_ad_viking_shield_round_39],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,nord_face_young_1, nord_face_old_2],
  ["nord_scout_multiplayer_ai3","Rigwiga Engle (El. I.)","Ridwigas Engles",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_13,
   [itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
    itm_leather_gloves,itm_decorated_leather_shoes_grey,itm_iron_greaves,
    itm_tattered_leather_armor_ylw,itm_padded_leather_blue,itm_ad_viking_byrnie_02,itm_ad_viking_byrnie_04,itm_ad_viking_byrnie_06,itm_mail_shirt_9_trig,itm_mail_shirt_2_trig,
    itm_horn_helmet,itm_horn_helmet_2,itm_spangenhelm_helm,itm_vaegir_war_helmet,itm_briton_helm4,itm_briton_helm3,itm_nordic_veteran_archer_helmet,itm_footman_helmet,
    itm_scimitar,itm_new_sword3,itm_le_pictishsword3,itm_saxonsword,itm_le_richsword1,
    itm_ad_viking_shield_round_15,itm_ad_viking_shield_round_30,itm_saxon_adorno_20,itm_saxon_adorno_1,itm_saxon_adorno_2,itm_saxon_adorno_3,itm_saxon_adorno_4,itm_saxon_adorno_5],
   def_attrib3|level(28),wp(210),knows_warrior_veteran|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  ["nord_archer_multiplayer_ai3","Sceotand Engle (Missile)","Sceotandas Engles",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_13,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_short_bow,itm_hunting_bow,
    itm_ankle_boots,itm_wrapping_boots,
    itm_leather_steppe_cap_a,itm_roman_shirt,itm_fattiglinenskjortir,itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsr01,
    itm_cudgel,itm_dagger,itm_axe],
   basic_ranged_attrib|str_10|level(17),wp(45)|wp_archery(125),knows_ironflesh_1|knows_power_draw_2|knows_power_throw_1,nord_face_young_1, nord_face_old_2],
  ["nord_champion_multiplayer_ai3","Gesith Engle (Lig. C.)","Gesithas Engles",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_13,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_saddle_horse,itm_steppe_horse,itm_charger,itm_normal_horse24,itm_normal_horse25,itm_normal_horse26,
    itm_decorated_leather_shoes_green,itm_decorated_leather_shoes_blue,itm_carbatinae_2_blue,
    itm_bl_tunic03,itm_redvikingshirt,itm_redtunic,itm_bl_tunic03,itm_leather_armor_c2,itm_leather_armor_c,itm_vae_thick_coat2,itm_vae_thick_coat3,itm_tattered_leather_armor_gr,
    itm_padded_leather_brown,itm_byrnie,itm_tattered_leather_armor_ylw,itm_mail_shirt_1_trig,
    itm_vaegir_war_helmet,itm_briton_helm,itm_briton_helm2,itm_magyar_helmet_a,itm_vaegir_mask,itm_talak_spangenhelm,itm_horn_helmet,itm_horn_helmet_3,
    itm_hunting_dagger,itm_new_sword3,itm_spear_8,itm_spear_4,
    itm_saxon_adorno_20,itm_saxon_adorno_1,itm_saxon_adorno_2,itm_tab_shield_small_round_c],
   def_attrib3|level(23),wp(170),knows_warrior_normal|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  ###sigue
  ["nord_veteran_multiplayer_ai4","Beadu rinc Engle (Hv. I.)","Beadu rincas Engles",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_14,
   [itm_throwing_spears3,itm_javelin,itm_throwing_spears4,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_2_grey,
    itm_piel_coat01,itm_piel_coat03,itm_bl_boar_fur,
    itm_bl_tunic03,itm_redvikingshirt,itm_redtunic,itm_bl_tunic03,itm_leather_armor_c2,itm_leather_armor_c,itm_vae_thick_coat2,itm_vae_thick_coat3,itm_tattered_leather_armor_gr,
    itm_rathos_bowl_helmet,itm_bowl_helmet,itm_sarranid_helmet1,itm_horn_helmet_3,itm_khergit_cavalry_helmet,
    itm_dagger,itm_saxon_axe,itm_axe,itm_spear_3,itm_spear_2,itm_lui_battleaxetwoh,
    itm_ad_viking_shield_round_31,itm_ad_viking_shield_round_32,itm_ad_viking_shield_round_43,itm_ad_viking_shield_round_34,itm_ad_viking_shield_round_36,itm_ad_viking_shield_round_37,itm_ad_viking_shield_round_38,itm_ad_viking_shield_round_39],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,nord_face_young_1, nord_face_old_2],
  ["nord_scout_multiplayer_ai4","Rigwiga Engle (El. I.)","Ridwigas Engles",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_14,
   [itm_throwing_spears3,itm_throwing_spears4,itm_jarid,
    itm_leather_gloves,itm_decorated_leather_shoes_grey,itm_iron_greaves,
    itm_tattered_leather_armor_ylw,itm_padded_leather_blue,itm_ad_viking_byrnie_02,itm_ad_viking_byrnie_04,itm_ad_viking_byrnie_06,itm_mail_shirt_9_trig,itm_mail_shirt_2_trig,
    itm_horn_helmet,itm_horn_helmet_2,itm_spangenhelm_helm,itm_vaegir_war_helmet,itm_briton_helm4,itm_briton_helm3,itm_nordic_veteran_archer_helmet,itm_footman_helmet,
    itm_scimitar,itm_new_sword3,itm_le_pictishsword3,itm_saxonsword,itm_le_richsword1,
    itm_ad_viking_shield_round_15,itm_ad_viking_shield_round_30,itm_saxon_adorno_20,itm_saxon_adorno_1,itm_saxon_adorno_2,itm_saxon_adorno_3,itm_saxon_adorno_4,itm_saxon_adorno_5],
   def_attrib3|level(28),wp(210),knows_warrior_veteran|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  ["nord_archer_multiplayer_ai4","Sceotand Engle (Missile)","Sceotandas Engles",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_14,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_short_bow,itm_hunting_bow,
    itm_ankle_boots,itm_wrapping_boots,
    itm_leather_steppe_cap_a,itm_roman_shirt,itm_fattiglinenskjortir,itm_bl_tunicsr01_2,itm_bl_tunicsr02,itm_mercia_tunic1,itm_blue_short_tunic,itm_bl_tunicsr01,
    itm_cudgel,itm_dagger,itm_axe],
   basic_ranged_attrib|str_10|level(17),wp(45)|wp_archery(125),knows_ironflesh_1|knows_power_draw_2|knows_power_throw_1,nord_face_young_1, nord_face_old_2],
  ["nord_champion_multiplayer_ai4","Gesith Engle (Lig. C.)","Gesithas Engles",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_14,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_saddle_horse,itm_steppe_horse,itm_charger,itm_normal_horse24,itm_normal_horse25,itm_normal_horse26,
    itm_decorated_leather_shoes_green,itm_decorated_leather_shoes_blue,itm_carbatinae_2_blue,
    itm_padded_leather_blue,itm_padded_leather_brown,itm_mail_shirthre,itm_mail_shirt_1_trig,
    itm_vaegir_war_helmet,itm_briton_helm,itm_briton_helm2,itm_magyar_helmet_a,itm_vaegir_mask,itm_talak_spangenhelm,itm_horn_helmet,itm_horn_helmet_3,
    itm_hunting_dagger,itm_new_sword3,itm_spear_8,itm_spear_4,
    itm_saxon_adorno_20,itm_saxon_adorno_1,itm_saxon_adorno_2,itm_tab_shield_small_round_c],
   def_attrib3|level(23),wp(170),knows_warrior_normal|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  ####
  ["swadian_crossbowman_multiplayer_ai7","Saethydd (Missile)","Saethydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_15,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(200),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai7","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_15,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai7","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_15,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["gwrdas_multiplayer_ai7","Gwrda (Skrm.)","Gwrdas",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_15,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,itm_white_cloak,itm_irishcloak,itm_piel_coat07,
    itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_vae_thick_coat2,itm_vae_thick_coat3,
    itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
    itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],
  ###
  ["swadian_crossbowman_multiplayer_ai8","Saethydd (Missile)","Saethydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_16,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(200),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai8","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_16,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai8","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_16,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["gwrdas_multiplayer_ai8","Gwrda (Skrm.)","Gwrdas",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_16,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,itm_white_cloak,itm_irishcloak,itm_piel_coat07,
    itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_vae_thick_coat2,itm_vae_thick_coat3,
    itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
    itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],
  ####
  ["rhodok_veteran_crossbowman_multiplayer_ai","Saiogdear Goidel (Missile)","Saiogdears Goidels",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_17,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newwht,itm_black_hood,itm_head_wrappings,itm_common_hood,
    itm_leather_vest,itm_steppe_armor,itm_gambeson,itm_tunic_a,itm_koszula_gaelicka,itm_bl_tunicsr03,itm_bl_tunicsr03_2,itm_bl_tunicsr01,itm_vaelicus_tunic_3,itm_tunic_c,
    itm_club,itm_scianshort,itm_scianshortbone],
   basic_ranged_attrib|level(18),wp(60)|wp_archery(150),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_veteran_spearman_multiplayer_ai","Ocaire (Hv. I.)","Ocaires",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_17,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_nordiclightarmor4,itm_nordiclightarmor5,itm_nordiclightarmor6,itm_nordiclightarmor7,itm_nordiclightarmor8,itm_gatheredcloaks1,itm_gatheredcloaks2,itm_gatheredcloaks3,itm_gatheredcloaks5,
    itm_skull_cap_new_c,itm_leather_cap,itm_bowl_helmet,
    itm_scianshortbone,itm_war_spear,itm_spear,itm_celtic1,
    itm_vae_escudo_picto,itm_vae_escudo_picto2,itm_vae_escudo_picto3,itm_vae_escudo_picto4,itm_vae_escudo_picto5,itm_vae_escudo_picto6,itm_vae_escudo_picto7,itm_vae_escudo_picto8,itm_vae_escudo_picto9],
   def_attrib2|level(25),wp(185),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai","Marcach (Med. C.)","Marcachs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_17,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_saddle_horse,itm_steppe_horse,itm_charger,itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,
    itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
    itm_gatheredcloaks1,itm_vaelicus_t_21,itm_vaelicus_t_26,itm_vaelicus_t_27,itm_vaelicus_t_35,itm_padded_jack_3_trig,itm_padded_jack_6_trig,itm_padded_jack_7_trig,itm_padded_jack_9_trig,
    itm_helm_captaina,itm_leather_cap,itm_celtycka_lebka,itm_celtycka_iron,itm_blue_cloak_hood,
    itm_scianlongbone,itm_celticv2_1,itm_spear_8,itm_sarranid_axe_b,
    itm_tab_shield_round_c,itm_celtic_shield_small_round_b,itm_celtic_shield_small_round_e,itm_celtic_vae_shield5,itm_scyld5,itm_scyld6,itm_scyld7,itm_tarcza_harfa_vae_16,itm_tarcza_harfa_vae_17,itm_gaelic_shield_h,itm_gaelic_shield_i],
   def_attrib3|level(27),wp(200),knows_warrior_veteran,rhodok_face_middle_1, rhodok_face_older_2],
  ["steppe_bandit_multiplayer_ai","Scotos","Scoti",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_17,
   [itm_darts,itm_javelin,itm_throwing_knives,itm_javelin,itm_throwing_knives,itm_sniper_crossbow,itm_flintlock_pistol,
    itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_padded_jack_6_trig,itm_bl_tunicsr03_2,itm_bl_tunicsr01,itm_vaelicus_tunic_3,itm_tunic_c,itm_pict_tunic5,itm_shirtb,itm_shirte,itm_pelt_coat,itm_light_leather,itm_mail_with_surcoat,itm_military_cleaver_b,
    itm_celtycka_lebka,itm_celtycka_iron,itm_leather_cap,
    itm_irish_sword,itm_spear,itm_boar_spear,itm_sarranid_two_handed_axe_a,itm_celticv2_1,itm_scianshort,
    itm_leathershield_small_d,itm_vae_cuadrado_8,itm_vae_cuadrado_9,itm_leathershield_medium,itm_vae_cuadrado_1,itm_vae_cuadrado_2,itm_scyld1,itm_scyld2,itm_scyld3,itm_scyld4,
    itm_gaelic_shield_a,itm_gaelic_shield_b,itm_gaelic_shield_c,],
   def_attrib2|level(25),wp(185),knows_warrior_veteran|knows_athletics_5,khergit_face_young_1, khergit_face_old_2],
  ###
  ["swadian_crossbowman_multiplayer_ai9","Saethydd (Missile)","Saethydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_18,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(200),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai9","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_18,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_normal|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai9","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_18,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["gwrdas_multiplayer_ai9","Gwrda (Skrm.)","Gwrdas",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_18,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,itm_white_cloak,itm_irishcloak,itm_piel_coat07,
    itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_vae_thick_coat2,itm_vae_thick_coat3,
    itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
    itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],
  ####
  ["rhodok_veteran_crossbowman_multiplayer_ai2","Saiogdear Goidel (Missile)","Saiogdears Goidels",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_19,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newwht,itm_black_hood,itm_head_wrappings,itm_common_hood,
    itm_leather_vest,itm_steppe_armor,itm_gambeson,itm_tunic_a,itm_koszula_gaelicka,itm_bl_tunicsr03,itm_bl_tunicsr03_2,itm_bl_tunicsr01,itm_vaelicus_tunic_3,itm_tunic_c,
    itm_club,itm_scianshort,itm_scianshortbone],
   basic_ranged_attrib|level(18),wp(60)|wp_archery(150),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_veteran_spearman_multiplayer_ai2","Ocaire (Med. I.)","Ocaires",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_19,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_nordiclightarmor4,itm_nordiclightarmor5,itm_nordiclightarmor6,itm_nordiclightarmor7,itm_nordiclightarmor8,itm_gatheredcloaks1,itm_gatheredcloaks2,itm_gatheredcloaks3,itm_gatheredcloaks5,
    itm_skull_cap_new_c,itm_leather_cap,itm_bowl_helmet,
    itm_scianshortbone,itm_war_spear,itm_spear,itm_celtic1,
    itm_vae_escudo_picto,itm_vae_escudo_picto2,itm_vae_escudo_picto3,itm_vae_escudo_picto4,itm_vae_escudo_picto5,itm_vae_escudo_picto6,itm_vae_escudo_picto7,itm_vae_escudo_picto8,itm_vae_escudo_picto9],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai2","Marcach (Med. C.)","Marcachs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_19,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_saddle_horse,itm_steppe_horse,itm_charger,itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,
    itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
    itm_gatheredcloaks1,itm_vaelicus_t_21,itm_vaelicus_t_26,itm_vaelicus_t_27,itm_vaelicus_t_35,itm_padded_jack_3_trig,itm_padded_jack_6_trig,itm_padded_jack_7_trig,itm_padded_jack_9_trig,
    itm_helm_captaina,itm_leather_cap,itm_celtycka_lebka,itm_celtycka_iron,itm_blue_cloak_hood,
    itm_scianlongbone,itm_celticv2_1,itm_spear_8,itm_sarranid_axe_b,
    itm_tab_shield_round_c,itm_celtic_shield_small_round_b,itm_celtic_shield_small_round_e,itm_celtic_vae_shield5,itm_scyld5,itm_scyld6,itm_scyld7,itm_tarcza_harfa_vae_16,itm_tarcza_harfa_vae_17,itm_gaelic_shield_h,itm_gaelic_shield_i],
   def_attrib3|level(27),wp(200),knows_warrior_veteran,rhodok_face_middle_1, rhodok_face_older_2],
  ["gael_deaisbard_multiplayer_ai","Deaisbard (Elit. Skrm.)","Deaisbards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_19,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_nobleman_outfit,itm_fur_coat,itm_vaelicus_t_25,itm_vaelicus_t_27,itm_sarranid_elite_armor,itm_vaegir_elite_armor,itm_brigandine_red,itm_mail_with_surcoat,itm_surcoat_over_mail,
    itm_skull_cap_new_c,itm_leather_steppe_cap_c,itm_celtycka_lebka,itm_celtycka_iron,
    itm_scianshortbone,itm_celticv2_1,itm_celticv2_2,itm_irishword2,itm_celtic1,
    itm_tab_shield_round_c,itm_tarcza_harfa_vae_13,itm_tarcza_harfa_vae_14,itm_tarcza_harfa_vae_15,itm_scyld8,itm_scyld9,itm_tarcza_harfa_vae_18,itm_tarcza_harfa_vae_19],
   def_attrib3|level(27),wp(200)|wp_throwing(260),knows_warrior_veteran,rhodok_face_young_1, rhodok_face_older_2],
  ###
  ["khergit_dismounted_lancer_multiplayer_ai","Each Raidh (Lig. C.","Each Raidhs",tf_mounted|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_20,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_sumpter_horse,itm_warhorse_sarranid3,itm_arabian_horse_a,itm_steppe_horse,itm_charger,itm_saddle_horse,itm_normal_horse29,itm_normal_horse31,
    itm_bare_legs_blue,itm_decorated_leather_shoes_bare,
    itm_mail_with_tunic_green,itm_picto_gordo2,itm_vae_thick_coat10,itm_vae_thick_coat6,itm_vae_thick_coat3,itm_vae_thick_coat2,itm_vae_thick_coat1,itm_pelt_coat,itm_pelt_coat2,
    itm_scythe,itm_sarranid_axe_b,itm_scianshortbone,itm_scianlongbone,itm_hand_axe,itm_irish_long_sword,
    itm_celtic_vae_shield5,itm_celtic_vae_shield7, itm_h_shield,itm_vae_h_shield1,itm_vae_h_shield2,itm_vae_h_shield3,itm_vae_h_shield4,itm_vae_h_shield5,itm_vae_caledonian_shield12],
   def_attrib2|level(25),wp(185),knows_warrior_normal|knows_ironflesh_4|knows_power_strike_4,khergit_face_young_1, khergit_face_older_4],
  ["khergit_veteran_horse_archer_multiplayer_ai","Eite Fuidir (Elit. Skrm.)","Elite Fuidirs",tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_20,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_head_wrappings,itm_common_hood,
    itm_war_paint_two,itm_long_mail_coat,itm_mail_with_tunic_red,itm_hide_coat,itm_linen_shirt,itm_wool_coat,itm_dress,itm_picto_gordo1,itm_war_paint_two_5,itm_war_paint_two_2,
    itm_irish_sword,itm_scianshortbone,itm_scianshort,itm_scianlong,itm_scianlongbone,
    itm_vae_cuadrado_19,itm_vae_cuadrado_20,itm_vae_cuadrado_21,itm_vae_cuadrado_3,itm_vae_cuadrado_4,itm_vae_cuadrado_5,itm_h_shield,itm_vae_h_shield1,itm_vae_h_shield2,itm_vae_h_shield3,],
   def_attrib2|level(26),wp(190)|wp_throwing(230),knows_warrior_veteran|knows_ironflesh_4|knows_power_strike_4,khergit_face_young_1, khergit_face_older_4],
  ["khergit_lancer_multiplayer_ai","Bruide (Hv. I.)","Bruides",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_20,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_leather_gloves,itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
    itm_heraldric_armor,itm_studded_leather_coat,itm_sleeveless_tunic,itm_gairlom,itm_tuniczka,
    itm_padded_jack_4_trig,itm_padded_jack_6_trig,itm_heraldic_mail_with_tabard,
    itm_skull_cap_new_c,itm_leather_steppe_cap_b,itm_bowl_helmet_nasal,itm_bowl_helmet,
    itm_irish_sword,itm_le_pictishsword6,itm_le_pictishsword5,itm_scianshortbone,
    itm_tab_shield_round_c,itm_vae_cuadrado_22,itm_vae_cuadrado_23,itm_vae_cuadrado_24,itm_vae_cuadrado_25,itm_vae_cuadrado_26,itm_celtic_vae_shield7,itm_celtic_vae_shield8,itm_celtic_shield_small_round_f,itm_celtic_shield_small_round_e,itm_vae_cuadrado_28],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_ironflesh_5|knows_power_strike_5|knows_athletics_4,khergit_face_young_1, khergit_face_older_4],
  ["khergit_skirmisher_multiplayer_ai","Saiogdear Picti (Missile)","Saiogdears Picti",tf_guarantee_ranged|tf_guarantee_boots,0,0,fac_kingdom_20,
   [itm_arrows,itm_bolts,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,itm_hunting_crossbow,
    itm_bare_legs_blue,itm_carbatinae_1_bare,itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,
    itm_vaelicus_tunic_12,itm_vaelicus_tunic_11,itm_vaelicus_tunic_10,itm_vaelicus_tunic_7,itm_vaelicus_tunic_5,itm_vaelicus_tunic_4,itm_vaelicus_tunic_1,itm_vaelicus_tunic_9,itm_thick_coat,itm_coat_with_cape,
    itm_pictish_hatchet,itm_cudgel,itm_scianshort,itm_scianshortbone],
   basic_ranged_attrib|level(18),wp(60)|wp_archery(140)|wp_crossbow(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,khergit_face_younger_1, khergit_face_old_2],
  #######
  ["swadian_crossbowman_multiplayer_ai10","Saethydd (Missile)","Saethydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_21,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(200),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai10","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_21,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai10","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_21,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["gwrdas_multiplayer_ai10","Gwrda (Skrm.)","Gwrdas",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_21,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,itm_white_cloak,itm_irishcloak,itm_piel_coat07,
    itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_vae_thick_coat2,itm_vae_thick_coat3,
    itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
    itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],

  ["swadian_crossbowman_multiplayer_ai11","Saethydd (Missile)","Saethydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_22,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(200),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai11","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_22,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai11","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_22,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["gwrdas_multiplayer_ai11","Gwrda (Skrm.)","Gwrdas",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_22,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,itm_white_cloak,itm_irishcloak,itm_piel_coat07,
    itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_vae_thick_coat2,itm_vae_thick_coat3,
    itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
    itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],

  ["swadian_crossbowman_multiplayer_ai12","Saethydd (Missile)","Saethydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_23,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(200),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai12","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_23,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai12","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_23,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["gwrdas_multiplayer_ai12","Gwrda (Skrm.)","Gwrdas",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_23,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,itm_white_cloak,itm_irishcloak,itm_piel_coat07,
    itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_vae_thick_coat2,itm_vae_thick_coat3,
    itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
    itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],

  ["swadian_crossbowman_multiplayer_ai13","Saethydd (Missile)","Saethydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_24,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(200),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai13","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_24,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai13","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_24,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["gwrdas_multiplayer_ai13","Gwrda (Skrm.)","Gwrdas",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_24,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,itm_white_cloak,itm_irishcloak,itm_piel_coat07,
    itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_vae_thick_coat2,itm_vae_thick_coat3,
    itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
    itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],

  ["swadian_crossbowman_multiplayer_ai14","Saethydd (Missile)","Saethydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_25,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(200),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai14","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_25,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai14","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_25,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["gwrdas_multiplayer_ai14","Gwrda (Skrm.)","Gwrdas",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_25,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,itm_white_cloak,itm_irishcloak,itm_piel_coat07,
    itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_vae_thick_coat2,itm_vae_thick_coat3,
    itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
    itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],

  ["swadian_crossbowman_multiplayer_ai15","Saethydd (Missile)","Saethydds",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_26,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_bare_legs_blue,itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newblu,itm_hood_newblk,itm_hood_newwht,itm_black_hood,
    itm_shirt,itm_roman_shirt,itm_armor_8,itm_armor_9,itm_linen_tunic,itm_short_tunic,itm_red_tunic,itm_green_tunic,itm_blue_tunic,itm_armor_26,
    itm_wooden_stick,itm_hand_axe,itm_cudgel],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(200),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_infantry_multiplayer_ai15","Pedyt (Hv. I.)","Pedytes",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_26,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_blue,itm_carbatinae_1_grey,itm_carbatinae_1_green,
    itm_piel_coat04,itm_piel_coat05,itm_piel_coat06,itm_piel_coat07,
    itm_shirt,itm_roman_shirt,itm_shirt_blu,itm_shirt_grn,itm_linen_tunic,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,
    itm_padded_jack_9_trig,itm_goatist_tunic,itm_padded_jack_6_trig,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_spear_2,itm_broadsword,itm_scianshort,
    itm_ad_viking_shield_round_25,itm_ad_viking_shield_round_26,itm_ad_viking_shield_round_27,itm_ad_viking_shield_round_28,itm_ad_viking_shield_round_29],
   def_attrib2|level(26),wp(190),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai15","Marchoc (Med. C.)","Marcach",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_26,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,
    itm_decorated_leather_shoes,itm_decorated_leather_shoes_orange,itm_ankle_boots,
    itm_padded_jack_3_trig,itm_padded_jack_7_trig,itm_khergit_elite_armor,itm_sarranid_mail_shirt,itm_mail_shirt_1,itm_mail_shirt_2,
    itm_irishcloak,itm_piel_coat07,itm_piel_coat05,itm_rathos_bowl_helmet,itm_briton_helm,itm_norman_helmet,itm_rath_spangenlord5,itm_rathos_spangenhelm_a_yellow2,
    itm_sarranid_axe_b,itm_saxonsword1,itm_scythe,itm_hunting_dagger,
    itm_shield_round_02,itm_shield_round_03,itm_shield_round_04,itm_shield_round_05,itm_shield_round_06,itm_shield_round_07,itm_shield_round_01],
   def_attrib3|level(27),wp(200),knows_warrior_veteran|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
  ["gwrdas_multiplayer_ai15","Gwrda (Skrm.)","Gwrdas",tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_26,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_1,itm_carbatinae_2_grey,itm_carbatinae_1_green,itm_black_cloak,itm_white_cloak,itm_irishcloak,itm_piel_coat07,
    itm_shirt_grn,itm_shirt_ylw,itm_shirt_tel,itm_shirt_blk,itm_bl_tunic02,itm_vae_thick_coat2,itm_vae_thick_coat3,
    itm_helm_captaina,itm_skull_cap_new_c,itm_leather_warrior_cap,itm_leather_steppe_cap_b,
    itm_gallic_axe_1,itm_sarranid_two_handed_axe_b,itm_scianshort,itm_shield_8,itm_shield_9,itm_shield_10,itm_shield_11,itm_shield_12,itm_shield_13,itm_shield_14,itm_shield_15],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_old_2],
  ################
  ["rhodok_veteran_crossbowman_multiplayer_ai3","Saiogdear Goidel (Missile)","Saiogdears Goidels",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_27,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newwht,itm_black_hood,itm_head_wrappings,itm_common_hood,
    itm_leather_vest,itm_steppe_armor,itm_gambeson,itm_tunic_a,itm_koszula_gaelicka,itm_bl_tunicsr03,itm_bl_tunicsr03_2,itm_bl_tunicsr01,itm_vaelicus_tunic_3,itm_tunic_c,
    itm_club,itm_scianshort,itm_scianshortbone],
   basic_ranged_attrib|level(18),wp(60)|wp_archery(150),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_veteran_spearman_multiplayer_ai3","Ocaire (Med. I.)","Ocaires",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_27,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_nordiclightarmor4,itm_nordiclightarmor5,itm_nordiclightarmor6,itm_nordiclightarmor7,itm_nordiclightarmor8,itm_gatheredcloaks1,itm_gatheredcloaks2,itm_gatheredcloaks3,itm_gatheredcloaks5,
    itm_skull_cap_new_c,itm_leather_cap,itm_bowl_helmet,
    itm_scianshortbone,itm_war_spear,itm_spear,itm_celtic1,
    itm_vae_escudo_picto,itm_vae_escudo_picto2,itm_vae_escudo_picto3,itm_vae_escudo_picto4,itm_vae_escudo_picto5,itm_vae_escudo_picto6,itm_vae_escudo_picto7,itm_vae_escudo_picto8,itm_vae_escudo_picto9],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai3","Marcach (Med. C.)","Marcachs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_27,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_saddle_horse,itm_steppe_horse,itm_charger,itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,
    itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
    itm_gatheredcloaks1,itm_vaelicus_t_21,itm_vaelicus_t_26,itm_vaelicus_t_27,itm_vaelicus_t_35,itm_padded_jack_3_trig,itm_padded_jack_6_trig,itm_padded_jack_7_trig,itm_padded_jack_9_trig,
    itm_helm_captaina,itm_leather_cap,itm_celtycka_lebka,itm_celtycka_iron,itm_blue_cloak_hood,
    itm_scianlongbone,itm_celticv2_1,itm_spear_8,itm_sarranid_axe_b,
    itm_tab_shield_round_c,itm_celtic_shield_small_round_b,itm_celtic_shield_small_round_e,itm_celtic_vae_shield5,itm_scyld5,itm_scyld6,itm_scyld7,itm_tarcza_harfa_vae_16,itm_tarcza_harfa_vae_17,itm_gaelic_shield_h,itm_gaelic_shield_i],
   def_attrib3|level(27),wp(200),knows_warrior_veteran,rhodok_face_middle_1, rhodok_face_older_2],
  ["gael_deaisbard_multiplayer_ai3","Deaisbard (Elit. Skrm.)","Deaisbards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_27,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_nobleman_outfit,itm_fur_coat,itm_vaelicus_t_25,itm_vaelicus_t_27,itm_sarranid_elite_armor,itm_vaegir_elite_armor,itm_brigandine_red,itm_mail_with_surcoat,itm_surcoat_over_mail,
    itm_skull_cap_new_c,itm_leather_steppe_cap_c,itm_celtycka_lebka,itm_celtycka_iron,
    itm_scianshortbone,itm_celticv2_1,itm_celticv2_2,itm_irishword2,itm_celtic1,
    itm_tab_shield_round_c,itm_tarcza_harfa_vae_13,itm_tarcza_harfa_vae_14,itm_tarcza_harfa_vae_15,itm_scyld8,itm_scyld9,itm_tarcza_harfa_vae_18,itm_tarcza_harfa_vae_19],
   def_attrib3|level(27),wp(200)|wp_throwing(260),knows_warrior_veteran,rhodok_face_young_1, rhodok_face_older_2],

  ["rhodok_veteran_crossbowman_multiplayer_ai4","Saiogdear Goidel (Missile)","Saiogdears Goidels",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_28,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newwht,itm_black_hood,itm_head_wrappings,itm_common_hood,
    itm_leather_vest,itm_steppe_armor,itm_gambeson,itm_tunic_a,itm_koszula_gaelicka,itm_bl_tunicsr03,itm_bl_tunicsr03_2,itm_bl_tunicsr01,itm_vaelicus_tunic_3,itm_tunic_c,
    itm_club,itm_scianshort,itm_scianshortbone],
   basic_ranged_attrib|level(18),wp(60)|wp_archery(150),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_veteran_spearman_multiplayer_ai4","Ocaire (Med. I.)","Ocaires",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_28,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_nordiclightarmor4,itm_nordiclightarmor5,itm_nordiclightarmor6,itm_nordiclightarmor7,itm_nordiclightarmor8,itm_gatheredcloaks1,itm_gatheredcloaks2,itm_gatheredcloaks3,itm_gatheredcloaks5,
    itm_skull_cap_new_c,itm_leather_cap,itm_bowl_helmet,
    itm_scianshortbone,itm_war_spear,itm_spear,itm_celtic1,
    itm_vae_escudo_picto,itm_vae_escudo_picto2,itm_vae_escudo_picto3,itm_vae_escudo_picto4,itm_vae_escudo_picto5,itm_vae_escudo_picto6,itm_vae_escudo_picto7,itm_vae_escudo_picto8,itm_vae_escudo_picto9],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai4","Marcach (Med. C.)","Marcachs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_28,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_saddle_horse,itm_steppe_horse,itm_charger,itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,
    itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
    itm_gatheredcloaks1,itm_vaelicus_t_21,itm_vaelicus_t_26,itm_vaelicus_t_27,itm_vaelicus_t_35,itm_padded_jack_3_trig,itm_padded_jack_6_trig,itm_padded_jack_7_trig,itm_padded_jack_9_trig,
    itm_helm_captaina,itm_leather_cap,itm_celtycka_lebka,itm_celtycka_iron,itm_blue_cloak_hood,
    itm_scianlongbone,itm_celticv2_1,itm_spear_8,itm_sarranid_axe_b,
    itm_tab_shield_round_c,itm_celtic_shield_small_round_b,itm_celtic_shield_small_round_e,itm_celtic_vae_shield5,itm_scyld5,itm_scyld6,itm_scyld7,itm_tarcza_harfa_vae_16,itm_tarcza_harfa_vae_17,itm_gaelic_shield_h,itm_gaelic_shield_i],
   def_attrib3|level(27),wp(200),knows_warrior_veteran,rhodok_face_middle_1, rhodok_face_older_2],
  ["gael_deaisbard_multiplayer_ai4","Deaisbard (Elit. Skrm.)","Deaisbards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_28,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_nobleman_outfit,itm_fur_coat,itm_vaelicus_t_25,itm_vaelicus_t_27,itm_sarranid_elite_armor,itm_vaegir_elite_armor,itm_brigandine_red,itm_mail_with_surcoat,itm_surcoat_over_mail,
    itm_skull_cap_new_c,itm_leather_steppe_cap_c,itm_celtycka_lebka,itm_celtycka_iron,
    itm_scianshortbone,itm_celticv2_1,itm_celticv2_2,itm_irishword2,itm_celtic1,
    itm_tab_shield_round_c,itm_tarcza_harfa_vae_13,itm_tarcza_harfa_vae_14,itm_tarcza_harfa_vae_15,itm_scyld8,itm_scyld9,itm_tarcza_harfa_vae_18,itm_tarcza_harfa_vae_19],
   def_attrib3|level(27),wp(200)|wp_throwing(260),knows_warrior_veteran,rhodok_face_young_1, rhodok_face_older_2],

  ["rhodok_veteran_crossbowman_multiplayer_ai5","Saiogdear Goidel (Missile)","Saiogdears Goidels",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_29,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newwht,itm_black_hood,itm_head_wrappings,itm_common_hood,
    itm_leather_vest,itm_steppe_armor,itm_gambeson,itm_tunic_a,itm_koszula_gaelicka,itm_bl_tunicsr03,itm_bl_tunicsr03_2,itm_bl_tunicsr01,itm_vaelicus_tunic_3,itm_tunic_c,
    itm_club,itm_scianshort,itm_scianshortbone],
   basic_ranged_attrib|level(18),wp(60)|wp_archery(150),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_veteran_spearman_multiplayer_ai5","Ocaire (Med. I.)","Ocaires",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_29,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_nordiclightarmor4,itm_nordiclightarmor5,itm_nordiclightarmor6,itm_nordiclightarmor7,itm_nordiclightarmor8,itm_gatheredcloaks1,itm_gatheredcloaks2,itm_gatheredcloaks3,itm_gatheredcloaks5,
    itm_skull_cap_new_c,itm_leather_cap,itm_bowl_helmet,
    itm_scianshortbone,itm_war_spear,itm_spear,itm_celtic1,
    itm_vae_escudo_picto,itm_vae_escudo_picto2,itm_vae_escudo_picto3,itm_vae_escudo_picto4,itm_vae_escudo_picto5,itm_vae_escudo_picto6,itm_vae_escudo_picto7,itm_vae_escudo_picto8,itm_vae_escudo_picto9],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai5","Marcach (Med. C.)","Marcachs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_29,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_saddle_horse,itm_steppe_horse,itm_charger,itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,
    itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
    itm_gatheredcloaks1,itm_vaelicus_t_21,itm_vaelicus_t_26,itm_vaelicus_t_27,itm_vaelicus_t_35,itm_padded_jack_3_trig,itm_padded_jack_6_trig,itm_padded_jack_7_trig,itm_padded_jack_9_trig,
    itm_helm_captaina,itm_leather_cap,itm_celtycka_lebka,itm_celtycka_iron,itm_blue_cloak_hood,
    itm_scianlongbone,itm_celticv2_1,itm_spear_8,itm_sarranid_axe_b,
    itm_tab_shield_round_c,itm_celtic_shield_small_round_b,itm_celtic_shield_small_round_e,itm_celtic_vae_shield5,itm_scyld5,itm_scyld6,itm_scyld7,itm_tarcza_harfa_vae_16,itm_tarcza_harfa_vae_17,itm_gaelic_shield_h,itm_gaelic_shield_i],
   def_attrib3|level(27),wp(200),knows_warrior_veteran,rhodok_face_middle_1, rhodok_face_older_2],
  ["gael_deaisbard_multiplayer_ai5","Deaisbard (Elit. Skrm.)","Deaisbards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_29,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_nobleman_outfit,itm_fur_coat,itm_vaelicus_t_25,itm_vaelicus_t_27,itm_sarranid_elite_armor,itm_vaegir_elite_armor,itm_brigandine_red,itm_mail_with_surcoat,itm_surcoat_over_mail,
    itm_skull_cap_new_c,itm_leather_steppe_cap_c,itm_celtycka_lebka,itm_celtycka_iron,
    itm_scianshortbone,itm_celticv2_1,itm_celticv2_2,itm_irishword2,itm_celtic1,
    itm_tab_shield_round_c,itm_tarcza_harfa_vae_13,itm_tarcza_harfa_vae_14,itm_tarcza_harfa_vae_15,itm_scyld8,itm_scyld9,itm_tarcza_harfa_vae_18,itm_tarcza_harfa_vae_19],
   def_attrib3|level(27),wp(200)|wp_throwing(260),knows_warrior_veteran,rhodok_face_young_1, rhodok_face_older_2],

  ["rhodok_veteran_crossbowman_multiplayer_ai6","Saiogdear Goidel (Missile)","Saiogdears Goidels",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_30,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newwht,itm_black_hood,itm_head_wrappings,itm_common_hood,
    itm_leather_vest,itm_steppe_armor,itm_gambeson,itm_tunic_a,itm_koszula_gaelicka,itm_bl_tunicsr03,itm_bl_tunicsr03_2,itm_bl_tunicsr01,itm_vaelicus_tunic_3,itm_tunic_c,
    itm_club,itm_scianshort,itm_scianshortbone],
   basic_ranged_attrib|level(18),wp(60)|wp_archery(150),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_veteran_spearman_multiplayer_ai6","Ocaire (Med. I.)","Ocaires",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_30,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_nordiclightarmor4,itm_nordiclightarmor5,itm_nordiclightarmor6,itm_nordiclightarmor7,itm_nordiclightarmor8,itm_gatheredcloaks1,itm_gatheredcloaks2,itm_gatheredcloaks3,itm_gatheredcloaks5,
    itm_skull_cap_new_c,itm_leather_cap,itm_bowl_helmet,
    itm_scianshortbone,itm_war_spear,itm_spear,itm_celtic1,
    itm_vae_escudo_picto,itm_vae_escudo_picto2,itm_vae_escudo_picto3,itm_vae_escudo_picto4,itm_vae_escudo_picto5,itm_vae_escudo_picto6,itm_vae_escudo_picto7,itm_vae_escudo_picto8,itm_vae_escudo_picto9],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai6","Marcach (Med. C.)","Marcachs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_30,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_saddle_horse,itm_steppe_horse,itm_charger,itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,
    itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
    itm_gatheredcloaks1,itm_vaelicus_t_21,itm_vaelicus_t_26,itm_vaelicus_t_27,itm_vaelicus_t_35,itm_padded_jack_3_trig,itm_padded_jack_6_trig,itm_padded_jack_7_trig,itm_padded_jack_9_trig,
    itm_helm_captaina,itm_leather_cap,itm_celtycka_lebka,itm_celtycka_iron,itm_blue_cloak_hood,
    itm_scianlongbone,itm_celticv2_1,itm_spear_8,itm_sarranid_axe_b,
    itm_tab_shield_round_c,itm_celtic_shield_small_round_b,itm_celtic_shield_small_round_e,itm_celtic_vae_shield5,itm_scyld5,itm_scyld6,itm_scyld7,itm_tarcza_harfa_vae_16,itm_tarcza_harfa_vae_17,itm_gaelic_shield_h,itm_gaelic_shield_i],
   def_attrib3|level(27),wp(200),knows_warrior_veteran,rhodok_face_middle_1, rhodok_face_older_2],
  ["gael_deaisbard_multiplayer_ai6","Deaisbard (Elit. Skrm.)","Deaisbards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_30,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_nobleman_outfit,itm_fur_coat,itm_vaelicus_t_25,itm_vaelicus_t_27,itm_sarranid_elite_armor,itm_vaegir_elite_armor,itm_brigandine_red,itm_mail_with_surcoat,itm_surcoat_over_mail,
    itm_skull_cap_new_c,itm_leather_steppe_cap_c,itm_celtycka_lebka,itm_celtycka_iron,
    itm_scianshortbone,itm_celticv2_1,itm_celticv2_2,itm_irishword2,itm_celtic1,
    itm_tab_shield_round_c,itm_tarcza_harfa_vae_13,itm_tarcza_harfa_vae_14,itm_tarcza_harfa_vae_15,itm_scyld8,itm_scyld9,itm_tarcza_harfa_vae_18,itm_tarcza_harfa_vae_19],
   def_attrib3|level(27),wp(200)|wp_throwing(260),knows_warrior_veteran,rhodok_face_young_1, rhodok_face_older_2],

  ["rhodok_veteran_crossbowman_multiplayer_ai7","Saiogdear Goidel (Missile)","Saiogdears Goidels",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_31,
   [itm_arrows,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_hunting_bow,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_hood_newwht,itm_black_hood,itm_head_wrappings,itm_common_hood,
    itm_leather_vest,itm_steppe_armor,itm_gambeson,itm_tunic_a,itm_koszula_gaelicka,itm_bl_tunicsr03,itm_bl_tunicsr03_2,itm_bl_tunicsr01,itm_vaelicus_tunic_3,itm_tunic_c,
    itm_club,itm_scianshort,itm_scianshortbone],
   basic_ranged_attrib|level(18),wp(60)|wp_archery(150),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_veteran_spearman_multiplayer_ai7","Ocaire (Med. I.)","Ocaires",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_31,
   [itm_javelin,itm_javelin,itm_javelin,itm_javelin,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_nordiclightarmor4,itm_nordiclightarmor5,itm_nordiclightarmor6,itm_nordiclightarmor7,itm_nordiclightarmor8,itm_gatheredcloaks1,itm_gatheredcloaks2,itm_gatheredcloaks3,itm_gatheredcloaks5,
    itm_skull_cap_new_c,itm_leather_cap,itm_bowl_helmet,
    itm_scianshortbone,itm_war_spear,itm_spear,itm_celtic1,
    itm_vae_escudo_picto,itm_vae_escudo_picto2,itm_vae_escudo_picto3,itm_vae_escudo_picto4,itm_vae_escudo_picto5,itm_vae_escudo_picto6,itm_vae_escudo_picto7,itm_vae_escudo_picto8,itm_vae_escudo_picto9],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai7","Marcach (Med. C.)","Marcachs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_31,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_saddle_horse,itm_steppe_horse,itm_charger,itm_normal_horse11,itm_normal_horse12,itm_normal_horse13,
    itm_carbatinae_1_bare,itm_decorated_leather_shoes_bare,
    itm_gatheredcloaks1,itm_vaelicus_t_21,itm_vaelicus_t_26,itm_vaelicus_t_27,itm_vaelicus_t_35,itm_padded_jack_3_trig,itm_padded_jack_6_trig,itm_padded_jack_7_trig,itm_padded_jack_9_trig,
    itm_helm_captaina,itm_leather_cap,itm_celtycka_lebka,itm_celtycka_iron,itm_blue_cloak_hood,
    itm_scianlongbone,itm_celticv2_1,itm_spear_8,itm_sarranid_axe_b,
    itm_tab_shield_round_c,itm_celtic_shield_small_round_b,itm_celtic_shield_small_round_e,itm_celtic_vae_shield5,itm_scyld5,itm_scyld6,itm_scyld7,itm_tarcza_harfa_vae_16,itm_tarcza_harfa_vae_17,itm_gaelic_shield_h,itm_gaelic_shield_i],
   def_attrib3|level(27),wp(200),knows_warrior_veteran,rhodok_face_middle_1, rhodok_face_older_2],
  ["gael_deaisbard_multiplayer_ai7","Deaisbard (Elit. Skrm.)","Deaisbards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_31,
   [itm_javelin_jinetes,itm_javelin_jinetes,itm_javelin_jinetes,
    itm_carbatinae_2_bare,itm_carbatinae_1_bare,
    itm_nobleman_outfit,itm_fur_coat,itm_vaelicus_t_25,itm_vaelicus_t_27,itm_sarranid_elite_armor,itm_vaegir_elite_armor,itm_brigandine_red,itm_mail_with_surcoat,itm_surcoat_over_mail,
    itm_skull_cap_new_c,itm_leather_steppe_cap_c,itm_celtycka_lebka,itm_celtycka_iron,
    itm_scianshortbone,itm_celticv2_1,itm_celticv2_2,itm_irishword2,itm_celtic1,
    itm_tab_shield_round_c,itm_tarcza_harfa_vae_13,itm_tarcza_harfa_vae_14,itm_tarcza_harfa_vae_15,itm_scyld8,itm_scyld9,itm_tarcza_harfa_vae_18,itm_tarcza_harfa_vae_19],
   def_attrib3|level(27),wp(200)|wp_throwing(260),knows_warrior_veteran,rhodok_face_young_1, rhodok_face_older_2],

  ["multiplayer_empieza","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],

#Multiplayer troops (they must have the base items only, nothing else)
  ["sarranid_archer_multiplayer","Jute Skirmish","Jutes Archers",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,vaegir_face_middle_1, vaegir_face_older_2],
  ["sarranid_footman_multiplayer","Jute Footman","Jutes footman",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],
  ["sarranid_mamluke_multiplayer","Jute Horseman","Jutes Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["frankish_footman_multiplayer","Frank Warrior","Frankish Warriors",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["vaegir_archer_multiplayer","Saxon Skirmish","Saxon Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,nord_face_young_1, nord_face_older_2],
  ["vaegir_spearman_multiplayer","Saxon Spearman","Saxon Spearman",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer","Saxon Horseman","Saxon Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib2|level(23),wp(170),knows_warrior_normal,nord_face_young_1, nord_face_older_2],

  ["vaegir_archer_multiplayer2","Saxon Skirmish","Saxon Archers",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,nord_face_young_1, nord_face_older_2],
  ["vaegir_spearman_multiplayer2","Saxon Spearman","Saxon Spearman",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer2","Saxon Horseman","Saxon Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib2|level(23),wp(170),knows_warrior_normal,nord_face_young_1, nord_face_older_2],

  ["nord_archer_multiplayer","Angle Skirmish","Angle Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,nord_face_young_1, nord_face_older_2],
  ["nord_veteran_multiplayer","Angle Warrior","Angle Warriors",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer","Angle Horseman","Angle Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib2|level(23),wp(170),knows_warrior_normal,nord_face_young_1, nord_face_older_2],
  ["dena_veteran_multiplayer4","Dena Pirate","Dena Pirates",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,nord_face_young_1, nord_face_older_2],


  ["vaegir_archer_multiplayer3","Saxon Skirmish","Saxon Archers",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,nord_face_young_1, nord_face_older_2],
  ["vaegir_spearman_multiplayer3","Saxon Spearman","Saxon Spearman",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer3","Saxon Horseman","Saxon Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib2|level(23),wp(170),knows_warrior_normal,nord_face_young_1, nord_face_older_2],
  ["frisian_spearman_multiplayer3","Frisian Mercenary","Frisians Mercenaries",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["swadian_crossbowman_multiplayer","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["swadian_crossbowman_multiplayer2","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer2","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer2","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["swadian_crossbowman_multiplayer3","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer3","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer3","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["nord_archer_multiplayer2","Angle Skirmish","Angle Archers",tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,nord_face_young_1, nord_face_older_2],
  ["nord_veteran_multiplayer2","Angle Warrior","Angle Warriors",tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer2","Angle Horseman","Angle Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib2|level(23),wp(170),knows_warrior_normal,nord_face_young_1, nord_face_older_2],

  ["swadian_crossbowman_multiplayer4","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_10,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer4","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_10,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer4","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_10,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["swadian_crossbowman_multiplayer5","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_11,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer5","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_11,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer5","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_11,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["swadian_crossbowman_multiplayer6","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_12,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer6","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_12,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer6","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_12,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["nord_archer_multiplayer3","Angle Skirmish","Angle Archers",tf_guarantee_all,0,0,fac_kingdom_13,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,nord_face_young_1, nord_face_older_2],
  ["nord_veteran_multiplayer3","Angle Warrior","Angle Warriors",tf_guarantee_all,0,0,fac_kingdom_13,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer3","Angle Horseman","Angle Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_13,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib2|level(23),wp(170),knows_warrior_normal,nord_face_young_1, nord_face_older_2],

  ["nord_archer_multiplayer4","Angle Skirmish","Angle Archers",tf_guarantee_all,0,0,fac_kingdom_14,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,nord_face_young_1, nord_face_older_2],
  ["nord_veteran_multiplayer4","Angle Warrior","Angle Warriors",tf_guarantee_all,0,0,fac_kingdom_14,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer4","Angle Horseman","Angle Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_14,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib2|level(23),wp(170),knows_warrior_normal,nord_face_young_1, nord_face_older_2],

  ["swadian_crossbowman_multiplayer7","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_15,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer7","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_15,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer7","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_15,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["swadian_crossbowman_multiplayer8","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_16,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer8","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_16,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer8","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_16,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["rhodok_veteran_crossbowman_multiplayer","Irish Skirmish","Irish Archers",tf_guarantee_all,0,0,fac_kingdom_17,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_sergeant_multiplayer","Irish Spearman","Irish Spearmen",tf_guarantee_all,0,0,fac_kingdom_17,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer","Irish Horseman","Irish Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_17,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,rhodok_face_young_1, rhodok_face_older_2],
  ["scoti_sergeant_multiplayer","Scoti Footman","Scotos Footmen",tf_guarantee_all,0,0,fac_kingdom_17,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],

  ["swadian_crossbowman_multiplayer9","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_18,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer9","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_18,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer9","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_18,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["rhodok_veteran_crossbowman_multiplayer2","Irish Skirmish","Irish Archers",tf_guarantee_all,0,0,fac_kingdom_19,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_sergeant_multiplayer2","Irish Spearman","Irish Spearmen",tf_guarantee_all,0,0,fac_kingdom_19,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer2","Irish Horseman","Irish Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_19,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,rhodok_face_young_1, rhodok_face_older_2],

  ["khergit_veteran_horse_archer_multiplayer","Skirmisher Pict","Skirmishers Picts",tf_guarantee_all,0,0,fac_kingdom_20,
   [itm_ankle_boots],
   def_attrib2|level(21),wp(150)|wp_throwing(180),knows_warrior_normal|knows_ironflesh_4|knows_power_strike_4,khergit_face_young_1, khergit_face_older_4],
  ["khergit_lancer_multiplayer","Pictish Spearman","Pictish Spearmen",tf_guarantee_all,0,0,fac_kingdom_20,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal|knows_ironflesh_4|knows_power_strike_4,khergit_face_middle_1, khergit_face_older_4],
  ["khergit_horse_multiplayer","Pictish Horseman","Pictish Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_20,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib2|level(23),wp(170),knows_warrior_normal|knows_ironflesh_4|knows_power_strike_4,khergit_face_young_1, khergit_face_older_4],

  ["swadian_crossbowman_multiplayer10","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer10","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer10","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["swadian_crossbowman_multiplayer11","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer11","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer11","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["swadian_crossbowman_multiplayer12","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_23,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer12","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_23,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer12","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_23,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["swadian_crossbowman_multiplayer13","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_24,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer13","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_24,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer13","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_24,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["swadian_crossbowman_multiplayer14","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_25,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer14","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_25,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer14","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_25,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["swadian_crossbowman_multiplayer15","Briton Skirmish","Briton Archers",tf_guarantee_all,0,0,fac_kingdom_26,
   [itm_ankle_boots],
   veteran_ranged_attrib|str_14|level(23),wp(70)|wp_archery(170),knows_warrior_normal|knows_power_draw_3|knows_power_throw_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer15","Briton Infantry","Briton Infantry",tf_guarantee_all,0,0,fac_kingdom_26,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_man_at_arms_multiplayer15","Briton Horseman","Briton Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_26,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_veteran,swadian_face_young_1, swadian_face_middle_2],

  ["rhodok_veteran_crossbowman_multiplayer3","Irish Skirmish","Irish Archers",tf_guarantee_all,0,0,fac_kingdom_27,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_sergeant_multiplayer3","Irish Spearman","Irish Spearmen",tf_guarantee_all,0,0,fac_kingdom_27,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer3","Irish Horseman","Irish Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_27,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,rhodok_face_young_1, rhodok_face_older_2],

  ["rhodok_veteran_crossbowman_multiplayer4","Irish Skirmish","Irish Archers",tf_guarantee_all,0,0,fac_kingdom_28,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_sergeant_multiplayer4","Irish Spearman","Irish Spearmen",tf_guarantee_all,0,0,fac_kingdom_28,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer4","Irish Horseman","Irish Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_28,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,rhodok_face_young_1, rhodok_face_older_2],

  ["rhodok_veteran_crossbowman_multiplayer5","Irish Skirmish","Irish Archers",tf_guarantee_all,0,0,fac_kingdom_29,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_sergeant_multiplayer5","Irish Spearman","Irish Spearmen",tf_guarantee_all,0,0,fac_kingdom_29,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer5","Irish Horseman","Irish Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_29,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,rhodok_face_young_1, rhodok_face_older_2],

  ["rhodok_veteran_crossbowman_multiplayer6","Irish Skirmish","Irish Archers",tf_guarantee_all,0,0,fac_kingdom_30,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_sergeant_multiplayer6","Irish Spearman","Irish Spearmen",tf_guarantee_all,0,0,fac_kingdom_30,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer6","Irish Horseman","Irish Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_30,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,rhodok_face_young_1, rhodok_face_older_2],

  ["rhodok_veteran_crossbowman_multiplayer7","Irish Skirmish","Irish Archers",tf_guarantee_all,0,0,fac_kingdom_31,
   [itm_ankle_boots],
   basic_ranged_attrib|level(19),wp(60)|wp_archery(140),knows_warrior_basic|knows_power_draw_2|knows_power_throw_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_sergeant_multiplayer7","Irish Spearman","Irish Spearmen",tf_guarantee_all,0,0,fac_kingdom_31,
   [itm_ankle_boots],
   def_attrib2|level(23),wp(170),knows_warrior_normal,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer7","Irish Horseman","Irish Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_31,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,rhodok_face_young_1, rhodok_face_older_2],

#chief capitan
  ["capitan1","Jute Lord","Jutes Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["mercenario1","Frank Captain","Frankish Captains",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_ankle_boots],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa1","Elite Jute Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan2","Saxon Lord","Saxon Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa2","Elite Saxon Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan3","Saxon Lord","Saxon Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa3","Elite Saxon Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan4","Angle Lord","Angle Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["mercenario2","Dena Captain","Dena Captains",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_ankle_boots],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa4","Elite Angle Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan5","Saxon Lord","Saxon Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["mercenario3","Frisian War Chief","Frisian Captains",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_ankle_boots],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa5","Elite Saxon Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan6","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa6","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan7","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa7","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan8","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["mercenario4","Cantabrian Mercenary Leader","Cantabrian Captains",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_ankle_boots],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa8","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan9","Angle Lord","Angle Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa9","Elite Angle Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan10","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_10,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa10","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_10,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan11","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_11,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa11","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_11,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan12","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_12,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa12","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_12,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan13","Angle Lord","Angle Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_13,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa13","Elite Angle Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_13,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan14","Angle Lord","Angle Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_14,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa14","Elite Angle Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_14,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan15","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_15,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa15","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_15,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan16","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_16,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa16","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_16,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan17","Irish Lord","Irish Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_17,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["mercenario5","Scoti Captain","Scoti Captains",tf_guarantee_all,0,0,fac_kingdom_17,
   [itm_ankle_boots],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa17","Elite Irish Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_17,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan18","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_18,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa18","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_18,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan19","Irish Lord","Irish Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_19,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa19","Elite Irish Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_19,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan20","Pictish Lord","Pictish Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_20,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa20","Elite Pictish Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_20,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan21","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa21","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan22","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa22","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan23","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_23,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa23","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_23,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan24","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_24,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa24","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_24,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan25","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_25,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa25","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_25,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan26","Briton Lord","Briton Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_26,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa26","Elite Briton Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_26,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan27","Irish Lord","Irish Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_27,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa27","Elite Irish Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_27,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan28","Irish Lord","Irish Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_28,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa28","Elite Irish Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_28,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan29","Irish Lord","Irish Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_29,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa29","Elite Irish Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_29,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan30","Irish Lord","Irish Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_30,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa30","Elite Irish Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_30,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],

  ["capitan31","Irish Lord","Irish Lords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_31,
   [itm_ankle_boots,itm_donkey_mount],
   def_attrib3|level(23),wp(170),knows_warrior_normal,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa31","Elite Irish Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_kingdom_31,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],
  ["tropa32","Elite Irish Soldier","Elite Soldiers",tf_guarantee_all,0,0,fac_commoners,
   [itm_ankle_boots],
   def_attrib3|level(25),wp(185),knows_warrior_veteran,vaegir_face_middle_1, vaegir_face_older_2],
  #chief capitan acaba


  ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_commoners, [], 0, 0, 0, 0, 0],

]


#Troop upgrade declarations

upgrade2(troops,"farmer", "watchman","mercenary_crossbowman")
upgrade2(troops,"townsman","watchman","mercenary_crossbowman")
upgrade2(troops,"watchman","caravan_guard","mercenary_horseman")
upgrade(troops,"caravan_guard","mercenary_swordsman")
upgrade2(troops, "mercenary_swordsman", "hired_blade", "frisian_warrior")
upgrade(troops,"mercenary_horseman","mercenary_cavalry")

upgrade2(troops,"swadian_recruit","swadian_militia","swadian_skirmisher")

upgrade2(troops,"swadian_militia","swadian_footman","swadian_infantry")
upgrade(troops,"swadian_footman","swadian_crossbowman")
upgrade2(troops,"swadian_infantry","swadian_sergeant","swadian_man_at_arms")
upgrade(troops,"swadian_skirmisher","swadian_sharpshooter")
upgrade(troops,"swadian_sergeant","campeon")

upgrade(troops,"swadian_man_at_arms","swadian_knight")

upgrade2(troops,"vaegir_recruit","vaegir_footman","vaegir_skirmisher")
upgrade2(troops,"vaegir_footman","vaegir_veteran","vaegir_infantry")

upgrade2(troops,"vaegir_veteran","vaegir_guard","vaegir_horseman")
upgrade(troops,"vaegir_guard","vaegir_knight")

upgrade(troops,"vaegir_infantry","vaegir_archer")

upgrade(troops,"vaegir_archer","vaegir_marksman")

upgrade2(troops,"sarranid_recruit","sarranid_footman","sarranid_skirmisher")
upgrade2(troops,"sarranid_footman","sarranid_veteran_footman","sarranid_infantry")

upgrade2(troops,"sarranid_veteran_footman","sarranid_guard","sarranid_horseman")

upgrade(troops,"sarranid_guard","sarranid_mamluke")

upgrade(troops,"sarranid_infantry","sarranid_archer")

upgrade(troops,"sarranid_archer","sarranid_master_archer")

upgrade2(troops,"khergit_tribesman","khergit_skirmisher","khergit_horseman")
upgrade2(troops,"khergit_horseman","khergit_veteran_horse_archer","khergit_horse_archer")
upgrade2(troops,"khergit_veteran_horse_archer","khergit_lancer","picti_bruide")
upgrade(troops,"picti_bruide","picti_gaisgidh")
upgrade2(troops,"khergit_horse_archer","picti_each","fuidir_elite")
upgrade(troops,"picti_each","picti_airig")

upgrade2(troops,"nord_recruit","nord_footman","nord_huntsman")
upgrade2(troops,"nord_footman","nord_trained_footman","nord_warrior")
upgrade2(troops,"nord_trained_footman","nord_veteran","nord_champion")
upgrade(troops,"nord_veteran","nord_archer")
upgrade(troops,"nord_warrior","nord_veteran_archer")
upgrade(troops,"nord_veteran_archer","engle_hearth")

upgrade2(troops,"rhodok_tribesman","rhodok_spearman","rhodok_crossbowman")
upgrade2(troops,"rhodok_spearman","rhodok_trained_spearman","rhodok_veteran_spearman")
upgrade(troops,"rhodok_trained_spearman","rhodok_trained_crossbowman")
upgrade2(troops,"rhodok_veteran_spearman","gael_deaisbard","rhodok_veteran_crossbowman")

upgrade(troops,"rhodok_veteran_crossbowman","rhodok_sharpshooter")
upgrade(troops,"rhodok_trained_crossbowman","rhodok_sergeant")

#new tree connections
upgrade(troops,"mountain_bandit","desert_bandit")
upgrade(troops,"desert_bandit","forest_bandit")

upgrade(troops,"looter_leader2","mercenary_leader")
# upgrade(troops,"sea_raider_leader2","mercenary_leader")
#upgrade(troops,"forest_bandit","mercenary_crossbowman")
#new tree connections ended

upgrade(troops,"looter","bandit")
upgrade2(troops, "bandit", "brigand", "taiga_bandit")
upgrade(troops, "brigand", "slave_hunter")
upgrade(troops,"taiga_bandit","slave_hunter")

upgrade(troops,"slave_driver","manhunter")
upgrade(troops,"manhunter","slave_hunter")
upgrade(troops,"slave_hunter","slave_crusher")
upgrade(troops,"slave_crusher","slaver_chief")

#TEMPERED chief TROOP UPGRADES BEGIN
upgrade(troops,"shepherd","watchman")
upgrade2(troops,"fresena","thene_saltan_fresena","herem_fresena")
upgrade(troops,"thene_saltan_fresena","skel_fresena")

#tempered chief acaba
upgrade(troops,"refugee","follower_woman")
upgrade(troops,"peasant_woman","follower_woman")
upgrade(troops,"follower_woman","hunter_woman")
upgrade(troops,"hunter_woman","fighter_woman")
upgrade(troops,"fighter_woman","sword_sister")
