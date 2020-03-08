from header_common import *
from header_items import *
from header_operations import *
from header_triggers import *
from header_item_modifiers import *
from ID_factions import *


imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
#imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent

pictish_kingdoms = [
  fac_kingdom_20
]

irish_kingdoms = [
  fac_kingdom_17, fac_kingdom_19, fac_kingdom_27,
  fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31
]

pictish_irish_kindoms = pictish_kingdoms + irish_kingdoms

## CC distancia de tiro chief commander
missile_distance_trigger = [
  (ti_on_missile_hit,
    [
      (store_trigger_param_1, ":shooter_agent"),

      (eq, "$g_report_shot_distance", 1),
      (get_player_agent_no, ":player_agent"),
      (try_begin),
        (eq, ":shooter_agent", ":player_agent"),
        (agent_get_position, pos2, ":shooter_agent"),
        (agent_get_horse, ":horse_agent", ":player_agent"),
        (try_begin),
          (gt, ":horse_agent", -1),
          (position_move_z, pos2, 220),
        (else_try),
          (position_move_z, pos2, 150),
        (try_end),
        (get_distance_between_positions, ":distance", pos1, pos2),
        (store_div, reg61, ":distance", 100),
        (store_mod, reg62, ":distance", 100),
        (try_begin),
          (lt, reg62, 10),
          (str_store_string, s1, "@{reg61}.0{reg62}"),
        (else_try),
          (str_store_string, s1, "@{reg61}.{reg62}"),
        (try_end),
       # (display_message, "@Shot distance: {s1} meters.", 0xCCCCCC), #hemos pues off chief porque igual es algo pesado.
      (try_end),
    ])]
## CC

def create_item(prefix, subfix):
  return prefix + subfix

def create_prefix(id, name, extra_mesh=[]):
  name = id[2] if len(id) == 3 else name
  extra_mesh = id[3] if len(id) == 4 else extra_mesh
  mesh = [(id[1], 0)] + extra_mesh
  return [id[0], name, mesh]

def create_items(ids, subfix, name, extra_mesh=[]):
  return [create_item(create_prefix(id, name, extra_mesh), subfix) for id in ids]

north_horse_subfix = [
  itp_merchandise|itp_type_horse, 0, 2000,
  abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|
  horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic
]
north_horses = create_items([
  ["warhorse_sarranid", "roman_horse_2"],
  ["saddle_horse3", "roman_horse_1"],
  ["steppe_horse3", "WRoman1"],
  ["charger3", "WRoman2"],
  ["normal_horse11", "normal_horse11"],
  ["normal_horse12", "normal_horse12"],
  ["normal_horse13", "normal_horse13"],
  ["normal_horse14", "normal_horse14"],
  ["normal_horse15", "normal_horse15"],
  ["normal_horse16", "normal_horse16"],
  ["normal_horse21", "normal_horse21"],
  ["normal_horse22", "normal_horse22"],
  ["normal_horse24", "normal_horse24"],
  ["normal_horse25", "normal_horse25"],
  ["normal_horse26", "normal_horse26"],
  ["normal_horse27", "normal_horse27"],
  ["normal_horse29", "normal_horse29"],
  ["normal_horse30", "normal_horse30"],
  ["normal_horse31", "normal_horse31"],
  ["warhorse_sarranid3", "WPict1"],
  ["arabian_horse_a", "WPict2"],
  ["saddle_horse", "gallic_horse_1"],
  ["steppe_horse", "gallic_horse_2"],
  ["charger", "gallic_horse_3"],
], north_horse_subfix, "North Horse", [("horse_c",imodbits_horse_good)])

draft_horse_subfix = [
  itp_merchandise|itp_type_horse, 0, 2300,
  abundance(20)|body_armor(16)|hit_points(90)|difficulty(2)|horse_speed(36)|
  horse_maneuver(35)|horse_charge(17)|horse_scale(94),imodbits_horse_basic
]
draft_horses = create_items([
  ["arabian_horse_b", "normal_horse1"],
  ["courser", "normal_horse2"],
  ["arabian_horse_b2", "normal_horse3"],
  ["arabian_horse_a3", "normal_horse4"],
  ["arabian_horse_b3", "normal_horse5"],
  ["arabian_horse_a4", "normal_horse6"],
  ["courser4", "normal_horse7"],
  ["arabian_horse_b4", "normal_horse8"],
  ["courser5", "normal_horse9"],
  ["normal_horse17", "normal_horse17"],
  ["normal_horse18", "normal_horse18"],
  ["normal_horse19", "normal_horse19"],
  ["normal_horse20", "normal_horse20"],
  ["normal_horse23", "normal_horse23"],
  ["normal_horse28", "normal_horse28"],
], draft_horse_subfix, "Draft Horse")

paraveredus_horse_subfix = [
  itp_merchandise|itp_type_horse, 0, 2400,
  abundance(10)|hit_points(85)|body_armor(12)|difficulty(3)|horse_speed(46)|
  horse_maneuver(44)|horse_charge(12)|horse_scale(88),
  imodbits_horse_basic|imodbit_champion
]
paraveredus_horses = create_items([
  ["hunter", "WSumpterChestnut"],
  ["warhorse", "WSumpterBrown"]
], paraveredus_horse_subfix, "Paraveredus", [("hunting_horse",imodbits_horse_good)])

pictish_long_tunic_subfix = [
  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 560,
  weight(1)|abundance(30)|head_armor(0)|body_armor(15)|leg_armor(4),
  imodbits_cloth, [], pictish_irish_kindoms
]
pictish_long_tunics = create_items([
  ["tribal_warrior_outfit", "outaa1"],
  ["nomad_robe", "outaa2"],
  ["heraldric_armor", "outaa3"],
  ["studded_leather_coat", "outaa4"],
], pictish_long_tunic_subfix, "Pictish Long Tunic")

irish_long_tunic_subfix = [
  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 430 ,
  weight(1)|abundance(50)|head_armor(0)|body_armor(12)|leg_armor(4),
  imodbits_cloth, [], pictish_irish_kindoms
]
irish_long_tunics = create_items([
  ["courtly_outfit", "merchant_outf1"],
  ["nobleman_outfit", "merchant_outf2"],
  ["nomad_armor", "shirt_shirt_a"],
  ["khergit_armor", "shirt_shirt_c"],
  ["fur_coat", "merchant_outf5"],
], irish_long_tunic_subfix, "Irish Long Tunic")

godelic_jacket_subfix = [
  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 300,
  weight(4)|abundance(50)|head_armor(0)|body_armor(12)|leg_armor(2)|difficulty(0),
  imodbits_cloth, [], irish_kingdoms
]
godelic_jackets = create_items([
  ["nomad_vest", "a_gaelic_jacket", "Grey Godelic Jacket"],
  ["leather_jacket", "b_gaelic_jacket", "Grey Godelic Jacket"],
  ["ragged_outfit", "c_gaelic_jacket", "Green Godelic Jacket"],
], godelic_jacket_subfix, "Godelic Jacket")

worn_robe_subfix = [
  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 363,
  weight(1)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(4)|difficulty(0),
  imodbits_cloth
]
worn_robes = create_items([
  ["sarranid_jellaba_blue", "sarranid_jellaba_blue", "Blue Worn Robe"],
  ["sarranid_cloth_robe_b", "sar_robegrn"],
  ["skirmisher_armor", "sar_robeylw"],
  ["archers_vest", "sar_robewht"],
  ["sarranid_leather_armor", "sar_robeprp"],
  ["sarranid_cavalry_robe", "sar_robe_bbge"],
  ["sarranid_cloth_robe", "sar_robe_bbge"],
  ["robe", "sar_robered", "Robe"],
  ["sarranid_jellaba_white", "sarranid_jellaba_white", "White Worn Robe"],
], worn_robe_subfix, "Worn Robe")

poor_boots_subfix = [
  itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 100,
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0),
  imodbits_cloth
]
poor_boots = create_items([
  ["wrapping_boots", "wrapping_boots_a_bry", "Wrapping Boots"],
  ["ankle_boots", "ankle_boots_a_new_bry", "Ankle Boots"],
  ["bare_legs_blue", "bare_legs_blue", "Leather Shoes"],
  ["carbatinae_1_bare", "carbatinae_1_bare", "Bare Carbatinae", [("carbatinae_2_bare", 0)]],
], poor_boots_subfix, "Poor Boots")

quality_carbatinae_subfix = [
  itp_merchandise|itp_type_foot_armor |itp_civilian|itp_attach_armature, 0, 280,
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0),
  imodbits_cloth
]
quality_carbatinaes = create_items([
  ["quality_carbatinae_white", "carbatinae_1", "White Quality Carbatinae", [("carbatinae_2",0)]],
  ["quality_carbatinae_green", "carbatinae_1_green", "Green Quality Carbatinae", [("carbatinae_2_green",0)]],
  ["quality_carbatinae_blue", "carbatinae_1_blue", "Blue Quality Carbatinae", [("carbatinae_2_blue",0)]],
  ["quality_carbatinae_grey", "carbatinae_1_grey", "Grey Quality Carbatinae", [("carbatinae_2_grey",0)]],
  ["quality_carbatinae_orange", "carbatinae_1_orange", "Orange Quality Carbatinae", [("carbatinae_2_orange",0)]],
  ["quality_carbatinae_red", "carbatinae_1_red", "Red Quality Carbatinae", [("carbatinae_2_red",0)]],
], quality_carbatinae_subfix, "Quality Carbatinae")

rich_carbatinae_subfix = [
  itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 600,
  weight(1)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0),
  imodbits_cloth
]
rich_carbatinaes = create_items([
  ["rich_carbatinae_white", "decorated_leather_shoes", "White Rich Carbatinae"],
  ["rich_carbatinae_green", "decorated_leather_shoes_green", "Green Rich Carbatinae"],
  ["rich_carbatinae_blue", "decorated_leather_shoes_blue", "Blue Rich Carbatinae"],
  ["rich_carbatinae_grey", "decorated_leather_shoes_grey", "Grey Rich Carbatinae"],
  ["rich_carbatinae_orange", "decorated_leather_shoes_orange", "Orange Rich Carbatinae"],
  ["rich_carbatinae_red", "decorated_leather_shoes_red", "Red Rich Carbatinae"],
], rich_carbatinae_subfix, "Rich Carbatinae")

carbatinae_greaves_subfix = [
  itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 890,
  weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0),
  imodbits_armor
]
carbatinae_greaves = create_items([
  ["carbatinae_greaves_white", "carbatinae_1_greaves", "White Greaves", [("carbatinae_2_greaves",0)]],
  ["carbatinae_greaves_green", "carbatinae_1_greaves_green", "Green Greaves", [("carbatinae_2_greaves_green",0)]],
  ["carbatinae_greaves_blue", "carbatinae_1_greaves_blue", "Blue Greaves", [("carbatinae_2_greaves_blue",0)]],
  ["carbatinae_greaves_grey", "carbatinae_1_greaves_grey", "Grey Greaves", [("carbatinae_2_greaves_grey",0)]],
  ["carbatinae_greaves_orange", "carbatinae_1_greaves_orange", "Orange Greaves", [("carbatinae_2_greaves_orange",0)]],
  ["carbatinae_greaves_red", "carbatinae_1_greaves_red", "Red Greaves", [("carbatinae_2_greaves_red",0)]],
], carbatinae_greaves_subfix, "Greaves")

rich_greaves_subfix = [
  itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 980,
  weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(0),
  imodbits_armor
]
rich_greaves = create_items([
  ["rich_greaves_white", "decorated_leather_shoes_greaves", "White Rich Greaves"],
  ["rich_greaves_green", "decorated_leather_shoes_greaves_green", "Green Rich Greaves"],
  ["rich_greaves_blue", "decorated_leather_shoes_greaves_blue", "Blue Rich Greaves"],
  ["rich_greaves_grey", "decorated_leather_shoes_greaves_grey", "Grey Rich Greaves"],
  ["rich_greaves_orange", "decorated_leather_shoes_greaves_orange", "Orange Rich Greaves"],
  ["rich_greaves_red", "decorated_leather_shoes_greaves_red", "Red Rich Greaves"],
], rich_greaves_subfix, "Rich Greaves")

splinted_greaves_subfix = [
  itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 1040,
  weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0),
  imodbits_armor
]
splinted_greaves = create_items([
  ["splinted_leather_greaves", "splinted_greaves_a_bry", "Splinted Leather Greaves"],
  ["rus_splinted_greaves", "rus_splint_greaves", "Rus Splinted Greaves"],
], splinted_greaves_subfix, "Splinted Greaves")

