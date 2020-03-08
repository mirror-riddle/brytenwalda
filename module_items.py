from module_items_helper import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################


items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
 ["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile,missile_distance_trigger],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile,missile_distance_trigger],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile,missile_distance_trigger ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Round Shield", [("leathershield_small_b",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

 ["tutorial_dagger","Dagger", [("hunting_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],


 ["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],
# Items before this point are hardwired and their order should not be changed!
#cambiados chief
 ["practice_sword","Practice Sword", [("pattern_spatha",0),("sword_medieval_b_scabbard2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 900 , weight(1.25)|difficulty(1)|spd_rtng(82) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(10 ,  pierce),imodbits_none ],
 ["heavy_practice_sword","War Axe", [("05einhendi_haloygox",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
620 , weight(3)|difficulty(1)|spd_rtng(71) | weapon_length(100)|swing_damage(42 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["practice_dagger","Practice Dagger", [("hunting_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 60 , weight(0.5)|difficulty(0)|spd_rtng(97) | weapon_length(40)|swing_damage(11 , cut) | thrust_damage(11 ,  pierce),imodbits_none ],
 ["practice_axe", "Practice Axe", [("le_werkaxt1",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
457 , weight(2)|difficulty(1)|spd_rtng(77) | weapon_length(70)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ], #chief modificado
 ["arena_axe", "Axe", [("le_werkaxt1",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 300 , weight(1.5)|difficulty(0)|spd_rtng(77) | weapon_length(60)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["arena_sword", "Sword", [("pattern_spatha",0),("sword_medieval_b_scabbard2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 900 , weight(1.25)|difficulty(0)|spd_rtng(82) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(10 ,  pierce),imodbits_sword_high ],
 ["arena_sword_two_handed",  "War Axe", [("01tveirhendr_hedmarkox",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
620 , weight(3)|difficulty(1)|spd_rtng(71) | weapon_length(100)|swing_damage(42 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["arena_lance",         "Arena Spear", [("05krokaspjott1",0)],itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 420 , weight(4)|abundance(80)|difficulty(1)|spd_rtng(92) | weapon_length(160)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
 ["practice_staff","Practice Spear", [("05krokaspjott1",0)],itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 180 , weight(2.25)|difficulty(1)|spd_rtng(82) | weapon_length(145)|swing_damage(15 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm],
 ["practice_lance","Practice Spear", [("05krokaspjott1",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 180 , weight(2.25)|difficulty(1)|spd_rtng(82) | weapon_length(145)|swing_damage(15 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm],
 ["practice_shield","Practice Shield", [("leathershield_small_b",0)],  itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(4.5)|hit_points(400)|body_armor(6)|spd_rtng(55)|shield_width(70)|difficulty(0),imodbits_shield],
 ["practice_bow","Hunting Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)],itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back,
267 , weight(1)|difficulty(0)|spd_rtng(70) | shoot_speed(45) | thrust_damage(14 ,  pierce)|accuracy(65),imodbits_bow ], #chief cambiado
##                                                     ("hunting_bow",0)],                  itp_type_bow|itp_two_handed|itp_primary|itp_attach_left_hand, itcf_shoot_bow, 4,weight(1.5)|spd_rtng(90)|shoot_speed(40)|thrust_damage(19,blunt),imodbits_none],
 ["practice_crossbow", "Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
100, weight(2)|difficulty(0)|spd_rtng(60) | shoot_speed(28) | thrust_damage(21 ,  pierce)|max_ammo(6)|weapon_length(65),imodbits_thrown ],

 ["practice_javelin", "Practice Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
100, weight(2)|difficulty(0)|spd_rtng(60) | shoot_speed(28) | thrust_damage(21 ,  pierce)|max_ammo(6)|weapon_length(65),imodbits_thrown,missile_distance_trigger ], #chief cambiado max_ammo
 ["practice_javelin_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
100, weight(2)|difficulty(0)|spd_rtng(70) |swing_damage(4, cut)| thrust_damage(19,  pierce)|weapon_length(65),imodbits_polearm ], #chief cambiado
 ["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(6, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown,missile_distance_trigger ],
 ["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(6, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown ],
# ["cheap_shirt","Cheap Shirt", [("shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 4,weight(1.25)|body_armor(3),imodbits_none],
 ["practice_horse","Practice Horse", [("saddle_horse",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(35)|horse_maneuver(37)|horse_charge(8),imodbits_none],
 ["practice_arrows","Practice Arrows", [("arena_arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_default_ammo, itcf_carry_quiver_back, 100,weight(3)|abundance(110)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(60),imodbits_missile,missile_distance_trigger], #chief cambiado
## ["practice_arrows","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo)], itp_type_arrows, 0, 31,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],
 ["practice_bolts","Practice Dagger", [("hunting_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 60 , weight(0.5)|difficulty(0)|spd_rtng(97) | weapon_length(40)|swing_damage(11 , cut) | thrust_damage(11 ,  pierce),imodbits_none ],
 ["practice_arrows_10_amount","Practice Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(10),imodbits_missile,missile_distance_trigger],
 ["practice_arrows_100_amount","Practice Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_missile,missile_distance_trigger],
 ["practice_bolts_9_amount","Practice Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(9),imodbits_missile,missile_distance_trigger],
 ["practice_boots", "Practice Boots", [("carbatinae_2",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],
 ["red_tourney_armor","Red Tourney Armor", [("arena_tunicR_new",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["blue_tourney_armor","Blue Tourney Armor", [("arena_tunicB_new",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["green_tourney_armor","Green Tourney Armor", [("arena_tunicG_new",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["gold_tourney_armor","White Tourney Armor", [("arena_tunicW_new",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["red_tourney_helmet","Red Tourney Helmet",[("skull_cap_new_c",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["blue_tourney_helmet","Blue Tourney Helmet",[("leather_cap",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["green_tourney_helmet","Green Tourney Helmet",[("leather_cap",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["gold_tourney_helmet","Gold Tourney Helmet",[("skull_cap_new_c",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],

["arena_shield_red", "Shield", [("leathershield_medium",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  700 , weight(4.5)|hit_points(300)|body_armor(20)|spd_rtng(65)|shield_width(70)|difficulty(0),imodbits_shield ], #chief cambiado
["arena_shield_blue", "Shield", [("woodenshield_small_d",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  700 , weight(4.5)|hit_points(300)|body_armor(20)|spd_rtng(65)|shield_width(70)|difficulty(0),imodbits_shield ], #chief cambiado
["arena_shield_green", "Shield", [("leathershield_medium_b",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  700 , weight(4.5)|hit_points(300)|body_armor(20)|spd_rtng(65)|shield_width(70)|difficulty(0),imodbits_shield ], #chief cambiado
["arena_shield_yellow", "Shield", [("leathershield_medium_y",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  700 , weight(4.5)|hit_points(300)|body_armor(20)|spd_rtng(65)|shield_width(70)|difficulty(0),imodbits_shield ], #chief cambiado

["arena_armor_white", "Armor", [("arena_tunicW_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 600 , weight(4)|abundance(90)|head_armor(0)|body_armor(30)|leg_armor(0)|difficulty(0) ,imodbits_armor ], #cambiado chief
["arena_armor_red", "Armor", [("arena_tunicR_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 600 , weight(4)|abundance(90)|head_armor(0)|body_armor(30)|leg_armor(0)|difficulty(0) ,imodbits_armor ], #cambiado chief
["arena_armor_blue", "Armor", [("arena_tunicB_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 600 , weight(4)|abundance(90)|head_armor(0)|body_armor(30)|leg_armor(0)|difficulty(0) ,imodbits_armor ], #cambiado chief
["arena_armor_green", "Armor", [("arena_tunicG_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 600 , weight(4)|abundance(90)|head_armor(0)|body_armor(30)|leg_armor(0)|difficulty(0) ,imodbits_armor ], #cambiado chief
["arena_armor_yellow", "Armor", [("shirt_ylw",0)], itp_type_body_armor  |itp_covers_legs ,0, 600 , weight(4)|abundance(90)|head_armor(0)|body_armor(30)|leg_armor(0)|difficulty(0) ,imodbits_armor ], #cambiado chief
["arena_tunic_white", "Tunic White ", [("arena_tunicW_new",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 140 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(5)|leg_armor(2), imodbits_cloth ], #cambiado chief
["arena_tunic_red", "Tunic Red", [("arena_tunicR_new",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 140 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(5)|leg_armor(2), imodbits_cloth ],#cambiado chief
["arena_tunic_blue", "Tunic Blue", [("arena_tunicB_new",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 140 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(5)|leg_armor(2), imodbits_cloth ],#cambiado chief
["arena_tunic_green", "Tunic Green", [("arena_tunicG_new",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 140 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(5)|leg_armor(2), imodbits_cloth ],#cambiado chief
["arena_tunic_yellow", "Tunic Yellow", [("shirt_ylw",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 140 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(5)|leg_armor(2), imodbits_cloth ],#cambiado chief

#headwear
["arena_helmet_red", "Headwrapping", [("leather_cap",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0), imodbits_plate ], #cambiar chief
["arena_helmet_blue", "Headwrapping", [("leather_cap",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0), imodbits_plate ], #cambiar chief
["arena_helmet_green", "Headwrapping", [("leather_cap",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0), imodbits_plate ], #cambiar chief
["arena_helmet_yellow", "Headwrapping", [("leather_cap",0)], itp_type_head_armor|itp_fit_to_head   ,0, 400 , weight(1.75)|abundance(70)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ], #cambiar chief #cambiado chief
["steppe_helmet_white", "Headwrapping", [("leather_cap",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0), imodbits_plate ],  #cambiar chief
["steppe_helmet_red", "Cap Red", [("leather_cap",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0), imodbits_plate ],  #cambiar chief
["steppe_helmet_blue", "Cap Blue", [("leather_cap",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0), imodbits_plate ],  #cambiar chief
["steppe_helmet_green", "Cap Green", [("leather_cap",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0), imodbits_plate ],  #cambiar chief
["steppe_helmet_yellow", "Cap Yellow", [("leather_cap",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0), imodbits_plate ], #cambiar chief
["tourney_helm_white", "Tourney Helm", [("Rathos_Spangenhelm_a",0)], itp_type_head_armor|itp_fit_to_head,0, 600 , weight(2)|abundance(50)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ], #cambiar chief
["tourney_helm_red", "Tourney Helm", [("Rathos_Spangenhelm_a",0)], itp_type_head_armor|itp_fit_to_head,0, 600 , weight(2)|abundance(50)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ], #cambiar chief
["tourney_helm_blue", "Tourney Helm", [("Rathos_Spangenhelm_a",0)], itp_type_head_armor|itp_fit_to_head,0, 600 , weight(2)|abundance(50)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ], #cambiar chief
["tourney_helm_green", "Tourney Helm", [("Rathos_Spangenhelm_a",0)], itp_type_head_armor|itp_fit_to_head,0, 600 , weight(2)|abundance(50)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ], #cambiar chief
["tourney_helm_yellow", "Tourney Helm", [("Rathos_Spangenhelm_a",0)], itp_type_head_armor|itp_fit_to_head,0, 600 , weight(2)|abundance(50)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ], #cambiar chief
["arena_turban_red", "Cap", [("skull_cap_new_c",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0), imodbits_plate ], #cambiar chief
["arena_turban_blue", "Cap", [("skull_cap_new_c",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0), imodbits_plate ], #cambiar chief
["arena_turban_green", "Cap", [("skull_cap_new_c",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0), imodbits_plate ], #cambiar chief
["arena_turban_yellow", "Cap", [("skull_cap_new_c",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0), imodbits_plate ], #cambiar chief
#termina cambiado chief
# A treatise on The Method of Mechanical Theorems Archimedes
#chief cambiados libros
#This book must be at the beginning of readable books
 ["book_tactics","History of the Peloponnesian War", [("book_a",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
 ["book_persuasion","Rhetorica ad Herennium", [("book_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
 ["book_leadership","The Life of Alexander the Great", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none], #cambiar chief
 ["book_intelligence","Paedeia", [("book_e",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
 ["book_trade","Oeconomica, of Aristoteles", [("book_f",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
 ["book_weapon_mastery", "Polity of the Lacedaemonians, of Xenofonte", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_engineering","De architectura, of Vitrivius", [("book_open",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],

#Reference books
#This book must be at the beginning of reference books
 ["book_wound_treatment_reference","De Materia Medica, of Dioscorides", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_training_reference","Epitoma Rei Militaris", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_surgery_reference","Synopsis of Aelius Galenus", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
#chief cambiados libros acaba
#puesto chief quest
 ["relic","Vulgata Biblia", [("book_e",0)], itp_type_book, 0, 5000,weight(2)|abundance(10),imodbits_none],
 #other trade goods (first one is spice)
 ["spice","Spice", [("spice_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 780,weight(40)|abundance(10)|max_ammo(20),imodbits_none,[],[fac_kingdom_1]],
 ["salt","Salt", [("salt_sack",0)], itp_merchandise|itp_type_goods, 0, 305,weight(50)|abundance(120),imodbits_none,[],[fac_kingdom_6],[fac_kingdom_4],[fac_kingdom_16],[fac_kingdom_9],[fac_kingdom_11]],
#chief cambiado termina

 #["flour","Flour", [("salt_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 40,weight(50)|abundance(100)|food_quality(45)|max_ammo(50),imodbits_none],
#cambios chief
 ["oil","Oil", [("oil",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 650,weight(50)|abundance(10)|max_ammo(20),imodbits_none,[],[fac_kingdom_8]],

 ["pottery","Pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0, 200,weight(50)|abundance(90),imodbits_none,[],[fac_kingdom_4],[fac_kingdom_3],[fac_kingdom_5],[fac_kingdom_16],[fac_kingdom_11],[fac_kingdom_9],[fac_kingdom_15],[fac_kingdom_14]],

 ["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0, 280,weight(40)|abundance(90),imodbits_none,[],[fac_kingdom_4],[fac_kingdom_5],[fac_kingdom_17],[fac_kingdom_19],[fac_kingdom_27],[fac_kingdom_28],[fac_kingdom_29],[fac_kingdom_30],[fac_kingdom_31]],
 ["linen","Linen", [("linen",0)], itp_merchandise|itp_type_goods, 0, 365,weight(40)|abundance(50),imodbits_none,[],[fac_kingdom_28],[fac_kingdom_26],[fac_kingdom_15],[fac_kingdom_20]],

 ["wool","Wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0, 230,weight(40)|abundance(90),imodbits_none,[],[fac_kingdom_14],[fac_kingdom_15],[fac_kingdom_12],[fac_kingdom_13],[fac_kingdom_18],[fac_kingdom_20]],
 ["wool_cloth","Wool Cloth", [("wool_cloth",0)], itp_merchandise|itp_type_goods, 0, 300,weight(40)|abundance(90),imodbits_none,[],[fac_kingdom_12],[fac_kingdom_13],[fac_kingdom_18],[fac_kingdom_20]],

 ["raw_silk","Tile", [("raw_silk_bundle",0)], itp_merchandise|itp_type_goods, 0, 1000,weight(30)|abundance(10),imodbits_none,[],[fac_kingdom_16],[fac_kingdom_9],[fac_kingdom_11],[fac_kingdom_15],[fac_kingdom_14],[fac_kingdom_20],[fac_kingdom_18],[fac_kingdom_13],[fac_kingdom_12]],
 ["raw_dyes","Dyes", [("dyes",0)], itp_merchandise|itp_type_goods, 0, 400,weight(10)|abundance(50),imodbits_none,[],[fac_kingdom_3],[fac_kingdom_5],[fac_kingdom_11],[fac_kingdom_17],[fac_kingdom_28],[fac_kingdom_30]],
 ["velvet","Fine Cloth", [("velvet",0)], itp_merchandise|itp_type_goods, 0, 425,weight(40)|abundance(30),imodbits_none,[],[fac_kingdom_1],[fac_kingdom_2],[fac_kingdom_3],[fac_kingdom_5]],

 ["iron","Mineral", [("ore_iron",0)], itp_merchandise|itp_type_goods, 0,304,weight(60)|abundance(10),imodbits_none,[],[fac_kingdom_2],[fac_kingdom_7],[fac_kingdom_8],[fac_kingdom_6],[fac_kingdom_21],[fac_kingdom_22],[fac_kingdom_23],[fac_kingdom_24],[fac_kingdom_25],[fac_kingdom_26],[fac_kingdom_10]],
 ["stone","Stone", [("iron_bar",0)], itp_merchandise|itp_type_goods, 0,104,weight(60)|abundance(10),imodbits_none,[],[fac_kingdom_27],[fac_kingdom_28],[fac_kingdom_29],[fac_kingdom_30],[fac_kingdom_31],[fac_kingdom_17],[fac_kingdom_6],[fac_kingdom_7],[fac_kingdom_8]],
 ["tools","Tools", [("iron_hammer",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none,[],[fac_kingdom_2],[fac_kingdom_4],[fac_kingdom_5],[fac_kingdom_19],[fac_kingdom_22],[fac_kingdom_23],[fac_kingdom_24],[fac_kingdom_26],[fac_kingdom_9],[fac_kingdom_11]],

 ["raw_leather","Hides", [("leatherwork_inventory",0)], itp_merchandise|itp_type_goods, 0, 320,weight(40)|abundance(90),imodbits_none,[],[fac_kingdom_12],[fac_kingdom_13],[fac_kingdom_18],[fac_kingdom_20]],
 ["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0, 400,weight(40)|abundance(90),imodbits_none,[],[fac_kingdom_13],[fac_kingdom_18],[fac_kingdom_20]],

 ["raw_date_fruit","Silver", [("ore_silver",0)], itp_merchandise|itp_type_goods, 0, 320,weight(60)|abundance(10),imodbits_none,[],[fac_kingdom_6],[fac_kingdom_7],[fac_kingdom_8],[fac_kingdom_21],[fac_kingdom_22],[fac_kingdom_23],[fac_kingdom_24],[fac_kingdom_25],[fac_kingdom_26]],
 ["furs","Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0, 391,weight(40)|abundance(90),imodbits_none,[],[fac_kingdom_13],[fac_kingdom_18],[fac_kingdom_20]],

 ["wine","Wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 350,weight(30)|abundance(10)|food_quality(10)|max_ammo(40),imodbits_none,[],[fac_kingdom_1],[fac_kingdom_8]],
 ["ale","Beer", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 280,weight(30)|abundance(10)|food_quality(30)|max_ammo(50),imodbits_none,[],[fac_kingdom_4],[fac_kingdom_9]],
 ["mead","Mead", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 310,weight(30)|abundance(10)|food_quality(30)|max_ammo(50),imodbits_none,[],[fac_kingdom_11],[fac_kingdom_9],[fac_kingdom_21],[fac_kingdom_22],[fac_kingdom_26],[fac_kingdom_23],[fac_kingdom_25],[fac_kingdom_24],[fac_kingdom_10]],
#cambios chief acaban
# ["dry_bread", "wheat_sack", itp_type_goods|itp_consumable, 0, slt_none,view_goods,95,weight(2),max_ammo(50),imodbits_none],
#foods (first one is smoked_fish)
 #chief cambiado ammo x3
 ["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 90,weight(15)|abundance(110)|food_quality(50)|max_ammo(150),imodbits_none],
 ["cheese","Cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(6)|abundance(110)|food_quality(40)|max_ammo(90),imodbits_none],
 ["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 220,weight(5)|abundance(90)|food_quality(40)|max_ammo(90),imodbits_none],
 ["sausages","Sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 35,weight(10)|abundance(110)|food_quality(40)|max_ammo(120),imodbits_none],
 ["cabbages","Cabbages", [("cabbage",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 40,weight(15)|abundance(110)|food_quality(40)|max_ammo(150),imodbits_none],
 ["dried_meat","Dried Meat", [("smoked_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(15)|abundance(100)|food_quality(70)|max_ammo(150),imodbits_none],
 ["apples","Fruit", [("apple_basket",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 40,weight(20)|abundance(110)|food_quality(40)|max_ammo(150),imodbits_none],
 ["raw_grapes","Grapes", [("grapes_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 75,weight(40)|abundance(60)|food_quality(10)|max_ammo(30),imodbits_none], #x2 for wine
 ["raw_olives","Olives", [("olive_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 150,weight(40)|abundance(60)|food_quality(10)|max_ammo(30),imodbits_none], #x3 for oil
 ["grain","Grain", [("wheat_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 20,weight(30)|abundance(110)|food_quality(40)|max_ammo(150),imodbits_none],

 ["cattle_meat","Beef", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 120,weight(20)|abundance(100)|food_quality(80)|max_ammo(150),imodbits_none],
 ["bread","Bread", [("bread_a",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 20,weight(30)|abundance(110)|food_quality(40)|max_ammo(150),imodbits_none],
 ["chicken","Chicken", [("chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 65,weight(10)|abundance(110)|food_quality(40)|max_ammo(150),imodbits_none],
 ["pork","Pork", [("pork",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 89,weight(15)|abundance(100)|food_quality(70)|max_ammo(150),imodbits_none],
 ["butter","Butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 100,weight(6)|abundance(110)|food_quality(40)|max_ammo(90),imodbits_none],

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting chief Mod begin#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
 ["deer_meat","Venison", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(30)|abundance(100)|food_quality(40)|max_ammo(30),imodbits_none],
 ["boar_meat","Boar Meat", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 160,weight(30)|abundance(100)|food_quality(80)|max_ammo(50),imodbits_none],
 ["wolf_meat","Wolf Meat", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 30,weight(30)|abundance(100)|food_quality(30)|max_ammo(50),imodbits_none],
 ["coat_meat","Goat Meat", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(100)|food_quality(30)|max_ammo(50),imodbits_none],
 ["coat_2_meat","Goat Meat", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(100)|food_quality(30)|max_ammo(50),imodbits_none],
 ["wilddonkey_meat","Wild Donkey Meat", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 250,weight(30)|abundance(100)|food_quality(30)|max_ammo(50),imodbits_none],
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting chief Mod end#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#



 #Would like to remove flour altogether and reduce chicken, pork and butter (perishables) to non-trade items. Apples could perhaps become a generic "fruit", also representing dried fruit and grapes
 # Armagan: changed order so that it'll be easier to remove them from trade goods if necessary.
#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

# Quest Items

 ["siege_supply","Supplies", [("ale_barrel",0)], itp_type_goods, 0, 96,weight(40)|abundance(70),imodbits_none],
 ["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
 ["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],


# Tutorial Items

 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile,missile_distance_trigger],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile,missile_distance_trigger],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile,missile_distance_trigger ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Round Shield", [("leathershield_small_b",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],

####################HORSES chief caballos finales ##############################################################
#############################################################################################################
# Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.
  [
    "sumpter_horse","Pony", [("rus_horse",0)],
    itp_merchandise|itp_type_horse,0, 1800,
    abundance(50)|hit_points(60)|body_armor(10)|difficulty(1)|horse_speed(37)
    |horse_maneuver(36)|horse_charge(9)|horse_scale(86),imodbits_horse_basic
  ],

  *north_horses,

  *draft_horses,

  *paraveredus_horses,

  #Acorazados
  [
    "greek_armored_horse","Greek armored horse", [("HalfCata2",0)],
    itp_type_horse, 0, 3300,
    abundance(10)|body_armor(22)|hit_points(115)|difficulty(3)|horse_speed(37)|
    horse_maneuver(33)|horse_charge(19)|horse_scale(100),
    imodbits_horse_basic|imodbit_champion
  ],

  #burro2 chief
  [
    "donkey","Donkey", [("donkey_mount",0), ("donkey_mount2",0)],
    itp_merchandise|itp_type_horse, 0, 800,
    abundance(80)|hit_points(55)|body_armor(7)|difficulty(0)|horse_speed(32)|
    horse_maneuver(33)|horse_charge(8)|horse_scale(79),imodbits_horse_basic
  ],

  [
    "mule","Mule", [("mule",0)],
    itp_merchandise|itp_type_horse, 0, 1050,
    abundance(70)|hit_points(65)|body_armor(10)|difficulty(0)|horse_speed(35)|
    horse_maneuver(35)|horse_charge(8)|horse_scale(86),imodbits_horse_basic
  ],

###################caballos y monturas acaba finales chief####################################
###############################################################


##########FELCHAS CHIEF empieza finales #########################
 ####################################################################3
  [
    "arrows","Arrows", [
      ("arrow",0),
      ("flying_arrow",ixmesh_flying_ammo),
      ("quiver", ixmesh_carry)
    ],
    itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back,200,
    weight(3)|abundance(110)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(40),
    imodbits_missile,missile_distance_trigger
  ], #chief cambiado

  [
    "khergit_arrows","Byzantine Arrows", [
      ("arrow_b",0),
      ("flying_arrow_b",ixmesh_flying_ammo),
      ("spak_ar_bag", ixmesh_carry)
    ],
    itp_type_arrows|itp_unique, itcf_carry_quiver_back_right, 410,
    weight(3.5)|abundance(30)|weapon_length(95)|thrust_damage(3,pierce)|max_ammo(40),
    imodbits_missile,missile_distance_trigger
  ],

  [
    "fire_arrows","Fire Arrow", [
      ("arrow",0),
      ("flying_missile_fire",ixmesh_flying_ammo),
      ("quiver", ixmesh_carry)
    ],
    itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 200,
    weight(3)|abundance(110)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(40),
    imodbits_missile,missile_distance_trigger
  ], #chief cambiado

  [
    "bolts","Bolts", [
      ("bolt",0),
      ("flying_bolt",ixmesh_flying_ammo),
      ("bolt_bag", ixmesh_carry),
      ("bolt_bag_b", ixmesh_carry|imodbit_large_bag)
    ],
    itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield,
    itcf_carry_quiver_right_vertical, 164,
    weight(1)|abundance(50)|weapon_length(63)|thrust_damage(1,pierce)|max_ammo(30),
    imodbits_missile, [], pictish_kingdoms
  ], #chief cambiado

#################flechas chief finales acaba############################333
 ##################################################################


####OTROSSSSSSS##############
  [
    "pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_new",0)],
    itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 25 ,
    weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(2)|difficulty(0),
    imodbits_cloth
  ], #cambiado chief

  [
    "pilgrim_hood", "Pilgrim Hood", [("pil_hood",0)],
    itp_type_head_armor|itp_civilian, 0, 35,
    weight(1.25)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),
    imodbits_cloth
  ], #cambiado chief

# ARMOR
#handwear

##########Guantes empieza chief #################################
  [
    "leather_gloves","Leather Gloves", [("leather_gloves_L",0)],
    itp_merchandise|itp_type_hand_armor,0, 190,
    weight(0.25)|abundance(120)|body_armor(10)|difficulty(0),imodbits_cloth
  ],

#unique
  [
    "mail_mittens","Mail Mittens", [("mail_mittens_L",0)],
    itp_unique|itp_type_hand_armor,0, 390,
    weight(1.5)|abundance(10)|body_armor(20)|difficulty(0),imodbits_armor
  ],

##################Guantes acaba chief ###############################

###################Calzado botas empieza chief finales ###############################
###############################################################
######Calzado############
###Notas: irlandeses y pictos solo bare.
###Clase baja
#footwear
  [
    "wrapping_boots", "Wrapping Boots", [("wrapping_boots_a_bry",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,100,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth
  ],

  [
    "ankle_boots", "Ankle Boots", [("ankle_boots_a_new_bry",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,100,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief
#bare, piernas desnudas

  [
    "bare_legs_blue", "Leather shoes", [("bare_legs_blue",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,100,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth
  ],

  [
    "carbatinae_2_bare", "Bare Carbatinae", [("carbatinae_2_bare",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,100,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth
  ],

  [
    "carbatinae_1_bare", "Bare Carbatinae", [("carbatinae_1_bare",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,100,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth
  ],

#unidades medias
  [
    "decorated_leather_shoes_bare", "Bare Decorated leather shoes", [("bare_legs_blue",0)],
    itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,150,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth
  ],

  [
    "carbatinae_1", "White Quality Carbatinae", [("carbatinae_1",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,280,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "carbatinae_2", "White Quality Carbatinae", [("carbatinae_2",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,280,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "carbatinae_1_green", "Green Quality Carbatinae", [("carbatinae_1_green",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,280,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "carbatinae_2_green", "Green Quality Carbatinae", [("carbatinae_2_green",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,280,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "carbatinae_1_blue", "Blue Quality Carbatinae", [("carbatinae_1_blue",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,280,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "carbatinae_2_blue", "Blue Quality Carbatinae", [("carbatinae_2_blue",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,280,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "carbatinae_1_grey", "Grey Quality Carbatinae", [("carbatinae_1_grey",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,280,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "carbatinae_2_grey", "Grey Quality Carbatinae", [("carbatinae_2_grey",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,280,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "carbatinae_1_orange", "Orange Quality Carbatinae", [("carbatinae_1_orange",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,280,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "carbatinae_2_orange", "Orange Quality Carbatinae", [("carbatinae_2_orange",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian|itp_attach_armature,0,280,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "carbatinae_1_red", "Red Quality Carbatinae", [("carbatinae_1_red",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian | itp_attach_armature,0,280,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "carbatinae_2_red", "Red Quality Carbatinae", [("carbatinae_2_red",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,280,
    weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  #Clase alta civil
  [
    "decorated_leather_shoes", "White Rich Carbatinae", [("decorated_leather_shoes",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,600,
    weight(1)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "decorated_leather_shoes_green", "Green Rich Carbatinae", [("decorated_leather_shoes_green",0)],
    itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,600,
    weight(1)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "decorated_leather_shoes_blue", "Blue Rich Carbatinae", [("decorated_leather_shoes_blue",0)],
    itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,600,
    weight(1)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "decorated_leather_shoes_grey", "Grey Rich Carbatinae", [("decorated_leather_shoes_grey",0)],
    itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,600,
    weight(1)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "decorated_leather_shoes_orange", "Orange Rich Carbatinae", [("decorated_leather_shoes_orange",0)],
    itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,600,
    weight(1)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief

  [
    "decorated_leather_shoes_red", "Red Rich Carbatinae", [("decorated_leather_shoes_red",0)],
    itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,600,
    weight(1)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth
  ], #cambiado chief


  #Clase alta militar
  [
    "iron_greaves", "White Greaves", [("carbatinae_1_greaves",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor
  ],

  [
    "mail_boots", "White Greaves", [("carbatinae_2_greaves",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor
  ],

  [
    "light_leather_boots", "White Greaves", [("decorated_leather_shoes_greaves",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor
  ],

  [
    "carbatinae_1_greaves_green", "Green Greaves", [("carbatinae_1_greaves_green",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor
  ],

  [
    "carbatinae_2_greaves_green", "Green Greaves", [("carbatinae_2_greaves_green",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor
  ],

  [
    "carbatinae_1_greaves_blue", "Blue Greaves", [("carbatinae_1_greaves_blue",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor
  ],

  [
    "carbatinae_2_greaves_blue", "Blue Greaves", [("carbatinae_2_greaves_blue",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor
  ],

  [
    "carbatinae_1_greaves_grey", "Grey Greaves", [("carbatinae_1_greaves_grey",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 ,
     weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor
  ],

  [
    "carbatinae_2_greaves_grey", "Grey Greaves", [("carbatinae_2_greaves_grey",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor
  ],

  [
    "carbatinae_1_greaves_orange", "Orange Greaves", [("carbatinae_1_greaves_orange",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor
  ],

  [
    "carbatinae_2_greaves_orange", "Orange Greaves", [("carbatinae_2_greaves_orange",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor
  ],

  [
    "carbatinae_2_greaves_red", "Red Greaves", [("carbatinae_2_greaves_red",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor
  ],

  [
    "splinted_greaves", "Red Greaves", [("carbatinae_1_greaves_red",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor
  ],

  [
    "splinted_leather_greaves", "Splinted Leather Greaves", [("splinted_greaves_a_bry",0)],
    itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 910 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(26)|difficulty(0) ,imodbits_armor
  ],
  #greaves elite nobles solo
  [
    "mail_chausses", "Rus Splinted Greaves", [("rus_splint_greaves",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 980 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(0) ,imodbits_armor
  ],

  [
    "decorated_leather_shoes_greaves_green", "Green Rich Greaves", [("decorated_leather_shoes_greaves_green",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 920 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(26)|difficulty(0) ,imodbits_armor
  ],

  [
    "decorated_leather_shoes_greaves_blue", "Blue Rich Greaves", [("decorated_leather_shoes_greaves_blue",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 920 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(26)|difficulty(0) ,imodbits_armor
  ],

  [
    "decorated_leather_shoes_greaves_grey", "Grey Rich Greaves", [("decorated_leather_shoes_greaves_grey",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 920 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(26)|difficulty(0) ,imodbits_armor
  ],

  [
    "decorated_leather_shoes_greaves_orange", "Orange Rich Greaves", [("decorated_leather_shoes_greaves_orange",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 920 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(26)|difficulty(0) ,imodbits_armor
  ],

  [
    "leather_boots", "Red Rich Greaves", [("decorated_leather_shoes_greaves_red",0)],
    itp_merchandise|itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 920 ,
    weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(26)|difficulty(0) ,imodbits_armor
  ],

####Calzado acaba chief finales ###############################################
######################################################################

###Pictish and irish long tunic para druidas, bajos jefes y bajos nobles
  *pictish_long_tunics,

  #irish
  *irish_long_tunics,

  *godelic_jackets,

  *worn_robes,

  ###cristianos
  [
    "blue_gambeson", "Monk Robe", [("priest_1",0)],
    itp_type_body_armor|itp_covers_legs|itp_civilian,0,170,
    weight(4)|abundance(50)|head_armor(0)|body_armor(11)|leg_armor(5)|difficulty(0) ,imodbits_cloth
  ],

  [
    "red_gambeson", "Bishop Robe", [("priest_3",0)],
    itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 975,
    weight(5)|abundance(10)|head_armor(0)|body_armor(13)|leg_armor(5)|difficulty(0) ,imodbits_cloth
  ],

  #Otros
  [
    "padded_cloth", "Galeno's Tunic", [("surgeon",0)],
    itp_type_body_armor|itp_covers_legs, 0, 197,
    weight(7)|abundance(10)|head_armor(0)|body_armor(7)|leg_armor(2)|difficulty(0) ,imodbits_cloth
  ],

#####tunicas largas acaba chief##############
###########################################

##########tunicas cortas finales################
 #############################################

#Con capa para elite o lores
#Britones
 ["steppe_outfit", "Cloaked Tunic", [("BL_NT_Blue06COAT",0)], itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth , #cambiado chief
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["cloaked_tunic", "Cloaked Tunic", [("BL_NT_Green11COAT",0)], itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth , #cambiado chief
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["sleeveless_leather_tunic", "Cloaked Tunic", [("BL_NT_Red12COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth , #cambiado chief
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#pictos
["nordic_outfit", "Cloaked Tunic", [("BL_NT_Blue04COAT",0)], itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth , #cambiado chief
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["nordic_outfit2", "Cloaked Tunic", [("BL_NT_Blue08COAT",0)], itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth , #cambiado chief
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["sleeveless_tunic", "Cloaked Tunic", [("BL_NT_Red04COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth , #cambiado chief
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#lo mismo para irlandeses
["nordic_armor", "Cloaked Tunic", [("BL_NT_Blue11COAT",0)], itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth , #cambiado chief
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["hide_armor", "Cloaked Tunic", [("BL_NT_Green10COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth , #cambiado chief
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
##tunicas normales para pictos e irlandeses
 ["dane_tunic1", "Red Tunic", [("BL_NT_Red04",0)],itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 210 , weight(2)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2)|difficulty(0) ,imodbits_cloth , #cambiado chief
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["wessex_tunic1", "Woolen Tunic", [("woolen_tunic_a",0)],itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 210 , weight(2)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2)|difficulty(0) ,imodbits_cloth , #cambiado chief
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["pict_tunic5", "Woolen Tunic ", [("woolen_tunic_c",0)],itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 210 , weight(2)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2)|difficulty(0) ,imodbits_cloth , #cambiado chief
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["pict_tunic6", "Short Tunic ", [("BL_NT_Blue07",0)],itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 210 , weight(2)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2)|difficulty(0) ,imodbits_cloth , #cambiado chief
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["pict_tunic7", "Short Tunic ", [("BL_NT_Green03",0)], itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 210 , weight(2)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2)|difficulty(0) ,imodbits_cloth , #cambiado chief
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#para pobres irlandeses y pictos
 ["bl_tunicsr02_2", "Cloak Dirty Tunic", [("BL_TunicR02_2",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["bl_tunicsr03", "Cloak Red Tunic", [("BL_TunicR03",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["bl_tunicsr03_2", "Red Tunic", [("BL_TunicR03_2",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],


#tunicas simples para todos
["shirt", "Shirt", [("shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 110 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ], #cambiado chief
["roman_shirt", "Poor Shirt", [("roman_shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 110 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ], #cambiado chief
["bl_tunicsr01", "Poorman Tunic", [("BL_TunicR01",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ],
["bl_tunicsr01_2", "Cloak Poorman Tunic", [("BL_TunicR01_2",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ],
["bl_tunicsr02", "Dirty Tunic", [("BL_TunicR02",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ],

["shirtb", "Green tunic", [("shirtb",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ],
["shirtc", "White tunic", [("shirtc",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ],
["shirtd", "Blue tunic", [("shirtd",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ],
["shirte", "Dirty tunic", [("shirte",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ],

#todos clase media
 ["armor_8", "Blue Tunic", [("armor_8",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth],
 ["armor_9", "Narrow Tunic", [("armor_9",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth],
["linen_tunic", "Linen Tunic", [("shirt_a_bry",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth],
#repetimos aqui
["short_tunic", "Tunic", [("shirt_a_bry",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth],
 ["red_tunic", "Red Tunic", [("arena_tunicR_new",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth],
 ["green_tunic", "Green Tunic", [("arena_tunicG_new",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth],
 ["blue_tunic", "Blue Tunic", [("arena_tunicB_new",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth],
 ["leather_steppe_cap_a", "Narrow Tunic", [("arena_tunicY_new",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth],
 ["woolen_hood", "White Tunic", [("arena_tunicW_new",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth],

 #peasant con capucha britones, e invadores
["peasant_archer", "Farmer tunic", [("peasant_archer",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(50)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
["armor_26", "Farmer tunic", [("armor_26",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(50)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
["armor_27", "Farmer tunic", [("armor_27",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(50)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
["peasant_man_c", "Farmer tunic", [("peasant_man_c",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(50)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
["peasant_man_d", "Farmer tunic", [("peasant_man_d",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(50)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
["peasant_man_e", "Farmer tunic", [("peasant_man_e",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(50)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
["peasant_man_f", "Farmer tunic", [("peasant_man_f",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(50)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
["leather_jerkin", "Farmer tunic", [("peasant_man_b",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(50)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],

#Vendedores
["coarse_tunic1", "Merchant White Tunic", [("coarse_tunic_wt",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(3), imodbits_cloth ],
["coarse_tunic2", "Merchant Red Tunic", [("coarse_tunic_rd",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(3), imodbits_cloth ],
["coarse_tunic3", "Merchant Green Tunic", [("coarse_tunic_verde",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 800 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(3), imodbits_cloth ],
["coarse_tunic4", "Merchant Brown Tunic ", [("coarse_tunic_brn",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(3), imodbits_cloth ],
["coarse_tunic5", "Merchant Yellow Tunic", [("coarse_tunic_ylw",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(3), imodbits_cloth ],
["coarse_tunic_blu", "Merchant Blue Tunic", [("coarse_tunic_blu",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(3), imodbits_cloth ],
["coarse_tunic_grn", "Merchant Green Tunic", [("coarse_tunic_grn",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(3), imodbits_cloth ],
["coarse_tunic_red", "Merchant Rich Tunic", [("coarse_tunic_vlt",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(3), imodbits_cloth ],
["coarse_tunic", "Merchant Poor Tunic", [("coarse_tunic_a_bry",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(3), imodbits_cloth ],
["leather_apron", "Leather Apron", [("leather_apron",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 161 , weight(3)|abundance(100)|head_armor(0)|body_armor(3)|leg_armor(3)|difficulty(0) ,imodbits_cloth ], #cambiado chief
#usar tb: coarse_tunic (para vendedor pobre), leather_apron (taberneros),



###clase alta o elite pictos o irlandeses
 #clase alta, tunicas de cuadros con capas atras
#pictos
["braz", "Long Pictish Tunic", [("braz",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(30)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], [fac_kingdom_20]],
["czerwony", "Pictish Tunic", [("czerwony",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(30)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], [fac_kingdom_20]],
["gairlom", "Pictish Tunic", [("vaelicus_t_5",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(30)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], [fac_kingdom_20]],
["tuniczka", "Pictish Tunic", [("byrnie_a_tunic_d",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(20)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], [fac_kingdom_20]],
["yellow2", "Pictish Tunic", [("vaelicus_t_5",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(20)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], [fac_kingdom_20]],
["yellow1", "Pictish Tunic", [("vaelicus_t_9",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(20)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], [fac_kingdom_20]],
["vaelicus_t_9", "Pictish Tunic", [("byrnie_a_tunic_c",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(20)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], [fac_kingdom_20]],
#irlandeses
["vaelicus_t_16", "Godelic Tunic", [("byrnie_a_tunic",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(20)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], [fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vaelicus_t_19", "Godelic Tunic", [("byrnie_a_tunic_b",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(20)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], [fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vaelicus_t_21", "Godelic Tunic", [("vaelicus_t_21",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(20)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], [fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vaelicus_t_25", "Godelic Tunic", [("byrnie_a_tunic_e",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(20)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], [fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vaelicus_t_26", "Godelic Tunic", [("vaelicus_t_26",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(20)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], [fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vaelicus_t_27", "Godelic Tunic", [("vaelicus_t_27",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(20)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], [fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#con pelo
["vaelicus_t_35", "Godelic Fur Tunic", [("vaelicus_t_35",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 620 , weight(1)|abundance(20)|head_armor(0)|body_armor(13)|leg_armor(3), imodbits_cloth,
[], [fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vaelicus_t_36", "Godelic Fur Tunic", [("vaelicus_t_36",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 620 , weight(1)|abundance(20)|head_armor(0)|body_armor(13)|leg_armor(3), imodbits_cloth,
[], [fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],


#Tunica abierta arriba, clase media y baja
 #irlandeses
["tunic_a", "Godelic Tunic", [("tunic_a",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["tunic_c", "Godelic Tunic", [("tunic_c",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vaelicus_tunic_3", "Godelic Tunic", [("vaelicus_tunic_3",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vaelicus_tunic_6", "Godelic Tunic", [("vaelicus_tunic_6",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vaelicus_tunic_8", "Godelic Tunic", [("vaelicus_tunic_8",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vaelicus_tunic_9", "Godelic Tunic", [("vaelicus_tunic_9",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#Pictos
["tunic_b", "Pictish Tunic", [("tunic_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]],
["vaelicus_tunic_1", "Pictish Tunic", [("vaelicus_tunic_1",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]],
["vaelicus_tunic_2", "Pictish Tunic", [("vaelicus_tunic_2",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]],
["vaelicus_tunic_4", "Pictish Tunic", [("vaelicus_tunic_4",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]],
["vaelicus_tunic_5", "Pictish Tunic", [("vaelicus_tunic_5",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]],
["vaelicus_tunic_7", "Pictish Tunic", [("vaelicus_tunic_7",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]],
["vaelicus_tunic_10", "Pictish Tunic", [("vaelicus_tunic_10",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]],
["vaelicus_tunic_11", "Pictish Tunic", [("vaelicus_tunic_11",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]],
["vaelicus_tunic_12", "Pictish Tunic", [("vaelicus_tunic_12",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], [fac_kingdom_20]],



#clase baja irlandeses tunica corta
 ["koszula_gaelicka", "Irish Tunic", [("koszula_gaelicka",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#clase media alta irlandesa
 ["bl_tunic05", "Godelic Rich Tunic", [("BL_Tunic05",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["bl_tunic06", "Godelic Rich Tunic", [("BL_Tunic06",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["bl_tunic07", "Godelic Rich Tunic", [("BL_Tunic07",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["bl_tunic08", "Godelic Rich Tunic", [("BL_Tunic08",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["bl_tunic11", "Godelic Rich Tunic", [("BL_Tunic11",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],


#britones
 #clase media
["shirt_blu", "Blue Tunic", [("shirt_blu",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["shirt_grn", "Green Tunic", [("shirt_grn",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["shirt_ylw", "Yellow Tunic", [("shirt_ylw",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["shirt_tel", "Briton Tunic", [("shirt_tel",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["shirt_blk", "Briton Tunic", [("shirt_blk",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["bl_tunic02", "Briton Green Tunic", [("BL_Tunic02",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
#elite o alta
["shirt_red", "Blue Tunic", [("shirt_red",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["bl_tunic01", "Rich Blue Tunic", [("BL_Tunic01",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["bl_tunic04", "Rich Tunic", [("BL_Tunic04",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["bl_tunic09", "Rich Red Tunic", [("BL_Tunic09",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["bl_tunic10", "Rich Blue Tunic", [("BL_Tunic10",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],

#rey briton o mejor para el tipo del muro de hadriano
["romantunic_purple", "Tunic Purple", [("romantunic_purple",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 450 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(5)|leg_armor(2)|difficulty(0), imodbits_cloth ],

##invasores####
#clase baja
 ["fattiglinenskjortir", "Blue Shirt", [("fattiglinenskjortir",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["mercia_tunic1", "Mercia Tunic", [("BL_NT_Green01",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["blue_short_tunic", "Short Tunic", [("BL_NT_Blue01",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["wessex_tunic3", "Saxon Tunic", [("BL_NT_Red01",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["bl_tunicsleather", "Rustic Tunic", [("BL_TunicLeather",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["bl_tunicsleather_2", "Rustic Tunic", [("BL_TunicLeather_2",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["bl_tunicsleather_3", "Cloak Rustic Tunic", [("BL_TunicLeather_3",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

 ###clase media
["bl_tunic03", "Red Tunic", [("BL_Tunic03",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["bluevikingshirt", "Blue Shirt", [("bluevikingshirt",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["redvikingshirt", "Linen Shirt", [("redvikingshirt",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["blue_short_tunic2", "Linen Tunic", [("linen_tunic_a",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["mercia_tunic10", "Linen Tunic", [("linen_tunic_b",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["wessex_tunic4", "Linen Tunic", [("linen_tunic_c",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["redtunic", "Woolen Tunic", [("woolen_tunic_b",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
#usamos tb: arena_tunic_red, arena_tunic_blue,arena_tunic_green,arena_tunic_yellow (son tunicas para clase media o alta)
#clase alta
["noblemanshirt", "Nobleman Shirt", [("noblemanshirt",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 260 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(3), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["noblemanshirt_gaelic", "Nobleman Shirt", [("noblemanshirt_gaelic",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 260 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(3), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["noblemanshirt_pictish", "Nobleman shirt", [("noblemanshirt_pictish",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 260 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(3), imodbits_cloth ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],


#tunicas con capa para nobles
#invasores
 ["nordiclightarmor1", "Noble Tunic", [("nordiclightarmor61",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 1000 , weight(10)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(8), imodbits_cloth ],
 ["nordiclightarmor2", "Noble Tunic", [("nordiclightarmor62",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 1000 , weight(10)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(8), imodbits_cloth ],
 ["nordiclightarmor3", "Noble Tunic", [("nordiclightarmor64",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 1000 , weight(10)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(8), imodbits_cloth ],
#britones
 ["nordiclightarmor10", "Noble Tunic", [("nordiclightarmor66",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 1000 , weight(10)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(8), imodbits_cloth ],
 ["nordiclightarmor11", "Noble Tunic", [("nordiclightarmor65",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 1000 , weight(10)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(8), imodbits_cloth ],
 ["nordiclightarmor12", "Noble Tunic", [("nordiclightarmor63",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 1000 , weight(10)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(8), imodbits_cloth ],
#irlandeses y pictos
 ["nordiclightarmor4", "Noble Tunic", [("nordiclightarmor4",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 1000 , weight(10)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(8), imodbits_cloth ],
 ["nordiclightarmor5", "Noble Tunic", [("nordiclightarmor5",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 1000 , weight(10)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(8), imodbits_cloth ],
 ["nordiclightarmor6", "Noble Tunic", [("nordiclightarmor6",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 1000 , weight(10)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(8), imodbits_cloth ],
 ["nordiclightarmor7", "Noble Tunic", [("nordiclightarmor41",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 1000 , weight(10)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(8), imodbits_cloth ],
 ["nordiclightarmor8", "Noble Tunic", [("nordiclightarmor51",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 1000 , weight(10)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(8), imodbits_cloth ],
# ["nordiclightarmor9", "Noble Tunic", [("nordiclightarmor9",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 1300 , weight(10)|abundance(50)|head_armor(0)|body_armor(35)|leg_armor(0)|difficulty(11), imodbits_armor ],


#tunicas cortas finales acaba###############
 ############################################


######vestuario mujeres chief finales
 #mujeres todas las razas plebeyas campesinas, villages
["blue_tunic_long", "Long Shirt", [("vae_tunica_larga5",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["lady_dress_ruby", "Long Shirt", [("vae_tunica_larga6",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["woolen_dress", "Woolen Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 130 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(2)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["peasant_dress_b_new", "Woman Dress", [("peasant_dress_b_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 130 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(2)|difficulty(0) ,imodbits_cloth ], #cambiado chief

########mujeres####################
#tunicas largas pictos mujeres plebeyas campesinas
["blue_tunic2", "Long Shirt", [("vae_tunica_larga5",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["pict_long_tunic1", "Long Shirt", [("vae_tunica_larga1",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["pict_long_tunic2", "Long Shirt", [("vae_tunica_larga2",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["pict_long_tunic3", "Long Shirt", [("vae_tunica_larga3",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["pict_long_tunic4", "Long Shirt", [("vae_tunica_larga4",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["lady_dress_green", "Long Shirt", [("vae_tunica_larga7",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["lady_dress_blue", "Long Shirt", [("vae_tunica_larga8",0)],itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],


#todas las razas, veils para cabezas
#simple
["sarranid_head_cloth", "Pink Veil", [("veil_a",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veil_b", "Blue Veil", [("veil_b",0)],  itp_type_head_armor | itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veil_d", "Wool Veil", [("veil_d",0)],  itp_type_head_armor | itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veil_c", "Dark Blue Veil", [("veil_c",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veil_e", "White Veil", [("veil_e",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veil_f", "Green Veil", [("veil_f",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veil_g", "Grey Veil", [("veil_g",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#el amplio , senoras
["sarranid_felt_head_cloth", "Veil", [("common_veil_a",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["common_veil_b", "Grey Veil", [("common_veil_b",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["common_veil_d", "Narrow Veil", [("common_veil_d",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["common_veil_c", "Orange Veil", [("common_veil_c",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["common_veil_e", "Wool Veil", [("common_veil_e",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#mujeres cabeza campesinas irlandesas
["wimple_a", "Wimple", [("wimple_a_new_bry",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,90, weight(0.5)|abundance(10)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth], #chief cambiado
["wimple_with_veil", "Wimple with Veil", [("wimple_b_new_bry",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,90, weight(0.5)|abundance(10)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth], #chief cambiado

#britonas
["red_dress", "Briton Dress", [("briton_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
 ["brown_dress", "Blue Dress", [("briton_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["green_dress", "Wool Dress", [("briton_dress_c",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress", "Woman Dress", [("briton_dress_d",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress_b", "Woman Dress", [("briton_dress_e",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],

#nobles mujeres invasoras
["kenttunik", "Woman Dress", [("kenttunik",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["tunikwjac1", "Woman Dress", [("tunikwjac1",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],

#pictas e irlandesas
["sarranid_dress_a", "Woman Dress", [("pictishdressazul",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_dress_b", "Woman Dress", [("pictishdress2",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["pictishdress3", "Woman Dress", [("pictishdress3",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["pictishdress1", "Woman Dress", [("pictishdress1",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["pictishdressverde", "Woman Dress", [("pictishdressverde",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["pictishdress", "Woman Dress", [("pictishdress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
####mujeres ropa acaba############
 #####################################

#Pictos

#####desnudos pictos finales#############
 ###########################################
["war_paint_two", "Pictish naked", [("war_paint_two",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintus", "Pictish naked", [("war_paintus",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["1celtbody", "Pictish naked", [("BL_Body08_male",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["2celtbody", "Pictish naked", [("2celtbody",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["3celtbody", "Pictish naked", [("3celtbody",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["5celtbody", "Pictish naked", [("5celtbody",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["6celtbody", "Pictish naked", [("6celtbody",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paint_two_5", "Pictish naked", [("BL_Body01_male",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paint_two_2", "Pictish naked", [("BL_Body02_male",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintus_2", "Pictish naked", [("BL_Body03_male",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintus_3", "Pictish naked", [("war_paintus_3",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintus_4", "Pictish naked", [("war_paintus_4",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintus_5", "Pictish naked", [("BL_Body04_male",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintus_6", "Pictish naked", [("BL_Body07_male",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintus_7", "Pictish naked", [("war_paintus_7",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintus_8", "Pictish naked", [("war_paintus_8",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintus_10", "Pictish naked", [("war_paintus_10",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintus_11", "Pictish naked", [("war_paintus_11",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintus_12", "Pictish naked", [("BL_Body09_male",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
#gordos
["picto_gordo1", "Big Pictish naked", [("picto_gordo1",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["picto_gordo2", "Big Pictish naked", [("picto_gordo2",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["picto_gordo3", "Big Pictish naked", [("picto_gordo3",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
#mujeres
["picta_1", "Pictish woman naked", [("picta1",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["picta_2", "Pictish woman naked", [("picta2",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["picta_3", "Pictish woman naked", [("picta3",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["picta_4", "Pictish woman naked", [("picta4",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["picta_5", "Pictish woman naked", [("picta1",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["picta_6", "Pictish woman naked", [("picta2",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["picta_7", "Pictish woman naked", [("picta3",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["picta_8", "Pictish woman naked", [("picta4",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["picta_9", "Pictish woman naked", [("picta3",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["picta_10", "Pictish woman naked", [("picta4",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],


#pictos desnudos con capa y pantalon (pictos)
["linen_shirt", "Cloaked Body", [("BL_Celts01COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 180 , weight(5)|abundance(60)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["wool_coat", "Cloaked Body", [("BL_Celts02COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 180 , weight(5)|abundance(60)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["dress", "Cloaked Body", [("BL_Celts03COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 180 , weight(5)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(6)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["blue_dress", "Cloaked Body", [("BL_Celts04COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 180 , weight(5)|abundance(60)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["tabard", "Cloaked Body", [("BL_Celts05COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 180 , weight(5)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(6)|difficulty(0) ,imodbits_cloth ], #cambiado chief
#irlandeses
["leather_vest", "Cloaked Body", [("BL_Celts06COAT",0)], itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 900 , weight(5)|abundance(10)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0) ,imodbits_cloth, #cambiado chief
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["steppe_armor", "Cloaked Body", [("BL_Celts07COAT",0)],itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 900 , weight(5)|abundance(10)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0) ,imodbits_cloth, #cambiado chief
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["gambeson", "Cloaked Body", [("BL_Celts08COAT",0)],itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 880 , weight(5)|abundance(10)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0) ,imodbits_cloth, #cambiado chief
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#chief acaba

#pantalones sin camisa chief, irlandeses
["coat", "Green Pants", [("BL_Celts06",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 400 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["leather_coat", "Red Pants", [("BL_Celts07",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 400 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["mail_coat", "Blue Pants", [("BL_Celts08",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 400 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

#pantalones con pintura,  pictos
["long_mail_coat", "Blue Pants", [("BL_Celts05",0)], itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],
["mail_with_tunic_red", "Red Pants", [("BL_Celts04",0)], itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],
["mail_with_tunic_green", "Blue Pants", [("BL_Celts03",0)], itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],
["hide_coat", "Green Pants", [("BL_Celts02",0)], itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],
["merchant_outfit", "Narrow Pants", [("BL_Celts01",0)], itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],
["homespun_dress", "Blue Pants", [("BL_Celts10",0)], itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],
["thick_coat", "Red Pants", [("BL_Celts11",0)], itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],
["coat_with_cape", "Blue Pants", [("BL_Celts12",0)], itp_type_body_armor  |itp_covers_legs ,0, 100 , weight(0.5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],

################desnudos pictos finales#####################
 ###############################################################



##############ROPA acaba chief #############################################################


############# ARMOR armadura chief finales empieza ###############################################
###################################################################################################

#malla cubre pecho, y piernas, son largas, valen para pictos e irlandeses
["mail_coat_1", "Brown Kingly Mail", [("mail_vest_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10160 , weight(22)|abundance(2)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(14) ,imodbits_armor,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["mail_coat_2", "Blue Kingly Mail", [("mail_vest_blu",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10160 , weight(22)|abundance(2)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(14) ,imodbits_armor,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["mail_coat_3", "Red Kingly Mail", [("mail_vest_red",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10160 , weight(22)|abundance(2)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(14) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["mail_coat_4", "White Kingly Mail", [("mail_vest_wht",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10160 , weight(22)|abundance(2)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(14) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["mail_coat_5", "Green Kingly Mail", [("mail_vest_grn",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10160 , weight(22)|abundance(2)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(14) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["mail_coat_6", "Dark Kingly Mail", [("mail_vest_blk",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10160 , weight(22)|abundance(2)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(14) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
###solo nobles irlandeses o pictos
["hauberk5", "Long Mail Coat", [("mail_hauberk_jco",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 8000 , weight(23)|abundance(10)|head_armor(0)|body_armor(49)|leg_armor(23)|difficulty(13) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],



####mail coat para todos
["hauberk6", "Mail Coat", [("mail_coat_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mail_shirt_bluehorses", "Mail Coat", [("mail_coat_b",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mail_shirt_blueunicorn", "Mail Coat", [("mail_coat_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4060 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(12)|difficulty(14) ,imodbits_armor ],
["mail_shirt_brown", "Mail Coat", [("mail_coat_d",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mail_shirt_green", "Mail Coat", [("mail_coat_e",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(14) ,imodbits_armor ],
["mail_shirt_greenhorses", "Mail Coat", [("mail_coat_f",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mail_shirt_red", "Black Mail Coat", [("mail_coat_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(12)|difficulty(14) ,imodbits_armor ],
["mail_shirt_reddragon", "Brown Mail Coat", [("mail_coat_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mail_shirt_redhorses", "Dark Mail Coat", [("mail_coat_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mail_shirt_whiteaxes", "Mail Coat", [("mail_coat_4",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4060 , weight(19)|abundance(30)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(14) ,imodbits_armor ],
["mail_shirt_whiteraven", "Brown Mail Coat", [("mail_shirt_brown",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(12)|difficulty(14) ,imodbits_armor ],
["mail_shirt_green", "Green Mail Coat", [("mail_shirt_green",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mail_shirt_red", "Red Mail Coat", [("mail_shirt_red",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mail_shirt_a_copy", "Red Mail Coat", [("mail_shirt_a_copy",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["heraldic_mail_with_tunic", "Cheap Mail Coat", [("mail_shirt_a_oscuro",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4560 , weight(19)|abundance(30)|head_armor(0)|body_armor(43)|leg_armor(13)|difficulty(12) ,imodbits_armor ],
["hauberk_a_new", "Cheap Mail Coat", [("hauberk_a_new",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4680 , weight(19)|abundance(30)|head_armor(0)|body_armor(43)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
#Cota de malla cubre pecho y piernas, la usamos para nobles de bajo nivel y tropas de elite de todas las facciones, para britones mirar casos concretos, ya que muchos luchaban sin armadura
["mail_shirt_grn", "Green Mail Coat", [("mail_shirt_grn",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mail_shirt_red", "Red Mail Coat", [("mail_shirt_red",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mail_shirt_ylw", "Olive Mail Coat", [("mail_shirt_ylw",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mail_shirt_blk", "Grey Mail Coat", [("mail_shirt_blk",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mail_shirt_wht", "White Mail Coat", [("mail_shirt_wht",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
###mail coat para elite britona, nobles, gran calidad
["swadian_mail_hauberk", "Black Mail Coat", [("swadian_mail_hauberk",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5500 , weight(19)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(12)|difficulty(12) ,imodbits_armor ],
["wei_xiadi_sar_hauberk", "Blue Mail Coat", [("wei_xiadi_sar_hauberk",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5700 , weight(19)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["coat_of_plates", "Furred Smallring Mail", [("rough_smallring_fured",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4600 , weight(19)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(13)|difficulty(10) ,imodbits_armor ],


# malla cubre pecho y piernas, mas bonita, y mejor elaborada, con bolsa. SOLO NOBLES y super elite, no venta en mercados. SAJONES
["mail_coat_1_trig", "Blue Noble Mail", [("BL_VikingByrnie03",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["mail_coat_2_trig", "Red Noble Mail", [("BL_VikingByrnie01",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["mail_shirtdeer", "Green Noble Mail", [("BL_VikingByrnie04",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["nowa", "Brown Noble Mail", [("BL_VikingByrnie12",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["byrnie_b_new", "Green Noble Mail", [("BL_VikingByrnie02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["byrnie_e_new", "Brown Noble Mail", [("BL_VikingByrnie09",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["byrnie_f_new", "Brown Noble Mail", [("BL_VikingByrnie13",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["byrnie2", "Noble Mail", [("BL_VikingByrnie06",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 #byrnies con ropa a cuadros para irlandeses y pictos elite y nobles
["byrnie1", "Green Noble Mail", [("BL_VikingByrnie07",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["byrnie3", "Noble Mail", [("BL_VikingByrnie08",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["lorika", "Brown Noble Mail", [("BL_VikingByrnie15",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["mail_shirtred", "Brown Noble Mail", [("BL_VikingByrnie16",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ####un rey o noble irlandes o picto
 ["byrnie151", "Red Noble Mail", [("BL_VikingByrnie05",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["byrnie_c_new", "Purple Noble Mail", [("BL_VikingByrnie14",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ###para noble briton
 ["byrnie_g_new", " Noble Mail", [("BL_VikingByrnie10",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["byrnie_d_new", " Noble Mail", [("BL_VikingByrnie11",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7020 , weight(20)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

########armaduras pesadas byrnie, para invasores solamente
["byrnie", "Brown Lorica", [("byrnie1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["mail_shirthre", "Blue Lorica", [("byrnie3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["mail_shirtredwhite", "Green Lorica", [("byrnie_d_new",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["mail_shirt_1_trig", "Red Lorica", [("byrnie_f_new",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
#malla, brynie, protege torso y parte de piernas, para los sajones, con capa
["ad_viking_byrnie_01", "White Lorica", [("byrnie11",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_byrnie_02", "Blue Lorica", [("byrnie12",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_byrnie_03", "Blue Lorica", [("byrnie13",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_byrnie_04", "White Lorica", [("byrnie14",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_byrnie_05", "Green Lorica", [("ragged_armour_e",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_byrnie_06", "White Lorica", [("byrnie16",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["mail_shirt_9_trig", "White Lorica", [("byrnie10",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["mail_shirt_2_trig", "Olive Lorica", [("byrnie_g_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["mail_shirt_3_trig", "Leather over Mail", [("saxon_leather_vest_mail",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4590 , weight(20)|abundance(30)|head_armor(0)|body_armor(46)|leg_armor(5)|difficulty(13) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["mail_shirt_4_trig", "Blue Short Mail", [("norman_short_hauberk_blue",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4540 , weight(21)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(6)|difficulty(12) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["mail_shirt_6_trig", "Red Short Mail", [("norman_short_hauberk",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4540 , weight(21)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(6)|difficulty(12) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["mail_shirt_7_trig", "Yellow Short Mail", [("norman_short_hauberk_yellow",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4540 , weight(21)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(6)|difficulty(12) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["mail_shirt_8_trig", "White Shirt Mail", [("sarranid_mail_byrnie_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4340 , weight(19)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(12) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
####byrnie para pictos, aplicar a una unidad de elite.
["mail_shirtbluewhite", "Squared Lorica", [("byrnie2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4840 , weight(19)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(6)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_20]],
["byrnie6", "Squared Lorica", [("byrnie6",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4840 , weight(19)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(6)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_20]],
["byrnie8", "Squared Lorica", [("byrnie8",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4840 , weight(19)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(6)|difficulty(11) ,imodbits_armor,
 [], [fac_kingdom_20]],
####byrnie para britones. Aplicar a una unidad de elite.
["byrnie4", "Striped Lorica", [("byrnie4",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4840 , weight(19)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["byrnie5", "Striped Lorica", [("byrnie5",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4840 , weight(19)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
#byrnie solo para reyes irlandeses, es purpura
 ["mail_shirt_8_trig", "Purple Lorica", [("byrnie_c_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 8000 , weight(19)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(6)|difficulty(11) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

#malla con piel de lobo, cubre torso y piernas. Lleva pantalones, solo sajones, y puede que britones. ELITE Y NOBLES
["wolf_coat1", "Wolf Lorica", [("leatherovermail_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5600 , weight(22)|abundance(10)|head_armor(0)|body_armor(65)|leg_armor(10)|difficulty(14) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["wolfpelt_mail_coat", "Wolf Lorica", [("leatherovermail_b",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5600 , weight(22)|abundance(10)|head_armor(0)|body_armor(65)|leg_armor(10)|difficulty(14) ,imodbits_armor,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
####goat mail para britones elite
["mail_hauberk", "Goatist Mail", [("goatist_mail",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5600 , weight(22)|abundance(10)|head_armor(0)|body_armor(60)|leg_armor(15)|difficulty(14) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
####tunica larga con maya y capa, para nobles irlandeses y pictos
["haubergeon", "Long Mail Tunic", [("armor_11",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5600 , weight(22)|abundance(10)|head_armor(0)|body_armor(55)|leg_armor(20)|difficulty(14) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

####Mail shirt, la primera lleva capucha de campesino, vale para invasores y britones
["mail_shirt", "Mail Shirt", [("haubergeon_jco",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3660 , weight(15)|abundance(40)|head_armor(0)|body_armor(45)|leg_armor(6)|difficulty(11) ,imodbits_armor],
["lamellar_armor", "Long Byrnie", [("peasant_leather_mail_LS",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4360 , weight(15)|abundance(40)|head_armor(0)|body_armor(50)|leg_armor(6)|difficulty(11) ,imodbits_armor],

#malla cubre torso, y cuero protege piernas son las cartons banks, anadir a una unidad britonna, restringir su venta.
["mail_shirt_1", "Red Byrnie", [("tattered_leather_armor_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(40)|head_armor(0)|body_armor(49)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mail_shirt_2", "Yellow Byrnie", [("tattered_leather_armor_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(40)|head_armor(0)|body_armor(49)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mail_shirt_3", "Green Byrnie", [("tattered_leather_armor_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(40)|head_armor(0)|body_armor(49)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mail_shirt_4", "Blue Byrnie", [("tattered_leather_armor_b",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(40)|head_armor(0)|body_armor(49)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mail_shirt_6", "White Byrnie", [("tattered_leather_armor_w",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(40)|head_armor(0)|body_armor(49)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mail_shirt_7", "Brown Byrnie", [("tattered_leather_armor_5",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(40)|head_armor(0)|body_armor(49)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mail_shirt_8", "Blue Byrnie", [("tattered_leather_armor_bl",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3360 , weight(15)|abundance(40)|head_armor(0)|body_armor(49)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mail_shirt_9", "Green Byrnie", [("tattered_leather_armor_4",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(40)|head_armor(0)|body_armor(49)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["arena_tunicj_brown", "Grey Byrnie", [("tattered_leather_armor_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(40)|head_armor(0)|body_armor(49)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["arena_tunicj_magenta", "White Byrnie", [("tattered_leather_armor_7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(40)|head_armor(0)|body_armor(49)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["arena_tunicj_violet", "Blue Byrnie", [("tattered_leather_armor_8",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(40)|head_armor(0)|body_armor(49)|leg_armor(2)|difficulty(12) ,imodbits_armor],
#para elite de pictos e irlandeses solamente
["mail_with_surcoat", "Sleeveless Mail", [("gallic_armor_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4280 , weight(17)|abundance(20)|head_armor(0)|body_armor(42)|leg_armor(15)|difficulty(11) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["surcoat_over_mail", "Sleeveless Mail", [("gallic_armor_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4280 , weight(17)|abundance(20)|head_armor(0)|body_armor(42)|leg_armor(15)|difficulty(11) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["brigandine_red", "Sleeveless Mail", [("gallic_armor",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4280 , weight(17)|abundance(20)|head_armor(0)|body_armor(42)|leg_armor(15)|difficulty(11) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

#Armadura laminar, protege torso de bronce. Usar para francos, y algun lord de kent y wessex solamente.
["vikinglamellar2", "Bronce Lamellar Armor", [("BL_Lamellar04",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3510 , weight(10)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(5)|difficulty(10) ,imodbits_armor,
[], [fac_kingdom_1, fac_kingdom_5, fac_kingdom_3, fac_kingdom_2]],
["vikinglamellar3blue", "Bronce Lamellar Armor", [("BL_Lamellar02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3510 , weight(10)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(5)|difficulty(10) ,imodbits_armor,
[], [fac_kingdom_1, fac_kingdom_5, fac_kingdom_3, fac_kingdom_2]],
["vikinglamellar3green", "Bronce Lamellar Armor", [("BL_Lamellar01",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3510 , weight(10)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(5)|difficulty(10) ,imodbits_armor,
[], [fac_kingdom_1, fac_kingdom_5, fac_kingdom_3, fac_kingdom_2]],
["vikinglamellar3red", "Bronce Lamellar Armor", [("BL_Lamellar03",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3510 , weight(10)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(10) ,imodbits_armor,
[], [fac_kingdom_1, fac_kingdom_5, fac_kingdom_3, fac_kingdom_2]],
["bl_lamellar05", "Bronce Lamellar Armor", [("BL_Lamellar05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3510 , weight(10)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(5)|difficulty(10) ,imodbits_armor,
[], [fac_kingdom_1, fac_kingdom_5, fac_kingdom_3, fac_kingdom_2]],
["bl_lamellar06", "Bronce Lamellar Armor", [("BL_Lamellar06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3510 , weight(10)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(5)|difficulty(10) ,imodbits_armor,
[], [fac_kingdom_1, fac_kingdom_5, fac_kingdom_3, fac_kingdom_2]],
###lamellar metal para tropas francas y de kent, llevan cuadros, quizas solo francos, y algun noble irlandes
["vikinglamellar2blue", "Black Lamellar Armor", [("BL_SLamellar03",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3830 , weight(12)|abundance(10)|head_armor(0)|body_armor(43)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_1, fac_kingdom_5, fac_kingdom_3, fac_kingdom_2]],
["vikinglamellar2red", "Red Lamellar Armor", [("BL_SLamellar01",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3830 , weight(12)|abundance(10)|head_armor(0)|body_armor(43)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_1, fac_kingdom_5, fac_kingdom_3, fac_kingdom_2]],
["vikinglamellar2yellow", "Brown Lamellar Armor", [("BL_SLamellar02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3830 , weight(12)|abundance(10)|head_armor(0)|body_armor(43)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_1, fac_kingdom_5, fac_kingdom_3, fac_kingdom_2]],
###importacion lores irlandeses del sur, usar poco.
["vikinglamellar3", "Bronce Lamellar armor", [("BL_Lamellar07",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3510 , weight(10)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(5)|difficulty(10) ,imodbits_armor,
[], [fac_kingdom_1, fac_kingdom_5, fac_kingdom_3, fac_kingdom_2]],
["bl_lamellar08", "Bronze Lamellar Armor", [("BL_Lamellar08",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3510 , weight(10)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(5)|difficulty(10) ,imodbits_armor,
[], [fac_kingdom_1, fac_kingdom_5, fac_kingdom_3, fac_kingdom_2]],
["vikinglamellar1", "Bronce Lamellar armor", [("BL_Lamellar09",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3510 , weight(10)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(5)|difficulty(10) ,imodbits_armor,
[], [fac_kingdom_1, fac_kingdom_5, fac_kingdom_3, fac_kingdom_2]],

#ring mail vale para todos, incluso invasores
 ["cuir_bouilli", "Ring Mail", [("peasant_leather_ring_LS",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2800 , weight(13)|abundance(40)|head_armor(0)|body_armor(38)|leg_armor(5)|difficulty(8) ,imodbits_armor],
["mamluke_mail", "Ring Mail", [("peasant_leather_ring_fur_LS",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2800 , weight(13)|abundance(40)|head_armor(0)|body_armor(38)|leg_armor(5)|difficulty(8) ,imodbits_armor],

#Armadura laminar, protege torso. SOLO BRITONES, PICTOS E IRLANDESES
["lamellar_vest", "Scale Coat", [("scale_shirt",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3920 , weight(14)|abundance(10)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(13) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["lamellar_vest_khergit", "Scale Shirt", [("rod_lamellar_armor_e_copy",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3330 , weight(12)|abundance(10)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(12) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
###scale armadura corta
 ["khergit_elite_armor", "Scale Armor", [("idi_scale2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
 ["sarranid_mail_shirt", "Grey Scale Armor", [("idi_scale6",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["light_leather", "White Scale Armor", [("idi_scale7",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["mail_and_plate", "Scale Armor", [("khergit_scale_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["light_mail_and_plate", "Scale Armor", [("khergit_scale_c",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["banded_armor", "Scale Armor", [("idi_scale10",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["coat_of_plates_red", "Scale Armor", [("scale_shirt_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["plate_armor", "Scale Armor", [("idi_scale12",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["khergit_guard_armor", "Scale Armor", [("scale_shirt_c",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["idi_scale14", "Scale Armor", [("idi_scale14",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
###irlandeses y pictos
["scale_armor", "Scale Armor", [("idi_scale1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vaegir_elite_armor", "Scale Armor", [("idi_scale3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["sarranid_elite_armor", "Scale Armor", [("idi_scale4",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["arabian_armor_b", "Scale Armor", [("idi_scale5",0)],itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["heraldic_mail_with_surcoat", "Scale Coat", [("outaa_escalearmor",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3420 , weight(14)|abundance(10)|head_armor(0)|body_armor(41)|leg_armor(8)|difficulty(11) ,imodbits_armor,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],


########################################################################################
 ####armaduras pesadas finales acaba chief############################################


###################ARMADURAS MEDIAS CHIEF finales###########################################

#gambeson de lino, cubre torso, cualquier faccion
["padded_jack_3_trig", "White Linen Coat", [("armor_15",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1170 , weight(4)|abundance(60)|head_armor(0)|body_armor(29)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
["padded_jack_4_trig", "Linen Coat", [("ped_padded1_brown",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1170 , weight(4)|abundance(60)|head_armor(0)|body_armor(29)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
["padded_jack_6_trig", "Blue Linen Coat", [("armor_17",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1170 , weight(4)|abundance(60)|head_armor(0)|body_armor(29)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
["padded_jack_7_trig", "Dirty Linen Coat", [("ped_padded1_narrow",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1090 , weight(4)|abundance(80)|head_armor(0)|body_armor(27)|leg_armor(5)|difficulty(6) ,imodbits_armor ],
["padded_jack_9_trig", "Linen Coat with Cloak", [("ped_padded1_creme",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1090 , weight(4)|abundance(80)|head_armor(0)|body_armor(27)|leg_armor(5)|difficulty(6) ,imodbits_armor ],

#kaftan
["padded_jack_8_trig", "Padded Warrior Jacket", [("Kaftan_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 680 , weight(3)|abundance(40)|head_armor(0)|body_armor(25)|leg_armor(4)|difficulty(4) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

["tattered_leather_armor_red", "Red Warrior Jacket", [("Kaftan2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["tattered_leather_armor_blu", "Blue Warrior Jacket", [("Kaftan3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["tattered_leather_armor_ylw", "Red Warrior Jacket", [("Kaftan",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["tattered_leather_armor_blk", "Blue Warrior Jacket", [("Kaftan4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["tattered_leather_armor_gr", "Blue Warrior Jacket", [("kaftanh",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["padded_leather_blue", "Green Warrior Jacket", [("kaftani",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["padded_leather_brown", "Blue Warrior Jacket", [("kaftan_vae_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["leather_armor_c", "Blue Warrior Jacket", [("kaftan_vae_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["leather_armor_c2", "Red Warrior Jacket", [("kaftan_vae_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

##kaftan for leather
["tattered_leather_armor_wht", "Purple Warrior Jacket", [("kaftang",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 620 , weight(3)|abundance(10)|head_armor(0)|body_armor(21)|leg_armor(4)|difficulty(4) ,imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

#armadura de piel de animal sajones y britones
["leather_vest_green", "Green Leather Vest", [("saxon_leather_vest_green",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 820 , weight(4)|abundance(60)|head_armor(0)|body_armor(23)|leg_armor(2)|difficulty(6) ,imodbits_cloth ], #cambiado chief
["leather_vest_blue", "Blue Leather Vest", [("saxon_leather_vest_blue",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 820 , weight(4)|abundance(60)|head_armor(0)|body_armor(23)|leg_armor(2)|difficulty(6) ,imodbits_cloth ], #cambiado chief
["leather_vest_red", "Red Leather Vest", [("saxon_leather_vest_red",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 820 , weight(4)|abundance(60)|head_armor(0)|body_armor(23)|leg_armor(2)|difficulty(6) ,imodbits_cloth ], #cambiado chief
["coat_of_plates1", "Rawhide Coat", [("coat_of_plates1",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ], #cambiado chief
["coat_of_plates3", "Rawhide Coat", [("coat_of_plates3",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ], #cambiado chief
["coat_of_plates4", "Rawhide Coat", [("coat_of_plates4",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ], #cambiado chief
["coat_of_plates5", "Rawhide Coat", [("coat_of_plates5",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ], #cambiado chief
["coat_of_plates6", "Rawhide Coat", [("coat_of_plates1m",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ], #cambiado chief
["coat_of_plates8", "Rawhide Coat", [("coat_of_plates3m",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ], #cambiado chief
["coat_of_plates9", "Rawhide Coat", [("coat_of_plates4m",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ], #cambiado chief
["coat_of_plates10", "Rawhide Coat", [("coat_of_plates5m",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ], #cambiado chief
["coat_of_plates11", "Rawhide Coat", [("coat_of_plates6m",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ], #cambiado chief

["goatist_tunic", "Goatist Tunic", [("goatist_tunic",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1160 , weight(4)|abundance(20)|head_armor(0)|body_armor(22)|leg_armor(12)|difficulty(6) ,imodbits_cloth ], #cambiado chief

##tunica con pellejo piel encima, campesinos
["pelt_coat", "Pelt Coat", [("thick_coat_a_bry",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 700 , weight(3)|abundance(80)|head_armor(0)|body_armor(18)|leg_armor(2)|difficulty(2) ,imodbits_cloth ], #cambiado chief
["pelt_coat2", "Pelt Coat", [("wei_xiadi_rod_thick_coat",0)],  itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 700 , weight(3)|abundance(80)|head_armor(0)|body_armor(18)|leg_armor(2)|difficulty(2) ,imodbits_cloth ], #cambiado chief
#tunica similar a anterior pero con tela dura
["vae_thick_coat1", "Simple Coat", [("vae_thick_coat1",0)],  itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 700 , weight(3)|abundance(80)|head_armor(0)|body_armor(18)|leg_armor(2)|difficulty(2) ,imodbits_cloth ], #cambiado chief
["vae_thick_coat2", "Simple Coat", [("vae_thick_coat2",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 800 , weight(3)|abundance(80)|head_armor(0)|body_armor(24)|leg_armor(2)|difficulty(2) ,imodbits_cloth ], #cambiado chief
["vae_thick_coat3", "Simple Coat", [("vae_thick_coat3",0)],  itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 700 , weight(3)|abundance(80)|head_armor(0)|body_armor(18)|leg_armor(2)|difficulty(2) ,imodbits_cloth ], #cambiado chief
["vae_thick_coat6", "Hide Coat", [("vae_thick_coat6",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 800 , weight(3)|abundance(80)|head_armor(0)|body_armor(24)|leg_armor(2)|difficulty(2) ,imodbits_cloth ], #cambiado chief
["vae_thick_coat10", "Hide Coat", [("vae_thick_coat10",0)],  itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 700 , weight(3)|abundance(80)|head_armor(0)|body_armor(18)|leg_armor(2)|difficulty(2) ,imodbits_cloth ], #cambiado chief

##fur jackets
["idi_furjacket1", "Fur Jacket", [("idi_furjacket1",0)],  itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(3)|abundance(70)|head_armor(0)|body_armor(19)|leg_armor(4)|difficulty(4) ,imodbits_cloth ], #cambiado chief
["idi_furjacket2", "Fur Jacket", [("idi_furjacket2",0)],  itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(3)|abundance(70)|head_armor(0)|body_armor(19)|leg_armor(4)|difficulty(4) ,imodbits_cloth ], #cambiado chief
["idi_furjacket3", "Fur Jacket", [("idi_furjacket3",0)],  itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(3)|abundance(70)|head_armor(0)|body_armor(19)|leg_armor(4)|difficulty(4) ,imodbits_cloth ], #cambiado chief
["idi_furjacket4", "Fur Jacket", [("idi_furjacket4",0)],  itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(3)|abundance(70)|head_armor(0)|body_armor(19)|leg_armor(4)|difficulty(4) ,imodbits_cloth ], #cambiado chief
["idi_furjacket5", "Fur Jacket", [("idi_furjacket5",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(3)|abundance(70)|head_armor(0)|body_armor(19)|leg_armor(4)|difficulty(4) ,imodbits_cloth ], #cambiado chief
["idi_furjacket6", "Fur Jacket", [("idi_furjacket6",0)],  itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(3)|abundance(70)|head_armor(0)|body_armor(19)|leg_armor(4)|difficulty(4) ,imodbits_cloth ], #cambiado chief
####Gathered cloak, los que van en plan miliciano con la capa
["gatheredcloaks1", "Blue Gathered Cloak", [("gatheredcloak1",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(2)|abundance(50)|head_armor(0)|body_armor(17)|leg_armor(6)|difficulty(2) ,imodbits_cloth ], #cambiado chief
["gatheredcloaks2", "Green Gathered Cloak", [("gatheredcloak2",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(2)|abundance(50)|head_armor(0)|body_armor(17)|leg_armor(6)|difficulty(2) ,imodbits_cloth ], #cambiado chief
["gatheredcloaks3", "Yellow Gathered Cloak", [("gatheredcloak3",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(2)|abundance(50)|head_armor(0)|body_armor(17)|leg_armor(6)|difficulty(2) ,imodbits_cloth ], #cambiado chief
["gatheredcloaks4", "Gathered Cloak", [("gatheredcloak4",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(2)|abundance(50)|head_armor(0)|body_armor(17)|leg_armor(6)|difficulty(2) ,imodbits_cloth ], #cambiado chief
["gatheredcloaks5", "Blue Gathered Cloak", [("gatheredcloak5",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(2)|abundance(50)|head_armor(0)|body_armor(17)|leg_armor(6)|difficulty(2) ,imodbits_cloth ], #cambiado chief

###tipo gordo
 ["fat_body", "Fat Body", [("fat_body",0)],  itp_unique| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(3)|abundance(10)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(4) ,imodbits_cloth ], #cambiado chief


###################ARMADURAS MEDIAS CHIEF finales acaba#############################
 ################################################################################


#######################################chief armor acaba##########################

#Quest-specific - perhaps can be used for prisoners,
["burlap_tunic", "Burlap Tunic", [("shirt",0)], itp_type_body_armor  |itp_covers_legs ,0,
 25 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(1)|difficulty(0) ,imodbits_armor ], #cambiado chief


###############################sombreros y yemos chief #######################################
###Gorros acabados chief###############
 ###################################
 ["pictish_hood", "Hood", [("pictish_hood",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth], #chief cambiado
 ["youhou_assassin_hood", "Hood", [("youhou_assassin_hood",0)],itp_type_head_armor|itp_civilian,0,280, weight(1)|abundance(10)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth], #chief cambiado
 ["youhou_assassin_hood_red", "Hood", [("youhou_assassin_hood_red",0)],itp_type_head_armor|itp_civilian,0,280, weight(1)|abundance(10)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth], #chief cambiado
#frigio
["woolen_cap_newblu", "Blue phrygian cap", [("woolen_cap_newblu",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["woolen_cap_newred", "Narrow phrygian cap", [("woolen_cap_newred",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["woolen_cap_newgrn", "Green phrygian cap", [("woolen_cap_newgrn",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["woolen_cap_newblk", "Black phrygian cap", [("woolen_cap_newblk",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["woolen_cap_newwht", "White phrygian cap", [("woolen_cap_newwht",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["woolen_cap", "Woolen Cap", [("woolen_cap_new_bry",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, #chief cambiado
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
#hood
["hood_newblu", "Hood", [("hood_newblu",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,110, weight(1)|abundance(90)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_newred", "Hood", [("hood_newred",0)],itp_type_head_armor|itp_civilian,0,110, weight(1)|abundance(90)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_newblk", "Hood", [("hood_newblk",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,110, weight(1)|abundance(90)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_newwht", "Hood", [("hood_newwht",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,110, weight(1)|abundance(90)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["black_hood", "Black Hood", [("hood_black_bry",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,110, weight(1)|abundance(90)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth], #cambiado chief
#otros
["head_wrappings","Head Wrapping",[("head_wrapping_bry",0)],itp_type_head_armor|itp_fit_to_head,0,30, weight(0.25)|head_armor(6),imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick], #chief cambiado

#tipo gordo
 ["turret_hat_ruby", "Fat Man", [("large_man_full",0)], itp_unique|itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 70 , weight(0.5)|abundance(10)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],


####gorros acabados chief##########3
 ############################

###Bandana
["turret_hat_blue", "Bandana", [("bandana1",0)], itp_merchandise|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_fit_to_head,0,60, weight(0.5)|abundance(10)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth], #chief cambiado
["turret_hat_green", "Bandana", [("bandana2",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_fit_to_head,0,60, weight(0.5)|abundance(10)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth], #chief cambiado


["common_hood", "Hood", [("hood_new_bry",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,40, weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth], #chief cambiado

####gorros acabados chief##########3
 ############################

######################capas finaliza chief############
 #########################################################
#Capas, para viajeros, nobles en castillo, espias (las de capucha), damas

#capas para nobles y damas
["red_cloakt", "Red Coat", [("BL_coat11c",0)], itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(2)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["green_cloakt", "Nobleman Coat", [("BL_coat12b",0)], itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(2)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["celta_capa3", "Cloak", [("BL_coat03c",0)], itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(2)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["celta_capa4", "Cloak", [("BL_coat06b",0)], itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(2)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["celta_capa5", "Cloak", [("BL_coat06c",0)], itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(2)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["celta_capa6", "Cloak", [("BL_coat08c",0)], itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(2)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["celta_capa7", "Cloak", [("BL_coat09b",0)], itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(2)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],


#viajeros ricos y clase media
["red_cloak_hood", "Rich Cloak", [("BL_coat16",0)],itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["blue_cloak_hood", "Blue Cloak", [("BL_coat19c",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["green_cloak", "Green Cloak", [("BL_coat12",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(2)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["blue_cloak", "Blue Cloak", [("BL_coat14",0)],itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(2)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["richbluecoat", "Rich Cloak", [("BL_coat14b",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["irishcloak", "Gael Cloak", [("BL_coat19",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],


#Viajeros pobres
["black_cloak", "Cloak", [("BL_coat03b",0)], itp_type_head_armor| itp_attach_armature|itp_fit_to_head,0, 193 , weight(2)|abundance(100)|head_armor(1)|body_armor(5)|leg_armor(3) ,imodbits_cloth ],
["white_cloak", "Cloak", [("BL_coat011",0)], itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head,0, 193 , weight(2)|abundance(100)|head_armor(1)|body_armor(5)|leg_armor(3) ,imodbits_cloth ],
["white_cloak_hood", "Cloak", [("cloak12",0)], itp_type_head_armor| itp_attach_armature|itp_fit_to_head,0, 193 , weight(2)|abundance(100)|head_armor(3)|body_armor(5)|leg_armor(3) ,imodbits_cloth ],
["celta_capa1", "Godelic cloak", [("BL_coat03",0)], itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(2)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["celta_capa2", "Cloak", [("BL_coat03b",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(2)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["red_cloak", "Cloak", [("BL_coat011",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
  [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

#espias
["green_cloak_hoodc", "Green cloak and hood with mask", [("cloak27",0)], itp_type_head_armor| itp_attach_armature| itp_fit_to_head,0, 193 , weight(2)|abundance(100)|head_armor(3)|body_armor(5)|leg_armor(3) ,imodbits_cloth ],
["brown_cloak_hoodc", "Brown cloak and hood with mask", [("cloak28",0)], itp_type_head_armor| itp_attach_armature| itp_fit_to_head,0, 193 , weight(2)|abundance(100)|head_armor(3)|body_armor(5)|leg_armor(3) ,imodbits_cloth ],
["black_cloak_hoodc", "Black cloak and hood with mask", [("cloak29",0)], itp_type_head_armor| itp_attach_armature| itp_fit_to_head,0, 193 , weight(2)|abundance(100)|head_armor(3)|body_armor(5)|leg_armor(3) ,imodbits_cloth ],
["grey_cloak_hoodc", "Grey cloak and hood with mask", [("cloak30",0)], itp_type_head_armor| itp_attach_armature| itp_fit_to_head,0, 193 , weight(2)|abundance(100)|head_armor(3)|body_armor(5)|leg_armor(3) ,imodbits_cloth ],

####cloaks para invasores y britones, y comunes en tiendas
 #piel
["piel_coat01", "Fur Cloak", [("BL_coat01",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["piel_coat02", "Cloak", [("BL_coat01b",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["piel_coat03", "Cloak", [("BL_coat01c",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["piel_coat04", "Cloak", [("BL_coat02",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["piel_coat05", "Cloak", [("BL_coat02b",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["piel_coat06", "Cloak", [("BL_coat02c",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["piel_coat07", "Cloak", [("BL_coat04",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature| itp_doesnt_cover_hair|itp_fit_to_head|itp_civilian,0, 580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

#FUR chief jabali
 ["bl_boar_fur", "Fur Cloak", [("BL_boar_fur",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_fit_to_head | itp_doesnt_cover_hair,0, 300 , weight(1.5)|abundance(10)|head_armor(1)|body_armor(15)|leg_armor(0)|difficulty(4) ,imodbits_cloth, #cambiado chief
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
#Boar Fur chief es el completo, capa y cabeza
["bl_boar", "Boar Fur", [("BL_boar",0)], itp_type_head_armor| itp_attach_armature|itp_fit_to_head ,0, 1580 , weight(3)|abundance(10)|head_armor(20)|body_armor(15)|leg_armor(0)|difficulty(4) ,imodbits_cloth, #cambiado chief
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],


####################capas finaliza chief########################
 ############################################################


###############yelmos finales chief#############################
 ################################################################

#especiales: cabeza barbuda para algun heroe o similar
 ["khergit_guard_helmet", "Barbar Head", [("barbar_helm",0)], itp_unique|itp_type_head_armor|itp_fit_to_head|itp_covers_head |itp_civilian  ,0, 1300 , weight(3)|abundance(10)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

###cabezas de animales, especial para paganos
 #boar helmet chief especial para paganos
["boar_helmet", "Boar Hat", [("BL_boarhelmet",0)],  itp_type_head_armor|itp_civilian ,0, 700 , weight(2)|abundance(30)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(3) ,imodbits_cloth ], #cambiado chief
["goat_cap", "Goat Cap", [("goat_cap",0)],  itp_type_head_armor|itp_civilian ,0, 700 , weight(2)|abundance(30)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(3) ,imodbits_cloth ], #cambiado chief
["felt_steppe_cap", "Goat Hat", [("goat_bascinet",0)],  itp_type_head_armor|itp_civilian ,0, 700 , weight(2)|abundance(30)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(3) ,imodbits_cloth ], #cambiado chief


#Todas las facciones ####ligeros
#bajo
#acabado
["helm_captaina", "Leather Cap With Plum", [("helm_captainA",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 280 , weight(1)|abundance(60)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_cloth ],
["leather_cap", "Leather Cap", [("leather_cap_a_new_bry",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 170 , weight(0.5)|abundance(90)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], #moficiado chief
["skull_cap_new_c", "Leather Cap", [("skull_cap_new_c",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 200 , weight(1)|abundance(80)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_warrior_cap", "Straw Hat", [("straw_hat_new_bry",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 90 , weight(1)|abundance(80)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["leather_steppe_cap_b", "Reinforced Skullcap", [("skull_cap_new_a_bry",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 200 , weight(1)|abundance(80)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], #cambiado chief
["leather_steppe_cap_c", "Skullcap", [("skull_cap_new_b_bry",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 190 , weight(1)|abundance(80)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], #cambiado chief


#Coronas, solo reyes finales ####
 #################################
#sajones
["sib_lombardy", "Crown", [("sib_Lombardy",0)],itp_type_head_armor|itp_unique|itp_civilian| itp_doesnt_cover_hair,0,5000, weight(2)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
#britones#Pictos#Irish
["sib_couronne", "Crown", [("sib_couronne",0)],itp_type_head_armor|itp_unique|itp_civilian| itp_doesnt_cover_hair,0,5000, weight(2)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
###########coronas finales#############3
 ##########################

###TODOS
#tropas elite
 ["norman_helmet", "Leather Helmet with Plum", [("rath_spangenlord3",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 780 , weight(1.75)|abundance(40)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ], #cambiado chief
["sarranid_helmet1", "North Helmet", [("rath_spangenlord2",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 780 , weight(1.75)|abundance(40)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ], #cambiado chief
["rath_spangenlord5", "Helmet with Plum", [("rath_spangenlord5",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 860 , weight(1.75)|abundance(20)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ], #cambiado chief
 ["rathos_bowl_helmet", "Bowl Helmet with leather neckguard", [("Rathos_bowl_helmet",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 540 , weight(1.5)|abundance(80)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_plate],
 ["bowl_helmet_nasal", "Bowl Helmet with Nasal", [("bowl_helmet_nasal",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 560 , weight(1.5)|abundance(80)|head_armor(27)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_plate],
["spangenhelm_a", "Brythonic Helmet", [("spangenhelm_a",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 830 , weight(1.75)|abundance(40)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ], #cambiado chief
["spangenhelm_a_trim", "Germanic Helmet", [("spangenhelm_a_trim",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 830 , weight(1.75)|abundance(40)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ], #cambiado chief
#este da problemas con los lods, puede causar fallos vigilar
["khergit_cavalry_helmet", "Cavalry Helmet", [("romanspangenhelm",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 810 , weight(1.75)|abundance(40)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ], #cambiado chief
#este da problemas con los lods, puede causar fallos vigilar
 ["bowl_helmet", "Bowl Helmet", [("bowl_helmet",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 520 , weight(1.5)|abundance(80)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_plate],

#spangenhelmet como el encontrado en hungria del siglo IV
 ["arming_cap", "Basic Late Roman Helmet", [("old_spangenhelm",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 520 , weight(1.5)|abundance(80)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_plate],
["padded_coif", "Late Roman Helmet", [("old_spangenhelmcheek",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 700 , weight(1.5)|abundance(60)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate ], #cambiado chief
["steppe_cap", "Elite Late Roman Helmet", [("old_spangenhelmaven",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 810 , weight(1.75)|abundance(20)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ], #cambiado chief

#nobles
 ["spangenhelm_a_ornate", "Nobleman Helmet with plum", [("spangenhelm_a_ornate",0)], itp_type_head_armor|itp_fit_to_head   ,0, 940 , weight(1.75)|abundance(10)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ], #cambiado chief


###BRITONES
#nobles britones yelmo o tropas super elite
["barf_helm", "Elite Helm", [("barf_helm",0)], itp_type_head_armor|itp_fit_to_head   ,0, 1150 , weight(2)|abundance(10)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["dux_ridge_helm", "Dux helm", [("dux_ridge_helm",0)], itp_type_head_armor|itp_fit_to_head ,0, 1340 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["rathos_spangenhelm_a_gold", "Rich Helm", [("Rathos_Spangenhelm_a_Gold",0)], itp_type_head_armor|itp_fit_to_head ,0, 1060 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["rathos_spangenhelm_a_light_gold", "Light Nobleman Helm", [("Rathos_Spangenhelm_a_light_Gold",0)], itp_type_head_armor|itp_fit_to_head ,0, 860 , weight(1.75)|abundance(10)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["rathos_spangenhelm_b_gold", "Nobleman Helm", [("Rathos_Spangenhelm_b_Gold",0)], itp_type_head_armor|itp_fit_to_head ,0, 1060 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["romanelitehelm", "Rich Elite Helm", [("romanelitehelm",0)], itp_type_head_armor|itp_fit_to_head   ,0, 1150 , weight(2)|abundance(10)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],

#tropas elite
#cambiado por otro mas adecado
["helmet_with_neckguard", "Veteran Helmet", [("spangenhelm_a_ornate",0)], itp_merchandise|itp_type_head_armor   ,0, 900 , weight(1.75)|abundance(50)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
 [], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
#["helmet_with_neckguard", "Veteran Helmet", [("helmetx2",0)], itp_merchandise|itp_type_head_armor   ,0, 900 , weight(1.75)|abundance(50)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
# [], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
#sigue
["briton_helm", "Briton Helm", [("briton_helm",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 780 , weight(2)|abundance(60)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["briton_helm2", "Briton Helm", [("briton_helm2",0)],  itp_type_head_armor|itp_fit_to_head ,0, 780 , weight(2)|abundance(60)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["briton_helm3", "Briton Helm", [("briton_helm3",0)], itp_type_head_armor|itp_fit_to_head ,0, 780 , weight(2)|abundance(60)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["briton_helm4", "Briton Helm", [("briton_helm4",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 780 , weight(2)|abundance(60)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["briton_helm5", "Elite Briton Helm", [("briton_helm5",0)], itp_type_head_armor|itp_fit_to_head ,0, 820 , weight(2)|abundance(40)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["rathos_spangenhelm_a", "Helm", [("Rathos_Spangenhelm_a",0)], itp_type_head_armor|itp_fit_to_head ,0, 760 , weight(2)|abundance(60)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["rathos_spangenhelm_b", "Helm", [("Rathos_Spangenhelm_b",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 760 , weight(2)|abundance(60)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["rathos_spangenhelm_a_light", "Light Helm", [("Rathos_Spangenhelm_a_light",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 720 , weight(1.75)|abundance(40)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["rathos_spangenhelm_b_light", "Light Helm", [("Rathos_Spangenhelm_b_light",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 720 , weight(1.75)|abundance(40)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(4) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["rathos_spangenhelm_yellow_plum", "Chief Helm", [("Rathos_Spangenhelm_yellow_plum",0)], itp_type_head_armor|itp_fit_to_head ,0, 760 , weight(2)|abundance(60)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["rathos_spangenhelm_a_yellow2", "Chief Helm", [("Rathos_Spangenhelm_a_yellow2",0)], itp_type_head_armor|itp_fit_to_head ,0, 760 , weight(2)|abundance(60)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],

#Rey Briton
["dux_ridge_helm_gold", "Dux Helm Gold", [("dux_ridge_helm_gold",0)], itp_type_head_armor|itp_fit_to_head ,0, 1580 , weight(2)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["rathos_spangenhelm_a_gold_decorated", "Prince Helm", [("Rathos_Spangenhelm_a_Gold_Decorated",0)], itp_type_head_armor|itp_fit_to_head ,0, 820 , weight(2.25)|abundance(10)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["rathos_spangenhelm_b_gold_decorated", "Chief Helm", [("Rathos_Spangenhelm_b_Gold_Decorated",0)], itp_type_head_armor|itp_fit_to_head ,0, 820 , weight(2.25)|abundance(10)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["briton_helm6", "Rich Briton Helm", [("briton_helm6",0)], itp_type_head_armor|itp_fit_to_head ,0, 880 , weight(2)|abundance(10)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["briton_helm7", "Nobleman Briton Helm", [("briton_helm7",0)], itp_type_head_armor|itp_fit_to_head ,0, 880 , weight(2)|abundance(10)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],


 ###INVASORES
###invasores, yelmos comunes metalicos para tropas elite
 ["frisian_helmet_mesh", "Frisian Helmet", [("frisian_helmet_mesh",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 720 , weight(1.5)|abundance(40)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3]],
["horn_helmet", "Horn Helmet", [("Horn_Helmet",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 500 , weight(1)|abundance(90)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(2) ,imodbits_cloth,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["horn_helmet_2", "Leather Helmet with Boar", [("Horn_Helmet_2",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 560 , weight(1)|abundance(80)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(2) ,imodbits_cloth,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["horn_helmet_3", "Iron Helmet with Boar", [("Horn_Helmet_3",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 760 , weight(1)|abundance(30)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(2) ,imodbits_cloth,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["vendel14", "Jute Helmet", [("vendel14",0)], itp_type_head_armor|itp_fit_to_head   ,0, 1080 , weight(1.5)|abundance(20)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3]],
 ["gaul_helmet", "Saxon Helmet", [("gaul_helmet",0)], itp_type_head_armor|itp_fit_to_head   ,0, 720 , weight(1.5)|abundance(40)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3]],
#este da problemas con los lods, puede causar fallos vigilar
["spangenhelm_helm", "Germanic Helm", [("spangenhelm_helm",0)], itp_type_head_armor|itp_fit_to_head ,0, 760 , weight(2)|abundance(60)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
#mercios, tambien vale para britones cercanos a mercia, este da problemas con los lods, puede causar fallos vigilar
["vaegir_war_helmet", "Wollaston Mierce helmet", [("wollaston_mercian",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head ,0, 980 , weight(2)|abundance(10)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_9]],
#con goat en cabeza
["nomad_cap", "Goat Wollaston Mierce helmet", [("wollaston_mercian2",0)], itp_type_head_armor|itp_fit_to_head ,0, 1180 , weight(2)|abundance(10)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_9]],

#nobles y elite
  ["vendel14_2", "Nobleman Jute Helmet", [("vendel14_2",0)], itp_type_head_armor|itp_fit_to_head   ,0, 1180 , weight(1.5)|abundance(10)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3]],
#Noble sajon, anglo o juto
["talak_spangenhelm", "Anglo Helmet", [("talak_spangenhelm",0)], itp_type_head_armor|itp_fit_to_head   ,0, 980 , weight(2)|abundance(20)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["vendel_helmet", "Nobleman Jute Helm", [("vendel_helmet",0)], itp_type_head_armor|itp_fit_to_head   ,0, 1150 , weight(2)|abundance(10)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["vendel_helmet2", "Angle Helm", [("talak_ped_mercian2",0)], itp_type_head_armor|itp_fit_to_head   ,0, 1150 , weight(2)|abundance(10)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["nordic_helmet", "Expensive Helm", [("Valsgarde_guards",0)],  itp_type_head_armor|itp_fit_to_head   ,0, 960 , weight(2)|abundance(20)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["khergit_lady_hat", "Nobleman Helm", [("Valsgarde_guards2",0)],  itp_type_head_armor|itp_fit_to_head   ,0, 960 , weight(2)|abundance(20)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["khergit_lady_hat_b", "Warlord Helm", [("Valsgarde_small",0)],  itp_type_head_armor|itp_fit_to_head   ,0, 920 , weight(2)|abundance(20)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

#con goat en la cabeza
 ["nomad_cap_b", "Goat Nobleman Helmet", [("vendel_helmetgoat",0)], itp_type_head_armor|itp_fit_to_head   ,0, 1350 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

#rey juto
  ["vendel14_3", "King Jute Helmet", [("vendel14_3",0)], itp_type_head_armor|itp_fit_to_head   ,0, 1280 , weight(1.5)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
[], [fac_kingdom_1]],
#Rey anglo
["talak_sutton_hoo", "Saxon Prince Helmet", [("talak_sutton_hoo",0)], itp_type_head_armor|itp_fit_to_head   ,0, 1320 , weight(2.5)|abundance(10)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#rey sajon o juto, o dena pirate
["valsgarde_new", "Scandza Helmet", [("valsgarde_new",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head   ,0, 1400 , weight(3)|abundance(10)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(14) ,imodbits_plate ],

#chief valsgarde helmets de dinamarca para determinadas unidades de elite de INVASORES
#proteccion base, tropas elite sajones y jutos
["footman_helmet", "Dena Helmet", [("BL_01_Valsgarde02",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 850 , weight(2)|abundance(30)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5]],
["sarranid_veiled_helmet", "Dena Helmet with Boar", [("BL_01_Valsgarde02BOAR",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 880 , weight(2)|abundance(30)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5]],
#con cabeza de goat encima, para paganos sajones
["fur_hat", "Goat Helmet", [("BL_03_Valsgarde02",0)], itp_type_head_armor|itp_fit_to_head ,0, 1080 , weight(2)|abundance(30)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5]],

#proteccion media, tropas noble sajones jutos y anglos
["flat_topped_helmet", "Dena Warrior Helm", [("BL_01_Valsgarde05",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 900 , weight(2)|abundance(20)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5]],
["nordic_huscarl_helmet", "Dena Warrior Helmet with Boar", [("BL_01_Valsgarde05BOAR",0)],  itp_type_head_armor|itp_fit_to_head ,0, 930 , weight(2)|abundance(20)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["kettle_hat", "Dena Pirate Helm", [("BL_01_Valsgarde03",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 900 , weight(2)|abundance(20)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5]],
["nordic_veteran_archer_helmet", "Pirate Helm with Boar", [("BL_01_Valsgarde03BOAR",0)], itp_type_head_armor|itp_fit_to_head ,0, 930 , weight(2)|abundance(20)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["nordic_footman_helmet", "Frisian Helmet", [("BL_01_Valsgarde04",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 900 , weight(2)|abundance(20)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5]],
["nordic_fighter_helmet", "Frisian Helmet with Boar", [("BL_01_Valsgarde04BOAR",0)], itp_type_head_armor|itp_fit_to_head ,0, 930 , weight(2)|abundance(20)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

["spiked_helmet", "Captain Helm", [("BL_01_Valsgarde01",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head ,0, 920 , weight(2)|abundance(10)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["sarranid_mail_coif", "Captain Helmet with Boar", [("BL_01_Valsgarde01BOAR",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head ,0, 950 , weight(2)|abundance(10)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

#proteccion alta, bajos nobles y elite sajones jutos y anglos
["nasal_helmet", "Dena Elite Helm", [("BL_01_Valsgarde09",0)], itp_type_head_armor|itp_fit_to_head ,0, 900 , weight(2)|abundance(10)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["vaegir_fur_helmet", "Dena Elite Helm with Boar", [("BL_01_Valsgarde09BOAR",0)], itp_type_head_armor|itp_fit_to_head ,0, 930 , weight(2)|abundance(10)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["magyar_helmet_a", "Dena Elite Helm", [("BL_01_Valsgarde10",0)], itp_type_head_armor|itp_fit_to_head ,0, 900 , weight(2)|abundance(10)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["rus_helmet_a", "Dena Elite Helm with Boar", [("BL_01_Valsgarde10BOAR",0)], itp_type_head_armor|itp_fit_to_head ,0, 930 , weight(2)|abundance(10)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

#proteccion muy alta, bajos nobles y elite sajones jutos y anglos
["segmented_helmet", "Dena Elite Helm", [("BL_01_Valsgarde07",0)],  itp_type_head_armor|itp_fit_to_head ,0, 920 , weight(2)|abundance(10)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["vaegir_fur_cap", "Dena Elite Helm with Boar", [("BL_01_Valsgarde07BOAR",0)],  itp_type_head_armor|itp_fit_to_head ,0, 950 , weight(2)|abundance(10)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["byzantion_helmet_a", "Dena Elite Helm", [("BL_01_Valsgarde08",0)],  itp_type_head_armor|itp_fit_to_head ,0, 920 , weight(2)|abundance(10)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["vaegir_mask", "Dena Elite Helm with Boar", [("BL_01_Valsgarde08BOAR",0)],  itp_type_head_armor|itp_fit_to_head ,0, 950 , weight(2)|abundance(10)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

####
#valsgarde and boar Captain dena pirate
["nordic_warlord_helmet", "Captain Helmet with Boar", [("BL_02_Valsgarde01",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head ,0, 950 , weight(2)|abundance(10)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["full_helm", "Captain Helmet with Boar", [("BL_02_Valsgarde01BOAR",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head ,0, 980 , weight(2)|abundance(10)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["great_helmet", "Captain Helmet with Boar", [("BL_04_Valsgarde01BOAR",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head ,0, 980 , weight(2)|abundance(10)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["winged_great_helmet", "Captain Helmet with Boar", [("BL_04_Valsgarde01",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head ,0, 950 , weight(2)|abundance(10)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

#valsgarde reyes y altos nobles sajones, jutos y anglos
["sarranid_felt_hat", "Warlord Helmet", [("BL_02_Valsgarde07",0)], itp_type_head_armor|itp_fit_to_head ,0, 980 , weight(2)|abundance(10)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["sarranid_felt_hat", "Warlord Helmet with Boar", [("BL_02_Valsgarde07BOAR",0)], itp_type_head_armor|itp_fit_to_head ,0, 1010 , weight(2)|abundance(10)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["bascinet", "Nobleman Dena Helmet", [("BL_02_Valsgarde09",0)], itp_type_head_armor|itp_fit_to_head ,0, 980 , weight(2)|abundance(10)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["bascinet_2", "Nobleman Dena Helmet with Boar", [("BL_02_Valsgarde09BOAR",0)], itp_type_head_armor|itp_fit_to_head ,0, 1010 , weight(2)|abundance(10)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

["bascinet_3", "Dena Noble Helmet", [("BL_03_Valsgarde03",0)], itp_type_head_armor|itp_fit_to_head ,0, 920 , weight(2)|abundance(10)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["sipahi_helmet_a", "Dena Noble Helmet with Boar", [("BL_03_Valsgarde03BOAR",0)], itp_type_head_armor|itp_fit_to_head ,0, 950 , weight(2)|abundance(10)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["guard_helmet", "Dena Lord Helmet", [("BL_03_Valsgarde10",0)], itp_type_head_armor|itp_fit_to_head ,0, 920 , weight(2)|abundance(10)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["black_helmet", "Dena Lord Helmet with Boar", [("BL_03_Valsgarde10BOAR",0)], itp_type_head_armor|itp_fit_to_head ,0, 950 , weight(2)|abundance(10)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

["khergit_war_helmet", "Warlord Helmet", [("BL_04_Valsgarde07",0)], itp_type_head_armor|itp_fit_to_head ,0, 980 , weight(2)|abundance(10)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["khergit_helmet", "Warlord Helmet with Boar", [("BL_04_Valsgarde07BOAR",0)], itp_type_head_armor|itp_fit_to_head ,0, 1010 , weight(2)|abundance(10)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["turban", "Nobleman Dena Helmet", [("BL_04_Valsgarde03",0)], itp_type_head_armor|itp_fit_to_head ,0, 980 , weight(2)|abundance(10)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["desert_turban", "Nobleman Dena Helmet with Boar", [("BL_04_Valsgarde03BOAR",0)], itp_type_head_armor|itp_fit_to_head ,0, 1010 , weight(2)|abundance(10)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["vaegir_spiked_helmet", "Warlord Helmet", [("BL_04_Valsgarde08",0)], itp_type_head_armor|itp_fit_to_head ,0, 980 , weight(2)|abundance(10)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["vaegir_lamellar_helmet", "Warlord Helmet with Boar", [("BL_04_Valsgarde08BOAR",0)], itp_type_head_armor|itp_fit_to_head ,0, 1010 , weight(2)|abundance(10)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],




####IRLANDESES Y PICTOS
#irlandeses y pictos
 #elite
 ["celtycka_lebka", "Godelic Bowl Helmet", [("celtycka_lebka",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 520 , weight(1.5)|abundance(80)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_plate,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["celtycka_iron", "Iron Bowl Helmet", [("celtycka_iron",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head   ,0, 680 , weight(1.5)|abundance(60)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#este da problemas con los lods, puede causar fallos vigilar
["szpadelhelmet", "Godelic Helmet", [("szpadelhelmet",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 760 , weight(2)|abundance(60)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["szpadelhelmet1", "Godelic Helmet", [("szpadelhelmet",0)],  itp_type_head_armor|itp_fit_to_head ,0, 760 , weight(2)|abundance(60)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["szpadelhelmet2", "Godelic Helmet", [("szpadelhelmet2",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 760 , weight(2)|abundance(60)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["szpadelhelmet3", "Godelic Helmet", [("szpadelhelmet3",0)],  itp_type_head_armor|itp_fit_to_head ,0, 760 , weight(2)|abundance(60)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["szpadelhelmet4", "Godelic Helmet", [("szpadelhelmet4",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 760 , weight(2)|abundance(60)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["szpadelhelmet5", "Godelic Helmet", [("szpadelhelmet5",0)],  itp_type_head_armor|itp_fit_to_head ,0, 760 , weight(2)|abundance(60)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],


#reyes y nobles irlandeses
#este da problemas con los lods, puede causar fallos vigilar
["szpadelhelmet6", "Godelic Nobleman Helmet", [("szpadelhelmet6",0)],  itp_type_head_armor|itp_fit_to_head ,0, 860 , weight(2)|abundance(10)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["szpadelhelmet_gold", "Elite Briton Helm", [("szpadelhelmet_gold",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 760 , weight(2)|abundance(60)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],

#para decapitaciones, casco chief invisible
["sarranid_horseman_helmet", "No head", [("no_head",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head   ,0, 180 , weight(2)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],

####Yelmos finales acaba#################################
 ############################################################


# Chief empieza########
####ARMAS DE ATAQUE#########


###armas de no filo, porras, mazas madera etc... finalizadas
 #######################
["wooden_stick",         "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
2 , weight(2)|difficulty(0)|spd_rtng(82) | weapon_length(80)|swing_damage(16 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
["club",         "Club", [("club",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
20 , weight(1.5)|difficulty(4)|spd_rtng(80) | weapon_length(65)|swing_damage(17 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ], #cambiado chief
["club_one",         "Club", [("club_one",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
 125 , weight(2)|difficulty(6)|spd_rtng(87) | weapon_length(35)|swing_damage(19 , blunt) | thrust_damage(5 ,  pierce),imodbits_none ],
["cudgel",         "Wooden Club", [("palka",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
100 , weight(2)|difficulty(0)|spd_rtng(87) | weapon_length(65)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
["palka2",         "Wooden Club", [("palka2",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
100 , weight(2)|difficulty(0)|spd_rtng(87) | weapon_length(65)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
["palka3",         "Wooden Club", [("palka3",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
100 , weight(2)|difficulty(0)|spd_rtng(87) | weapon_length(65)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
["palka4",         "Wooden Club", [("palka4",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
100 , weight(2)|difficulty(0)|spd_rtng(87) | weapon_length(65)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
["palka5",         "Wooden Club", [("palka5",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
100 , weight(2)|difficulty(0)|spd_rtng(87) | weapon_length(65)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
["spiked_club",         "Spiked Club", [("spiked_club",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
130 , weight(3)|difficulty(0)|spd_rtng(77) | weapon_length(85)|swing_damage(22 , pierce) | thrust_damage(0 ,  pierce),imodbits_none ], #cambiado chief
["sickle",         "Sickle", [("sickle",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,
100 , weight(1.5)|difficulty(0)|spd_rtng(86) | weapon_length(40)|swing_damage(15 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
#####no filo
 ##############################

####cuchillos y seax chief###################
 ###########################################

["knife",         "Knife", [("peasant_knife",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
205 , weight(0.5)|difficulty(0)|spd_rtng(97) | weapon_length(30)|swing_damage(16 , cut) | thrust_damage(16 ,  pierce),imodbits_sword ], #cambiado chief
["butchering_knife", "Butchering Knife", [("khyber_knife",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,
185 , weight(0.75)|difficulty(0)|spd_rtng(82) | weapon_length(40)|swing_damage(19 , cut) | thrust_damage(9 ,  pierce),imodbits_sword ], #chief cambiado

#todos
["hunting_dagger",         "Hunting Seax", [("hunting_dagger",0),("seaxsheath", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 280 , weight(0.5)|difficulty(0)|spd_rtng(97) | weapon_length(60)|swing_damage(17 , cut) | thrust_damage(17 ,  pierce),imodbits_sword ],
["nordic_sword", "Simple Lang Knife", [("simple_langseax",0),("simple_langseax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 270 , weight(0.5)|difficulty(0)|spd_rtng(92) | weapon_length(65)|swing_damage(14 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
["broadsword",         "Simple Knife", [("simple_seax",0),("simple_seax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 270 , weight(0.5)|difficulty(0)|spd_rtng(92) | weapon_length(65)|swing_damage(14 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
#irlandeses y pictos
#scians para tropas medias (nivel 20 a 25), son baratos y terribles
["scianshort",         "Short Scian", [("scianshort",0),("scianshort", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip, 300 , weight(0.8)|difficulty(6)|spd_rtng(92) | weapon_length(70)|swing_damage(18 , cut) | thrust_damage(20 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["scianshortbone",         "Short Bone Scian", [("scianshortbone",0),("scianshortbone", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip, 300 , weight(0.8)|difficulty(6)|spd_rtng(92) | weapon_length(70)|swing_damage(18 , cut) | thrust_damage(20 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],


#sajones, aglos y jutos
["talak_seax", "Light Seax", [("vikingr_seax",0),("vikingr_seax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 280 , weight(0.5)|difficulty(0)|spd_rtng(92) | weapon_length(65)|swing_damage(14 , cut) | thrust_damage(19 ,  pierce),imodbits_sword,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["had_seax", "Saxon Seax", [("saxon_seax",0),("saxon_seax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 280 , weight(0.5)|difficulty(0)|spd_rtng(92) | weapon_length(65)|swing_damage(14 , cut) | thrust_damage(19 ,  pierce),imodbits_sword,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["langseax", "Lang Seax", [("langseax",0),("langseax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 350 , weight(0.5)|difficulty(0)|spd_rtng(88) | weapon_length(82)|swing_damage(17 , cut) | thrust_damage(17 ,  pierce),imodbits_sword,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ornate_seax", "Ornate Seax", [("ornate_seax",0),("ornate_seax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 280 , weight(0.5)|difficulty(0)|spd_rtng(92) | weapon_length(65)|swing_damage(14 , cut) | thrust_damage(19 ,  pierce),imodbits_sword,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["dagger",         "Seax", [("seax",0),("seax",ixmesh_carry),("seax",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 80 , weight(0.5)|difficulty(0)|spd_rtng(92) | weapon_length(65)|swing_damage(14 , cut) | thrust_damage(19 ,  pierce),imodbits_sword,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["falchion",         "Cleaver Seax", [("cleaver_seax",0),("cleaver_seax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 280 , weight(0.5)|difficulty(0)|spd_rtng(92) | weapon_length(65)|swing_damage(14 , cut) | thrust_damage(19 ,  pierce),imodbits_sword,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["scimitar",         "Seax", [("seax_hp_tri",0),("seaxsheath", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 280 , weight(0.5)|difficulty(0)|spd_rtng(92) | weapon_length(65)|swing_damage(14 , cut) | thrust_damage(19 ,  pierce),imodbits_sword,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
###############cuchillos y seaxa caba chief#############################


####Espadas chief finales #####################
########################################
#basica todas las culturas, spatha romana
["spatha", "Spatha", [("pattern_spatha",0),("roman_cav_sword_2_scabbard", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 900 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(14 ,  pierce),imodbits_sword_high ],
###otras basicas
#scab problem
["le_pictishsword2", "Rich Spatha", [("le_pictishsword2",0),("scab_vikingsw", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1200 , weight(1.25)|difficulty(9)|spd_rtng(83) | weapon_length(95)|swing_damage(36 , cut) | thrust_damage(14 ,  pierce),imodbits_sword_high ],
 ["bl_sword01_01", "Sword", [("BL_Sword01_01",0),("BL_Sword01_01", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 1000 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ],
 ["bl_sword01_02", "Sword", [("BL_Sword01_02",0),("BL_Sword01_02", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 1000 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ],
 ["new_sword1", "Sword", [("Sword1",0),("Sword1", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 1000 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ],
 ["new_sword2", "Sword", [("Sword2",0),("Sword2", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 1000 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ],
 ["bl_sword01_03", "Sword", [("BL_Sword01_03",0),("BL_Sword01_03", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 1000 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ],
#scba problem acaba
 ["le_bamburghsword", "Sword", [("le_bamburghsword",0),("sword_medieval_b_scabbard2", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 950 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(13 ,  pierce),imodbits_sword_high ],
 ["bamburghsword2", "Sword", [("BamburghSword2",0),("sword_medieval_b_scabbard2", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 950 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(13 ,  pierce),imodbits_sword_high ],

#Invasores
#basica
 ["saxonsword", "Saxon Sword", [("RichSword1",0),("RichSword1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1020 , weight(1.25)|difficulty(8)|spd_rtng(83) | weapon_length(95)|swing_damage(32 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
#scab problem 1 debajo
 ["le_richsword1", "Germanic Sword", [("le_richsword1",0),("le_richsword1", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 1020 , weight(1.25)|difficulty(9)|spd_rtng(81) | weapon_length(90)|swing_damage(35 , cut) | thrust_damage(14 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
# tropas elite
 ["new_sword3", "Angle Sword", [("Sword3",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1020 , weight(1.25)|difficulty(9)|spd_rtng(81) | weapon_length(90)|swing_damage(35 , cut) | thrust_damage(14 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["le_pictishsword3", "Rich Saxon Sword", [("le_pictishsword3",0),("Scab_Pict_Sword", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1200 , weight(1.25)|difficulty(9)|spd_rtng(83) | weapon_length(95)|swing_damage(36 , cut) | thrust_damage(15 ,  pierce),imodbits_sword_high ],
#ricos nobles y tropas sumun
["saxon_richsword", "Nobleman Spatha", [("RichSpatha",0),("RichSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1100 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
#sin uso
["saxon_richsword2", "Nobleman Spatha", [("RichSpatha",0),("RichSpatha_scab", ixmesh_carry)], itp_unique|itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1100 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(90)|swing_damage(38 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

 ["new_sword4", "Angle Rich Sword", [("Sword4",0),("RichSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1020 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

## tropas de elite
 ["le_richsword2", "Rich Sword", [("le_richsword2",0),("RichSword3_scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1100 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
#sin uso
["le_richsword22", "Rich Sword", [("le_richsword2",0),("RichSword3_scab", ixmesh_carry)], itp_unique|itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.25)|difficulty(7)|spd_rtng(82) | weapon_length(94)|swing_damage(37 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

#sutton hoo sword, reyes y nobles anglos, sajones y jutos
 ["suttonhoosword", "Richman Sword", [("SuttonSpatha",0),("SuttonSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1040 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["bl_shsword", "Lord Sword", [("BL_shSword",0),("SuttonSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1040 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["le_pictishsword7", "Princep Angle Sword", [("le_pictishsword7",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1040 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

##jutos, sussex, dena pirates
["valssword", "Dena Sword", [("ValsSword1",0),("ValsSword1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1150 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(19 ,  pierce),imodbit_masterwork,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_5]],

###britones
#basicas britones
 ["celticsword", "Briton Sword", [("RichSword3",0),("RichSword3_scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["saxonsword1", "Sword", [("saxon_sword",0),("RichSword1_Scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(16 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],


#irlandeses y pictos
#scians para tropas medias (nivel 20 a 25), son baratos y terribles
 ["scianlong", "Long Scian", [("scianlong",0),("scianlong", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 1040 , weight(1.25)|difficulty(6)|spd_rtng(86) | weapon_length(94)|swing_damage(29 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["scianlongbone", "Scian Long Bone", [("scianlongbone",0),("scianlongbone", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 1040 , weight(1.25)|difficulty(6)|spd_rtng(86) | weapon_length(94)|swing_damage(29 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],


 #comun
 #britones, irlandeses y pictos
["irish_long_sword", "Celt Long Sword", [("irish_long_sword",0),("irish_long_sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip, 840 , weight(1.25)|difficulty(8)|spd_rtng(81) | weapon_length(99)|swing_damage(34 , cut) | thrust_damage(8 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["irish_long_sword2", "Celt Long Sword", [("irish_long_sword",0),("irish_long_sword", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip, 840 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(39 , cut) | thrust_damage(10 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#corta
["irish_sword",         "Godelic Short Sword", [("irish_sword",0),("irish_sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip, 1080 , weight(0.8)|difficulty(2)|spd_rtng(92) | weapon_length(70)|swing_damage(20 , cut) | thrust_damage(35 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["le_pictishsword6",         "Nobleman Short Sword", [("le_pictishsword6",0),("le_pictishsword6", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip, 1080 , weight(0.8)|difficulty(2)|spd_rtng(92) | weapon_length(70)|swing_damage(20 , cut) | thrust_damage(35 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["celtic2",         "Godelic Rich Short Sword", [("Celtic2",0),("Celtic2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip, 1080 , weight(0.8)|difficulty(2)|spd_rtng(92) | weapon_length(70)|swing_damage(22 , cut) | thrust_damage(33 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["le_pictishsword5",         "Rich Short Sword", [("le_pictishsword5",0),("le_pictishsword5", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip, 1080 , weight(0.8)|difficulty(2)|spd_rtng(92) | weapon_length(70)|swing_damage(22 , cut) | thrust_damage(33 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#larga
 ["pictish_longsword", "Pictish Longsword", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(81) | weapon_length(99)|swing_damage(34 , cut) | thrust_damage(13 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["pictish_longsword2", "Pictish Longsword", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(39 , cut) | thrust_damage(14 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#media
["irishword2",         "Godelic Sword", [("irishword2",0),("gallic_sword_scabbard_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip, 1160 , weight(1)|difficulty(8)|spd_rtng(87) | weapon_length(82)|swing_damage(30 , cut) | thrust_damage(28 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["celtic1",         "Godelic Sword", [("Celtic1",0),("CelticShort1_1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip, 1160 , weight(1)|difficulty(6)|spd_rtng(87) | weapon_length(82)|swing_damage(30 , cut) | thrust_damage(28 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#tipica
 ["celticv2_1", "Wooden pommel Sword", [("CelticV2_1",0),("CelticV2_1_scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.25)|difficulty(8)|spd_rtng(81) | weapon_length(90)|swing_damage(35 , cut) | thrust_damage(15 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["celticv2_2", "Wooden pommel Sword", [("CelticV2_2",0),("CelticV2_2_scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.25)|difficulty(8)|spd_rtng(81) | weapon_length(90)|swing_damage(35 , cut) | thrust_damage(15 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#tropas de elite
 ["celticshort1_1", "Warrior Sword", [("CelticShort1_1",0),("CelticShort1_1_Scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["celticshort1_2", "Celtic Sword", [("CelticShort1_2",0),("CelticShort1_2_Scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

#irlandeses y pictos nobles y rey
["pict_sword", "Princep Sword", [("Pict_sword",0),("Scab_Pict_Sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1080 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["kirkburn", "Nobleman Sword", [("Kirkburn",0),("Kirkburn_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1080 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

#champion sword para determinada elite o unidad, es una espada a dos manos
["celticsword2", "Goidel Champion Sword", [("gaelic_champion_sword",0),("gaelic_champion_sword", ixmesh_carry)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back,
 1220 , weight(2.35)|difficulty(11)|spd_rtng(81) | weapon_length(110)|swing_damage(44 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ],#espada


################espadas especiales
["espada_beowulf", "Hrunting", [("beowulfsword",0),("beowulfsword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 1260 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(97)|swing_damage(42 , cut) | thrust_damage(25 ,  pierce),imodbit_masterwork],
["new_sword","Erudino", [("le_pictishsword6",0),("le_pictishsword6", ixmesh_carry)], itp_type_one_handed_wpn|itp_always_loot|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 1118 , weight(1.25)|difficulty(10)|spd_rtng(82) | weapon_length(85)|swing_damage(24 , cut) | thrust_damage(35 ,  pierce),imodbit_masterwork], #chief cambiado
["suttonhoosword2", "Bandit King Sword", [("ValsSword1",0),("ValsSword1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1220 , weight(1.25)|difficulty(12)|spd_rtng(83) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(20 ,  pierce),imodbit_masterwork,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
#falcata
 ["long_axe_b", "Virio's Falcata", [("mackie_falcata01",0),("mackie_falcata01", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 1260 , weight(1)|difficulty(9)|spd_rtng(90) | weapon_length(89)|swing_damage(50 , cut) | thrust_damage(15 ,  pierce),imodbit_masterwork],

#king annan
 ["suttonhooswordking", "Cyning Annan's Sword", [("BL_shSword",0),("RichSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1120 , weight(1.25)|difficulty(12)|spd_rtng(82) | weapon_length(95)|swing_damage(36 , cut) | thrust_damage(20 ,  pierce),imodbit_masterwork,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["suttonhooswordking2", "Cyning Annan's Sword", [("BL_shSword",0),("RichSpatha_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1120 , weight(1.25)|difficulty(12)|spd_rtng(82) | weapon_length(95)|swing_damage(39 , cut) | thrust_damage(22 ,  pierce),imodbit_masterwork,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
#siren song
["siren_song", "Siren Song", [("bamburgh_sword",0),("sword_medieval_b_scabbard2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.3)|difficulty(12)|spd_rtng(82) | weapon_length(95)|swing_damage(37 , cut) | thrust_damage(13 ,  pierce),imodbit_masterwork,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["bastard_sword", "Siren Song", [("bamburgh_sword",0),("sword_medieval_b_scabbard2", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.3)|difficulty(12)|spd_rtng(82) | weapon_length(95)|swing_damage(40 , cut) | thrust_damage(15 ,  pierce),imodbit_masterwork,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

["sword_of_war", "Widow Maker", [("le_pictishsword7",0),("RichSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2500 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(16 ,  pierce),imodbits_sword_high ],
["great_sword", "Widow Maker", [("le_pictishsword7",0),("RichSpatha_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2500 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(37 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high ],

["arming_sword", "Wyrd", [("le_pictishsword7",0),("RichSword1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1640 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

["sword",         "Cniht", [("le_pictishsword7",0),("RichSword1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1640 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

["sarranid_cavalry_sword",         "Ic eom Eanferth", [("le_pictishsword7",0),("RichSword1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1640 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

["arabian_sword_d",         "Ri Petroc's Sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ],

["nomad_sabre",         "Ri Allech's Sword", [("BL_Sword01_02",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ],

#espada del rey de kent
["scimitar_b",         "Cyning Eadbald's Sword", [("ValsSword1",0),("ValsSword1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2500 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(16 ,  pierce),imodbits_sword_high ],
["scimitar_b2",         "Cyning Eadbald's Sword", [("ValsSword1",0),("ValsSword1_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2500 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(37 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high ],

#
 ["arabian_sword_a",         "Cyning Cynegils's Sword", [("RichSpatha",0),("RichSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2500 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(16 ,  pierce),imodbits_sword_high ],
["arabian_sword_b",         "Cyning Cynegils's Sword", [("RichSpatha",0),("RichSpatha_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2000 , weight(1.25)|difficulty(12)|spd_rtng(82) | weapon_length(95)|swing_damage(37 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high ],

 ["bastard_sword_a",         "Ri Cynddylan's Sword", [("RichSpatha",0),("RichSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2500 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(16 ,  pierce),imodbits_sword_high ],
["bastard_sword_b",         "Ri Cynddylan's Sword", [("RichSpatha",0),("RichSpatha_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2000 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(37 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high ],
#chief acaba

["sword_medieval_a",         "Ri Nowy's Sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ],
["sword_medieval_b",         "Ri Rhiwallon's Sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ],
["sword_medieval_c",         "Decapitator", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_long",         "Archangel", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ],
["sword_medieval_d_long",         "My Lady Sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ],
["sword_viking_1",         "Dyrnwyn", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high ],


["sword_viking_2", "Ruire Rogallach's Sword", [("Pict_sword",0),("Scab_Pict_Sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1580 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

["sword_viking_3", "Toiseach Gartnait's Sword", [("Kirkburn",0),("Kirkburn_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1580 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(36 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high],

#champion sword para rey
["sword_khergit_1", "Ruire Congal's Sword", [("gaelic_champion_sword",0),("gaelic_champion_sword", ixmesh_carry)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back,
 1520 , weight(2.35)|difficulty(12)|spd_rtng(82) | weapon_length(110)|swing_damage(47 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high ],#espada

["sword_medieval_b_small", "Ard Ruire Domnaill's Sword", [("Pict_sword",0),("Scab_Pict_Sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1580 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],



###########espadas chief acaba

#####Hachas finales#################################
 ####################################################
###########hachas 1m chief#########################
#todos
["hatchet",         "Hatchet", [("hatchet",0)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
360 , weight(2)|difficulty(2)|spd_rtng(80) | weapon_length(55)|swing_damage(25 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ], #chief modificado
["axefaradon2", "Axe", [("axefaradon2",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 462 , weight(1.5)|difficulty(8)|spd_rtng(80) | weapon_length(70)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["axe_2", "Big Axe", [("axe_2",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 495 , weight(2.5)|difficulty(8)|spd_rtng(75) | weapon_length(65)|swing_damage(34 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["axehammer_2", "Axe Hammer", [("axehammer_2",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 367 , weight(1.5)|difficulty(6)|spd_rtng(80) | weapon_length(61)|swing_damage(29 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["axehammer_1", "Axe Hammer", [("axehammer_1",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 444 , weight(2)|difficulty(6)|spd_rtng(77) | weapon_length(92)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["axe_hammer_long", "Long Axe Hammer", [("axe_hammer_long",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 462 , weight(2)|difficulty(6)|spd_rtng(75) | weapon_length(92)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["lui_waronehandedaxec", "Warrior Axe", [("axe_c",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 490 , weight(1.5)|difficulty(8)|spd_rtng(78) | weapon_length(70)|swing_damage(33 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["hand_axe",         "Hand Axe", [("le_werkaxt1",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
457 , weight(2)|difficulty(9)|spd_rtng(80) | weapon_length(70)|swing_damage(30 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ], #chief modificado
#invasores
 ["axe",                 "Engle Axe", [("axefaradon3",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
469 , weight(2)|difficulty(9)|spd_rtng(80) | weapon_length(73)|swing_damage(30 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["vikingaxeb",                 "Frankish Long Axe", [("vikingaxeb",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
481 , weight(2)|difficulty(9)|spd_rtng(79) | weapon_length(80)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5]],
 ["frankish_axe2",                 "Frankish Axe", [("frankish_Axe2",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
517 , weight(2)|difficulty(7)|spd_rtng(80) | weapon_length(76)|swing_damage(34 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5]],
 ["vikingaxe",                 "Decorated Axe", [("vikingaxe",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
467 , weight(2)|difficulty(9)|spd_rtng(79) | weapon_length(70)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["saxon_axe",                 "Saxon Axe", [("p_axe_1",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
461 , weight(2)|difficulty(9)|spd_rtng(80) | weapon_length(76)|swing_damage(32 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["lui_battleaxetwoh",                 "Germanic Axe", [("lui_battleaxetwoh",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
483 , weight(2)|difficulty(9)|spd_rtng(79) | weapon_length(79)|swing_damage(33 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
#elite, Rey o noble Sajon, anglo o juto
["talak_bearded_axe", "Hand Axe", [("talak_bearded_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 497 , weight(2)|difficulty(10)|spd_rtng(78) | weapon_length(65)|swing_damage(35 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["talak_nordic_axe",                 "Decorated Elite Axe", [("talak_nordic_axe",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
481 , weight(2)|difficulty(9)|spd_rtng(80) | weapon_length(79)|swing_damage(33 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["talak_jomsviking_axe", "War Axe", [("05einhendi_hedmarkrox",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 480 , weight(2)|difficulty(12)|spd_rtng(80) | weapon_length(65)|swing_damage(32 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],

#britones
 ["axehammer1",                 "Basic Axe Hammer", [("axehammer",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
439 , weight(2)|difficulty(7)|spd_rtng(79) | weapon_length(73)|swing_damage(29 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
 ["gallic_axe_1", "Briton Axe", [("gallic_axe_1",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 433 , weight(1.5)|difficulty(8)|spd_rtng(80) | weapon_length(63)|swing_damage(30 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

#pictos
 ["pictish_hatchet", "Pictish Hatchet", [("pictish_hatchet",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 491 , weight(1.5)|difficulty(8)|spd_rtng(80) | weapon_length(60)|swing_damage(34 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["one_handed_war_axe_a", "Short Hatchet", [("cavalry_Axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 492 , weight(1.5)|difficulty(8)|spd_rtng(79) | weapon_length(61)|swing_damage(33 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

#especiales 1 m
 ["one_handed_battle_axe_c", "Penda's Axe", [("talak_bearded_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 897 , weight(2)|difficulty(10)|spd_rtng(81) | weapon_length(70)|swing_damage(39 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_b", "Special Hatchet", [("cavalry_Axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 892 , weight(1.5)|difficulty(8)|spd_rtng(82) | weapon_length(66)|swing_damage(38 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],


######Hachas 2M

["battle_axe",         "Battle Axe", [("einhendi_haloygox",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
570 , weight(3)|difficulty(12)|spd_rtng(69) | weapon_length(98)|swing_damage(46 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["war_axe",         "Two Handed Axe", [("01tveirhendr_hedmarkox",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
620 , weight(3)|difficulty(13)|spd_rtng(66) | weapon_length(100)|swing_damage(48 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
#chief hachas especiales, hacha 2 m de rey
["thunder",         "Thunder", [("01einhendi_trondrox",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
2000 , weight(4)|difficulty(14)|spd_rtng(70) | weapon_length(100)|swing_damage(50 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["woden_fury",         "Woden Fury", [("03einhendi_trondrox",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
2000 , weight(4)|difficulty(14)|spd_rtng(70) | weapon_length(100)|swing_damage(50 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sword_two_handed_b",        "My Wife", [("02tveirhendr_hedmarkox",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
2000 , weight(4)|difficulty(14)|spd_rtng(70) | weapon_length(100)|swing_damage(50 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sword_two_handed_a",         "Manslayer", [("05einhendi_trondrox",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
2000 , weight(4)|difficulty(14)|spd_rtng(70) | weapon_length(100)|swing_damage(50 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
#################hachas 2 m acaba chief ############################
#############hachas acaba#########################################
 ####################################################################


################################spears lanzas y armas de asta empiezan###########################################################
 ###########################################################################################################
###todos palos
["staff",         "Staff", [("wooden_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 70 , weight(1.5)|difficulty(0)|spd_rtng(90) | weapon_length(140)|swing_damage(18 , blunt) | thrust_damage(16 ,  blunt),imodbits_polearm ], #cambiado chief
["quarter_staff", "Short Staff", [("staff_new",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 90 , weight(2)|difficulty(0)|spd_rtng(90) | weapon_length(130)|swing_damage(18 , blunt) | thrust_damage(17 ,  blunt),imodbits_polearm ], #cambiado chief
#Tempered added polearms chief
["shepherds_crook", "Shepherd's Crook", [("shepherds_crook",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 190 , weight(2)|difficulty(0)|spd_rtng(87) | weapon_length(150)|swing_damage(19 , blunt) | thrust_damage(10 ,  blunt),imodbits_polearm ],
#campesinos base
 ["pitch_fork",         "Pitch Fork", [("pitchfork_1",0)], itp_merchandise|itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 60 ,weight(3.5)|difficulty(0)|spd_rtng(70) | weapon_length(154)|swing_damage(17 , blunt) | thrust_damage(14 ,  pierce),imodbit_bent ], #chief cambiado
 ["battle_fork",         "Pitch Fork", [("pitchfork_2",0)], itp_merchandise|itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 70 ,weight(3.5)|difficulty(0)|spd_rtng(70) | weapon_length(164)|swing_damage(18 , blunt) | thrust_damage(15 ,  pierce),imodbit_bent ], #chief cambiado


#todos
#medium spear
["spear_1",         "Heavy Spear", [("fjadraspjot",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 420 , weight(4)|abundance(80)|difficulty(8)|spd_rtng(95) | weapon_length(160)|swing_damage(16 , blunt) | thrust_damage(32 ,  pierce),imodbits_polearm ],
["spear_2",         "Medium Spear", [("krokaspjott2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 460 , weight(2.25)|abundance(80)|difficulty(7)|spd_rtng(96) | weapon_length(155)|swing_damage(15 , blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],
["spear_3",         "Light Spear", [("hoggkesja",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 160 , weight(1.7)|abundance(90)|difficulty(6)|spd_rtng(97) | weapon_length(157)|swing_damage(14 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["spear_6",         "Spear", [("spjot",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 440 , weight(1.4)|abundance(90)|difficulty(4)|spd_rtng(98) | weapon_length(145)|swing_damage(13 , blunt) | thrust_damage(29 ,  pierce),imodbits_polearm ],
["lance",         "Boar Spear", [("svia2",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 425 , weight(1.18)|abundance(80)|difficulty(6)|spd_rtng(99) | weapon_length(145)|swing_damage(12 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],

#long spear
["spear_8",         "Long Spear", [("spjotkesja",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 180 , weight(2.55)|abundance(60)|difficulty(8)|spd_rtng(95) | weapon_length(251)|swing_damage(15 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["spear_4",         "Long War Spear", [("langr_bryntvari",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 495 , weight(3.28)|abundance(40)|difficulty(10)|spd_rtng(95) | weapon_length(230)|swing_damage(16 , blunt) | thrust_damage(32 ,  pierce),imodbits_polearm ],


#britones lanzas
 ["hasta",         "Long Hasta", [("hasta",0)], itp_type_polearm|itp_merchandise|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 510 , weight(3)|difficulty(10)|spd_rtng(96) | weapon_length(182)|swing_damage(14 , cut) | thrust_damage(34 ,  pierce),imodbits_polearm,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
 ["roman_spear_1",         "Briton Hasta", [("roman_spear_1",0)], itp_type_polearm|itp_merchandise|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 470 , weight(3)|difficulty(10)|spd_rtng(96) | weapon_length(172)|swing_damage(15 , cut) | thrust_damage(32 ,  pierce),imodbits_polearm,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
 ["roman_spear_2",         "Hasta", [("roman_spear_2",0)], itp_type_polearm|itp_merchandise|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 470 , weight(3)|difficulty(10)|spd_rtng(96) | weapon_length(177)|swing_damage(15 , cut) | thrust_damage(32 ,  pierce),imodbits_polearm,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
#spear de dos manos britona
["spear_7",         "Briton Two-Handed Spear", [("langr_hoggspjott1",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_spear|itcf_carry_spear, 600 , weight(2.5)|abundance(60)|difficulty(12)|spd_rtng(95) | weapon_length(242)|swing_damage(20 , blunt) | thrust_damage(40 ,  pierce),imodbits_polearm,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["sarranid_two_handed_axe_b",         "Briton Short Spear", [("01atgeirr1",0)], itp_type_polearm|itp_merchandise|itp_offset_lance| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 360 , weight(0.69)|abundance(100)|difficulty(0)|spd_rtng(107) | weapon_length(114)|swing_damage(12 , cut) | thrust_damage(24 ,  pierce),imodbits_polearm,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["sarranid_two_handed_mace_1",        "Briton Medium Spear", [("02spjot",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 440 , weight(1.4)|abundance(90)|difficulty(4)|spd_rtng(94) | weapon_length(145)|swing_damage(15 , blunt) | thrust_damage(29 ,  pierce),imodbits_polearm,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["sarranid_mace_1",         "Briton Light Spear", [("01krokaspjott2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 460 , weight(2.25)|abundance(80)|difficulty(6)|spd_rtng(97) | weapon_length(155)|swing_damage(13 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["sarranid_axe_b", "Briton Long Spear", [("01langr_bryntvari",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 495 , weight(3.28)|abundance(40)|difficulty(10)|spd_rtng(95) | weapon_length(230)|swing_damage(16 , blunt) | thrust_damage(32 ,  pierce),imodbits_polearm,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["scythe",         "Long Spear", [("02spjotkesja",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 180 , weight(2.55)|abundance(60)|difficulty(8)|spd_rtng(95) | weapon_length(251)|swing_damage(15 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],

###invasores
#saxon 2 h spear, lanza a dos manos
["twohand_spear",         "Two-Handed Spear", [("saxon2hspear",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_spear|itcf_carry_spear, 400 , weight(4)|difficulty(0)|spd_rtng(85) | weapon_length(199)|swing_damage(0 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
#spear 2 h cstadi con hoja larga como cuchilla
["saxon_spear", "Long Blade Spear", [("ped_heavy_spear_long",0)], itp_type_polearm|itp_merchandise|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear, 880, weight(3)|difficulty(10)|spd_rtng(94)|weapon_length(136)|swing_damage(40,cut)|thrust_damage(36,pierce), imodbits_polearm ],
 #1 mano
["sarranid_axe_a",         "Saxon Short Spear", [("atgeirr1",0)], itp_type_polearm|itp_merchandise|itp_offset_lance| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_sword_left_hip, 360 , weight(0.69)|abundance(100)|difficulty(0)|spd_rtng(107) | weapon_length(114)|swing_damage(12 , cut) | thrust_damage(24 ,  pierce),imodbits_polearm,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
# ["saxon_spear",         "Saxon Spear", [("saxon_spear",0)], itp_type_polearm|itp_merchandise|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 440 , weight(3)|difficulty(10)|spd_rtng(88) | weapon_length(175)|swing_damage(12 , cut) | thrust_damage(32 ,  pierce),imodbits_polearm,
#[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["spear_5",         "Saxon Long Spear", [("langr_svia",0)],itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 500 , weight(3.25)|difficulty(8)|spd_rtng(95) | weapon_length(235)|swing_damage(17 , blunt) | thrust_damage(31 ,  pierce),imodbits_polearm,
[], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

# Goedendag Irish y pictos
 ["club_with_spike_head",  "Hunting Spear", [("04hoggkesja",0)],  itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 160 , weight(1.7)|abundance(90)|difficulty(7)|spd_rtng(97) | weapon_length(157)|swing_damage(15 , blunt) | thrust_damage(31 ,  pierce),imodbits_polearm,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["sarranid_two_handed_axe_a",          "Medium Spear", [("02bryntvari",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 180 , weight(2.25)|difficulty(6)|spd_rtng(97) | weapon_length(145)|swing_damage(15 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["boar_spear",         "Pictish Boar Spear", [("02svia2",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 425 , weight(1.18)|abundance(80)|difficulty(6)|spd_rtng(88) | weapon_length(145)|swing_damage(16 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["military_fork",          "Medium Spear", [("03bryntvari",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 180 , weight(2.25)|difficulty(6)|spd_rtng(97) | weapon_length(145)|swing_damage(15 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["spear",         "Godelic Light Spear", [("05hoggkesja",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 160 , weight(1.7)|abundance(90)|difficulty(7)|spd_rtng(97) | weapon_length(157)|swing_damage(15 , blunt) | thrust_damage(31 ,  pierce),imodbits_polearm,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["war_spear",         "Godelic Heavy Spear", [("fjadraspjot",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 420 , weight(4)|abundance(80)|difficulty(9)|spd_rtng(97) | weapon_length(160)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],


#lanzas magicas especiales reyes y nobles
["long_spiked_club",         "Hope Warrior", [("02krokaspjott1",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 360 , weight(2.55)|difficulty(8)|spd_rtng(93) | weapon_length(180)|swing_damage(17 , blunt) | thrust_damage(33 ,  pierce),imodbit_balanced ],
["long_hafted_knobbed_mace",         "Breath of Dragon", [("05bryntvari2",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 360 , weight(2.55)|difficulty(8)|spd_rtng(86) | weapon_length(155)|swing_damage(15 , blunt) | thrust_damage(33 ,  pierce),imodbit_balanced ],
["long_hafted_spiked_mace",         "Raven", [("04bryntvari2",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 360 , weight(2.55)|difficulty(8)|spd_rtng(96) | weapon_length(155)|swing_damage(17 , blunt) | thrust_damage(33 ,  pierce),imodbit_balanced ],
#lanzas especiales chief
 ["shortened_spear",         "Dawn Ray", [("krokaspjott1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 260 , weight(2.55)|difficulty(8)|spd_rtng(96) | weapon_length(180)|swing_damage(13 , blunt) | thrust_damage(32 ,  pierce),imodbit_balanced ],
#Chief new mace neko y quest
["new_mace","Neko's Spear", [("krokaspjott1",0)] , itp_type_polearm|itp_always_loot|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear|itcf_carry_spear,
 1060,weight(2.55)|difficulty(8)|spd_rtng(90) | weapon_length(180)|swing_damage(14 , blunt) | thrust_damage(32 ,  pierce),imodbit_balanced ], #chief cambiado

#####estandartes finales chief####
 #############################
#sajon, anglo y juto banner
["wessexbanner1",         "Boar Banner", [("wessexbanner1",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword, 780 , weight(2)|difficulty(2)|spd_rtng(75) | weapon_length(140)|swing_damage(18 , cut) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
["wessexbanner2",         "Horse Banner", [("wessexbanner2",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword, 780 , weight(2)|difficulty(2)|spd_rtng(75) | weapon_length(140)|swing_damage(18 , cut) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
["wessexbanner3",         "Banner", [("wessexbanner3",0)],itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword, 780 , weight(2)|difficulty(2)|spd_rtng(75) | weapon_length(140)|swing_damage(18 , cut) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
["wessexbanner4",         "Banner", [("wessexbanner4",0)],itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword, 780 , weight(2)|difficulty(2)|spd_rtng(75) | weapon_length(140)|swing_damage(18 , cut) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
["wessexbanner5",         "Banner", [("wessexbanner5",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword, 780 , weight(2)|difficulty(2)|spd_rtng(75) | weapon_length(140)|swing_damage(18 , cut) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
["wessexbanner6",         "Banner", [("wessexbanner6",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword, 780 , weight(2)|difficulty(2)|spd_rtng(75) | weapon_length(140)|swing_damage(18 , cut) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
["wessexbanner7",         "Banner", [("wessexbanner7",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword, 780 , weight(2)|difficulty(2)|spd_rtng(75) | weapon_length(140)|swing_damage(18 , cut) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
["wessexbanner8",         "Banner", [("wessexbanner8",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword, 780 , weight(2)|difficulty(2)|spd_rtng(75) | weapon_length(140)|swing_damage(18 , cut) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
["wessexbanner9",         "Banner", [("wessexbanner9",0)], itp_merchandise|itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword, 780 , weight(2)|difficulty(2)|spd_rtng(75) | weapon_length(140)|swing_damage(18 , cut) | thrust_damage(0 ,  pierce),imodbits_none ], #chief cambiado
#todo correcto pero problemas para ajustar textura, pasable por ahora
["personalbanner",         "Personal Banner", [("personalbanner",0)], itp_merchandise|itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword, 780 , weight(2)|difficulty(2)|spd_rtng(75) | weapon_length(140)|swing_damage(18 , cut) | thrust_damage(0 ,  pierce),imodbits_none,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],
#####estandartes finales acaba####
 ##############################
###############lanzas chief acaba #######################################
###########################################################################


##chief armas acaba#########

# SHIELDS
###Shields chief############################################################
#escudo pequenos####
 #########
 #comunes

["wooden_shield", "Small Round Shield", [("buckler1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["nordic_shield", "Small Round Shield", [("buckler52",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["talak_buckler", "Small Round Shield", [("talak_buckler",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["ckler", "Small Round Shield", [("ckler",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  200 , weight(2.5)|hit_points(240)|body_armor(4)|spd_rtng(85)|shield_width(45),imodbits_shield ],
["buckler6", "Small Round Shield", [("buckler6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler7", "Small Round Shield", [("buckler7",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler8", "Small Round Shield", [("buckler8",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler9", "Small Round Shield", [("buckler9",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler10", "Small Round Shield", [("buckler10",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler11", "Small Round Shield", [("buckler11",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler12", "Small Round Shield", [("buckler12",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler13", "Small Round Shield", [("buckler13",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler14", "Small Round Shield", [("buckler14",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler15", "Small Round Shield", [("buckler15",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler16", "Small Round Shield", [("buckler16",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler28", "Small Round Shield", [("buckler28",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler32", "Small Round Shield", [("buckler32",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler42", "Small Round Shield", [("buckler42",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],

#celtas altos
 ["buckler17", "Small Round Shield", [("buckler17",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler18", "Small Round Shield", [("buckler18",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler19", "Small Round Shield", [("buckler19",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler20", "Small Round Shield", [("buckler20",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler21", "Small Round Shield", [("buckler21",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler22", "Small Round Shield", [("buckler22",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler23", "Small Round Shield", [("buckler23",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler24", "Small Round Shield", [("buckler24",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler25", "Small Round Shield", [("buckler25",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler26", "Small Round Shield", [("buckler26",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler27", "Small Round Shield", [("buckler27",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],
["buckler29", "Small Round Shield", [("buckler29",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(75)|shield_width(40),imodbits_shield ],

#pictos
["buckler2", "Small shield", [("buckler2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(70)|shield_width(40),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["buckler3", "Small shield", [("buckler3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(70)|shield_width(40),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["buckler4", "Small shield", [("buckler4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(70)|shield_width(40),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["buckler5", "Small shield", [("buckler5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  300 , weight(2)|hit_points(250)|body_armor(5)|spd_rtng(70)|shield_width(40),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

#ligeros acaba
#irlandeses escudos ligeros
 ["gaelic_shield_a", "Gaelic Shield", [("Gaelic_Shield_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  340 , weight(4)|hit_points(270)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["gaelic_shield_b", "Gaelic Shield", [("Gaelic_Shield_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  340 , weight(4)|hit_points(270)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["gaelic_shield_c", "Gaelic Shield", [("Gaelic_Shield_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  340 , weight(4)|hit_points(270)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["gaelic_shield_d", "Gaelic Shield", [("Gaelic_Shield_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  340 , weight(4)|hit_points(270)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["gaelic_shield_e", "Gaelic Shield", [("Gaelic_Shield_e",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  340 , weight(4)|hit_points(270)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["gaelic_shield_f", "Gaelic Shield", [("Gaelic_Shield_f",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  340 , weight(4)|hit_points(270)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["gaelic_shield_g", "Gaelic Shield", [("Gaelic_Shield_g",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  340 , weight(4)|hit_points(270)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["gaelic_shield_h", "Gaelic Shield", [("Gaelic_Shield_h",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  340 , weight(4)|hit_points(270)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["gaelic_shield_i", "Gaelic Shield", [("Gaelic_Shield_i",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  340 , weight(4)|hit_points(270)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["gaelic_shield_j", "Gaelic Shield", [("Gaelic_Shield_j",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  340 , weight(4)|hit_points(270)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

#escudos lenticular celtas e irlandeses
 ["celtic_shield_small_round_a", "Lenticular Shield", [("celtic_shield_small_round_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["celtic_shield_small_round_b", "Lenticular Shield", [("celtic_shield_small_round_b",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["celtic_shield_small_round_c", "Lenticular Shield", [("celtic_shield_small_round_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["celtic_shield_small_round_d", "Lenticular Shield", [("celtic_shield_small_round_d",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["celtic_shield_small_round_e", "Lenticular Shield", [("celtic_shield_small_round_e",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["celtic_shield_small_round_f", "Lenticular Shield", [("celtic_shield_small_round_f",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  410 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["shield_small_round", "Lenticular Shield", [("shield_small_round",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#escudos medianos. cambiar motivos y mirar faccion, son los lenticulares
  ["celtic_vae_shield1", "Lenticular Round Shield", [("celtic_vae_shield1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
  ["celtic_vae_shield2", "Lenticular Round Shield", [("celtic_vae_shield2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
  ["celtic_vae_shield3", "Lenticular Round Shield", [("celtic_vae_shield3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
  ["celtic_vae_shield4", "Lenticular Round Shield", [("celtic_vae_shield4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
  ["celtic_vae_shield5", "Lenticular Round Shield", [("celtic_vae_shield5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#lenticular celtas
  ["celtic_vae_shield6", "Lenticular Round Shield", [("celtic_vae_shield6",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
  ["celtic_vae_shield7", "Lenticular Round Shield", [("celtic_vae_shield7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
  ["celtic_vae_shield8", "Lenticular Round Shield", [("celtic_vae_shield8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
  ["celtic_vae_shield9", "Lenticular Round Shield", [("celtic_vae_shield9",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
  ["celtic_vae_shield10", "Lenticular Round Shield", [("celtic_vae_shield10",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(2.5)|hit_points(400)|body_armor(7)|spd_rtng(60)|shield_width(60)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],


#TODOS: infanteria ligera
#["wooden_buckler1", "Small shield", [("wooden_buckler1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  185 , weight(2)|hit_points(250)|body_armor(2)|spd_rtng(70)|shield_width(40),imodbits_shield ],
################ligeros chief #######


########Pictos

####escudos medios
#elite pictos
["caledonian_shield", "Pict Shield", [("caledonian_shield",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["caledonian_shield_dog", "Pict Shield", [("caledonian_shield_dog",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["caledonian_shield_raven", "Pict Shield", [("caledonian_shield_raven",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["square_shield", "Pict Simple Shield", [("square_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  200 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(60)|shield_width(55),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield1", "Pict Shield", [("vae_caledonian_shield1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield2", "Pict Shield", [("vae_caledonian_shield2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield3", "Pict Shield", [("vae_caledonian_shield3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield4", "Pict Shield", [("vae_caledonian_shield4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield5", "Pict Shield", [("vae_caledonian_shield5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield6", "Pict Shield", [("vae_caledonian_shield6",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield7", "Pict Shield", [("vae_caledonian_shield7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield8", "Pict Shield", [("vae_caledonian_shield8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield9", "Pict Shield", [("vae_caledonian_shield9",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield10", "Pict Shield", [("vae_caledonian_shield10",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield11", "Pict Shield", [("vae_caledonian_shield11",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield12", "Pict Shield", [("vae_caledonian_shield12",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield13", "Pict Shield", [("vae_caledonian_shield13",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield14", "Pict Shield", [("vae_caledonian_shield14",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_caledonian_shield15", "Pict Shield", [("vae_caledonian_shield15",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  385 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

#h_shield
["h_shield", "H Shield", [("h_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_h_shield1", "H Shield", [("vae_h_shield1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_h_shield2", "H Shield", [("vae_h_shield2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_h_shield3", "H Shield", [("vae_h_shield3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_h_shield4", "H Shield", [("vae_h_shield4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_h_shield5", "H Shield", [("vae_h_shield5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_h_shield6", "H Shield", [("vae_h_shield6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_h_shield7", "H Shield", [("vae_h_shield7",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_h_shield8", "H Shield", [("vae_h_shield8",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_h_shield9", "H Shield", [("vae_h_shield9",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_h_shield10", "H Shield", [("vae_h_shield10",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_h_shield11", "H Shield", [("vae_h_shield11",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_h_shield12", "H Shield", [("vae_h_shield12",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#tarcza_harfa
 ["tarcza_harfa", "Pictish shield", [("tarcza_harfa",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_1", "Pictish shield", [("tarcza_harfa_vae_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_2", "Pictish shield", [("tarcza_harfa_vae_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_3", "Pictish shield", [("tarcza_harfa_vae_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_4", "Pictish shield", [("tarcza_harfa_vae_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_5", "Pictish shield", [("tarcza_harfa_vae_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_6", "Pictish shield", [("tarcza_harfa_vae_6",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_7", "Pictish shield", [("tarcza_harfa_vae_7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_8", "Pictish shield", [("tarcza_harfa_vae_8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_9", "Pictish shield", [("tarcza_harfa_vae_9",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_10", "Pictish shield", [("tarcza_harfa_vae_10",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_11", "Pictish shield", [("tarcza_harfa_vae_11",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_12", "Pictish shield", [("tarcza_harfa_vae_12",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_13", "Pictish shield", [("tarcza_harfa_vae_13",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_14", "Pictish shield", [("tarcza_harfa_vae_14",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_15", "Pictish shield", [("tarcza_harfa_vae_15",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_16", "Pictish shield", [("tarcza_harfa_vae_16",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_17", "Pictish shield", [("tarcza_harfa_vae_17",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_18", "Pictish shield", [("tarcza_harfa_vae_18",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_19", "Pictish shield", [("tarcza_harfa_vae_19",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_20", "Pictish shield", [("tarcza_harfa_vae_20",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["tarcza_harfa_vae_21", "Pictish shield", [("tarcza_harfa_vae_21",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3)|hit_points(250)|body_armor(4)|spd_rtng(80)|shield_width(40)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#escudo cuadrado, pictos e irlandeses
["tarcze_celtyckie", "Square Shield", [("tarcze_celtyckie",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["pict_shield_a", "Square Shield", [("pict_shield_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_1", "Square Shield", [("vae_cuadrado_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_2", "Square Shield", [("vae_cuadrado_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_3", "Square Shield", [("vae_cuadrado_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_4", "Square Shield", [("vae_cuadrado_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_5", "Square Shield", [("vae_cuadrado_5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_6", "Square Shield", [("vae_cuadrado_6",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_7", "Square Shield", [("vae_cuadrado_7",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_8", "Square Shield", [("vae_cuadrado_8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_9", "Square Shield", [("vae_cuadrado_9",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_10", "Square Shield", [("vae_cuadrado_10",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_11", "Square Shield", [("vae_cuadrado_11",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_12", "Square Shield", [("vae_cuadrado_12",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_13", "Square Shield", [("vae_cuadrado_13",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_14", "Square Shield", [("vae_cuadrado_14",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_15", "Square Shield", [("vae_cuadrado_15",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_16", "Square Shield", [("vae_cuadrado_16",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_17", "Square Shield", [("vae_cuadrado_17",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_18", "Square Shield", [("vae_cuadrado_18",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_19", "Square Shield", [("vae_cuadrado_19",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_20", "Square Shield", [("vae_cuadrado_20",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_21", "Square Shield", [("vae_cuadrado_21",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_22", "Square Shield", [("vae_cuadrado_22",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_23", "Square Shield", [("vae_cuadrado_23",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_24", "Square Shield", [("vae_cuadrado_24",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_25", "Square Shield", [("vae_cuadrado_25",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_26", "Square Shield", [("vae_cuadrado_26",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_27", "Square Shield", [("vae_cuadrado_27",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["vae_cuadrado_28", "Square Shield", [("vae_cuadrado_28",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(3)|hit_points(280)|body_armor(7)|spd_rtng(65)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

###escudo rectangular picto e irlandes
 ["vae_escudo_picto", "Rectangular Shield", [("vae_escudo_picto",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto2", "Rectangular Shield", [("vae_escudo_picto2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto3", "Rectangular Shield", [("vae_escudo_picto3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto4", "Rectangular Shield", [("vae_escudo_picto4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto5", "Rectangular Shield", [("vae_escudo_picto5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto6", "Rectangular Shield", [("vae_escudo_picto6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto7", "Rectangular Shield", [("vae_escudo_picto7",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto8", "Rectangular Shield", [("vae_escudo_picto8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto9", "Rectangular Shield", [("vae_escudo_picto9",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto10", "Rectangular Shield", [("vae_escudo_picto10",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto11", "Rectangular Shield", [("vae_escudo_picto11",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto12", "Rectangular Shield", [("vae_escudo_picto12",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto13", "Rectangular Shield", [("vae_escudo_picto13",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto14", "Rectangular Shield", [("vae_escudo_picto14",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto15", "Rectangular Shield", [("vae_escudo_picto15",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto27", "Rectangular Shield", [("vae_escudo_picto27",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["vae_escudo_picto28", "Rectangular Shield", [("vae_escudo_picto28",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["shield_ip", "Rectangular Shield", [("Shield_IP",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],


#escudo scyld#### irlandeses y pictos
["scyld", "Pictish Shield", [("scyld",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["scyld1", "Pictish Shield", [("vae_scyld1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["scyld2", "Pictish Shield", [("vae_scyld2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["scyld3", "Pictish Shield", [("vae_scyld3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["scyld4", "Pictish Shield", [("vae_scyld4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["scyld5", "Pictish Shield", [("vae_scyld5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["scyld6", "Pictish Shield", [("vae_scyld6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["scyld7", "Pictish Shield", [("vae_scyld7",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["scyld8", "Pictish Shield", [("godelic_shield3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["scyld9", "Pictish Shield", [("godelic_shield2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["scyld10", "Pictish Shield", [("godelic_shield1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(300)|body_armor(8)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,
 [], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#####




###########escudos pesados chief ########

########invasores
###escudos pesados
 ["viking_shield_round_27", "Round Shield", [("BL_Roundshields_03",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["viking_shield_round_28", "Round Shield", [("BL_Roundshields_04",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["viking_shield_round_17", "Round Shield", [("BL_Roundshields_01",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["viking_shield_round_33", "Round Shield", [("BL_Roundshields_20",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["viking_shield_round_26", "Round Shield", [("BL_Roundshields_02",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["viking_shield_round_34", "Round Shield", [("BL_Roundshields_05",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_ocho", "Round Shield", [("BL_Roundshields_06",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["steel_shield", "Round Shield", [("BL_Roundshields_22",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

["nomad_shield", "Round Shield", [("BL_Roundshields_21",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["leather_covered_round_shield", "Round Shield", [("BL_Roundshields_13",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["hide_covered_round_shield", "Round Shield", [("BL_Roundshields_17",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_heater_c", "Round Shield", [("BL_Roundshields_18",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["bl_roundshields_a", "Round Shield", [("BL_Roundshields_15",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["norman_shield_1",         "Round Shield", [("BL_Roundshields_07",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["norman_shield_2",         "Round Shield", [("BL_Roundshields_08",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["norman_shield_3",         "Round Shield", [("BL_Roundshields_16",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

["norman_shield_4",         "Round Shield", [("BL_Roundshields_10",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["norman_shield_6",         "Frisian Round Shield", [("BL_Roundshields_09",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["norman_shield_7",         "Frisian Round Shield", [("BL_Roundshields_14",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["norman_shield_8",         "Frisian Round Shield", [("BL_Roundshields_19",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
 ["plate_covered_round_shield", "Godelic Round Shield", [("BL_Roundshields_12",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["norman_shield_5",         "Round Shield", [("BL_Roundshields_11",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

###

#inf pesada
["ad_viking_shield_round_01", "Round Shield", [("ad_viking_shield_round_01",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_02", "Round Shield", [("ad_viking_shield_round_02",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_03", "Round Shield", [("ad_viking_shield_round_03",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_04", "Round Shield", [("ad_viking_shield_round_04",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_05", "Round Shield", [("ad_viking_shield_round_05",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["ad_viking_shield_round_06", "Round Shield", [("ad_viking_shield_round_06",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_07", "Round Shield", [("ad_viking_shield_round_07",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_08", "Round Shield", [("ad_viking_shield_round_08",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_09", "Round Shield", [("ad_viking_shield_round_09",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_10", "Round Shield", [("ad_viking_shield_round_10",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_11", "Round Shield", [("ad_viking_shield_round_11",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_12", "Round Shield", [("ad_viking_shield_round_12",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_13", "Round Shield", [("ad_viking_shield_round_13",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_16", "Round Shield", [("ad_viking_shield_round_16",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_17", "Round Shield", [("ad_viking_shield_round_17",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_18", "Round Shield", [("ad_viking_shield_round_18",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_19", "Round Shield", [("ad_viking_shield_round_19",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_20", "Round Shield", [("ad_viking_shield_round_20",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_21", "Round Shield", [("ad_viking_shield_round_21",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_22", "Round Shield", [("ad_viking_shield_round_22",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_23", "Round Shield", [("ad_viking_shield_round_23",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_24", "Round Shield", [("ad_viking_shield_round_24",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_25", "Round Shield", [("ad_viking_shield_round_25",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_26", "Round Shield", [("ad_viking_shield_round_26",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_27", "Round Shield", [("ad_viking_shield_round_27",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_28", "Round Shield", [("ad_viking_shield_round_28",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_29", "Round Shield", [("ad_viking_shield_round_29",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_31", "Round Shield", [("ad_viking_shield_round_31",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["ad_viking_shield_round_32", "Round Shield", [("ad_viking_shield_round_32",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_33", "Round Shield", [("ad_viking_shield_round_33",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_34", "Round Shield", [("ad_viking_shield_round_34",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_35", "Round Shield", [("ad_viking_shield_round_35",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_36", "Round Shield", [("ad_viking_shield_round_36",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_37", "Round Shield", [("ad_viking_shield_round_37",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["ad_viking_shield_round_38", "Round Shield", [("ad_viking_shield_round_38",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_39", "Round Shield", [("ad_viking_shield_round_39",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_40", "Round Shield", [("ad_viking_shield_round_40",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_41", "Round Shield", [("ad_viking_shield_round_41",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_42", "Round Shield", [("ad_viking_shield_round_42",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_43", "Round Shield", [("ad_viking_shield_round_43",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

#reyes y altos nobles invasores, escudos con adornos metalicos
 ["ad_viking_shield_round_15", "King Round Shield", [("ad_viking_shield_round_15",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["ad_viking_shield_round_30", "King Round Shield", [("ad_viking_shield_round_30",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_20", "Nobleman Round Shield", [("saxon_adorno_20",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_1", "Nobleman Round Shield", [("saxon_adorno_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_2", "Nobleman Round Shield", [("saxon_adorno_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_3", "Nobleman Round Shield", [("saxon_adorno_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_4", "Nobleman Round Shield", [("saxon_adorno_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_5", "Nobleman Round Shield", [("saxon_adorno_5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

["saxon_adorno_6", "Nobleman Round Shield", [("saxon_adorno_6",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_7", "Nobleman Round Shield", [("saxon_adorno_7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_8", "Nobleman Round Shield", [("saxon_adorno_8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_9", "Nobleman Round Shield", [("saxon_adorno_9",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_10", "Nobleman Round Shield", [("saxon_adorno_10",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_11", "Nobleman Round Shield", [("saxon_adorno_11",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_12", "Nobleman Round Shield", [("saxon_adorno_12",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_13", "Nobleman Round Shield", [("saxon_adorno_13",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

["saxon_adorno_14", "Nobleman Round Shield", [("saxon_adorno_14",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_15", "Nobleman Round Shield", [("saxon_adorno_15",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_16", "Nobleman Round Shield", [("saxon_adorno_16",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_17", "Nobleman Round Shield", [("saxon_adorno_17",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_18", "Nobleman Round Shield", [("saxon_adorno_18",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["saxon_adorno_19", "Nobleman Round Shield", [("saxon_adorno_19",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  650 , weight(5)|hit_points(500)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],


["shield_1", "Round Shield", [("shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_2", "Round Shield", [("shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_3", "Round Shield", [("shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_4", "Round Shield", [("shield_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_5", "Round Shield", [("shield_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_6", "Round Shield", [("shield_6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_7", "Round Shield", [("shield_7",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_8", "Round Shield", [("shield_8",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_9", "Round Shield", [("shield_9",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_10", "Round Shield", [("shield_10",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_11", "Round Shield", [("shield_11",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_12", "Round Shield", [("shield_12",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_13", "Round Shield", [("shield_13",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_14", "Round Shield", [("shield_14",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_15", "Round Shield", [("shield_15",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_16", "Round Shield", [("shield_16",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["shield_17", "Round Shield", [("shield_17",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

#cualquier faccion
["leathershield_medium", "Round Shield", [("leathershield_medium",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["leathershield_small_d", "Round Shield", [("leathershield_small_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(4.5)|hit_points(310)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["leathershield_medium_y", "Round Shield", [("leathershield_medium_y",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["leathershield_medium_d", "Round Shield", [("leathershield_medium_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["leathershield_medium_b", "Round Shield", [("leathershield_medium_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["leathershield_small_b", "Round Shield", [("leathershield_small_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(4.5)|hit_points(310)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["woodenshield_medium", "Round Shield", [("woodenshield_medium",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["woodenshield_medium_d", "Round Shield", [("woodenshield_medium_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(310)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["woodenshield_small_d", "Round Shield", [("woodenshield_small_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(4.5)|hit_points(310)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["woodenshield_small", "Round Shield", [("woodenshield_small",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  400 , weight(4.5)|hit_points(310)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],

####escudos pesados celtas
["celticsaxon_adorno_1", "Celtic Round Shield", [("celticsaxon_adorno_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(400)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["celticsaxon_adorno_2", "Celtic Round Shield", [("celticsaxon_adorno_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(400)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["celticsaxon_adorno_3", "Celtic Round Shield", [("celticsaxon_adorno_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(400)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["celticsaxon_adorno_4", "Celtic Round Shield", [("celticsaxon_adorno_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(400)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["celticsaxon_adorno_5", "Celtic Round Shield", [("celticsaxon_adorno_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(400)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["celticsaxon_adorno_6", "Celtic Round Shield", [("celticsaxon_adorno_6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(400)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["celticsaxon_adorno_7", "Celtic Round Shield", [("celticsaxon_adorno_7",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(400)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["celticsaxon_adorno_8", "Celtic Round Shield", [("celticsaxon_adorno_8",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(400)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["celticsaxon_adorno_9", "Celtic Round Shield", [("celticsaxon_adorno_9",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(400)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["celticsaxon_adorno_10", "Celtic Round Shield", [("celticsaxon_adorno_10",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(400)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],

###escudos cantabros
["cantabro_shield_1", "Cantabrian Round Shield", [("cantabro_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  600 , weight(4.5)|hit_points(400)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield],
["cantabro_shield_2", "Cantabrian Round Shield", [("cantabro_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  600 , weight(4.5)|hit_points(400)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield],
["cantabro_shield_3", "Cantabrian Round Shield", [("cantabro_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  600 , weight(4.5)|hit_points(400)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield],
["cantabro_shield_4", "Cantabrian Round Shield", [("cantabro_shield_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  600 , weight(4.5)|hit_points(400)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield],
["cantabro_shield_5", "Cantabrian Round Shield", [("cantabro_shield_5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  600 , weight(4.5)|hit_points(400)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield],
["cantabro_shield_6", "Cantabrian Round Shield", [("cantabro_shield_6",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  600 , weight(4.5)|hit_points(400)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield],
["cantabro_shield_7", "Cantabrian Round Shield", [("cantabro_shield_7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  600 , weight(4.5)|hit_points(400)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield],
["cantabro_shield_8", "Cantabrian Round Shield", [("cantabro_shield_8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  600 , weight(4.5)|hit_points(400)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield],
["cantabro_shield_9", "Cantabrian Round Shield", [("cantabro_shield_9",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  600 , weight(4.5)|hit_points(400)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield],
["cantabro_shield_10", "Cantabrian Round Shield", [("cantabro_shield_10",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  600 , weight(4.5)|hit_points(400)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield],


#######Britones
####britones y celtas####
 ########################
["shield_round_01", "Briton Round Shield", [("shield_round_01",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
 ["shield_round_02", "Briton Round Shield", [("shield_round_02",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["shield_round_03", "Briton Round Shield", [("shield_round_03",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["shield_round_04", "Briton Round Shield", [("shield_round_04",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["shield_round_05", "Briton Round Shield", [("shield_round_05",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["shield_round_06", "Briton Round Shield", [("shield_round_06",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["shield_round_07", "Briton Round Shield", [("shield_round_07",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["shield_round_08", "Weak Round Shield", [("shield_round_08",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  500 , weight(4.5)|hit_points(350)|body_armor(9)|spd_rtng(55)|shield_width(70)|difficulty(2),imodbits_shield,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],


###############chief shields acaban############################


#nuevos escudos chief de brust Briton
#normal
 #unique chief
["tab_shield_round_a", "native", [("tableau_shield_round_5",0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
26 , weight(2.5)|hit_points(195)|body_armor(4)|spd_rtng(93)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":agent_no", ":troop_no")])]],
["tab_shield_round_b", "native", [("tableau_shield_round_3",0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
65 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":agent_no", ":troop_no")])]],
#chief unique acaba


["tab_shield_round_c", "Banner Round Shield", [("tableau_shield_round_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
400 , weight(4.5)|hit_points(350)|body_armor(8)|spd_rtng(55)|shield_width(65)|difficulty(2),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_round_shield_2", ":agent_no", ":troop_no")])]], #cambiado chief

#chief unique empieza
["tab_shield_round_d", "native", [("tableau_shield_round_1",0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
210 , weight(4)|hit_points(350)|body_armor(15)|spd_rtng(84)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_round_e", "native", [("tableau_shield_round_4",0)], itp_unique|itp_type_shield, itcf_carry_round_shield,
430 , weight(4.5)|hit_points(410)|body_armor(19)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":agent_no", ":troop_no")])]],

["tab_shield_kite_a", "native",   [("tableau_shield_kite_1" ,0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
33 , weight(2)|hit_points(165)|body_armor(5)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_kite_b", "native",   [("tableau_shield_kite_3" ,0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
70 , weight(2.5)|hit_points(215)|body_armor(10)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_kite_c", "native",   [("tableau_shield_kite_2" ,0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
156 , weight(3)|hit_points(265)|body_armor(13)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_kite_d", "native",   [("tableau_shield_kite_2" ,0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
320 , weight(3.5)|hit_points(310)|body_armor(18)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_kite_cav_a", "native",   [("tableau_shield_kite_4" ,0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
205 , weight(2)|hit_points(165)|body_armor(14)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],
["tab_shield_kite_cav_b", "native",   [("tableau_shield_kite_4" ,0)], itp_unique|itp_type_shield, itcf_carry_kite_shield,
360 , weight(2.5)|hit_points(225)|body_armor(23)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],

["tab_shield_heater_a", "native",   [("tableau_shield_heater_1" ,0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
36 , weight(2)|hit_points(160)|body_armor(6)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_b", "native",   [("tableau_shield_heater_1" ,0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
74 , weight(2.5)|hit_points(210)|body_armor(11)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_c", "native",   [("tableau_shield_heater_1" ,0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_d", "native",   [("tableau_shield_heater_1" ,0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
332 , weight(3.5)|hit_points(305)|body_armor(19)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_cav_a", "native",   [("tableau_shield_heater_2" ,0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
229 , weight(2)|hit_points(160)|body_armor(16)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_heater_cav_b", "native",   [("tableau_shield_heater_2" ,0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
390 , weight(2.5)|hit_points(220)|body_armor(23)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])]],

["tab_shield_pavise_a", "native",   [("tableau_shield_pavise_2" ,0)], itp_unique|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
60 , weight(3.5)|hit_points(280)|body_armor(4)|spd_rtng(89)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_b", "native",   [("tableau_shield_pavise_2" ,0)], itp_unique|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
114 , weight(4)|hit_points(360)|body_armor(8)|spd_rtng(85)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_c", "native",   [("tableau_shield_pavise_1" ,0)], itp_unique|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
210 , weight(4.5)|hit_points(430)|body_armor(10)|spd_rtng(81)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_d", "native",   [("tableau_shield_pavise_1" ,0)], itp_unique|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
370 , weight(5)|hit_points(550)|body_armor(14)|spd_rtng(78)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],

["tab_shield_small_round_a", "native", [("tableau_shield_small_round_3",0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
96 , weight(2)|hit_points(160)|body_armor(8)|spd_rtng(105)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_b", "native", [("tableau_shield_small_round_1",0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
195 , weight(2.5)|hit_points(200)|body_armor(14)|spd_rtng(103)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])]],
#chief unique acaba

["tab_shield_small_round_c", "Banner Small Round Shield", [("tableau_shield_small_round_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  390 , weight(2.5)|hit_points(300)|body_armor(7)|spd_rtng(60)|shield_width(60),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")])]], #chief cambiado


 #RANGED


#TODO:

["darts",         "darts", [("dart_b",0),("dart_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn,
85 , weight(2)|difficulty(1)|spd_rtng(90) | shoot_speed(30) | thrust_damage(23 ,  pierce)|max_ammo(7)|weapon_length(32)|accuracy(80),imodbits_thrown,missile_distance_trigger ,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],

#quitando quivers chief
##["javelin",         "Javelins", [("atgeirr1",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
##200, weight(2)|difficulty(1)|spd_rtng(75) | shoot_speed(28) | thrust_damage(27 ,  cut)|max_ammo(4)|weapon_length(65)|accuracy(55),imodbits_thrown,missile_distance_trigger ], #chief cambiado max_ammo
["javelin",         "Javelins", [("atgeirr1",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin,
200, weight(2)|difficulty(1)|spd_rtng(75) | shoot_speed(28) | thrust_damage(31 ,  cut)|max_ammo(4)|weapon_length(65)|accuracy(99),imodbits_thrown,missile_distance_trigger ], #chief cambiado max_ammo
["javelin_melee",         "Javelin", [("atgeirr1",0)], itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
200, weight(2)|difficulty(0)|spd_rtng(82) |swing_damage(9, cut)| thrust_damage(25,  cut)|weapon_length(65),imodbits_polearm ], #chief cambiado
#wooden javelin para britones solo
["throwing_knives",         "Wooden Javelins", [("kijek",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_next_item_as_melee ,itcf_throw_javelin,
190, weight(2)|difficulty(0)|spd_rtng(85) | shoot_speed(33) | thrust_damage(27 ,  cut)|max_ammo(4)|weapon_length(60)|accuracy(90),imodbits_thrown,missile_distance_trigger , #chief cambiado max_ammo
[], [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],
["throwing_daggers",         "Wooden Javelin", [("kijek",0)], itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
200, weight(2)|difficulty(0)|spd_rtng(88) |swing_damage(9, cut)| thrust_damage(20,  cut)|weapon_length(65),imodbits_polearm ], #chief cambiado
#jabalinas para jinetes ligeros
["javelin_jinetes",         "Horsemen Javelins", [("02atgeirr1",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
300, weight(4)|difficulty(2)|spd_rtng(75) | shoot_speed(28) | thrust_damage(31 ,  cut)|max_ammo(6)|weapon_length(65)|accuracy(95),imodbits_thrown,missile_distance_trigger ], #chief cambiado max_ammo
["shortened_military_scythe",         "Horseman Javelin", [("02atgeirr1",0)], itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
300, weight(4)|difficulty(0)|spd_rtng(82) |swing_damage(9, cut)| thrust_damage(25,  cut)|weapon_length(65),imodbits_polearm ], #chief cambiado
#chief cambiado modelo y todo kastad_krokaspjott
["throwing_spears",         "Throwing Spears", [("kastad_krokaspjott",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin,
425 , weight(2)|difficulty(2)|spd_rtng(65) | shoot_speed(17) | thrust_damage(41 ,  pierce)|max_ammo(1)|weapon_length(100)|accuracy(85),imodbits_thrown,missile_distance_trigger ], #cambiado chief
["throwing_spear_melee",         "Throwing Spear", [("kastad_krokaspjott",0)],itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
425 , weight(2)|difficulty(2)|spd_rtng(80) | swing_damage(10, cut) | thrust_damage(31 ,  pierce)|weapon_length(100),imodbits_thrown ], #cambiado chief
#invasores
["jarid",         "Angons", [("angon1",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin,
425 , weight(2)|difficulty(2)|spd_rtng(65) | shoot_speed(17) | thrust_damage(41 ,  pierce)|max_ammo(1)|weapon_length(100)|accuracy(85),imodbits_thrown,missile_distance_trigger , #cambiado chief
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["jarid_melee2",         "Angon", [("angon1",0)],itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
425 , weight(2)|difficulty(2)|spd_rtng(80) | swing_damage(10, cut) | thrust_damage(31 ,  pierce)|weapon_length(100),imodbits_thrown ], #cambiado chief

["throwing_spears3",         "Angons", [("05kastad_krokaspjott",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin,
415 , weight(2)|difficulty(2)|spd_rtng(75) | shoot_speed(19) | thrust_damage(37 ,  pierce)|max_ammo(1)|weapon_length(100)|accuracy(85),imodbits_thrown,missile_distance_trigger , #cambiado chief
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["heavy_throwing_axes_melee",         "Angon", [("05kastad_krokaspjott",0)],itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
415 , weight(2)|difficulty(2)|spd_rtng(80) | swing_damage(10, cut) | thrust_damage(31 ,  pierce)|weapon_length(100),imodbits_thrown ], #cambiado chief

["throwing_spears4",         "Angons", [("kastspjottmidtaggir",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin,
435 , weight(2)|difficulty(2)|spd_rtng(60) | shoot_speed(15) | thrust_damage(44 ,  pierce)|max_ammo(1)|weapon_length(100)|accuracy(85),imodbits_thrown,missile_distance_trigger , #cambiado chief
 [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14]],
["heavy_throwing_axes",         "Angon", [("kastspjottmidtaggir",0)],itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
435 , weight(2)|difficulty(2)|spd_rtng(80) | swing_damage(10, cut) | thrust_damage(31 ,  pierce)|weapon_length(100),imodbits_thrown ], #cambiado chief
#especial
["gae_bolga",         "Gae Bolga", [("01kastad_krokaspjott",0)], itp_type_thrown |itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin,
2225 , weight(3)|difficulty(3)|spd_rtng(75) | shoot_speed(25) | thrust_damage(60 ,  pierce)|max_ammo(1)|weapon_length(105)|accuracy(85),imodbit_balanced ,missile_distance_trigger], #cambiado chief
["gae_bolga_melee",         "Gae Bolga", [("01kastad_krokaspjott",0)],itp_type_polearm|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry , itc_staff,
2225 , weight(3)|difficulty(2)|spd_rtng(80) | swing_damage(7, cut) | thrust_damage(33 ,  pierce)|weapon_length(105),imodbit_balanced ], #cambiado chief


#TODO:
#TODO: Heavy throwing Spear
["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary ,itcf_throw_stone, 1 , weight(1)|difficulty(0)|spd_rtng(95) | shoot_speed(20) | thrust_damage(17 ,  blunt)|max_ammo(6)|weapon_length(8),imodbit_large_bag,missile_distance_trigger ], #chief cambiado


#TODO: Light Trowing axe, Heavy Throwing Axe
["light_throwing_axes", "Francisca", [("francisca",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee,itcf_throw_axe,
380, weight(3)|difficulty(4)|spd_rtng(65) | shoot_speed(15) | thrust_damage(42,cut)|max_ammo(1)|weapon_length(53),imodbits_thrown_minus_heavy,missile_distance_trigger, [], [fac_kingdom_1,fac_kingdom_2,fac_kingdom_3]], #cambiado chief
["light_throwing_axes_melee", "Francisca", [("francisca",0)], itp_type_one_handed_wpn |itp_primary|itp_secondary|itp_bonus_against_shield,itc_scimitar,
380, weight(3)|difficulty(4)|spd_rtng(75)|weapon_length(53)| swing_damage(35,cut),imodbits_thrown_minus_heavy, [], [fac_kingdom_1]], #cambiado chief
["throwing_axes", "Light Francisca", [("francisca_afilada",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee,itcf_throw_axe,
360, weight(2)|difficulty(2)|spd_rtng(69) | shoot_speed(18) | thrust_damage(39,cut)|max_ammo(1)|weapon_length(53),imodbits_thrown_minus_heavy,missile_distance_trigger, [], [fac_kingdom_1,fac_kingdom_2,fac_kingdom_3]], #cambiado chief
["throwing_axes_melee", "Light Francisca", [("francisca_afilada",0)], itp_type_one_handed_wpn |itp_primary|itp_secondary|itp_bonus_against_shield,itc_scimitar,
380, weight(2)|difficulty(2)|spd_rtng(75)|weapon_length(53)| swing_damage(35,cut),imodbits_thrown_minus_heavy, [], [fac_kingdom_1]], #cambiado chief


##################chief finales arcos empieza##############################################
 ###########################################################################################
["hunting_bow",         "Hunting Bow", [("hunting_bow1",0),("hunting_bow_carry1",ixmesh_carry)],itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 267 , weight(1)|difficulty(1)|spd_rtng(70) | shoot_speed(47) | thrust_damage(18 ,  pierce)|accuracy(85),imodbits_bow], #chief cambiado
#    [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])]],
["short_bow",         "Short Bow", [("short_bow1",0),("short_bow_carry1",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 368 , weight(1)|difficulty(1)|spd_rtng(67) | shoot_speed(44) | thrust_damage(20 ,  pierce  )|accuracy(90),imodbits_bow,#chief cambiado
    [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])]],
["nomad_bow",         "Composite Bow", [("nomad_bow1",0),("nomad_bow_case1", ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 690 , weight(1.25)|difficulty(2)|spd_rtng(64) | shoot_speed(55) | thrust_damage(24 ,  pierce)|accuracy(95),imodbits_bow, #chief cambiado
    [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])]], #arco poco usado, no en mercaders pero podemos anadirlo a unidades determinadas chief
["long_bow",         "Long Bow", [("long_bow1",0),("long_bow_carry1",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_cant_use_on_horseback|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 630 , weight(1.75)|difficulty(2)|spd_rtng(60) | shoot_speed(50) | thrust_damage(22 ,  pierce)|accuracy(99),imodbits_bow, #chief cambiado
    [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])],
 [fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23, fac_kingdom_24, fac_kingdom_25, fac_kingdom_26]],


###arco para incendiar
["khergit_bow",         "Fire Bow", [("khergit_bow",0),("khergit_bow_case", ixmesh_carry)], itp_type_bow |itp_unique|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 368 , weight(1)|difficulty(2)|spd_rtng(67) | shoot_speed(44) | thrust_damage(20 ,  pierce  )|accuracy(90),imodbits_bow,
    [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])]],

###ARCOS ESPECIALES heroes
 ["strong_bow",         "Dark Hunter", [("war_bow1",0),("war_bow_carry1", ixmesh_carry)], itp_type_bow |itp_primary|itp_cant_use_on_horseback|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 830 , weight(1.75)|difficulty(1)|spd_rtng(60) | shoot_speed(50) | thrust_damage(22 ,  pierce)|accuracy(99),imodbit_masterwork, #chief cambiado
    [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])]],
["war_bow",         "Eye-popping", [("strong_bow1",0),("strong_bow_case1",ixmesh_carry)],itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 890 , weight(1.25)|difficulty(1)|spd_rtng(64) | shoot_speed(55) | thrust_damage(24 ,  pierce)|accuracy(95),imodbit_masterwork, #chief cambiado
    [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])]],


["hunting_crossbow", "Pictish Crossbow", [("xenoargh_arbalest",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_cant_use_on_horseback|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
250 , weight(2.25)|difficulty(1)|spd_rtng(40) | shoot_speed(45) | thrust_damage(20 ,  pierce)|max_ammo(1)|accuracy(85),imodbits_crossbow, [], [fac_kingdom_20]], #chief cambiado

#sling sot chief
["sniper_crossbow", "Sling Rocks", [("throwing_stone",0),("throwing_stone",ixmesh_flying_ammo),("bolt_bag_c", ixmesh_carry)],
  itp_type_bullets|itp_merchandise, 0, 15,weight(0.5)|abundance(90)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(50),imodbits_missile],
["sniper_lead", "Sling Lead", [("throwing_stone",0),("throwing_stone",ixmesh_flying_ammo),("bolt_bag_c", ixmesh_carry)],
  itp_type_bullets|itp_merchandise, 0, 350,weight(0.7)|abundance(40)|weapon_length(3)|thrust_damage(6,pierce)|max_ammo(30),imodbits_missile],
#sling sot chief
["flintlock_pistol", "Sling", [("Sling",0)],
 itp_type_pistol |itp_merchandise|itp_primary|itp_cant_use_on_horseback ,itcf_throw_stone, 30, weight(0.5)|difficulty(0)|spd_rtng(60) | shoot_speed(50) | thrust_damage(19 ,blunt)|max_ammo(1)|accuracy(90),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],
["flintlock_pistol_militar", "Military Sling", [("Slingmilitargrande",0)],
 itp_type_pistol |itp_merchandise|itp_primary|itp_cant_use_on_horseback ,itcf_throw_stone, 90, weight(0.5)|difficulty(0)|spd_rtng(65) | shoot_speed(55) | thrust_damage(23 ,blunt)|max_ammo(1)|accuracy(93),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],
["heavy_crossbow", "Fustibalus", [("Staf_Sling_fustibalus",0)],
 itp_type_pistol |itp_merchandise|itp_primary|itp_cant_use_on_horseback ,itcf_throw_stone, 110, weight(1)|difficulty(0)|spd_rtng(70) | shoot_speed(75) | thrust_damage(23 ,blunt)|max_ammo(1)|accuracy(90),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],

# itp_type_crossbow |itp_merchandise|itp_primary ,itcf_throw_stone|itcf_carry_dagger_front_right|itcf_reload_pistol, 22 , weight(0.5)|difficulty(0)|spd_rtng(147) | shoot_speed(40) | thrust_damage(15 ,  blunt)|max_ammo(1),imodbits_crossbow ],
##
["torch",         "Torches", [("torch_h",0)], itp_type_thrown|itp_merchandise |itp_primary ,itcf_throw_axe, 41 , weight(5)|difficulty(1)|spd_rtng(99) | shoot_speed(20) | thrust_damage(15,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown,
 [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),]),
 (ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 20, pos1)])]], ###chief fire arrow cambia para asedios

###########################proyectiles acaba chief####################################
 ####################################################################################


 ["lyre", "Lyre", [("lyre",0)], itp_merchandise|itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  218 , weight(2.5)|hit_points(80)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
 ["lute", "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  218 , weight(2.5)|hit_points(80)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
 ["instruments_end", "Instruments End", [("leathershield_small_b",0)], 0, 0, 1, 0, 0],
#["lyre",         "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  218 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ], #chief cambiado
#["lute",         "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  218 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ], #chief cambiado
#bebe, hijo de player
["baby",         "Baby", [("baby",0)], itp_always_loot|itp_type_goods, 0, 255,weight(50)|abundance(120),imodbits_none],

#chief unique
##["short_sword", "Short Sword",
## [("sword_norman",0),("sword_norman_scabbard", ixmesh_carry),("sword_norman_rusty",imodbit_rusty),("sword_norman_rusty_scabbard", ixmesh_carry|imodbit_rusty)],
## itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(75)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],

##["strange_armor",  "native", [("samurai_armor",0)], itp_type_body_armor  |itp_covers_legs ,0, 1259 , weight(18)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(7) ,imodbits_armor ],
##["strange_boots",  "native", [("samurai_boots",0)], itp_type_foot_armor | itp_attach_armature,0, 465 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
##["strange_helmet", "native", [("samurai_helmet",0)], itp_type_head_armor   ,0, 824 , weight(2)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
##["strange_sword", "native", [("katana",0),("katana_scabbard",ixmesh_carry)], itp_type_two_handed_wpn| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 679 , weight(2.0)|difficulty(9)|spd_rtng(89) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(12 ,  pierce),imodbits_sword ],
##["strange_great_sword",  "native", [("no_dachi",0),("no_dachi_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 920 , weight(3.5)|difficulty(11)|spd_rtng(92) | weapon_length(125)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
##["strange_short_sword", "native", [("wakizashi",0),("wakizashi_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_wakizashi|itcf_show_holster_when_drawn, 321 , weight(1.25)|difficulty(0)|spd_rtng(108) | weapon_length(65)|swing_damage(15 , cut) | thrust_damage(24 ,  pierce),imodbits_sword ],
["court_dress", "Court Dress", [("court_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
#chief unique acaba

#################especiales chief#############################################
#piedra para asedio chief Siege warfare
["stones_siege",         "Siege Stones", [("siegestone",0)], itp_type_thrown |itp_unique|itp_primary|itp_secondary ,itcf_throw_stone, 10 , weight(4)|difficulty(4)|spd_rtng(60) | shoot_speed(8) | thrust_damage(25 ,  blunt)|max_ammo(3)|weapon_length(14),imodbits_none, #chief cambiado
[
    (ti_on_missile_hit,
      [
	  (try_begin),
		#Solid Round Script
        #pos1 - Missile hit position
        #param_1 - Shooter agent
		(this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),
		(store_trigger_param_1,":shooter"),
		(copy_position, pos63, pos1),
		(particle_system_burst,"psys_piedra_dust",pos1,1),
		(try_for_agents,":agent"),
			(agent_get_position,pos62,":agent"),
			(get_distance_between_positions,":dist",pos63,pos62),
			(try_begin),
				(lt,":dist",100),#1-meter radius,otherwise doesn't register enough
				(neg|agent_is_ally,":agent"),
				(agent_is_active,":agent"),
				(agent_is_alive,":agent"),
				(neq,":agent",":shooter"),
#				(agent_set_hit_points,":agent",0,1),#insta-death
				(agent_deliver_damage_to_agent,":shooter",":agent"),
			(play_sound,"snd_shield_broken"),
       (try_end),
		(try_end),
		(try_end),
]),
]],
["agua_hirviendo",         "Boiling Water", [("boiling_water",0)], itp_type_thrown|itp_can_penetrate_shield|itp_no_pick_up_from_ground |itp_unique|itp_primary|itp_secondary ,itcf_throw_stone, 10 , weight(5)|difficulty(5)|spd_rtng(60) | shoot_speed(6) | thrust_damage(35 ,  blunt)|max_ammo(3)|weapon_length(14),imodbits_none, #chief cambiado
[
 (ti_on_missile_hit,
      [
          #pos1 - Missile hit position
         #param_1 - Shooter agent
          (try_begin),
		     (this_or_next|multiplayer_is_server),
		     (neg|game_in_multiplayer_mode),

			(store_trigger_param_1,":shooter"),
			(copy_position, pos63, pos1),
			(particle_system_burst,"psys_agua_hirviendo",pos63,1),
			(particle_system_burst,"psys_agua_hirviendo",pos63,3),
			(particle_system_burst,"psys_agua_hirviendo",pos63,10),
(play_sound, "snd_dummy_destroyed"),
          			(spawn_scene_prop,"spr_dungeon_water_drops",63),
			(store_random_in_range,":random_no",10,45),
			(assign,reg0,":random_no"),
             (try_for_agents,":agent"),
                (agent_get_position,pos62,":agent"),
                (get_distance_between_positions,":dist",pos63,pos62),
                (try_begin),
				   (lt,":dist",245),
					(neg|agent_is_ally,":agent"),
					(agent_is_active,":agent"),
					(agent_is_alive,":agent"),
					(neq,":agent",":shooter"),
				   (store_agent_hit_points,":hp",":agent",1),
				   (val_sub,":hp",":random_no"),
					(try_begin),
						(lt,":hp",1),
						(agent_deliver_damage_to_agent,":shooter",":agent"),
					(else_try),
						(agent_set_hit_points,":agent",":hp",1),
					(try_end),
                (try_end),
             (try_end),
          (try_end),
]),
]],

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting chief Mod begin#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
 ["deer","Deer", [("deer",0)], itp_unique|itp_type_horse, 0, 1411,abundance(40)|hit_points(30)|body_armor(5)|difficulty(11)|horse_speed(50)|horse_maneuver(32)|horse_charge(20),imodbits_horse_basic],
 ["boar","Boar", [("boar",0)], itp_unique|itp_type_horse, 0, 1411,abundance(40)|hit_points(80)|body_armor(15)|difficulty(11)|horse_speed(25)|horse_maneuver(20)|horse_charge(200)|horse_scale(55),imodbits_horse_basic],
 ["wolf","Wolf", [("warg",0)], itp_unique|itp_type_horse, 0, 1411,abundance(40)|hit_points(80)|body_armor(10)|difficulty(11)|horse_speed(30)|horse_maneuver(40)|horse_charge(100)|horse_scale(55),imodbits_horse_basic],
 ["coat","Goat", [("goat",0)], itp_unique|itp_type_horse, 0, 1411,abundance(40)|hit_points(20)|body_armor(8)|difficulty(11)|horse_speed(35)|horse_maneuver(30)|horse_charge(20)|horse_scale(55),imodbits_horse_basic],
 ["coat_b","Goat", [("goat_c",0)], itp_unique|itp_type_horse, 0, 1411,abundance(40)|hit_points(20)|body_armor(8)|difficulty(11)|horse_speed(35)|horse_maneuver(30)|horse_charge(20)|horse_scale(55),imodbits_horse_basic],
 ["wilddonkey","Wild Donkey", [("wild_donkey",0)], itp_unique|itp_type_horse, 0, 1411,abundance(30)|hit_points(40)|body_armor(10)|difficulty(11)|horse_speed(25)|horse_maneuver(20)|horse_charge(50)|horse_scale(65),imodbits_horse_basic],
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting chief Mod end#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#Otros, cuerno####
 ###########
["horn", "Horn", [("horn",0),("bolaf",0)], itp_type_thrown |itp_primary|itp_no_pick_up_from_ground, itcf_throw_knife, 145 , weight(1.5)|difficulty(0)|spd_rtng(50) | shoot_speed(54) | thrust_damage(3 ,  cut)|max_ammo(3)|weapon_length(0),imodbits_thrown,
   [(ti_on_weapon_attack, [

       (play_sound,"snd_horn2"),(try_for_agents,":agent"),
                              (agent_is_alive,":agent"),
                              (agent_is_human,":agent"),
                              (agent_is_ally,":agent"),
       (store_agent_hit_points,":life",":agent",0),
##       (try_begin),
##       (agent_set_animation, ":troop", "anim_horn_blow"),
###                           (agent_set_animation, ":agent", "anim_cheer"),
##       (try_end),
       (val_add,":life",5),
       (agent_set_hit_points,":agent",":life",0),
       (agent_play_sound, ":agent", "snd_man_victory"),
       (try_end),
       (store_add,":recovery",5),
       (assign,reg1,":recovery"),
     #  (display_message,"@Horn rally men! (wounded troops recover 5 hitpoints)",0x6495ed),
                              ],)]],

####trofeos de batalla chief
  ["trophy_a","Battle Trophy", [("horn",0)], itp_type_goods|itp_always_loot, 0, 210,weight(3)|abundance(90),imodbits_none],
  ["trophy_b","War Trophy", [("wessexbanner8",0)], itp_type_goods|itp_always_loot, 0, 410,weight(7)|abundance(90),imodbits_none],
  ["trophy_c","Epic King Trophy", [("chest_c",0)], itp_type_goods|itp_always_loot, 0, 610,weight(10)|abundance(90),imodbits_none],
##chief begin
["dplmc_coat_of_plates_red_constable", "Constable Mail", [("byrnie16",0)], itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(0) ,imodbits_armor ],
 ["iniauhorn",         "Iniau Horn", [("horn",0)], itp_type_goods, 0, 255,weight(50)|abundance(120),imodbits_none],
############3
 ##################

##diplomacy chief end
#################especiales chief acaba ################################

####OTROS chief ##################################
["tunic_with_green_cape", "Tunic with Green Cape", [("peasant_man_a_bry",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 80 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(3)|leg_armor(1), imodbits_cloth ], #cambiado chief
["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ],
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["practice_bow_2","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
["practice_arrows_2","Practice Arrows", [("arena_arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile,missile_distance_trigger],
#cuerno multiplayer chief
["bodkin_arrows", "Horn", [("horn",0),], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword, 145 , weight(1.5)|difficulty(0)|spd_rtng(50) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_none],

["steel_bolts",         "Siege Stones", [("siegestone",0)], itp_type_thrown |itp_primary|itp_secondary ,itcf_throw_stone, 10 , weight(4)|difficulty(0)|spd_rtng(60) | shoot_speed(8) | thrust_damage(25 ,  blunt)|max_ammo(3)|weapon_length(14),imodbits_none, #chief cambiado
[
(ti_on_missile_hit,
  [
      (try_begin),
            #Solid Round Script
    #pos1 - Missile hit position
    #param_1 - Shooter agent
       #     (multiplayer_is_server),
            #(neg|game_in_multiplayer_mode),
            (store_trigger_param_1,":shooter"),
            (copy_position, pos63, pos1),
            (particle_system_burst,"psys_piedra_dust",pos1,1),
            (try_for_agents,":agent"),
                    (agent_get_position,pos62,":agent"),
                    (get_distance_between_positions,":dist",pos63,pos62),
                    (try_begin),
                            (lt,":dist",100),#1-meter radius,otherwise doesn't register enough
                            (neg|agent_is_ally,":agent"),
                            (agent_is_active,":agent"),
                            (agent_is_alive,":agent"),
                            (neq,":agent",":shooter"),
#				(agent_set_hit_points,":agent",0,1),#insta-death
                            (agent_deliver_damage_to_agent,":shooter",":agent"),
                             #(multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_shield_broken"),
                    (play_sound,"snd_shield_broken"),
                   (try_end),
            (try_end),
            (try_end),
]),
 ]],


["scale_gauntlets",         "Boiling Water", [("boiling_water",0)], itp_type_thrown|itp_can_penetrate_shield|itp_unique|itp_primary|itp_secondary ,itcf_throw_stone, 10 , weight(5)|difficulty(0)|spd_rtng(60) | shoot_speed(6) | thrust_damage(35 ,  blunt)|max_ammo(2)|weapon_length(14),imodbits_none, #chief cambiado
[(ti_on_missile_hit,
[
    (store_trigger_param_1, ":agent_no"),
   (call_script, "script_explosion_at_pos1", 500, 50, ":agent_no"),
])],
],

#armaduras raider, anadidas aqui para compatibilidad con savegames
["military_cleaver_b", "Raider Mail", [("raider_hauberk",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2060 , weight(17)|abundance(10)|head_armor(0)|body_armor(31)|leg_armor(4)|difficulty(10) ,imodbits_armor ],
["military_cleaver_c", "Raider Mail", [("raider_hauberk2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2060 , weight(17)|abundance(10)|head_armor(0)|body_armor(31)|leg_armor(4)|difficulty(10) ,imodbits_armor ],
["military_sickle_a", "Raider Mail", [("raider_hauberk3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2060 , weight(17)|abundance(10)|head_armor(0)|body_armor(31)|leg_armor(4)|difficulty(10) ,imodbits_armor ],


#chief unique
#chief original unique para q no se vea en el juego
#chief unique acaba
###########Flechas acaba chief ####################
#chief original unique para q no se vea en el juego
["lamellar_gauntlets","native", [("scale_gauntlets_a_L",0)], itp_unique|itp_type_hand_armor,0, 910, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
["gauntlets","native", [("gauntlets_L",0),("gauntlets_L",imodbit_reinforced)], itp_unique|itp_type_hand_armor,0, 1040, weight(1.0)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
#chief original unique para q no se vea en el juego acaba
#chief original unique
["nomad_boots", "native", [("ankle_boots_a_new_bry",0)], itp_unique| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 116 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["khergit_guard_boots",  "native", [("ankle_boots_a_new_bry",0)], itp_unique|itp_type_foot_armor | itp_attach_armature,0, 254 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
["khergit_leather_boots", "native", [("ankle_boots_a_new_bry",0)], itp_unique| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_a", "native", [("ankle_boots_a_new_bry",0)], itp_unique|itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_b", "native", [("ankle_boots_a_new_bry",0)], itp_unique| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_c", "native", [("ankle_boots_a_new_bry",0)], itp_unique| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 280 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_plate ],
["sarranid_boots_d", "native", [("ankle_boots_a_new_bry",0)], itp_unique| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 920 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_armor ],
#chief unique empiza
["light_crossbow", "native", [("xenoargh_arbalest",0)], itp_type_crossbow |itp_unique|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
67 , weight(2.5)|difficulty(8)|spd_rtng(45) | shoot_speed(59) | thrust_damage(44 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["crossbow",         "native",         [("xenoargh_arbalest",0)], itp_type_crossbow |itp_unique|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
182 , weight(3)|difficulty(8)|spd_rtng(43) | shoot_speed(66) | thrust_damage(49,pierce)|max_ammo(1),imodbits_crossbow ],
 #chief unique acaba

#chief unique
["heraldic_mail_with_tunic_b", "Shirt", [("shirt_a_bry",0)], itp_unique|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 400 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(15)|leg_armor(2), imodbits_cloth],
["heraldic_mail_with_tabard", "Shirt",[("shirt_a_bry",0)], itp_unique|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 400 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(15)|leg_armor(2), imodbits_cloth],
###native
["female_hood", "native", [("head_wrapping_bry",0)], itp_unique| itp_type_head_armor   ,0, 6 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat", "native", [("head_wrapping_bry",0)], itp_unique| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat_b", "native", [("head_wrapping_bry",0)], itp_unique| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_hose", "native", [("head_wrapping_bry",0)], itp_unique| itp_type_head_armor |itp_civilian  ,0, 9 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#chief unique acaba
#################basicas chief acaba NATIVE
#chief unique
##########nativos#########################
#chief unique
#######nativos############
########nativos
 ["voulge",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["khergit_sword_two_handed_a",         "native",[("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["khergit_sword_two_handed_b",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["two_handed_cleaver", "native",[("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["one_handed_battle_axe_a", "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["one_handed_war_axe_b", "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["two_handed_axe",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["two_handed_battle_axe_2",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["shortened_voulge",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["great_axe",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["long_axe",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["long_axe_alt",         "native",[("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["long_axe_b_alt",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["long_axe_c",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["long_axe_c_alt",      "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["bardiche",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["great_bardiche",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["voulge",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["long_bardiche",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["great_long_bardiche",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["hafted_blade_b",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
 ["hafted_blade_a",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["military_hammer", "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["maul",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["sledgehammer", "native",[("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["warhammer",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["pickaxe",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["fighting_pick", "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["military_pick", "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["morningstar",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["cleaver",         "native",[("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["sword_medieval_c_small", "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["sword_viking_2_small", "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["sword_viking_3_small", "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["sword_khergit_2", "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["sword_khergit_3", "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["sword_khergit_4", "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#chief unique acaba

["plate_boots", "native", [("ankle_boots_a_new_bry",0)], itp_unique| itp_type_foot_armor | itp_attach_armature,0,
 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_plate ],
["heraldic_mail_with_surcoat_for_tableau", "native", [("shirt_a_bry",0)], itp_unique|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 400 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(15)|leg_armor(2), imodbits_cloth],
["mail_boots_for_tableau", "native", [("ankle_boots_a_new_bry",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1, weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["mace_1",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["mace_2",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["mace_3",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["mace_4",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["winged_mace",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
["spiked_mace",         "native", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 ,  pierce),imodbits_sword,
[], [fac_kingdom_20, fac_kingdom_17, fac_kingdom_19, fac_kingdom_27, fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31]],
#chief unique acaba ############3otros #############################
["items_end", "Items End", [("leathershield_small_b",0)], 0, 0, 1, 0, 0],
]

#MOTO generate no-swing versions of weapons
from copy import deepcopy

def modmerge(var_set):
	try:
		var_name_1 = "items"
		orig_items = var_set[var_name_1]

		add_item = deepcopy(orig_items)
		for i_item in range(1,len(orig_items)):
			type = add_item[i_item][3] & 0x000000ff
			# if itp_type_one_handed_wpn <= type <= itp_type_polearm and add_item[i_item-1][3] & itp_next_item_as_melee == 0 and (get_thrust_damage(add_item[i_item][6]) % 256) > 0 and "tutorial" not in add_item[i_item][0] and "arena" not in add_item[i_item][0] and "practice" not in add_item[i_item][0] and "tpe" not in add_item[i_item][0]:
			if itp_type_one_handed_wpn <= type <= itp_type_polearm and (get_thrust_damage(add_item[i_item][6])&0xff) > 0 and "tutorial" not in add_item[i_item][0] and "arena" not in add_item[i_item][0] and "practice" not in add_item[i_item][0] and "tpe" not in add_item[i_item][0]:
				#Above checks that it is a weapon with thrust damage; also checks that it isn't a tournament-type weapon by checking the item ID (just to prevent not-used items)
				add_item[i_item][0] = 'noswing_'+add_item[i_item][0]                  #add noswing_ to the item's name
				add_item[i_item][6] = add_item[i_item][6] & ~(ibf_damage_mask << iwf_swing_damage_bits) #should set new item's swing damage to 0
				add_item[i_item][4] = add_item[i_item][4] & ~itcf_overswing_polearm  #remove itcf_ capabilties to prevent swinging without damage
				add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashright_polearm
				add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashleft_polearm
				add_item[i_item][4] = add_item[i_item][4] & ~itcf_overswing_onehanded
				add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashright_onehanded
				add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashleft_onehanded
				add_item[i_item][4] = add_item[i_item][4] & ~itcf_overswing_twohanded
				add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashright_twohanded
				add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashleft_twohanded
				if type == itp_type_polearm and add_item[i_item][3] & itp_two_handed == 0:
					add_item[i_item][4] = add_item[i_item][4] | itcf_thrust_onehanded  #so that the polearms use 'bent elbow' with shields, but normal without
				add_item[i_item][3] = add_item[i_item][3] & ~itp_merchandise
				# orig_items.insert((len(orig_items)-1), add_item[i_item])        #add right above itm_items_end
				orig_items.append(add_item[i_item])

	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)

try:
    component_name = "items"
    var_set = { "items" : items }
    modmerge(var_set)
except:
    raise
