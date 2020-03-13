from headers.common import *
from headers.parties import *
from ids.troops import *
from ids.factions import *
from ids.map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See headers.parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See headers.parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id.
#    7.2) Minimum number of troops in the stack.
#    7.3) Maximum number of troops in the stack.
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
    ("none", "none", icon_gray_knight, 0, fac_commoners, merchant_personality, []),
    ("rescued_prisoners", "Rescued Prisoners", icon_gray_knight, 0, fac_commoners, merchant_personality, []),
    ("enemy", "Enemy", icon_gray_knight, 0, fac_undeads, merchant_personality, []),
    ("hero_party", "Hero Party", icon_gray_knight, 0, fac_commoners, merchant_personality, []),
    ####################################################################################################################
    # Party templates before this point are hard-wired into the game and should not be changed.
    ####################################################################################################################
    ##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
    ("village_defenders", "Village Defenders", icon_peasant, 0, fac_commoners,
     merchant_personality, [(trp_farmer, 10, 20), (trp_peasant_woman, 0, 8)]),

    ("cattle_herd", "Cattle Herd", icon_cattle | carries_goods(10),
     0, fac_neutral, merchant_personality, [(trp_cattle, 80, 120)]),

    ##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
    ##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
    # Ryan BEGIN
    ("looters", "Bandits", icon_axeman | carries_goods(8), 0, fac_outlaws,
     bandit_personality, [(trp_looter, 3, 60)]),  # chief cambiado
    # Ryan END
    ("manhunters", "Young Warriors", icon_axeman, 0, fac_manhunters,
        soldier_personality, [(trp_manhunter, 12, 70)]),  # chief cambiado
    # ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

    #  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
    ("steppe_bandits", "Scoti Raiders", icon_axeman | carries_goods(2), 0, fac_mountain_bandits,
     bandit_personality, [(trp_looter_leader2, 1, 2), (trp_steppe_bandit, 18, 58)]),
    ("taiga_bandits", "Outlaw Warriors", icon_axeman | carries_goods(2), 0, fac_outlaws,
     bandit_personality, [(trp_looter_leader2, 1, 2), (trp_taiga_bandit, 18, 58)]),
    ("desert_bandits", "Bandits Gang", icon_axeman | carries_goods(2), 0, fac_outlaws,
     bandit_personality, [(trp_looter_leader2, 1, 2), (trp_desert_bandit, 18, 58)]),
    ("forest_bandits", "Unrights Gang", icon_axeman | carries_goods(2), 0, fac_forest_bandits,
     bandit_personality, [(trp_looter_leader2, 1, 2), (trp_forest_bandit, 14, 52), (trp_brigand, 18, 40)]),
    ("mountain_bandits", "Band of Thieves and Murderers", icon_axeman | carries_goods(2), 0,
     fac_outlaws, bandit_personality, [(trp_looter_leader2, 1, 2), (trp_mountain_bandit, 14, 60)]),
    ("sea_raiders", "Frankish Raiders", icon_axeman | carries_goods(2), 0, fac_mountain_bandits,
     bandit_personality, [(trp_sea_raider_leader2, 1, 2), (trp_sea_raider, 15, 70)]),
    ("sea_raiders2", "Dena Raiders", icon_axeman | carries_goods(2), 0, fac_mountain_bandits,
     bandit_personality, [(trp_sea_raider_leader2, 1, 2), (trp_black_khergit_horseman, 14, 70)]),
    # new party chief
    ("sea_band", "Warrior Band", icon_axeman | carries_goods(2), 0, fac_mountain_bandits, bandit_personality, [
     (trp_looter_leader2, 1, 2), (trp_sea_raider, 8, 40), (trp_looter, 18, 40), (trp_mountain_bandit, 15, 30)]),
    # chief acaba
    ("deserters", "Masterless Men", icon_axeman | carries_goods(3), 0, fac_deserters, bandit_personality, []),

    ("merchant_caravan", "Merchant Caravan", icon_gray_knight | carries_goods(40) | pf_auto_remove_in_town | pf_quest_party,
        0, fac_commoners, escorted_merchant_personality, [(trp_caravan_master, 1, 1), (trp_caravan_guard, 15, 25)]),
    ("troublesome_bandits", "Troublesome Bandits", icon_axeman | carries_goods(9)
        | pf_quest_party, 0, fac_outlaws, bandit_personality, [(trp_bandit, 14, 55)]),
    ("bandits_awaiting_ransom", "Bandits Awaiting Ransom", icon_axeman | carries_goods(9) | pf_auto_remove_in_town |
        pf_quest_party, 0, fac_neutral, bandit_personality, [(trp_bandit, 24, 58), (trp_kidnapped_girl, 1, 1, pmf_is_prisoner)]),
    ("kidnapped_girl", "Kidnapped Girl", icon_woman | pf_quest_party, 0,
        fac_neutral, merchant_personality, [(trp_kidnapped_girl, 1, 1)]),

    ("village_farmers", "Village Farmers", icon_peasant | pf_civilian, 0, fac_innocents,
        merchant_personality, [(trp_farmer, 5, 10), (trp_peasant_woman, 3, 8)]),
    # nuevo template chief de neko y relic quest
    ("new_template", "Neko party", icon_axeman | carries_goods(9) | pf_quest_party, 0,
        fac_neko, soldier_personality, [(trp_npc17, 1, 1), (trp_cantaber_iuventus, 18, 30)]),
    ("cado_template", "Cado party", icon_axeman | carries_goods(9) | pf_quest_party, 0,
        fac_neko, soldier_personality, [(trp_npc18, 1, 1), (trp_cantaber_iuventus, 388, 400)]),
    ("arrians", "Arrians", icon_axeman | carries_goods(9) | pf_auto_remove_in_town |
        pf_quest_party, 0, fac_neutral, bandit_personality, [(trp_thyr, 1, 1), (trp_guardian, 8, 20)]),
    ("eadfrith", "Eadfrith's Warband", icon_axeman | carries_goods(9) | pf_quest_party, 0,
        fac_eadfrith, soldier_personality, [(trp_especiales_3, 1, 1), (trp_hired_blade, 30, 50)]),

    ("spy_partners", "Unremarkable Travellers", icon_gray_knight | carries_goods(10) | pf_default_behavior |
        pf_quest_party, 0, fac_neutral, merchant_personality, [(trp_spy_partner, 1, 1), (trp_caravan_guard, 5, 11)]),
    ("runaway_serfs", "Runaway Serfs", icon_peasant | carries_goods(8) | pf_default_behavior |
        pf_quest_party, 0, fac_neutral, merchant_personality, [(trp_farmer, 6, 7), (trp_peasant_woman, 3, 3)]),
    ("spy", "Ordinary Townsman", icon_gray_knight | carries_goods(4) | pf_default_behavior |
        pf_quest_party, 0, fac_neutral, merchant_personality, [(trp_spy, 1, 1)]),
    ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight | carries_goods(3)
        | pf_default_behavior | pf_quest_party, 0, fac_neutral, merchant_personality, []),
    ##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
    ##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
    ##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
    ##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

    ("forager_party", "Foraging Party", icon_gray_knight | carries_goods(
        5) | pf_show_faction, 0, fac_commoners, merchant_personality, []),
    ("scout_party", "Scouts", icon_gray_knight | carries_goods(1)
        | pf_show_faction, 0, fac_commoners, bandit_personality, []),
    # NEW PATROLS somebody chief patrullas
    ("patrol_party", "Patrol", icon_gray_knight | carries_goods(2)
        | pf_show_faction, 0, fac_commoners, soldier_personality, []),
    ("patrols_end", "Patrol", icon_gray_knight, 0, fac_player_faction, aggressiveness_0 | courage_15, []),
    # NEW PATROLS somebody chief patrullas
    ("player_loot_wagon", "Supply Wagon", icon_mule | pf_show_faction, 0, fac_commoners,
        escorted_merchant_personality, []),  # Tempered chief added player loot wagon
    #  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
    ("messenger_party", "Messenger", icon_gray_knight | pf_show_faction, 0, fac_commoners, merchant_personality, []),
    ("raider_party", "Raiders", icon_gray_knight | carries_goods(
        16) | pf_quest_party, 0, fac_outlaws, bandit_personality, []),
    ("raider_captives", "Raider Captives", 0, 0, fac_commoners, 0, [(trp_peasant_woman, 6, 30, pmf_is_prisoner)]),
    ("kingdom_caravan_party", "Caravan", icon_mule | carries_goods(45) | pf_show_faction, 0,
        fac_commoners, merchant_personality, [(trp_caravan_master, 1, 1), (trp_caravan_guard, 12, 40)]),
    ("prisoner_train_party", "Prisoner Train", icon_gray_knight | carries_goods(
        5) | pf_show_faction, 0, fac_commoners, merchant_personality, []),
    ("default_prisoners", "Default Prisoners", 0, 0, fac_commoners, 0, [(trp_bandit, 5, 10, pmf_is_prisoner)]),

    ("routed_warriors", "Routed Enemies", icon_vaegir_knight, 0, fac_commoners, soldier_personality, []),



    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    #-#-#-#Hunting chief Mod begin#-#-#-#
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#

    ("deer_herd", "Deer Herd", icon_cattle | carries_goods(10), 0,
        fac_wild_animals, merchant_personality, [(trp_deer, 16, 40)]),
    ("boar_herd", "Boar Herd", icon_cattle | carries_goods(10), 0,
        fac_wild_animals, merchant_personality, [(trp_boar, 3, 12)]),
    ("wolf_herd", "Wolf Pack", icon_cattle | carries_goods(10), 0,
        fac_wild_animals, merchant_personality, [(trp_wolf, 4, 18)]),
    ("coat_herd", "Goat Herd", icon_cattle | carries_goods(10), 0,
        fac_wild_animals, merchant_personality, [(trp_coat, 4, 28)]),
    ("coatb_herd", "Goat Herd", icon_cattle | carries_goods(10), 0,
        fac_wild_animals, merchant_personality, [(trp_coat_b, 4, 28)]),
    ("wilddonkey_herd", "Wild Donkey Herd", icon_cattle | carries_goods(10),
        0, fac_wild_animals, merchant_personality, [(trp_wilddonkey, 6, 18)]),
    #  ("village_hunters","Village Hunters",icon_peasant,0,fac_innocents,soldier_personality,[(trp_hunter,8,16)]),

    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    #-#-#-#Hunting chief Mod end#-#-#-#
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#

    # Caravans
    ("center_reinforcements", "Reinforcements", icon_axeman | carries_goods(16), 0,
        fac_commoners, soldier_personality, [(trp_townsman, 5, 30), (trp_watchman, 4, 20)]),

    ("kingdom_hero_party", "War Party", icon_flagbearer_a | pf_show_faction |
        pf_default_behavior, 0, fac_commoners, soldier_personality, []),

    # Reinforcements
    # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
    # less-modernised templates are generally includes 7-14 troops in total,
    # med-modernised templates are generally includes 5-10 troops in total,
    # high-modernised templates are generally includes 3-5 troops in total

    ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_sarranid_recruit, 2, 4), (trp_sarranid_footman, 2, 5), (trp_sarranid_skirmisher, 1, 3)]),
    ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_sarranid_veteran_footman, 6, 12), (trp_sarranid_infantry, 6, 12), (trp_sarranid_guard, 3, 6)]),
    ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_sarranid_archer, 4, 10), (trp_centware_portaestandarte, 0, 1), (trp_centware_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_vaegir_recruit, 2, 4), (trp_vaegir_footman, 2, 5), (trp_vaegir_skirmisher, 1, 3)]),
    ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_vaegir_veteran, 6, 12), (trp_vaegir_infantry, 6, 12), (trp_vaegir_guard, 3, 6)]),
    ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_vaegir_archer, 4, 10), (trp_saxon_portaestandarte, 0, 1), (trp_saxon_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_vaegir_recruit, 2, 4), (trp_vaegir_footman, 2, 5), (trp_vaegir_skirmisher, 1, 3)]),
    ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_vaegir_veteran, 6, 12), (trp_vaegir_infantry, 6, 12), (trp_vaegir_guard, 3, 6)]),
    ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_archer, 4, 10), (
        trp_saxon_portaestandarte, 0, 1), (trp_anglo_pagano, 0, 1), (trp_saxon_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners,
        0, [(trp_nord_recruit, 2, 4), (trp_nord_footman, 2, 5), (trp_nord_huntsman, 1, 3)]),
    ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_nord_trained_footman, 6, 12), (trp_nord_warrior, 6, 12), (trp_nord_veteran, 3, 6)]),
    ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_nord_veteran_archer, 4, 10), (trp_anglo_portaestandarte, 0, 1), (trp_anglo_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_vaegir_recruit, 2, 3), (trp_fresena, 0, 1), (trp_vaegir_footman, 2, 5), (trp_vaegir_skirmisher, 1, 3)]),
    ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_vaegir_veteran, 6, 12), (trp_vaegir_infantry, 6, 12), (trp_vaegir_guard, 3, 6)]),
    ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_archer, 4, 10), (
        trp_saxon_portaestandarte, 0, 1), (trp_anglo_pagano, 0, 1), (trp_saxon_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 5), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_vaegir_veteran, 6, 12), (trp_vaegir_infantry, 6, 12), (trp_vaegir_guard, 3, 6)]),
    ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_vaegir_archer, 4, 10), (trp_saxon_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 4), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_swadian_footman, 5, 11), (trp_swadian_infantry, 5, 11), (trp_swadian_man_at_arms, 4, 8)]),
    ("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_swadian_sergeant, 4, 10), (trp_briton_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 4), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_swadian_footman, 5, 11), (trp_swadian_infantry, 5, 11), (trp_swadian_man_at_arms, 4, 8)]),
    ("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_swadian_sergeant, 4, 10), (trp_briton_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_9_reinforcements_a", "{!}kingdom_9_reinforcements_a", 0, 0, fac_commoners,
        0, [(trp_nord_recruit, 2, 4), (trp_nord_footman, 2, 5), (trp_nord_huntsman, 1, 3)]),
    ("kingdom_9_reinforcements_b", "{!}kingdom_9_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_nord_trained_footman, 6, 12), (trp_nord_warrior, 6, 12), (trp_nord_veteran, 3, 6)]),
    ("kingdom_9_reinforcements_c", "{!}kingdom_9_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_nord_veteran_archer, 4, 10), (trp_anglo_portaestandarte, 0, 1), (trp_anglo_pagano, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_10_reinforcements_a", "{!}kingdom_10_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 4), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_10_reinforcements_b", "{!}kingdom_10_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_swadian_footman, 5, 11), (trp_swadian_infantry, 5, 11), (trp_swadian_man_at_arms, 4, 8)]),
    ("kingdom_10_reinforcements_c", "{!}kingdom_10_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_swadian_sergeant, 4, 10), (trp_briton_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_11_reinforcements_a", "{!}kingdom_11_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 4), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_11_reinforcements_b", "{!}kingdom_11_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_swadian_footman, 5, 11), (trp_swadian_infantry, 5, 11), (trp_swadian_man_at_arms, 4, 8)]),
    ("kingdom_11_reinforcements_c", "{!}kingdom_11_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_swadian_sergeant, 4, 10), (trp_briton_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_12_reinforcements_a", "{!}kingdom_12_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 4), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_12_reinforcements_b", "{!}kingdom_12_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_swadian_footman, 5, 11), (trp_swadian_infantry, 5, 11), (trp_swadian_man_at_arms, 4, 8)]),
    ("kingdom_12_reinforcements_c", "{!}kingdom_12_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_sergeant, 4, 10), (
        trp_briton_portaestandarte, 1, 2), (trp_briton_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_13_reinforcements_a", "{!}kingdom_13_reinforcements_a", 0, 0, fac_commoners,
        0, [(trp_nord_recruit, 2, 4), (trp_nord_footman, 2, 5), (trp_nord_huntsman, 1, 3)]),
    ("kingdom_13_reinforcements_b", "{!}kingdom_13_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_nord_trained_footman, 6, 12), (trp_nord_warrior, 6, 12), (trp_nord_veteran, 3, 6)]),
    ("kingdom_13_reinforcements_c", "{!}kingdom_13_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_nord_veteran_archer, 4, 10), (trp_anglo_portaestandarte, 0, 1), (trp_anglo_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_14_reinforcements_a", "{!}kingdom_14_reinforcements_a", 0, 0, fac_commoners,
        0, [(trp_nord_recruit, 2, 4), (trp_nord_footman, 2, 5), (trp_nord_huntsman, 1, 3)]),
    ("kingdom_14_reinforcements_b", "{!}kingdom_14_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_nord_trained_footman, 6, 12), (trp_nord_warrior, 6, 12), (trp_nord_veteran, 3, 6)]),
    ("kingdom_14_reinforcements_c", "{!}kingdom_14_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_nord_veteran_archer, 4, 10), (trp_anglo_portaestandarte, 0, 1), (trp_anglo_pagano, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_15_reinforcements_a", "{!}kingdom_15_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 4), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_15_reinforcements_b", "{!}kingdom_15_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_swadian_footman, 5, 11), (trp_swadian_infantry, 5, 11), (trp_swadian_man_at_arms, 4, 8)]),
    ("kingdom_15_reinforcements_c", "{!}kingdom_15_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_swadian_sergeant, 4, 10), (trp_briton_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_16_reinforcements_a", "{!}kingdom_16_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 4), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_16_reinforcements_b", "{!}kingdom_16_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_swadian_footman, 5, 11), (trp_swadian_infantry, 5, 11), (trp_swadian_man_at_arms, 4, 8)]),
    ("kingdom_16_reinforcements_c", "{!}kingdom_16_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_swadian_sergeant, 4, 10), (trp_briton_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_17_reinforcements_a", "{!}kingdom_17_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_rhodok_tribesman, 2, 5), (trp_rhodok_spearman, 2, 4), (trp_rhodok_crossbowman, 2, 3)]),
    ("kingdom_17_reinforcements_b", "{!}kingdom_17_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_rhodok_trained_spearman, 4, 11), (trp_rhodok_veteran_spearman, 4, 10), (trp_rhodok_veteran_crossbowman, 4, 9)]),
    ("kingdom_17_reinforcements_c", "{!}kingdom_17_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_gael_deaisbard, 4, 10), (trp_gael_portaestandarte, 0, 1), (trp_gael_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_18_reinforcements_a", "{!}kingdom_18_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 4), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_18_reinforcements_b", "{!}kingdom_18_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_swadian_footman, 5, 11), (trp_swadian_infantry, 5, 11), (trp_swadian_man_at_arms, 4, 8)]),
    ("kingdom_18_reinforcements_c", "{!}kingdom_18_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_swadian_sergeant, 4, 10), (trp_briton_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_19_reinforcements_a", "{!}kingdom_19_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_rhodok_tribesman, 2, 5), (trp_rhodok_spearman, 2, 4), (trp_rhodok_crossbowman, 2, 3)]),
    ("kingdom_19_reinforcements_b", "{!}kingdom_19_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_rhodok_trained_spearman, 4, 11), (trp_rhodok_veteran_spearman, 4, 10), (trp_rhodok_veteran_crossbowman, 4, 9)]),
    ("kingdom_19_reinforcements_c", "{!}kingdom_19_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_gael_deaisbard, 4, 10), (trp_gael_portaestandarte, 0, 1), (trp_gael_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_20_reinforcements_a", "{!}kingdom_20_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_khergit_tribesman, 2, 3), (trp_pict_woman, 1, 2), (trp_khergit_horseman, 2, 4), (trp_khergit_skirmisher, 2, 3)]),
    ("kingdom_20_reinforcements_b", "{!}kingdom_20_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_khergit_horse_archer, 5, 11), (trp_khergit_veteran_horse_archer, 5, 11), (trp_picti_each, 4, 8)]),
    ("kingdom_20_reinforcements_c", "{!}kingdom_20_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_khergit_lancer, 4, 10), (trp_picto_portaestandarte, 0, 1), (trp_picto_sacerdote, 0, 1), (trp_picto_cuerno, 0, 1)]),

    ("kingdom_21_reinforcements_a", "{!}kingdom_21_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 4), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_21_reinforcements_b", "{!}kingdom_21_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_swadian_footman, 5, 11), (trp_swadian_infantry, 5, 11), (trp_swadian_man_at_arms, 4, 8)]),
    ("kingdom_21_reinforcements_c", "{!}kingdom_21_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_swadian_sergeant, 4, 10), (trp_briton_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_22_reinforcements_a", "{!}kingdom_22_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 4), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_22_reinforcements_b", "{!}kingdom_22_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_swadian_footman, 5, 11), (trp_swadian_infantry, 5, 11), (trp_swadian_man_at_arms, 4, 8)]),
    ("kingdom_22_reinforcements_c", "{!}kingdom_22_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_swadian_sergeant, 4, 10), (trp_briton_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_23_reinforcements_a", "{!}kingdom_23_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 4), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_23_reinforcements_b", "{!}kingdom_23_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_swadian_footman, 5, 11), (trp_swadian_infantry, 5, 11), (trp_swadian_man_at_arms, 4, 8)]),
    ("kingdom_23_reinforcements_c", "{!}kingdom_23_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_swadian_sergeant, 4, 10), (trp_briton_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_24_reinforcements_a", "{!}kingdom_24_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 4), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_24_reinforcements_b", "{!}kingdom_24_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_swadian_footman, 5, 11), (trp_swadian_infantry, 5, 11), (trp_swadian_man_at_arms, 4, 8)]),
    ("kingdom_24_reinforcements_c", "{!}kingdom_24_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_swadian_sergeant, 4, 10), (trp_briton_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_25_reinforcements_a", "{!}kingdom_25_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 4), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_25_reinforcements_b", "{!}kingdom_25_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_swadian_footman, 5, 11), (trp_swadian_infantry, 5, 11), (trp_swadian_man_at_arms, 4, 8)]),
    ("kingdom_25_reinforcements_c", "{!}kingdom_25_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_swadian_sergeant, 4, 10), (trp_briton_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_26_reinforcements_a", "{!}kingdom_26_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_swadian_recruit, 2, 4), (trp_swadian_militia, 2, 4), (trp_swadian_skirmisher, 2, 4)]),
    ("kingdom_26_reinforcements_b", "{!}kingdom_26_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_swadian_footman, 5, 11), (trp_swadian_infantry, 5, 11), (trp_swadian_man_at_arms, 4, 8)]),
    ("kingdom_26_reinforcements_c", "{!}kingdom_26_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_swadian_sergeant, 4, 10), (trp_briton_portaestandarte, 0, 1), (trp_briton_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_27_reinforcements_a", "{!}kingdom_27_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_rhodok_tribesman, 2, 5), (trp_rhodok_spearman, 2, 4), (trp_rhodok_crossbowman, 2, 3)]),
    ("kingdom_27_reinforcements_b", "{!}kingdom_27_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_rhodok_trained_spearman, 4, 11), (trp_rhodok_veteran_spearman, 4, 10), (trp_rhodok_veteran_crossbowman, 4, 9)]),
    ("kingdom_27_reinforcements_c", "{!}kingdom_27_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_gael_deaisbard, 4, 10), (trp_gael_portaestandarte, 0, 1), (trp_gael_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_28_reinforcements_a", "{!}kingdom_28_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_rhodok_tribesman, 2, 5), (trp_rhodok_spearman, 2, 4), (trp_rhodok_crossbowman, 2, 3)]),
    ("kingdom_28_reinforcements_b", "{!}kingdom_28_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_rhodok_trained_spearman, 4, 11), (trp_rhodok_veteran_spearman, 4, 10), (trp_rhodok_veteran_crossbowman, 4, 9)]),
    ("kingdom_28_reinforcements_c", "{!}kingdom_28_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_gael_deaisbard, 4, 10), (trp_gael_portaestandarte, 0, 1), (trp_gael_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_29_reinforcements_a", "{!}kingdom_29_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_rhodok_tribesman, 2, 5), (trp_rhodok_spearman, 2, 4), (trp_rhodok_crossbowman, 2, 3)]),
    ("kingdom_29_reinforcements_b", "{!}kingdom_29_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_rhodok_trained_spearman, 4, 11), (trp_rhodok_veteran_spearman, 4, 10), (trp_rhodok_veteran_crossbowman, 4, 9)]),
    ("kingdom_29_reinforcements_c", "{!}kingdom_29_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_gael_deaisbard, 4, 10), (trp_gael_portaestandarte, 0, 1), (trp_gael_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_30_reinforcements_a", "{!}kingdom_30_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_rhodok_tribesman, 2, 5), (trp_rhodok_spearman, 2, 4), (trp_rhodok_crossbowman, 2, 3)]),
    ("kingdom_30_reinforcements_b", "{!}kingdom_30_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_rhodok_trained_spearman, 4, 11), (trp_rhodok_veteran_spearman, 4, 10), (trp_rhodok_veteran_crossbowman, 4, 9)]),
    ("kingdom_30_reinforcements_c", "{!}kingdom_30_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_gael_deaisbard, 4, 10), (trp_gael_portaestandarte, 0, 1), (trp_gael_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ("kingdom_31_reinforcements_a", "{!}kingdom_31_reinforcements_a", 0, 0, fac_commoners, 0, [
        (trp_rhodok_tribesman, 2, 5), (trp_rhodok_spearman, 2, 4), (trp_rhodok_crossbowman, 2, 3)]),
    ("kingdom_31_reinforcements_b", "{!}kingdom_31_reinforcements_b", 0, 0, fac_commoners, 0, [
        (trp_rhodok_trained_spearman, 4, 11), (trp_rhodok_veteran_spearman, 4, 10), (trp_rhodok_veteran_crossbowman, 4, 9)]),
    ("kingdom_31_reinforcements_c", "{!}kingdom_31_reinforcements_c", 0, 0, fac_commoners, 0, [
        (trp_gael_deaisbard, 4, 10), (trp_gael_portaestandarte, 0, 1), (trp_gael_sacerdote, 0, 1), (trp_todos_cuerno, 0, 1)]),

    ##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,7),(trp_swadian_skirmisher,5,10),(trp_swadian_militia,11,26)]),
    ##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,5,10),(trp_swadian_infantry,5,10),(trp_swadian_crossbowman,3,8)]),
    ##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_knight,2,6),(trp_swadian_sergeant,2,5),(trp_swadian_sharpshooter,2,5)]),
    ##
    ##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,3,7),(trp_vaegir_skirmisher,5,10),(trp_vaegir_footman,11,26)]),
    ##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,4,9),(trp_vaegir_infantry,5,10),(trp_vaegir_archer,3,8)]),
    ##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_knight,3,7),(trp_vaegir_guard,2,5),(trp_vaegir_marksman,2,5)]),
    ##
    ##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,3,7),(trp_khergit_skirmisher,5,10),(trp_khergit_tribesman,11,26)]),
    ##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horse_archer,4,9),(trp_khergit_horse_archer,5,10),(trp_khergit_horseman,3,8)]),
    ##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer,3,7),(trp_khergit_veteran_horse_archer,2,5),(trp_khergit_horse_archer,2,5)]),
    ##
    ##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,3,7),(trp_nord_footman,5,10),(trp_nord_recruit,11,26)]),
    ##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_veteran,4,9),(trp_nord_warrior,5,10),(trp_nord_footman,3,8)]),
    ##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,3),(trp_nord_veteran,2,5),(trp_nord_warrior,2,5)]),
    ##
    ##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,3,7),(trp_rhodok_crossbowman,5,10),(trp_rhodok_tribesman,11,26)]),
    ##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,4,9),(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,3,8)]),
    ##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,7),(trp_rhodok_veteran_spearman,2,5),(trp_rhodok_veteran_crossbowman,2,5)]),



    ("steppe_bandit_lair", "Scoti Lair", icon_camp | carries_goods(2) | pf_is_static | pf_hide_defenders,
        0, fac_neutral, bandit_personality, [(trp_steppe_bandit, 15, 58)]),  # chief cambiado icono
    ("taiga_bandit_lair", "Outlaw Bandit Lair", icon_camp | carries_goods(2) | pf_is_static | pf_hide_defenders,
        0, fac_neutral, bandit_personality, [(trp_taiga_bandit, 15, 58)]),  # chief cambiado icono
    ("desert_bandit_lair", "Bandit Lair", icon_camp | carries_goods(2) | pf_is_static | pf_hide_defenders,
        0, fac_neutral, bandit_personality, [(trp_desert_bandit, 15, 58)]),  # chief cambiado icono
    ("forest_bandit_lair", "Unrights Bandit Camp", icon_camp | carries_goods(2) | pf_is_static |
        pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_forest_bandit, 15, 58)]),  # chief cambiado icono
    ("mountain_bandit_lair", "Morths Bandit Hideout", icon_camp | carries_goods(2) | pf_is_static |
        pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_mountain_bandit, 15, 58)]),  # chief cambiado icono
    ("sea_raider_lair", "Frankish Landing", icon_ship_on_land | carries_goods(2) | pf_is_static |
        pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_sea_raider, 15, 50)]),  # chief cambiado icono
    ("sea_raider_lair2", "Dena Landing", icon_ship_on_land | carries_goods(2) | pf_is_static | pf_hide_defenders,
        0, fac_neutral, bandit_personality, [(trp_black_khergit_horseman, 15, 50)]),  # chief cambiado icono
    ("looter_lair", "Kidnappers' Hideout", icon_camp | carries_goods(2) | pf_is_static | pf_hide_defenders,
        0, fac_neutral, bandit_personality, [(trp_looter, 15, 25)]),  # chief cambiado icono

    ("bandit_lair_templates_end", "{!}bandit_lair_templates_end", icon_axeman | carries_goods(
        2) | pf_is_static, 0, fac_outlaws, bandit_personality, [(trp_sea_raider, 15, 50)]),

    ("leaded_looters", "Band of Robbers", icon_axeman | carries_goods(8) | pf_quest_party,
        0, fac_neutral, bandit_personality, [(trp_looter_leader, 1, 1), (trp_looter, 3, 3)]),

    # diplomacy chief begin
    ("dplmc_spouse", "Your spouse", icon_woman | pf_civilian | pf_show_faction, 0, fac_neutral, merchant_personality, []),

    ("dplmc_gift_caravan", "Your Caravan", icon_mule | carries_goods(45) | pf_show_faction, 0,
        fac_commoners, escorted_merchant_personality, [(trp_caravan_master, 1, 1), (trp_caravan_guard, 5, 25)]),
    # recruiter kit begin
    ("dplmc_recruiter", "Recruiter", icon_gray_knight | pf_show_faction,
     0, fac_neutral, merchant_personality, [(trp_dplmc_recruiter, 1, 1)]),
    # recruiter kit end
    # diplomacy chief  end
    # tempered chief
    ("skirmish_party", "Skirmishers", icon_khergit | carries_goods(1) | pf_always_visible |
        pf_limit_members, 0, fac_commoners, aggressiveness_0 | courage_15, []),  # Tempered chief skirmish party
    ("spy_party", "Cautious Traveler", icon_gray_knight | carries_goods(1) | pf_always_visible | pf_limit_members, 0,
        fac_commoners, aggressiveness_0 | courage_15, [(trp_mercenary_skirmisher, 1, 1)]),  # Tempered chief spy party
    ("player_loot_wagon", "Supply Wagon", icon_mule | pf_show_faction | pf_quest_party, 0,
        fac_commoners, escorted_merchant_personality, []),  # Tempered chief added player loot wagon
    ("escaped_companion", "Exhausted Companion", icon_gray_knight | pf_show_faction, 0, fac_commoners,
        escorted_merchant_personality, []),  # Tempered chief added for defeated player companions
    ("funeral_pyre", "Funeral Pyre", icon_funeral_pyre | pf_is_static | pf_hide_defenders | pf_always_visible |
        pf_no_label, 0, fac_neutral, escorted_merchant_personality, []),  # tempered chief funeral pyre
    ("personal_messenger", "Messenger", icon_gray_knight | pf_always_visible | pf_limit_members, 0, fac_commoners,
        aggressiveness_0 | courage_15, [(trp_mercenary_skirmisher, 1, 1)]),  # Tempered chief messenger
    ("entrench", "Entrenchment", icon_last_entrench | pf_is_static |
        pf_always_visible | pf_no_label, 0, fac_neutral, bandit_personality, []),
    # tempered chief acaba
    # chief sacerdotes party
    ("sacerdotes_party", "Christian Clergy", icon_peasant | carries_goods(2), 0, fac_christians,
     merchant_personality, [(trp_picto_sacerdote, 3, 9), (trp_peasant_woman, 4, 15)]),
    ("paganos_party", "Pagan Priests", icon_peasant | carries_goods(2), 0, fac_pagans,
     merchant_personality, [(trp_anglo_pagano, 3, 9), (trp_farmer, 4, 15)]),

    # Script de refuerzos y reclutas a ciudades chief
    # ("reinforcements","Reinforcements",icon_axeman|pf_show_faction,0,fac_commoners,soldier_personality,[]),
    # mas chief
    # wulf
    ("sea_raiders_ships", "Frankish Pirates", icon_ship | pf_is_ship | carries_goods(
        2), 0, fac_outlaws, bandit_personality, [(trp_sea_raider, 20, 40)]),
    ("sea_raiders_ships2", "Dena Pirates", icon_ship | pf_is_ship | carries_goods(2),
        0, fac_outlaws, bandit_personality, [(trp_black_khergit_horseman, 20, 40)]),
    ("sea_raiders_ships3", "Scoti Pirates", icon_ship | pf_is_ship | carries_goods(
        2), 0, fac_outlaws, bandit_personality, [(trp_steppe_bandit, 20, 40)]),
    # wulf end   ("sea_pierats","Sea Pirates",icon_ship|pf_is_ship|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sea_raider,20,40)]),
    # otras chief
    ("bishop_party", "Bishop", icon_gray_knight | carries_goods(5) | pf_auto_remove_in_town | pf_quest_party,
        0, fac_commoners, escorted_merchant_personality, [(trp_bishop, 1, 1), (trp_picto_sacerdote, 4, 10)]),
    #  ("scouts","Pictish Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_kingdom_20,bandit_personality,[(trp_khergit_skirmisher,10,20),(trp_pict_woman,1,1)]),
    #  ("watchtower_scouts","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_kingdom_20,bandit_personality,[(trp_mercenary_horseman,5,7)]),
    ("iniau", "Iniau Scouts", icon_vaegir_knight | carries_goods(1), 0, fac_neko,
        bandit_personality, [(trp_iniau, 1, 1), (trp_swadian_sergeant, 43, 65)]),
    # chief followers seguidores
    # Floris addon seatrade chief
    ("sea_traders", "Sea Traders", icon_ship | pf_is_ship | carries_goods(50) | pf_show_faction, 0, fac_commoners,
        merchant_personality, [(trp_caravan_master, 1, 1), (trp_caravan_guard, 20, 40), (trp_mercenary_crossbowman, 10, 25)]),
    # Floris addon seatrade end
    # rigale chief
    ("ambushers", "Ambushers", icon_axeman | carries_goods(2), 0, fac_forest_bandits,
     aggressiveness_15 | courage_15, [(trp_forest_bandit, 5, 80)]),
    ("zamoshie_bandits", "North Bandits", icon_peasant | carries_goods(9) |
     pf_quest_party, 0, fac_outlaws, bandit_personality, [(trp_forest_bandit, 20, 49)]),

    ("ship"	, "Ship", icon_ship | pf_is_ship | pf_disabled | pf_is_static | pf_always_visible |
     pf_hide_defenders | pf_show_faction, 0, fac_commoners, merchant_personality, [(trp_mercenary_leader, 1, 1)]),
    ##  ("followers","Camp Followers",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,3),(trp_caravan_guard,4,6),(trp_farmer,3,14),(trp_follower_woman,15,60),(trp_fighter_woman,12,40)]),
    ##  ("followersplayer","Camp Followers",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,3),(trp_caravan_guard,4,6),(trp_farmer,3,14),(trp_follower_woman,15,60),(trp_fighter_woman,12,40)]),
    # Foragers SoT chief
    # anglos
    # ("bernician_foragers","Acerweras",icon_gray_knight|carries_goods(5),0,fac_kingdom_4,merchant_personality,[(trp_nord_footman,5,10),(trp_nord_huntsman,2,4),(trp_nord_warrior,2,4)]),
    # jutos
    # ("rheged_foragers","Foragers",icon_vaegir_knight|carries_goods(5),0,fac_kingdom_1,merchant_personality,[(trp_sarranid_footman,5,10),(trp_sarranid_skirmisher,2,4),(trp_sarranid_infantry,2,4)]),
    # britons
    # ("gododdin_foragers","Foragers",icon_vaegir_knight|carries_goods(5),0,fac_kingdom_3,merchant_personality,[(trp_swadian_militia,3,7),(trp_swadian_footman,3,5),(trp_swadian_skirmisher,2,6)]),
    # sajones
    # ("dalriadan_foragers","Foragers",icon_vaegir_knight|carries_goods(5),0,fac_kingdom_2,merchant_personality,[(trp_vaegir_footman,5,10),(trp_vaegir_skirmisher,2,4),(trp_vaegir_infantry,2,4)]),
    # irish
    # ("alcluyd_foragers","Foragers",icon_vaegir_knight|carries_goods(5),0,fac_kingdom_7,merchant_personality,[(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,2,4),(trp_rhodok_veteran_spearman,2,4)]),
    # pictos
    ##  ("pictish_foragers","Pictish Foragers",icon_vaegir_knight|carries_goods(5),0,fac_kingdom_5,merchant_personality,[(trp_khergit_skirmisher,6,12),(trp_picti_each,3,5),(trp_pict_woman,1,3)]),

]
