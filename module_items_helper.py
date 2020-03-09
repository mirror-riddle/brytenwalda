from header_common import *
from header_items import *
from header_operations import *
from header_triggers import *
from header_item_modifiers import *
from ID_factions import *


imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked | imodbit_lame | imodbit_spirited | imodbit_heavy | imodbit_stubborn
imodbits_cloth = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced | imodbit_lordly
imodbits_plate = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced | imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield = imodbit_cracked | imodbit_battered | imodbit_thick | imodbit_reinforced
imodbits_sword = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_tempered
imodbits_sword_high = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_tempered | imodbit_masterwork
imodbits_axe = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
#imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile = imodbit_bent | imodbit_large_bag
imodbits_thrown = imodbit_bent | imodbit_heavy | imodbit_balanced | imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced | imodbit_large_bag

imodbits_horse_good = imodbit_spirited | imodbit_heavy
imodbits_good = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent

jute_kingdoms = [
    fac_kingdom_1
]

pictish_kingdoms = [
    fac_kingdom_20
]

irish_kingdoms = [
    fac_kingdom_17, fac_kingdom_19, fac_kingdom_27,
    fac_kingdom_28, fac_kingdom_29, fac_kingdom_30, fac_kingdom_31
]

angle_kingdoms = [
    fac_kingdom_4, fac_kingdom_9, fac_kingdom_13, fac_kingdom_14
]

saxon_kingdoms = [
    fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5
]

saxon_kingdoms_minus_gewissae = [
    fac_kingdom_1, fac_kingdom_2, fac_kingdom_3
]

saxon_kingdoms_plus_east_angle = saxon_kingdoms + [fac_kingdom_4]

briton_kingdoms = [
    fac_kingdom_6, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10,
    fac_kingdom_11, fac_kingdom_12, fac_kingdom_15, fac_kingdom_16,
    fac_kingdom_18, fac_kingdom_21, fac_kingdom_22, fac_kingdom_23,
    fac_kingdom_24, fac_kingdom_25, fac_kingdom_26
]

angle_saxon_kingdoms = angle_kingdoms + saxon_kingdoms

pictish_irish_kingdoms = pictish_kingdoms + irish_kingdoms

# CC distancia de tiro chief commander
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
# CC


def create_item(prefix, subfix):
    return prefix + subfix


def create_prefix(id, name, extra_mesh=[]):
    name = id[2] if len(id) >= 3 else name
    extra_mesh = id[3] if len(id) >= 4 else extra_mesh
    mesh = [(id[1], 0)] + extra_mesh
    return [id[0], name, mesh]


def create_items(ids, subfix, name, extra_mesh=[]):
    return [create_item(create_prefix(id, name, extra_mesh), subfix) for id in ids]


def create_all_items(categories):
    all_items = []
    for category in categories:
        items = create_items(*category)
        all_items += items
    return all_items


def create_items_simple(ids, subfix):
    return [create_item(id, subfix) for id in ids]


def create_all_items_simple(categories):
    all_items = []
    for category in categories:
        items = create_items_simple(*category)
        all_items += items
    return all_items


all_horses = create_all_items([
    (
        [
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
        ],
        [
            itp_merchandise | itp_type_horse, 0, 2000,
            abundance(30) | hit_points(73) | body_armor(10) | difficulty(1) | horse_speed(42) |
            horse_maneuver(44) | horse_charge(10) | horse_scale(91),
            imodbits_horse_basic
        ],
        "North Horse",
        [("horse_c", imodbits_horse_good)]
    ),
    (
        [
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
        ],
        [
            itp_merchandise | itp_type_horse, 0, 2300,
            abundance(20) | body_armor(16) | hit_points(90) | difficulty(2) | horse_speed(36) |
            horse_maneuver(35) | horse_charge(17) | horse_scale(94),
            imodbits_horse_basic
        ],
        "Draft Horse"
    ),
    (
        [
            ["hunter", "WSumpterChestnut"],
            ["warhorse", "WSumpterBrown"]
        ],
        [
            itp_merchandise | itp_type_horse, 0, 2400,
            abundance(10) | hit_points(85) | body_armor(12) | difficulty(3) | horse_speed(46) |
            horse_maneuver(44) | horse_charge(12) | horse_scale(88),
            imodbits_horse_basic | imodbit_champion
        ],
        "Paraveredus",
        [("hunting_horse", imodbits_horse_good)]
    ),
])

all_boots = create_all_items([
    (
        [
            ["wrapping_boots", "wrapping_boots_a_bry", "Wrapping Boots"],
            ["ankle_boots", "ankle_boots_a_new_bry", "Ankle Boots"],
            ["bare_legs_blue", "bare_legs_blue", "Leather Shoes"],
            ["carbatinae_1_bare", "carbatinae_1_bare", "Bare Carbatinae", [("carbatinae_2_bare", 0)]],
        ],
        [
            itp_merchandise | itp_type_foot_armor | itp_civilian | itp_attach_armature, 0, 100,
            weight(1) | abundance(100) | body_armor(0) | leg_armor(10),
            imodbits_cloth
        ],
        "Poor Boots"
    ),  # poor boots
    (
        [
            [
                "quality_carbatinae_white", "carbatinae_1",
                "White Quality Carbatinae", [("carbatinae_2", 0)]
            ],
            [
                "quality_carbatinae_green", "carbatinae_1_green",
                "Green Quality Carbatinae", [("carbatinae_2_green", 0)]
            ],
            [
                "quality_carbatinae_blue", "carbatinae_1_blue",
                "Blue Quality Carbatinae", [("carbatinae_2_blue", 0)]
            ],
            [
                "quality_carbatinae_grey", "carbatinae_1_grey",
                "Grey Quality Carbatinae", [("carbatinae_2_grey", 0)]
            ],
            [
                "quality_carbatinae_orange", "carbatinae_1_orange",
                "Orange Quality Carbatinae", [("carbatinae_2_orange", 0)]
            ],
            [
                "quality_carbatinae_red", "carbatinae_1_red",
                "Red Quality Carbatinae", [("carbatinae_2_red", 0)]
            ],
        ],
        [
            itp_merchandise | itp_type_foot_armor | itp_civilian | itp_attach_armature, 0, 280,
            weight(1) | abundance(100) | body_armor(0) | leg_armor(16),
            imodbits_cloth
        ],
        "Quality Carbatinae"
    ),  # quality carbatinae
    (
        [
            ["rich_carbatinae_white", "decorated_leather_shoes", "White Rich Carbatinae"],
            ["rich_carbatinae_green", "decorated_leather_shoes_green", "Green Rich Carbatinae"],
            ["rich_carbatinae_blue", "decorated_leather_shoes_blue", "Blue Rich Carbatinae"],
            ["rich_carbatinae_grey", "decorated_leather_shoes_grey", "Grey Rich Carbatinae"],
            ["rich_carbatinae_orange", "decorated_leather_shoes_orange", "Orange Rich Carbatinae"],
            ["rich_carbatinae_red", "decorated_leather_shoes_red", "Red Rich Carbatinae"],
        ],
        [
            itp_merchandise | itp_type_foot_armor | itp_civilian | itp_attach_armature, 0, 600,
            weight(1) | abundance(30) | body_armor(0) | leg_armor(20),
            imodbits_cloth
        ],
        "Rich Carbatinae"
    ),  # rich carbatinaes
    (
        [
            [
                "carbatinae_greaves_white", "carbatinae_1_greaves",
                "White Greaves", [("carbatinae_2_greaves", 0)]
            ],
            [
                "carbatinae_greaves_green", "carbatinae_1_greaves_green",
                "Green Greaves", [("carbatinae_2_greaves_green", 0)]
            ],
            [
                "carbatinae_greaves_blue", "carbatinae_1_greaves_blue",
                "Blue Greaves", [("carbatinae_2_greaves_blue", 0)]
            ],
            [
                "carbatinae_greaves_grey", "carbatinae_1_greaves_grey",
                "Grey Greaves", [("carbatinae_2_greaves_grey", 0)]
            ],
            [
                "carbatinae_greaves_orange", "carbatinae_1_greaves_orange",
                "Orange Greaves", [("carbatinae_2_greaves_orange", 0)]
            ],
            [
                "carbatinae_greaves_red", "carbatinae_1_greaves_red",
                "Red Greaves", [("carbatinae_2_greaves_red", 0)]
            ],
        ],
        [
            itp_merchandise | itp_type_foot_armor | itp_civilian | itp_attach_armature, 0, 890,
            weight(2) | abundance(30) | body_armor(0) | leg_armor(25),
            imodbits_armor
        ],
        "Greaves"
    ),  # carbatinae greaves
    (
        [
            ["rich_greaves_white", "decorated_leather_shoes_greaves", "White Rich Greaves"],
            ["rich_greaves_green", "decorated_leather_shoes_greaves_green", "Green Rich Greaves"],
            ["rich_greaves_blue", "decorated_leather_shoes_greaves_blue", "Blue Rich Greaves"],
            ["rich_greaves_grey", "decorated_leather_shoes_greaves_grey", "Grey Rich Greaves"],
            ["rich_greaves_orange", "decorated_leather_shoes_greaves_orange", "Orange Rich Greaves"],
            ["rich_greaves_red", "decorated_leather_shoes_greaves_red", "Red Rich Greaves"],
        ],
        [
            itp_merchandise | itp_type_foot_armor | itp_civilian | itp_attach_armature, 0, 980,
            weight(2) | abundance(30) | body_armor(0) | leg_armor(28),
            imodbits_armor
        ],
        "Rich Greaves"
    ),  # rich greaves
    (
        [
            ["splinted_leather_greaves", "splinted_greaves_a_bry", "Splinted Leather Greaves"],
            ["rus_splinted_greaves", "rus_splint_greaves", "Rus Splinted Greaves"],
        ],
        [
            itp_merchandise | itp_type_foot_armor | itp_civilian | itp_attach_armature, 0, 1040,
            weight(2) | abundance(30) | body_armor(0) | leg_armor(30),
            imodbits_armor
        ],
        "Splinted Greaves"
    ),  # splinted greaves
])

all_robes_tunics_shirts = create_all_items_simple([
    (
        [
            ["cloth_robe_blue", "Blue Robe", [("sarranid_jellaba_blue", 0)]],
            ["cloth_robe_grey", "Grey Robe", [("sar_robered", 0)]],
            ["cloth_robe_grey_1", "Grey Robe", [("sar_robeylw", 0)]],
            ["cloth_robe_dark", "Dark Robe", [("sar_robegrn", 0)]],
            ["cloth_robe_dark_1", "Dark Robe", [("sar_robewht", 0)]],
            ["cloth_robe_dark_2", "Dark Robe", [("sar_robeprp", 0)]],
            ["cloth_robe_yellow", "Yellow Robe", [("sar_robe_bbge", 0)]],
            ["cloth_robe_white", "White Robe", [("sarranid_jellaba_white", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs, 0, 363,
            weight(1) | abundance(100) | body_armor(13) | leg_armor(4),
            imodbits_cloth
        ],
    ),  # cloth robes
    (
        [
            ["steppe_outfit", "Cloaked Tunic", [("BL_NT_Blue06COAT", 0)]],
            ["cloaked_tunic", "Cloaked Tunic", [("BL_NT_Green11COAT", 0)]],
            ["sleeveless_leather_tunic", "Cloaked Tunic", [("BL_NT_Red12COAT", 0)]],
            ["nordic_outfit", "Cloaked Tunic", [("BL_NT_Blue04COAT", 0)]],
            ["nordic_outfit2", "Cloaked Tunic", [("BL_NT_Blue08COAT", 0)]],
            ["sleeveless_tunic", "Cloaked Tunic", [("BL_NT_Red04COAT", 0)]],
            ["nordic_armor", "Cloaked Tunic", [("BL_NT_Blue11COAT", 0)]],
            ["hide_armor", "Cloaked Tunic", [("BL_NT_Green10COAT", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_civilian | itp_covers_legs, 0, 400,
            weight(2) | abundance(60) | body_armor(14) | leg_armor(2),
            imodbits_cloth, [], pictish_irish_kingdoms
        ]
    ),  # cloaked tunics
    (
        [
            ["dane_tunic1", "Red Tunic", [("BL_NT_Red04", 0)]],
            ["wessex_tunic1", "Woolen Tunic", [("woolen_tunic_a", 0)]],
            ["pict_tunic5", "Woolen Tunic ", [("woolen_tunic_c", 0)]],
            ["pict_tunic6", "Short Tunic ", [("BL_NT_Blue07", 0)]],
            ["pict_tunic7", "Short Tunic ", [("BL_NT_Green03", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_civilian | itp_covers_legs, 0, 210,
            weight(2) | abundance(60) | body_armor(11) | leg_armor(2),
            imodbits_cloth, [], pictish_irish_kingdoms
        ]
    ),  # pictish irish tunics
    (
        [
            ["shirt", "Shirt", [("shirt", 0)]],
            ["roman_shirt", "Poor Shirt", [("roman_shirt", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 110,
            weight(0.5) | abundance(100) | body_armor(10) | leg_armor(2),
            imodbits_cloth
        ]
    ),  # poor shirts
    (
        [
            ["bl_tunicsr01", "Poorman Tunic", [("BL_TunicR01", 0)]],
            ["bl_tunicsr01_2", "Cloak Poorman Tunic", [("BL_TunicR01_2", 0)]],
            ["bl_tunicsr02", "Dirty Tunic", [("BL_TunicR02", 0)]],
            ["shirtb", "Green tunic", [("shirtb", 0)]],
            ["shirtc", "White tunic", [("shirtc", 0)]],
            ["shirtd", "Blue tunic", [("shirtd", 0)]],
            ["shirte", "Dirty tunic", [("shirte", 0)]],
            ["armor_8", "Blue Tunic", [("armor_8", 0)]],
            ["armor_9", "Narrow Tunic", [("armor_9", 0)]],
            ["linen_tunic", "Linen Tunic", [("shirt_a_bry", 0)]],
            ["short_tunic", "Tunic", [("shirt_a_bry", 0)]],
            ["red_tunic", "Red Tunic", [("arena_tunicR_new", 0)]],
            ["green_tunic", "Green Tunic", [("arena_tunicG_new", 0)]],
            ["blue_tunic", "Blue Tunic", [("arena_tunicB_new", 0)]],
            ["leather_steppe_cap_a", "Narrow Tunic", [("arena_tunicY_new", 0)]],
            ["woolen_hood", "White Tunic", [("arena_tunicW_new", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 210,
            weight(0.5) | abundance(50) | body_armor(10) | leg_armor(2),
            imodbits_cloth
        ]
    ),  # poor tunics
    (
        [
            ["peasant_archer", "Farmer tunic", [("peasant_archer", 0)]],
            ["armor_26", "Farmer tunic", [("armor_26", 0)]],
            ["armor_27", "Farmer tunic", [("armor_27", 0)]],
            ["peasant_man_c", "Farmer tunic", [("peasant_man_c", 0)]],
            ["peasant_man_d", "Farmer tunic", [("peasant_man_d", 0)]],
            ["peasant_man_e", "Farmer tunic", [("peasant_man_e", 0)]],
            ["peasant_man_f", "Farmer tunic", [("peasant_man_f", 0)]],
            ["leather_jerkin", "Farmer tunic", [("peasant_man_b", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 320,
            weight(1) | abundance(50) | body_armor(11) | leg_armor(2),
            imodbits_cloth
        ]
    ),  # farmer tunics
    (
        [
            ["coarse_tunic1", "Merchant White Tunic", [("coarse_tunic_wt", 0)]],
            ["coarse_tunic2", "Merchant Red Tunic", [("coarse_tunic_rd", 0)]],
            ["coarse_tunic3", "Merchant Green Tunic", [("coarse_tunic_verde", 0)]],
            ["coarse_tunic4", "Merchant Brown Tunic ", [("coarse_tunic_brn", 0)]],
            ["coarse_tunic5", "Merchant Yellow Tunic", [("coarse_tunic_ylw", 0)]],
            ["coarse_tunic_blu", "Merchant Blue Tunic", [("coarse_tunic_blu", 0)]],
            ["coarse_tunic_grn", "Merchant Green Tunic", [("coarse_tunic_grn", 0)]],
            ["coarse_tunic_red", "Merchant Rich Tunic", [("coarse_tunic_vlt", 0)]],
            ["coarse_tunic", "Merchant Poor Tunic", [("coarse_tunic_a_bry", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 500,
            weight(0.5) | abundance(100) | body_armor(12) | leg_armor(3),
            imodbits_cloth
        ]
    ),  # merchant tunics
    (
        [
            ["koszula_gaelicka", "Irish Tunic", [("koszula_gaelicka", 0)]],
            ["bl_tunic05", "Godelic Rich Tunic", [("BL_Tunic05", 0)]],
            ["bl_tunic06", "Godelic Rich Tunic", [("BL_Tunic06", 0)]],
            ["bl_tunic07", "Godelic Rich Tunic", [("BL_Tunic07", 0)]],
            ["bl_tunic08", "Godelic Rich Tunic", [("BL_Tunic08", 0)]],
            ["bl_tunic11", "Godelic Rich Tunic", [("BL_Tunic11", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 200,
            weight(0.5) | abundance(50) | body_armor(10) | leg_armor(2),
            imodbits_cloth, [], pictish_irish_kingdoms
        ]
    ),  # pictish irish rich tunics
    (
        [
            ["braz", "Long Pictish Tunic", [("braz", 0)]],
            ["czerwony", "Pictish Tunic", [("czerwony", 0)]],
            ["gairlom", "Pictish Tunic", [("vaelicus_t_5", 0)]],
            ["tuniczka", "Pictish Tunic", [("byrnie_a_tunic_d", 0)]],
            ["yellow2", "Pictish Tunic", [("vaelicus_t_5", 0)]],
            ["yellow1", "Pictish Tunic", [("vaelicus_t_9", 0)]],
            ["vaelicus_t_9", "Pictish Tunic", [("byrnie_a_tunic_c", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 240,
            weight(1) | abundance(30) | body_armor(11) | leg_armor(2),
            imodbits_cloth, [], pictish_kingdoms
        ]
    ),  # pictish tunics
    (
        [
            ["tunic_b", "Pictish Tunic", [("tunic_b", 0)]],
            ["vaelicus_tunic_1", "Pictish Tunic", [("vaelicus_tunic_1", 0)]],
            ["vaelicus_tunic_2", "Pictish Tunic", [("vaelicus_tunic_2", 0)]],
            ["vaelicus_tunic_4", "Pictish Tunic", [("vaelicus_tunic_4", 0)]],
            ["vaelicus_tunic_5", "Pictish Tunic", [("vaelicus_tunic_5", 0)]],
            ["vaelicus_tunic_7", "Pictish Tunic", [("vaelicus_tunic_7", 0)]],
            ["vaelicus_tunic_10", "Pictish Tunic", [("vaelicus_tunic_10", 0)]],
            ["vaelicus_tunic_11", "Pictish Tunic", [("vaelicus_tunic_11", 0)]],
            ["vaelicus_tunic_12", "Pictish Tunic", [("vaelicus_tunic_12", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 240,
            weight(0.5) | abundance(50) | body_armor(9) | leg_armor(4),
            imodbits_cloth, [], pictish_kingdoms
        ]
    ),  # pictish poor tunics
    (
        [
            ["vaelicus_t_16", "Godelic Tunic", [("byrnie_a_tunic", 0)]],
            ["vaelicus_t_19", "Godelic Tunic", [("byrnie_a_tunic_b", 0)]],
            ["vaelicus_t_21", "Godelic Tunic", [("vaelicus_t_21", 0)]],
            ["vaelicus_t_25", "Godelic Tunic", [("byrnie_a_tunic_e", 0)]],
            ["vaelicus_t_26", "Godelic Tunic", [("vaelicus_t_26", 0)]],
            ["vaelicus_t_27", "Godelic Tunic", [("vaelicus_t_27", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 240,
            weight(1) | abundance(20) | body_armor(11) | leg_armor(2),
            imodbits_cloth, [], irish_kingdoms
        ]
    ),  # irish tunics
    (
        [
            ["tribal_warrior_outfit", "Long Tunic", [("outaa1", 0)]],
            ["nomad_robe", "Long Tunic", [("outaa2", 0)]],
            ["heraldric_armor", "Long Tunic", [("outaa3", 0)]],
            ["studded_leather_coat", "Long Tunic", [("outaa4", 0)]],
        ],
        [
            itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 560,
            weight(1) | abundance(30) | body_armor(15) | leg_armor(4),
            imodbits_cloth, [], pictish_irish_kingdoms
        ]
    ),
    (
        [
            ["courtly_outfit", "Irish Long Tunic", [("merchant_outf1", 0)]],
            ["nobleman_outfit", "Irish Long Tunic", [("merchant_outf2", 0)]],
            ["nomad_armor", "Irish Long Tunic", [("shirt_shirt_a", 0)]],
            ["khergit_armor", "Irish Long Tunic", [("shirt_shirt_c", 0)]],
            ["fur_coat", "Irish Long Tunic", [("merchant_outf5", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 320,
            weight(1) | abundance(50) | body_armor(12) | leg_armor(4),
            imodbits_cloth, [], pictish_irish_kingdoms
        ]
    ),  # irish long tunics
    (
        [
            ["nomad_vest", "Grey Godelic Jacket", [("a_gaelic_jacket", 0)]],
            ["leather_jacket", "Grey Godelic Jacket",
                [("b_gaelic_jacket", 0)]],
            ["ragged_outfit", "Green Godelic Jacket",
                [("c_gaelic_jacket", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 300,
            weight(4) | abundance(50) | body_armor(12) | leg_armor(2),
            imodbits_cloth, [], irish_kingdoms
        ]
    ),  # godelic jackets
    (
        [
            ["vaelicus_t_35", "Godelic Fur Tunic", [("vaelicus_t_35", 0)]],
            ["vaelicus_t_36", "Godelic Fur Tunic", [("vaelicus_t_36", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 420,
            weight(1) | abundance(20) | body_armor(13) | leg_armor(3),
            imodbits_cloth, [], irish_kingdoms
        ]
    ),  # godelic fur tunics
    (
        [
            ["tunic_a", "Godelic Tunic", [("tunic_a", 0)]],
            ["tunic_c", "Godelic Tunic", [("tunic_c", 0)]],
            ["vaelicus_tunic_3", "Godelic Tunic", [("vaelicus_tunic_3", 0)]],
            ["vaelicus_tunic_6", "Godelic Tunic", [("vaelicus_tunic_6", 0)]],
            ["vaelicus_tunic_8", "Godelic Tunic", [("vaelicus_tunic_8", 0)]],
            ["vaelicus_tunic_9", "Godelic Tunic", [("vaelicus_tunic_9", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 240,
            weight(0.5) | abundance(50) | body_armor(9) | leg_armor(4),
            imodbits_cloth, [], irish_kingdoms
        ]
    ),  # gidelic_tunics
    (
        [
            ["shirt_blu", "Briton Blue Tunic", [("shirt_blu", 0)]],
            ["shirt_grn", "Briton Green Tunic", [("shirt_grn", 0)]],
            ["shirt_ylw", "Briton Yellow Tunic", [("shirt_ylw", 0)]],
            ["shirt_tel", "Briton Tunic", [("shirt_tel", 0)]],
            ["shirt_blk", "Briton Tunic", [("shirt_blk", 0)]],
            ["bl_tunic02", "Briton Green Tunic", [("BL_Tunic02", 0)]],
            ["shirt_red", "Briton Blue Tunic", [("shirt_red", 0)]],
            ["bl_tunic01", "Briton Rich Blue Tunic", [("BL_Tunic01", 0)]],
            ["bl_tunic04", "Briton Rich Tunic", [("BL_Tunic04", 0)]],
            ["bl_tunic09", "Briton Rich Red Tunic", [("BL_Tunic09", 0)]],
            ["bl_tunic10", "Briton Rich Blue Tunic", [("BL_Tunic10", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 210,
            weight(0.5) | abundance(50) | body_armor(10) | leg_armor(2),
            imodbits_cloth, [], briton_kingdoms
        ]
    ),  # briton_tunics
    (
        [
            ["bl_tunicsr02_2", "Cloak Dirty Tunic", [("BL_TunicR02_2", 0)]],
            ["bl_tunicsr03", "Cloak Red Tunic", [("BL_TunicR03", 0)]],
            ["bl_tunicsr03_2", "Red Tunic", [("BL_TunicR03_2", 0)]],
            ["fattiglinenskjortir", "Blue Shirt", [("fattiglinenskjortir", 0)]],
            ["mercia_tunic1", "Mercia Tunic", [("BL_NT_Green01", 0)]],
            ["blue_short_tunic", "Short Tunic", [("BL_NT_Blue01", 0)]],
            ["wessex_tunic3", "Saxon Tunic", [("BL_NT_Red01", 0)]],
            ["bl_tunicsleather", "Rustic Tunic", [("BL_TunicLeather", 0)]],
            ["bl_tunicsleather_2", "Rustic Tunic", [("BL_TunicLeather_2", 0)]],
            ["bl_tunicsleather_3", "Cloak Rustic Tunic", [("BL_TunicLeather_3", 0)]],
            ["bl_tunic03", "Red Tunic", [("BL_Tunic03", 0)]],
            ["bluevikingshirt", "Blue Shirt", [("bluevikingshirt", 0)]],
            ["redvikingshirt", "Linen Shirt", [("redvikingshirt", 0)]],
            ["blue_short_tunic2", "Linen Tunic", [("linen_tunic_a", 0)]],
            ["mercia_tunic10", "Linen Tunic", [("linen_tunic_b", 0)]],
            ["wessex_tunic4", "Linen Tunic", [("linen_tunic_c", 0)]],
            ["redtunic", "Woolen Tunic", [("woolen_tunic_b", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 210,
            weight(0.5) | abundance(50) | body_armor(10) | leg_armor(2),
            imodbits_cloth, [], angle_saxon_kingdoms
        ]
    ),  # angle_saxon_tunics
    (
        [
            ["noblemanshirt", "Nobleman Shirt", [("noblemanshirt", 0)]],
            ["noblemanshirt_gaelic", "Nobleman Shirt", [("noblemanshirt_gaelic", 0)]],
            ["noblemanshirt_pictish", "Nobleman shirt", [("noblemanshirt_pictish", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 260,
            weight(0.5) | abundance(50) | body_armor(10) | leg_armor(3),
            imodbits_cloth
        ]
    ),  # noble_shirts
    (
        [
            ["nordiclightarmor1", "Noble Tunic", [("nordiclightarmor61", 0)]],
            ["nordiclightarmor2", "Noble Tunic", [("nordiclightarmor62", 0)]],
            ["nordiclightarmor3", "Noble Tunic", [("nordiclightarmor64", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 1000,
            weight(10) | abundance(50) | body_armor(25) | leg_armor(0) | difficulty(8),
            imodbits_cloth, [], angle_saxon_kingdoms
        ]
    ),  # angle_saxon_noble_tunics
    (
        [
            ["nordiclightarmor10", "Noble Tunic", [("nordiclightarmor66", 0)]],
            ["nordiclightarmor11", "Noble Tunic", [("nordiclightarmor65", 0)]],
            ["nordiclightarmor12", "Noble Tunic", [("nordiclightarmor63", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 1000,
            weight(10) | abundance(50) | body_armor(25) | leg_armor(0) | difficulty(8),
            imodbits_cloth, [], briton_kingdoms
        ]
    ),  # briton_noble_tunics
    (
        [
            ["nordiclightarmor4", "Noble Tunic", [("nordiclightarmor4", 0)]],
            ["nordiclightarmor5", "Noble Tunic", [("nordiclightarmor5", 0)]],
            ["nordiclightarmor6", "Noble Tunic", [("nordiclightarmor6", 0)]],
            ["nordiclightarmor7", "Noble Tunic", [("nordiclightarmor41", 0)]],
            ["nordiclightarmor8", "Noble Tunic", [("nordiclightarmor51", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 1000,
            weight(10) | abundance(50) | body_armor(25) | leg_armor(0) | difficulty(8),
            imodbits_cloth, [], pictish_irish_kingdoms
        ]
    ),  # pictish_irish_noble_tunics
    (
        [
            ["blue_tunic_long", "Long Shirt", [("vae_tunica_larga5", 0)]],
            ["lady_dress_ruby", "Long Shirt", [("vae_tunica_larga6", 0)]],
            ["woolen_dress", "Woolen Dress", [("woolen_dress", 0)]],
            ["peasant_dress_b_new", "Woman Dress", [("peasant_dress_b_new", 0)]],
            ["blue_tunic2", "Long Shirt", [("vae_tunica_larga5", 0)]],
            ["pict_long_tunic1", "Long Shirt", [("vae_tunica_larga1", 0)]],
            ["pict_long_tunic2", "Long Shirt", [("vae_tunica_larga2", 0)]],
            ["pict_long_tunic3", "Long Shirt", [("vae_tunica_larga3", 0)]],
            ["pict_long_tunic4", "Long Shirt", [("vae_tunica_larga4", 0)]],
            ["lady_dress_green", "Long Shirt", [("vae_tunica_larga7", 0)]],
            ["lady_dress_blue", "Long Shirt", [("vae_tunica_larga8", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 150,
            weight(1) | abundance(100) | body_armor(5) | leg_armor(3),
            imodbits_cloth, [], pictish_irish_kingdoms
        ]
    ),  # pictish irish long shirts
])

all_women_hats = create_all_items_simple([
    (
        [
            ["sarranid_head_cloth", "Pink Veil", [("veil_a", 0)]],
            ["veil_b", "Blue Veil", [("veil_b", 0)]],
            ["veil_d", "Wool Veil", [("veil_d", 0)]],
            ["veil_c", "Dark Blue Veil", [("veil_c", 0)]],
            ["veil_e", "White Veil", [("veil_e", 0)]],
            ["veil_f", "Green Veil", [("veil_f", 0)]],
            ["veil_g", "Grey Veil", [("veil_g", 0)]],
            ["sarranid_felt_head_cloth", "Veil", [("common_veil_a", 0)]],
            ["common_veil_b", "Grey Veil", [("common_veil_b", 0)]],
            ["common_veil_d", "Narrow Veil", [("common_veil_d", 0)]],
            ["common_veil_c", "Orange Veil", [("common_veil_c", 0)]],
            ["common_veil_e", "Wool Veil", [("common_veil_e", 0)]],
        ],
        [
            itp_type_head_armor | itp_civilian | itp_attach_armature, 0, 100,
            weight(0.5) | abundance(100) | head_armor(5) | body_armor(0) | leg_armor(0),
            imodbits_cloth
        ]
    ),  # veils
    (
        [
            ["wimple_a", "Wimple", [("wimple_a_new_bry", 0)]],
            ["wimple_with_veil", "Wimple", [("wimple_b_new_bry", 0)]],
        ],
        [
            itp_merchandise | itp_type_head_armor | itp_civilian | itp_fit_to_head, 0, 90,
            weight(0.5) | abundance(10) | head_armor(2) | body_armor(0) | leg_armor(0),
            imodbits_cloth
        ]
    ),  # wimple
])

all_women_dresses = create_all_items_simple([
    (
        [
            ["red_dress", "Briton Dress", [("briton_dress", 0)]],
            ["brown_dress", "Blue Dress", [("briton_dress_b", 0)]],
            ["green_dress", "Wool Dress", [("briton_dress_c", 0)]],
            ["sarranid_common_dress", "Woman Dress", [("briton_dress_d", 0)]],
            ["sarranid_common_dress_b", "Woman Dress", [("briton_dress_e", 0)]],
            ["kenttunik", "Woman Dress", [("kenttunik", 0)]],
            ["tunikwjac1", "Woman Dress", [("tunikwjac1", 0)]],
            ["sarranid_dress_a", "Woman Dress", [("pictishdressazul", 0)]],
            ["sarranid_dress_b", "Woman Dress", [("pictishdress2", 0)]],
            ["pictishdress3", "Woman Dress", [("pictishdress3", 0)]],
            ["pictishdress1", "Woman Dress", [("pictishdress1", 0)]],
            ["pictishdressverde", "Woman Dress", [("pictishdressverde", 0)]],
            ["pictishdress", "Woman Dress", [("pictishdress", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 500,
            weight(3) | abundance(100) | body_armor(10) | leg_armor(10),
            imodbits_cloth
        ]
    ),  # women dress
])

all_pictish_clothes = create_all_items_simple([
    (
        [
            ["war_paint_two", "Pictish naked", [("war_paint_two", 0)]],
            ["war_paintus", "Pictish naked", [("war_paintus", 0)]],
            ["1celtbody", "Pictish naked", [("BL_Body08_male", 0)]],
            ["2celtbody", "Pictish naked", [("2celtbody", 0)]],
            ["3celtbody", "Pictish naked", [("3celtbody", 0)]],
            ["5celtbody", "Pictish naked", [("5celtbody", 0)]],
            ["6celtbody", "Pictish naked", [("6celtbody", 0)]],
            ["war_paint_two_5", "Pictish naked", [("BL_Body01_male", 0)]],
            ["war_paint_two_2", "Pictish naked", [("BL_Body02_male", 0)]],
            ["war_paintus_2", "Pictish naked", [("BL_Body03_male", 0)]],
            ["war_paintus_3", "Pictish naked", [("war_paintus_3", 0)]],
            ["war_paintus_4", "Pictish naked", [("war_paintus_4", 0)]],
            ["war_paintus_5", "Pictish naked", [("BL_Body04_male", 0)]],
            ["war_paintus_6", "Pictish naked", [("BL_Body07_male", 0)]],
            ["war_paintus_7", "Pictish naked", [("war_paintus_7", 0)]],
            ["war_paintus_8", "Pictish naked", [("war_paintus_8", 0)]],
            ["war_paintus_10", "Pictish naked", [("war_paintus_10", 0)]],
            ["war_paintus_11", "Pictish naked", [("war_paintus_11", 0)]],
            ["war_paintus_12", "Pictish naked", [("BL_Body09_male", 0)]],
            ["picto_gordo1", "Big Pictish naked", [("picto_gordo1", 0)]],
            ["picto_gordo2", "Big Pictish naked", [("picto_gordo2", 0)]],
            ["picto_gordo3", "Big Pictish naked", [("picto_gordo3", 0)]],
            ["picta_1", "Pictish woman naked", [("picta1", 0)]],
            ["picta_2", "Pictish woman naked", [("picta2", 0)]],
            ["picta_3", "Pictish woman naked", [("picta3", 0)]],
            ["picta_4", "Pictish woman naked", [("picta4", 0)]],
            ["picta_5", "Pictish woman naked", [("picta1", 0)]],
            ["picta_6", "Pictish woman naked", [("picta2", 0)]],
            ["picta_7", "Pictish woman naked", [("picta3", 0)]],
            ["picta_8", "Pictish woman naked", [("picta4", 0)]],
            ["picta_9", "Pictish woman naked", [("picta3", 0)]],
            ["picta_10", "Pictish woman naked", [("picta4", 0)]],
        ],
        [
            itp_unique | itp_type_body_armor | itp_covers_legs, 0, 100,
            weight(0.5) | abundance(10) | body_armor(10) | leg_armor(5),
            imodbits_cloth
        ]
    ),  # pictish naked
    (
        [
            ["linen_shirt", "Cloaked Body", [("BL_Celts01COAT", 0)]],
            ["wool_coat", "Cloaked Body", [("BL_Celts02COAT", 0)]],
            ["dress", "Cloaked Body", [("BL_Celts03COAT", 0)]],
            ["blue_dress", "Cloaked Body", [("BL_Celts04COAT", 0)]],
            ["tabard", "Cloaked Body", [("BL_Celts05COAT", 0)]],
            ["leather_vest", "Cloaked Body", [("BL_Celts06COAT", 0)]],
            ["steppe_armor", "Cloaked Body", [("BL_Celts07COAT", 0)]],
            ["gambeson", "Cloaked Body", [("BL_Celts08COAT", 0)]],
        ],
        [
            itp_type_body_armor | itp_civilian | itp_covers_legs, 0, 180,
            weight(5) | abundance(60) | body_armor(15) | leg_armor(6),
            imodbits_cloth, [], pictish_irish_kingdoms
        ]
    ),  # cloaked body
    (
        [
            ["coat", "Green Pants", [("BL_Celts06", 0)]],
            ["leather_coat", "Red Pants", [("BL_Celts07", 0)]],
            ["mail_coat", "Blue Pants", [("BL_Celts08", 0)]],
            ["long_mail_coat", "Blue Pants", [("BL_Celts05", 0)]],
            ["mail_with_tunic_red", "Red Pants", [("BL_Celts04", 0)]],
            ["mail_with_tunic_green", "Blue Pants", [("BL_Celts03", 0)]],
            ["hide_coat", "Green Pants", [("BL_Celts02", 0)]],
            ["merchant_outfit", "Narrow Pants", [("BL_Celts01", 0)]],
            ["homespun_dress", "Blue Pants", [("BL_Celts10", 0)]],
            ["thick_coat", "Red Pants", [("BL_Celts11", 0)]],
            ["coat_with_cape", "Blue Pants", [("BL_Celts12", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs, 0, 100,
            weight(0.5) | abundance(100) | body_armor(10) | leg_armor(6),
            imodbits_cloth, [], pictish_irish_kingdoms
        ]
    )  # pictish pants
])

all_heavy_armors = create_all_items_simple([
    (
        [
            ["mail_coat_1", "Brown Kingly Mail", [("mail_vest_b", 0)]],
            ["mail_coat_2", "Blue Kingly Mail", [("mail_vest_blu", 0)]],
            ["mail_coat_3", "Red Kingly Mail", [("mail_vest_red", 0)]],
            ["mail_coat_4", "White Kingly Mail", [("mail_vest_wht", 0)]],
            ["mail_coat_5", "Green Kingly Mail", [("mail_vest_grn", 0)]],
            ["mail_coat_6", "Dark Kingly Mail", [("mail_vest_blk", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 10160,
            weight(22) | abundance(2) | body_armor(60) | leg_armor(20) | difficulty(14),
            imodbits_armor, [], pictish_irish_kingdoms
        ]
    ),  # pictish kingly mails
    (
        [
            ["hauberk5", "Long Mail Coat", [("mail_hauberk_jco", 0)]],
        ],
        [
            itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 8000,
            weight(23) | abundance(10) | body_armor(49) | leg_armor(23) | difficulty(13),
            imodbits_armor, [], pictish_irish_kingdoms
        ]
    ),  # long mail coats
    (
        [
            ["hauberk6", "Mail Coat", [("mail_coat_a", 0)]],
            ["mail_shirt_bluehorses", "Mail Coat", [("mail_coat_b", 0)]],
            ["mail_shirt_blueunicorn", "Mail Coat", [("mail_coat_c", 0)]],
            ["mail_shirt_brown", "Mail Coat", [("mail_coat_d", 0)]],
            ["mail_shirt_green", "Mail Coat", [("mail_coat_e", 0)]],
            ["mail_shirt_greenhorses", "Mail Coat", [("mail_coat_f", 0)]],
            ["mail_shirt_red", "Black Mail Coat", [("mail_coat_1", 0)]],
            ["mail_shirt_reddragon", "Brown Mail Coat", [("mail_coat_2", 0)]],
            ["mail_shirt_redhorses", "Dark Mail Coat", [("mail_coat_3", 0)]],
            ["mail_shirt_whiteaxes", "Mail Coat", [("mail_coat_4", 0)]],
            ["mail_shirt_whiteraven", "Brown Mail Coat", [("mail_shirt_brown", 0)]],
            ["mail_shirt_green", "Green Mail Coat", [("mail_shirt_green", 0)]],
            ["mail_shirt_red", "Red Mail Coat", [("mail_shirt_red", 0)]],
            ["mail_shirt_a_copy", "Red Mail Coat", [("mail_shirt_a_copy", 0)]],
            ["heraldic_mail_with_tunic", "Cheap Mail Coat", [("mail_shirt_a_oscuro", 0)]],
            ["hauberk_a_new", "Cheap Mail Coat", [("hauberk_a_new", 0)]],
            ["mail_shirt_grn", "Green Mail Coat", [("mail_shirt_grn", 0)]],
            ["mail_shirt_red", "Red Mail Coat", [("mail_shirt_red", 0)]],
            ["mail_shirt_ylw", "Olive Mail Coat", [("mail_shirt_ylw", 0)]],
            ["mail_shirt_blk", "Grey Mail Coat", [("mail_shirt_blk", 0)]],
            ["mail_shirt_wht", "White Mail Coat", [("mail_shirt_wht", 0)]],
            ["swadian_mail_hauberk", "Black Mail Coat", [("swadian_mail_hauberk", 0)]],
            ["wei_xiadi_sar_hauberk", "Blue Mail Coat", [("wei_xiadi_sar_hauberk", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 5560,
            weight(19) | abundance(30) | body_armor(45) | leg_armor(15) | difficulty(12),
            imodbits_armor
        ]
    ),  # mail coats
    (
        [
            ["coat_of_plates", "Furred Smallring Mail", [("rough_smallring_fured", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 4600,
            weight(19) | abundance(10) | body_armor(42) | leg_armor(13) | difficulty(10),
            imodbits_armor
        ]
    ),  # furred small ring mail
    (
        [
            ["mail_coat_1_trig", "Blue Noble Mail", [("BL_VikingByrnie03", 0)]],
            ["mail_coat_2_trig", "Red Noble Mail", [("BL_VikingByrnie01", 0)]],
            ["mail_shirtdeer", "Green Noble Mail", [("BL_VikingByrnie04", 0)]],
            ["nowa", "Brown Noble Mail", [("BL_VikingByrnie12", 0)]],
            ["byrnie_b_new", "Green Noble Mail", [("BL_VikingByrnie02", 0)]],
            ["byrnie_e_new", "Brown Noble Mail", [("BL_VikingByrnie09", 0)]],
            ["byrnie_f_new", "Brown Noble Mail", [("BL_VikingByrnie13", 0)]],
            ["byrnie2", "Noble Mail", [("BL_VikingByrnie06", 0)]],
            ["byrnie1", "Green Noble Mail", [("BL_VikingByrnie07", 0)]],
            ["byrnie3", "Noble Mail", [("BL_VikingByrnie08", 0)]],
            ["lorika", "Brown Noble Mail", [("BL_VikingByrnie15", 0)]],
            ["mail_shirtred", "Brown Noble Mail", [("BL_VikingByrnie16", 0)]],
            ["byrnie151", "Red Noble Mail", [("BL_VikingByrnie05", 0)]],
            ["byrnie_c_new", "Purple Noble Mail", [("BL_VikingByrnie14", 0)]],
            ["byrnie_g_new", " Noble Mail", [("BL_VikingByrnie10", 0)]],
            ["byrnie_d_new", " Noble Mail", [("BL_VikingByrnie11", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 7020,
            weight(20) | abundance(10) | body_armor(53) | leg_armor(10) | difficulty(13),
            imodbits_armor, [], angle_saxon_kingdoms
        ]
    ),  # angle saxon noble mails
    (
        [
            ["byrnie", "Brown Lorica", [("byrnie1", 0)]],
            ["mail_shirthre", "Blue Lorica", [("byrnie3", 0)]],
            ["mail_shirtredwhite", "Green Lorica", [("byrnie_d_new", 0)]],
            ["mail_shirt_1_trig", "Red Lorica", [("byrnie_f_new", 0)]],
            ["ad_viking_byrnie_01", "White Lorica", [("byrnie11", 0)]],
            ["ad_viking_byrnie_02", "Blue Lorica", [("byrnie12", 0)]],
            ["ad_viking_byrnie_03", "Blue Lorica", [("byrnie13", 0)]],
            ["ad_viking_byrnie_04", "White Lorica", [("byrnie14", 0)]],
            ["ad_viking_byrnie_05", "Green Lorica", [("ragged_armour_e", 0)]],
            ["ad_viking_byrnie_06", "White Lorica", [("byrnie16", 0)]],
            ["mail_shirt_9_trig", "White Lorica", [("byrnie10", 0)]],
            ["mail_shirt_2_trig", "Olive Lorica", [("byrnie_g_new", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 3840,
            weight(19) | abundance(30) | body_armor(45) | leg_armor(4) | difficulty(11),
            imodbits_armor, [], angle_saxon_kingdoms
        ]
    ),  # loricas
    (
        [
            ["mail_shirt_3_trig", "Leather over Mail", [("saxon_leather_vest_mail", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 4590,
            weight(20) | abundance(30) | body_armor(46) | leg_armor(5) | difficulty(13),
            imodbits_armor, [], angle_saxon_kingdoms
        ]
    ),  # leather over mail
    (
        [
            ["mail_shirt_4_trig", "Blue Short Mail", [("norman_short_hauberk_blue", 0)]],
            ["mail_shirt_6_trig", "Red Short Mail", [("norman_short_hauberk", 0)]],
            ["mail_shirt_7_trig", "Yellow Short Mail", [("norman_short_hauberk_yellow", 0)]],
            ["mail_shirt_8_trig", "White Shirt Mail", [("sarranid_mail_byrnie_a", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 4590,
            weight(20) | abundance(30) | body_armor(46) | leg_armor(5) | difficulty(13),
            imodbits_armor, [], angle_saxon_kingdoms
        ]
    ),  # short mails
    (
        [
            ["mail_shirtbluewhite", "Squared Lorica", [("byrnie2", 0)]],
            ["byrnie6", "Squared Lorica", [("byrnie6", 0)]],
            ["byrnie8", "Squared Lorica", [("byrnie8", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 4840,
            weight(19) | abundance(10) | body_armor(45) | leg_armor(6) | difficulty(11),
            imodbits_armor, [], pictish_kingdoms
        ]
    ),
    (
        [
            ["byrnie4", "Striped Lorica", [("byrnie4", 0)]],
            ["byrnie5", "Striped Lorica", [("byrnie5", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 4840,
            weight(19) | abundance(10) | body_armor(45) | leg_armor(6) | difficulty(11),
            imodbits_armor, [], briton_kingdoms
        ]
    ),
    (
        [
            ["mail_shirt_8_trig", "Purple Lorica", [("byrnie_c_new", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 8000,
            weight(19) | abundance(10) | body_armor(53) | leg_armor(6) | difficulty(11),
            imodbits_armor, [], pictish_irish_kingdoms
        ]
    ),
    (
        [
            ["wolf_coat1", "Wolf Lorica", [("leatherovermail_a", 0)]],
            ["wolfpelt_mail_coat", "Wolf Lorica", [("leatherovermail_b", 0)]],
        ],
        [
            itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 5600,
            weight(22) | abundance(10) | body_armor(65) | leg_armor(10) | difficulty(14),
            imodbits_armor, [], angle_saxon_kingdoms
        ]
    ),
    (
        [
            ["mail_hauberk", "Goatist Mail", [("goatist_mail", 0)]],
        ],
        [
            itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 5600,
            weight(22) | abundance(10) | body_armor(60) | leg_armor(15) | difficulty(14),
            imodbits_armor, [], briton_kingdoms
        ]
    ),
    (
        [
            ["haubergeon", "Long Mail Tunic", [("armor_11", 0)]],
        ],
        [
            itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 5600,
            weight(22) | abundance(10) | body_armor(55) | leg_armor(20) | difficulty(14),
            imodbits_armor, [], pictish_irish_kingdoms
        ]
    ),
    (
        [
            ["mail_shirt", "Mail Shirt", [("haubergeon_jco", 0)]],
            ["lamellar_armor", "Long Byrnie", [("peasant_leather_mail_LS", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 3660,
            weight(15) | abundance(40) | body_armor(45) | leg_armor(6) | difficulty(11),
            imodbits_armor
        ]
    ),
    (
        [
            ["lamellar_armor", "Long Byrnie", [("peasant_leather_mail_LS", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 4360,
            weight(15) | abundance(40) | body_armor(50) | leg_armor(6) | difficulty(11),
            imodbits_armor
        ]
    ),
    (
        [
            ["mail_shirt_1", "Red Byrnie", [("tattered_leather_armor_2", 0)]],
            ["mail_shirt_2", "Yellow Byrnie", [("tattered_leather_armor_1", 0)]],
            ["mail_shirt_3", "Green Byrnie", [("tattered_leather_armor_6", 0)]],
            ["mail_shirt_4", "Blue Byrnie", [("tattered_leather_armor_b", 0)]],
            ["mail_shirt_6", "White Byrnie", [("tattered_leather_armor_w", 0)]],
            ["mail_shirt_7", "Brown Byrnie", [("tattered_leather_armor_5", 0)]],
            ["mail_shirt_8", "Blue Byrnie", [("tattered_leather_armor_bl", 0)]],
            ["mail_shirt_9", "Green Byrnie", [("tattered_leather_armor_4", 0)]],
            ["arena_tunicj_brown", "Grey Byrnie", [("tattered_leather_armor_3", 0)]],
            ["arena_tunicj_magenta", "White Byrnie", [("tattered_leather_armor_7", 0)]],
            ["arena_tunicj_violet", "Blue Byrnie", [("tattered_leather_armor_8", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 3860,
            weight(15) | abundance(40) | body_armor(49) | leg_armor(2) | difficulty(12),
            imodbits_armor
        ]
    ),
    (
        [
            ["mail_with_surcoat", "Sleeveless Mail", [("gallic_armor_3", 0)]],
            ["surcoat_over_mail", "Sleeveless Mail", [("gallic_armor_2", 0)]],
            ["brigandine_red", "Sleeveless Mail", [("gallic_armor", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 4280,
            weight(17) | abundance(20) | body_armor(42) | leg_armor(15) | difficulty(11),
            imodbits_armor, [], pictish_irish_kingdoms
        ]
    ),
    (
        [
            ["vikinglamellar2", "Bronce Lamellar Armor", [("BL_Lamellar04", 0)]],
            ["vikinglamellar3blue", "Bronce Lamellar Armor", [("BL_Lamellar02", 0)]],
            ["vikinglamellar3green", "Bronce Lamellar Armor", [("BL_Lamellar01", 0)]],
            ["vikinglamellar3red", "Bronce Lamellar Armor", [("BL_Lamellar03", 0)]],
            ["bl_lamellar05", "Bronce Lamellar Armor", [("BL_Lamellar05", 0)]],
            ["bl_lamellar06", "Bronce Lamellar Armor", [("BL_Lamellar06", 0)]],
            ["vikinglamellar3", "Bronce Lamellar armor", [("BL_Lamellar07", 0)]],
            ["bl_lamellar08", "Bronze Lamellar Armor", [("BL_Lamellar08", 0)]],
            ["vikinglamellar1", "Bronce Lamellar armor", [("BL_Lamellar09", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 3510,
            weight(10) | abundance(10) | body_armor(42) | leg_armor(5) | difficulty(10),
            imodbits_armor, [], saxon_kingdoms
        ]
    ),
    (
        [
            ["vikinglamellar2blue", "Black Lamellar Armor", [("BL_SLamellar03", 0)]],
            ["vikinglamellar2red", "Red Lamellar Armor", [("BL_SLamellar01", 0)]],
            ["vikinglamellar2yellow", "Brown Lamellar Armor", [("BL_SLamellar02", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 3830,
            weight(12) | abundance(10) | body_armor(43) | leg_armor(6) | difficulty(11),
            imodbits_armor, [], saxon_kingdoms
        ]
    ),
])

all_medium_armors = create_all_items_simple([
    (
        [
            ["cuir_bouilli", "Ring Mail", [("peasant_leather_ring_LS", 0)]],
            ["mamluke_mail", "Ring Mail", [("peasant_leather_ring_fur_LS", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 2800,
            weight(13) | abundance(40) | body_armor(38) | leg_armor(5) | difficulty(8),
            imodbits_armor
        ]
    ),
    (
        [
            ["lamellar_vest", "Scale Coat", [("scale_shirt", 0)]],
            ["lamellar_vest_khergit", "Scale Shirt", [("rod_lamellar_armor_e_copy", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 3920,
            weight(14) | abundance(10) | body_armor(46) | leg_armor(16) | difficulty(13),
            imodbits_armor, [], briton_kingdoms
        ]
    ),
    (
        [
            ["khergit_elite_armor", "Scale Armor", [("idi_scale2", 0)]],
            ["sarranid_mail_shirt", "Grey Scale Armor", [("idi_scale6", 0)]],
            ["light_leather", "White Scale Armor", [("idi_scale7", 0)]],
            ["mail_and_plate", "Scale Armor", [("khergit_scale_a", 0)]],
            ["light_mail_and_plate", "Scale Armor", [("khergit_scale_c", 0)]],
            ["banded_armor", "Scale Armor", [("idi_scale10", 0)]],
            ["coat_of_plates_red", "Scale Armor", [("scale_shirt_a", 0)]],
            ["plate_armor", "Scale Armor", [("idi_scale12", 0)]],
            ["khergit_guard_armor", "Scale Armor", [("scale_shirt_c", 0)]],
            ["idi_scale14", "Scale Armor", [("idi_scale14", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 3130,
            weight(12) | abundance(10) | body_armor(42) | leg_armor(6) | difficulty(11),
            imodbits_armor, [], briton_kingdoms
        ]
    ),
    (
        [
            ["scale_armor", "Scale Armor", [("idi_scale1", 0)]],
            ["vaegir_elite_armor", "Scale Armor", [("idi_scale3", 0)]],
            ["sarranid_elite_armor", "Scale Armor", [("idi_scale4", 0)]],
            ["arabian_armor_b", "Scale Armor", [("idi_scale5", 0)]],
            ["heraldic_mail_with_surcoat", "Scale Coat", [("outaa_escalearmor", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 3130,
            weight(12) | abundance(10) | body_armor(42) | leg_armor(6) | difficulty(11),
            imodbits_armor, [], pictish_irish_kingdoms
        ]
    ),
    (
        [
            ["padded_jack_3_trig", "White Linen Coat", [("armor_15", 0)]],
            ["padded_jack_4_trig", "Brown Linen Coat", [("ped_padded1_brown", 0)]],
            ["padded_jack_6_trig", "Blue Linen Coat", [("armor_17", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 1170,
            weight(4) | abundance(60) | body_armor(29) | leg_armor(8) | difficulty(7),
            imodbits_armor
        ]
    ),
    (
        [
            ["padded_jack_7_trig", "Dirty Linen Coat", [("ped_padded1_narrow", 0)]],
            ["padded_jack_9_trig", "Linen Coat with Cloak", [("ped_padded1_creme", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 1090,
            weight(4) | abundance(80) | body_armor(27) | leg_armor(5) | difficulty(6),
            imodbits_armor
        ]
    )
])

all_light_armors = create_all_items_simple([
    (
        [
            ["padded_jack_8_trig", "Padded Warrior Jacket", [("Kaftan_new", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 680,
            weight(3) | abundance(40) | body_armor(25) | leg_armor(4) | difficulty(4),
            imodbits_cloth, [], angle_saxon_kingdoms
        ]
    ),
    (
        [
            ["tattered_leather_armor_red", "Red Warrior Jacket", [("Kaftan2", 0)]],
            ["tattered_leather_armor_blu", "Blue Warrior Jacket", [("Kaftan3", 0)]],
            ["tattered_leather_armor_ylw", "Red Warrior Jacket", [("Kaftan", 0)]],
            ["tattered_leather_armor_blk", "Blue Warrior Jacket", [("Kaftan4", 0)]],
            ["tattered_leather_armor_gr", "Blue Warrior Jacket", [("kaftanh", 0)]],
            ["padded_leather_blue", "Green Warrior Jacket", [("kaftani", 0)]],
            ["padded_leather_brown", "Blue Warrior Jacket", [("kaftan_vae_1", 0)]],
            ["leather_armor_c", "Blue Warrior Jacket", [("kaftan_vae_2", 0)]],
            ["leather_armor_c2", "Red Warrior Jacket", [("kaftan_vae_3", 0)]],
            ["tattered_leather_armor_wht", "Purple Warrior Jacket", [("kaftang", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 520,
            weight(3) | abundance(60) | body_armor(20) | leg_armor(3) | difficulty(4),
            imodbits_cloth, [], angle_saxon_kingdoms
        ]
    ),
    (
        [
            ["leather_vest_green", "Green Leather Vest", [("saxon_leather_vest_green", 0)]],
            ["leather_vest_blue", "Blue Leather Vest", [("saxon_leather_vest_blue", 0)]],
            ["leather_vest_red", "Red Leather Vest", [("saxon_leather_vest_red", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 820,
            weight(4) | abundance(60) | body_armor(23) | leg_armor(2) | difficulty(6),
            imodbits_cloth
        ]
    ),
    (
        [
            ["coat_of_plates1", "Rawhide Coat", [("coat_of_plates1", 0)]],
            ["coat_of_plates3", "Rawhide Coat", [("coat_of_plates3", 0)]],
            ["coat_of_plates4", "Rawhide Coat", [("coat_of_plates4", 0)]],
            ["coat_of_plates5", "Rawhide Coat", [("coat_of_plates5", 0)]],
            ["coat_of_plates6", "Rawhide Coat", [("coat_of_plates1m", 0)]],
            ["coat_of_plates8", "Rawhide Coat", [("coat_of_plates3m", 0)]],
            ["coat_of_plates9", "Rawhide Coat", [("coat_of_plates4m", 0)]],
            ["coat_of_plates10", "Rawhide Coat", [("coat_of_plates5m", 0)]],
            ["coat_of_plates11", "Rawhide Coat", [("coat_of_plates6m", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 1020,
            weight(6) | abundance(60) | body_armor(24) | leg_armor(8) | difficulty(6),
            imodbits_cloth
        ]
    ),
    (
        [
            ["goatist_tunic", "Goatist Tunic", [("goatist_tunic", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 1160,
            weight(4) | abundance(20) | body_armor(22) | leg_armor(12) | difficulty(6),
            imodbits_cloth
        ]
    ),
    (
        [
            ["pelt_coat", "Pelt Coat", [("thick_coat_a_bry", 0)]],
            ["pelt_coat2", "Pelt Coat", [("wei_xiadi_rod_thick_coat", 0)]],
            ["vae_thick_coat1", "Simple Coat", [("vae_thick_coat1", 0)]],
            ["vae_thick_coat2", "Simple Coat", [("vae_thick_coat2", 0)]],
            ["vae_thick_coat3", "Simple Coat", [("vae_thick_coat3", 0)]],
            ["vae_thick_coat6", "Hide Coat", [("vae_thick_coat6", 0)]],
            ["vae_thick_coat10", "Hide Coat", [("vae_thick_coat10", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 700,
            weight(3) | abundance(80) | body_armor(18) | leg_armor(2) | difficulty(2),
            imodbits_cloth
        ]
    ),
    (
        [
            ["idi_furjacket1", "Fur Jacket", [("idi_furjacket1", 0)]],
            ["idi_furjacket2", "Fur Jacket", [("idi_furjacket2", 0)]],
            ["idi_furjacket3", "Fur Jacket", [("idi_furjacket3", 0)]],
            ["idi_furjacket4", "Fur Jacket", [("idi_furjacket4", 0)]],
            ["idi_furjacket5", "Fur Jacket", [("idi_furjacket5", 0)]],
            ["idi_furjacket6", "Fur Jacket", [("idi_furjacket6", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 740,
            weight(3) | abundance(70) | body_armor(19) | leg_armor(4) | difficulty(4),
            imodbits_cloth
        ]
    ),
    (
        [
            ["gatheredcloaks1", "Blue Gathered Cloak", [("gatheredcloak1", 0)]],
            ["gatheredcloaks2", "Green Gathered Cloak", [("gatheredcloak2", 0)]],
            ["gatheredcloaks3", "Yellow Gathered Cloak", [("gatheredcloak3", 0)]],
            ["gatheredcloaks4", "Gathered Cloak", [("gatheredcloak4", 0)]],
            ["gatheredcloaks5", "Blue Gathered Cloak", [("gatheredcloak5", 0)]],
        ],
        [
            itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 740,
            weight(2) | abundance(50) | body_armor(17) | leg_armor(6) | difficulty(2),
            imodbits_cloth
        ]
    ),
    (
        [
            ["fat_body", "Fat Body", [("fat_body", 0)]],
        ],
        [
            itp_unique | itp_type_body_armor | itp_covers_legs | itp_civilian, 0, 10,
            weight(3) | abundance(10) | body_armor(14) | leg_armor(4) | difficulty(4),
            imodbits_cloth
        ]
    ),
    (
        [
            ["burlap_tunic", "Burlap Tunic", [("shirt", 0)]],
        ],
        [
            itp_type_body_armor | itp_covers_legs, 0, 25,
            weight(1) | abundance(100) | body_armor(5) | leg_armor(1),
            imodbits_armor
        ]
    ),
])

all_light_helments = create_all_items_simple([
    (
        [
            ["pictish_hood", "Pictish Hood", [("pictish_hood", 0)]],
            ["youhou_assassin_hood", "Assassin Hood", [("youhou_assassin_hood", 0)]],
            ["youhou_assassin_hood_red", "Assassin Hood", [("youhou_assassin_hood_red", 0)]],
        ],
        [
            itp_type_head_armor | itp_civilian, 0, 100,
            weight(1) | abundance(100) | head_armor(10) | body_armor(0) | leg_armor(0),
            imodbits_cloth
        ]
    ),
    (
        [
            ["woolen_cap_newblu", "Blue phrygian cap", [("woolen_cap_newblu", 0)]],
            ["woolen_cap_newred", "Narrow phrygian cap", [("woolen_cap_newred", 0)]],
            ["woolen_cap_newgrn", "Green phrygian cap", [("woolen_cap_newgrn", 0)]],
            ["woolen_cap_newblk", "Black phrygian cap", [("woolen_cap_newblk", 0)]],
            ["woolen_cap_newwht", "White phrygian cap", [("woolen_cap_newwht", 0)]],
            ["woolen_cap", "Woolen Cap", [("woolen_cap_new_bry", 0)]],
        ],
        [
            itp_merchandise | itp_type_head_armor | itp_civilian, 0, 100,
            weight(1) | abundance(100) | head_armor(10) | body_armor(0) | leg_armor(0),
            imodbits_cloth, [], angle_saxon_kingdoms
        ]
    ),
    (
        [
            ["hood_newblu", "Hood", [("hood_newblu", 0)]],
            ["hood_newred", "Hood", [("hood_newred", 0)]],
            ["hood_newblk", "Hood", [("hood_newblk", 0)]],
            ["hood_newwht", "Hood", [("hood_newwht", 0)]],
            ["black_hood", "Black Hood", [("hood_black_bry", 0)]],
            ["common_hood", "Hood", [("hood_new_bry", 0)]],
        ],
        [
            itp_merchandise | itp_type_head_armor | itp_civilian, 0, 110,
            weight(1) | abundance(90) | head_armor(10) | body_armor(0) | leg_armor(0),
            imodbits_cloth
        ]
    ),
    (
        [
            ["head_wrappings", "Head Wrapping", [("head_wrapping_bry", 0)]],
        ],
        [
            itp_type_head_armor | itp_fit_to_head, 0, 30, weight(0.25) | head_armor(6), imodbits_cloth
        ]
    ),
    (
        [
            ["turret_hat_ruby", "Fat Man", [("large_man_full", 0)]],
        ],
        [
            itp_unique | itp_type_head_armor | itp_civilian | itp_fit_to_head, 0, 70,
            weight(0.5) | abundance(10) | head_armor(8) | body_armor(0) | leg_armor(0),
            imodbits_cloth
        ]
    ),
    (
        [
            ["turret_hat_blue", "Bandana", [("bandana1", 0)]],
            ["turret_hat_green", "Bandana", [("bandana2", 0)]],
        ],
        [
            itp_merchandise | itp_type_head_armor | itp_civilian | itp_doesnt_cover_hair | itp_fit_to_head, 0, 60,
            weight(0.5) | abundance(10) | head_armor(6) | body_armor(0) | leg_armor(0),
            imodbits_cloth
        ]
    ),
    (
        [
            ["red_cloakt", "Red Coat", [("BL_coat11c", 0)]],
            ["green_cloakt", "Nobleman Coat", [("BL_coat12b", 0)]],
            ["celta_capa3", "Cloak", [("BL_coat03c", 0)]],
            ["celta_capa4", "Cloak", [("BL_coat06b", 0)]],
            ["celta_capa5", "Cloak", [("BL_coat06c", 0)]],
            ["celta_capa6", "Cloak", [("BL_coat08c", 0)]],
            ["celta_capa7", "Cloak", [("BL_coat09b", 0)]],
            ["red_cloak_hood", "Rich Cloak", [("BL_coat16", 0)]],
            ["blue_cloak_hood", "Blue Cloak", [("BL_coat19c", 0)]],
            ["green_cloak", "Green Cloak", [("BL_coat12", 0)]],
            ["blue_cloak", "Blue Cloak", [("BL_coat14", 0)]],
            ["richbluecoat", "Rich Cloak", [("BL_coat14b", 0)]],
            ["irishcloak", "Gael Cloak", [("BL_coat19", 0)]],
        ],
        [
            itp_merchandise | itp_type_head_armor | itp_attach_armature | itp_doesnt_cover_hair |
            itp_fit_to_head | itp_civilian, 0, 580,
            weight(2) | abundance(50) | head_armor(1) | body_armor(10) | leg_armor(5),
            imodbits_cloth, [], pictish_irish_kingdoms
        ]
    ),
    (
        [
            ["black_cloak", "Cloak", [("BL_coat03b", 0)]],
            ["white_cloak", "Cloak", [("BL_coat011", 0)]],
            ["white_cloak_hood", "Cloak", [("cloak12", 0)]],
        ],
        [
            itp_merchandise | itp_type_head_armor | itp_attach_armature | itp_fit_to_head, 0, 193,
            weight(2) | abundance(100) | head_armor(1) | body_armor(5) | leg_armor(3), imodbits_cloth
        ]
    ),
    (
        [
            ["celta_capa1", "Godelic cloak", [("BL_coat03", 0)]],
            ["celta_capa2", "Cloak", [("BL_coat03b", 0)]],
            ["red_cloak", "Cloak", [("BL_coat011", 0)]],
        ],
        [
            itp_merchandise | itp_type_head_armor | itp_attach_armature | itp_doesnt_cover_hair |
            itp_fit_to_head | itp_civilian, 0, 580,
            weight(2) | abundance(50) | head_armor(1) | body_armor(10) | leg_armor(5),
            imodbits_cloth, [], pictish_irish_kingdoms
        ]
    ),
    (
        [
            ["green_cloak_hoodc", "Green cloak and hood with mask", [("cloak27", 0)]],
            ["brown_cloak_hoodc", "Brown cloak and hood with mask", [("cloak28", 0)]],
            ["black_cloak_hoodc", "Black cloak and hood with mask", [("cloak29", 0)]],
            ["grey_cloak_hoodc", "Grey cloak and hood with mask", [("cloak30", 0)]],
        ],
        [
            itp_type_head_armor | itp_attach_armature | itp_fit_to_head, 0, 193,
            weight(2) | abundance(100) | head_armor(3) | body_armor(5) | leg_armor(3), imodbits_cloth
        ]
    ),
    (
        [
            ["piel_coat01", "Fur Cloak", [("BL_coat01", 0)]],
            ["piel_coat02", "Cloak", [("BL_coat01b", 0)]],
            ["piel_coat03", "Cloak", [("BL_coat01c", 0)]],
            ["piel_coat04", "Cloak", [("BL_coat02", 0)]],
            ["piel_coat05", "Cloak", [("BL_coat02b", 0)]],
            ["piel_coat06", "Cloak", [("BL_coat02c", 0)]],
            ["piel_coat07", "Cloak", [("BL_coat04", 0)]],
        ],
        [
            itp_merchandise | itp_type_head_armor | itp_attach_armature | itp_doesnt_cover_hair |
            itp_fit_to_head | itp_civilian, 0, 580,
            weight(1) | abundance(50) | head_armor(1) | body_armor(10) | leg_armor(5),
            imodbits_cloth, [], angle_saxon_kingdoms
        ]
    ),
    (
        [
            ["bl_boar_fur", "Fur Cloak", [("BL_boar_fur", 0)]],
        ],
        [
            itp_merchandise | itp_type_head_armor | itp_attach_armature | itp_fit_to_head |
            itp_doesnt_cover_hair, 0, 300,
            weight(1.5) | abundance(10) | head_armor(1) | body_armor(15) | leg_armor(0) | difficulty(4),
            imodbits_cloth, [], angle_saxon_kingdoms
        ]
    ),
    (
        [
            ["bl_boar", "Boar Fur", [("BL_boar", 0)]],
        ],
        [
            itp_merchandise | itp_type_head_armor | itp_attach_armature | itp_fit_to_head, 0, 1580,
            weight(3) | abundance(10) | head_armor(20) | body_armor(15) | leg_armor(0) | difficulty(4),
            imodbits_cloth, [], angle_saxon_kingdoms
        ]
    ),
    (
        [
            ["khergit_guard_helmet", "Barbar Head", [("barbar_helm", 0)]],
        ],
        [
            itp_unique | itp_type_head_armor | itp_fit_to_head | itp_covers_head | itp_civilian, 0, 1300,
            weight(3) | abundance(10) | head_armor(35) | body_armor(0) | leg_armor(0) | difficulty(9),
            imodbits_plate
        ]
    ),
    (
        [
            ["boar_helmet", "Boar Hat", [("BL_boarhelmet", 0)]],
            ["goat_cap", "Goat Cap", [("goat_cap", 0)]],
            ["felt_steppe_cap", "Goat Hat", [("goat_bascinet", 0)]],
        ],
        [
            itp_merchandise | itp_type_head_armor | itp_civilian, 0, 700,
            weight(2) | abundance(30) | head_armor(28) | body_armor(2) | leg_armor(0) | difficulty(3),
            imodbits_cloth
        ]
    ),
])
