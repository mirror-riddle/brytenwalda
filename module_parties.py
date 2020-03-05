from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small #chief cambiado

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(-21.19,63.45),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.
#needed to backup player's party and to avoid data corruption freelancer chief
  ("freelancer_party_backup","{!}",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #freelancer chief
  #("player_party_backup","{!}",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  
  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

#chief sea battles
("burning_buildings","If you see me, report the fire bug.",  pf_disabled|icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0, -50),[], 170),
 ("ship_colisions","If you see me, report the colision bug.",  pf_disabled|icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0, -50),[], 170),
#chief acaba
###############################################################  
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59,111),[]),

  ("town_1","Cantwaraburh",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-116.75,137.69),[],170), #done
  ("town_2","Seals-ey",     icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.86,154.12),[],260), #done
  ("town_3","Din_Eidyn",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.79,-80.34),[],80), #no
  ("town_4","Oxenaforda",     icon_town_1|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.44,114.44),[],290), #done
  ("town_5","Caer_Maunguid",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.74,45.31),[],90), #done
  ("town_6","Alt_Clut",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.18,-42.54),[],180), #done
  ("town_7","Caer_Ligualid",   icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.38,3.06),[],120), #done

  ("town_8","Grantebrycge", icon_town_1|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.72,101.41),[],175), #done
  ("town_9","Caer_Went",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.89,113.50),[],90), #done
  ("town_10","Eoferwic",   icon_town_1|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.99,22.27),[],310), #done
  ("town_11","Aegelesburh",   icon_town_1|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.64,114.48),[],150), #done
  ("town_12","Lundenwic", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-91.97,129.14),[],25), #done
  ("town_13","Din_Gonwy",icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.66,60.70),[],120), #done
  ("town_14","Rendlaesham",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125.85,109.86),[],135), #done

  ("town_15","Caer_Luit_Coyt",  icon_town_1|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.82,68.84),[],135), #Done
  ("town_16","Dorce_Ceaster",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.42,122.91),[],135), #done
  ("town_17","Caer_Uisc",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.07,158.63),[],255), #done
  ("town_18","Searoburh",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.74,143.47),[],135), #done

  ("town_19","Dun_At",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.55,-87.17),[],190), #done
  ("town_20","Loidis",     icon_town_1|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.05,39.99),[],120), #done
  ("town_21","Nas na Riogh",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.78,81.64),[],80), #no
  ("town_22","Caer_Meguaidd",     icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.83,81.25),[],290), #done
  ("town_23","Licidfelth",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.39,87.62),[],90), #Done
  ("town_24","Linnuis",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.16,63.25),[],155), #done
  ("town_25","Caer_Peris",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.50,98.58),[],240), #no

  ("town_26","Brycheiniog",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.68,109.78),[],170), #no
  ("town_27","Bebbanburh",     icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.85,-39.69),[],0), #done
  ("town_28","Llys_Pengwern",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.63,79.82),[],80), #done
  ("town_29","Din_Bych",     icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.99,112.58),[],290), #no
  ("town_30","Cruaghan",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.81,34.17),[],90), #done
  ("town_31","Temair",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.85,51.30),[],155), #done
  ("town_32","Rath_Celtair",   icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.56,24.91),[],0), #done

  ("town_33","Aileach",   icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.98,-20.60),[],0), #done
  ("town_34","Monid Crobh",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.75,-108.91),[],240), #done
  ("town_35","Dun_Iasgach",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.37,113.04),[],170), #no
  ("town_36","Caiseal",   icon_town_1|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(88.90,100),[],290), #done
  ("town_37","Duin_Foither",   icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.55,-130.92),[],0), #done
  ("town_38","Caer_Wenddoleu",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.03,-4.36),[],90), #done
  ("town_39","Dun_Taruo",   icon_town_1|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.09,-160.99),[],90), #done

  ("town_40","Clochair", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.25,17.81),[],45), #done
  ("town_41","Cirren_Ceaster",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.76,107.25),[],170), #done
  ("town_42","Din_Cado",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.63,127.78),[],90), #done

#   Aztaq_Castle       
#  Malabadi_Castle
  ("castle_1","Alne_Ceaster",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.38,106.12),[],50),
  ("castle_2","Ceasterfeld",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.67,70.03),[],75),
  ("castle_3","Caer_Lloyw",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.32,101.59),[],100),
  ("castle_4","Cisse_Ceaster",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-89.75,148.53),[],180),
  ("castle_5","Loch_Gabar",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.95,63.99),[],45),
  ("castle_6","Rath_Cormac",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(91.29,2.17),[],80),  
  ("castle_7","Dinas_Powys",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.93,126.15),[],45),
  ("castle_8","Theodford",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.89,102.24),[],30),
  ("castle_9","Ard_Breacain",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.13,45.01),[],15),
  ("castle_10","Hlew_Ceaster",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.26,151.32),[],110),
  ("castle_11","Colne_Ceaster",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-113.31,117.46),[],75),
  ("castle_12","Hrofaes_Ceaster",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.56,132.78),[],95),
  ("castle_13","Dinas",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.05,113.50),[],115),
  ("castle_14","Esterteferd",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.28,119.75),[],90),
  ("castle_15","Kelliwic",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.72,157.44),[],235),
  ("castle_16","Din_Tagell",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.54,134.35),[],45),
  ("castle_17","Caer_Legionis",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.72,58.50),[],15),
  ("castle_18","Caer_Magnis",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.38,90.58),[],300),
  ("castle_19","Biedcanford",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.49,122.52),[],280),
  ("castle_20","Gyldeford",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-90.65,135.48),[],260),
  ("castle_21","Cathair_Chomain",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.23,78.78),[],90),
  ("castle_22","Caer_Daun",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.63,55.89),[],260),
  ("castle_23","Hyrne_Ceaster",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.85,56.39),[],80),
  ("castle_24","Ard_Ladhrann",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(55.85,100.43),[],240),
  ("castle_25","Din_Arth",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.30,57.93),[],260),
  ("castle_26","Caer_Legeion_Guar_Usic",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.71,121.10),[],260),
  ("castle_27","Caer_Caratauc",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.10,98.09),[],260),
  ("castle_28","Cathair na Steige",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.88,114.40),[],60),

  ("castle_29","Ath_Cormac",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.80,18.35),[],60),
  ("castle_30","Caer_Durnac",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.94,149.39),[],260),
  ("castle_31","Vintan_Ceaster",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.53,144.50),[],260),
  ("castle_32","Boweseia",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.09,91.46),[],260),
  ("castle_33","Ligor_Ceaster",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.20,91.55),[],80),
  ("castle_34","Dinas_Bran",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.59,65.01),[],260),
  ("castle_35","Dinas_Emrys",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.71,68.88),[],260),
  ("castle_36","Caer_Guricon",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36.12,82.94),[],260),
  ("castle_37","Caer_Baddan",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.45,122.36),[],260),
  ("castle_38","Din_Cogan",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.08,110.68),[],260),
  ("castle_39","Cippanhamme",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.90,123.54),[],280),
  ("castle_40","Norwic",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-121.34,88.63),[],260),
  ("castle_41","Ath_an_Tearmainn",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.09,48.86),[],90),
  ("castle_42","Caer_Manaw",icon_town_desert|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.94,21.12),[],120),
  ("castle_43","Caer_Pentaloch",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.32,-65.79),[],260),
  ("castle_44","Iudeu",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.89,-81.21),[],260),
  ("castle_45","Dun_Chuile",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.98,96.20),[],80),
  ("castle_46","Din_Drust",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.80,-1.77),[],260),
  ("castle_47","Dun_na_mBarc",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.58,122.58),[],240),
  ("castle_48","Din_Rheged",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.51,-1.08),[],260),
  ("castle_49","Caer_Sws",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.36,97.12),[],260),
  ("castle_50","Duin_Ollaigh",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.83,-105.90),[],260),
  ("castle_51","Crumbford",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.34,73.45),[],280),
  ("castle_52","Chinesburie",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.16,83.36),[],260),

  ("castle_53","Denisesburna",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.39,-19.06),[],45),
  ("castle_54","Caer_Aeron",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.11,-12.59),[],90),
  ("castle_55","Dun_Devenel",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.52,-50.97),[],45),
  ("castle_56","Caer_Caradawg",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.09,-32.49),[],90),
  ("castle_57","Middelsburh",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.78,-6.02),[],45),
  ("castle_58","Ath_Mor",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.53,61.61),[],90),
  ("castle_59","Ath_Berchna",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.48,36.43),[],15),  
  ("castle_60","Rath_Clochair",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.33,4.80),[],260),
  ("castle_61","Din_Baer",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.26,-81.69),[],260),
  ("castle_62","Duin_Baitte",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.63,-185.32),[],280),
  ("castle_63","Duin_Bolg",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.41,-102.09),[],80),
  ("castle_64","Dun_Duirn",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.73,-96.43),[],260),
  ("castle_65","Ad_Gefrin",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.84,-42.38),[],260),
  ("castle_66","Duin_Caillen",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.56,-117.45),[],45),
  ("castle_67","Ard_Eachadha",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.96,31.85),[],45),
  ("castle_68","Dun_Aberte",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.05,-58.91),[],45),
  ("castle_69","Aidhne",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.70,46.72),[],90),
  ("castle_70","Dun_Buicead",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.71,76.22),[],90),
  ("castle_71","Dun_Nechtain",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.31,-153.79),[],90),
  ("castle_72","Dun_Sebuirge",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.95,-22.05),[],45),
  ("castle_73","Din_Hua_nAmalgada",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.34,19.78),[],80),
  ("castle_74","Magh_Rath",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.34,2.74),[],80),
  ("castle_75","Ath_na_Foraire",icon_briton_castle1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.01,24.69),[],80),
 

#     Rinimad      
#              Rietal Derchios Gerdus
# Tuavus   Pamir   vezona 
  
  ("village_1","Taddanleage",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.04,138.72),[],100),
  ("village_2","Wlencing",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.39,146.59),[],110),
  ("village_3","Wellatun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.12,53.09),[],120),
  ("village_4","Portesmuda",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.46,154.23),[],130),
  ("village_5","Cetgueli",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.54,116.12),[],170),
  ("village_6","Llan_Heledd",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.31,20.83),[],100),
  ("village_7","Ynys_Metcaut",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.16,-52.05),[],110),
  ("village_8","Herr_Hlaw",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.32,124.76),[],120),
  ("village_9","Gwinear",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.70,145.39),[],130),
  ("village_10","Gislheresuuyrth",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.62,126.48),[],170),

  ("village_11","Isura",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.29,-0.46),[],45),
  ("village_12","Swanawic",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.71,157.30),[],110),
  ("village_13","Aber_Lleu",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.45,-39.79),[],120),
  ("village_14","Bucgan_Ora",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.92,150.97),[],130),
  ("village_15","Ad_Candidam_Casam",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.60,2.79),[],90),
  ("village_16","Weargebuman",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.35,141.63),[],170),
  ("village_17","Brememium",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.68,-23.80),[],35),
  ("village_18","Mag_Uillin",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.96,65),[],180),
  ("village_19","Westarham",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-93.96,136.98),[],170),
  ("village_20","Ricestun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-89.81,64.34),[],170),

  ("village_21","Snetesham",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-102.49,83.91),[],100),
  ("village_22","Eglesfeld",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.76,49.71),[],110),
  ("village_23","Bos_Menegh",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.96,134.52),[],120),
  ("village_24","Wodetun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.41,125.65),[],130),
  ("village_25","Maes_Cogwy",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.04,40.40),[],170),
  ("village_26","Tref_Ilic",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.72,141.45),[],170),
  ("village_27","Maesmor",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.72,105.96),[],170),
  ("village_28","Waldham",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-90.29,48.77),[],170),
  ("village_29","Cantmael",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.33,129.47),[],170),

  ("village_30","Eclesia_hyll",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17,42.63),[],170),
  ("village_31","Cetham",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.03,135.53),[],100),
  ("village_32","Ynys_Mon",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.35,56.26),[],110),
  ("village_33","Glouvia",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.78,103.21),[],120),
  ("village_34","Badun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.84,118.37),[],130),
  ("village_35","Dommoc",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-143.25,102.79),[],170),
  ("village_36","Scythles",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.28,6.60),[],80),
  ("village_37","Pairc_Mor",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.41,64.79),[],90),
  ("village_38","Berewic",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.31,124.17),[],170),
  ("village_39","Buais",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.64,-4.90),[],45),
  ("village_40","Carwynnen",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.11,155.83),[],170),

  ("village_41","Tatessete",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.91,75.89),[],100),
  ("village_42","Niwantun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.22,78.16),[],110),
  ("village_43","Cantaleah",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-124.45,91.79),[],120),
  ("village_44","Costessey",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.39,83.97),[],130),
  ("village_45","Abercrdf",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.29,109.76),[],170),
  ("village_46","Wicstun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.45,29.86),[],260),
  ("village_47","Inderawuda",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.01,34.80),[],90),
  ("village_48","Poclintun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.22,25.41),[],180),
  ("village_49","Leodridan",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-88.28,129.60),[],10),
  ("village_50","Leim_an_Eich",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.80,-16.34),[],240),

  ("village_51","Eldretune",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.86,152.35),[],100),
  ("village_52","Hysetun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-99.33,96.97),[],110),
  ("village_53","Elmwella",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-124.27,100.56),[],120),
  ("village_54","Hreopedun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.06,89.31),[],130),
  ("village_55","Banesbyrig",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.25,103.21),[],170),
  ("village_56","Clacc_Inga_Tun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-115.38,122.07),[],170),
  ("village_57","Bartun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.37,7.18),[],90),
  ("village_58","Benchoer_Moer",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.80,57.96),[],170),
  ("village_59","Cructan",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.57,132.92),[],170),
  ("village_60","Dinypas",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.13,-73.09),[],170),

  ("village_61","Cluana",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.60,-113.36),[],90),
  ("village_62","Luith_Feirn",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.94,-87.03),[],80),
  ("village_63","Dofras",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125.45,143),[],100),
  ("village_64","Lan_Withennoc",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.07,149.45),[],100),
  ("village_65","Caeginesham",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.23,115.11),[],100),
  ("village_66","Llan_Forfael",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.95,18.78),[],100),
  ("village_67","Catraeth",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.22,-0.56),[],100),
  ("village_68","Mai_Dun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.08,143.66),[],100),
  ("village_69","Creic",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.88,-96.17),[],45),
  ("village_70","Banhedos",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.58,153.31),[],100),

  ("village_71","Aporcrosan",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.42,-177.75),[],240),
  ("village_72","Lann_Abae",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.94,-130.73),[],260),
  ("village_73","Ynas_Towy",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.28,107.29),[],55),
  ("village_74","Cymensoraham",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.76,143),[],15),
  ("village_75","Tappingtun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.69,127.80),[],10),
  ("village_76","Taceham",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.98,131.87),[],35),
  ("village_77","Halhfeax",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.20,48.98),[],160),
  ("village_78","Gwythel Yel",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.57,151.48),[],180),
  ("village_79","Moel_Fryn",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.14,111.96),[],0),
  ("village_80","Aewiue",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125.87,137.16),[],40),

  ("village_81","Ciorrincg",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.68,143.08),[],20),
  ("village_82","Drum_Ceatt",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.89,-19.71),[],90),  
  ("village_83","Ynys_Manaw",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.73,24.41),[],55),
  ("village_84","Du_Glas",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.13,-32.43),[],180),
  ("village_85","Cyddaingastun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.57,99.01),[],10),
  ("village_86","Gippeswic",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-133.49,112),[],35),
  ("village_87","Creodahanhyll",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.58,136.10),[],160),
  ("village_88","Merceham",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.41,118.23),[],180),
  ("village_89","Aemethyll",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.05,123.01),[],0),
  ("village_90","Earnningtun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.27,107.48),[],40),

  ("village_91","Alrwic",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.41,81.75),[],20),
  ("village_92","Caislen_Credi",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.90,-99.07),[],45),
  ("village_93","Hamtun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79,106.95),[],55),
  ("village_94","Fearr_Leah",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.36,95.59),[],15),
  ("village_95","Beormaingasham",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.83,94.61),[],10),
  ("village_96","Bertha",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.84,-104.42),[],90),
  ("village_97","Rae_Ban",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.82,40.51),[],90),
  ("village_98","Hyncaleah",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.54,97.89),[],180),
  ("village_99","Denetun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.75,72.41),[],0),

  ("village_100","Winteringasham",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81.62,42.96),[],20),
  ("village_101","Faffand",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.90,78.27),[],80),
  ("village_102","Lyme",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.67,56.66),[],55),
  ("village_103","Hanstige",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.52,87.01),[],15),
  ("village_104","Cinlipiuc",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.01,100.87),[],10),
  ("village_105","Ced",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.95,51.04),[],35),
  ("village_106","Llan_y_Hadein",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.18,113.44),[],160),
  ("village_107","Dumanyn",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.42,-75.39),[],180),
  ("village_108","Ardudwy",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.59,71.82),[],0),
  ("village_109","Grafrenn",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.92,64.06),[],45),

  ("village_110","Elfed",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.35,118.13),[],20),
  ("village_111","Merthyr_Tydfil",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.36,117.51),[],60),
  ("village_112","Eglwys_Tysilio",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.50,86.46),[],55),
  ("village_113","Abermynwy",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.42,110.79),[],15),
  ("village_114","Grwst",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.15,62.88),[],10),
  ("village_115","Halh",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.18,60.37),[],35),
  ("village_116","Hefenfelth",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50.28,-22.30),[],160),
  ("village_117","Campodunum",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.42,34.84),[],180),
  ("village_118","Llyn",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.18,72.78),[],0),
  ("village_119","Erging",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.08,112.49),[],40),

  ("village_120","Egleshalh",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.57,64.60),[],20),
  ("village_121","Amwythig",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.47,86.79),[],60),
  ("village_122","Beolatun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.69,100.94),[],55),
  ("village_123","Llan",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.61,93.18),[],15),
  ("village_124","Weorthingtun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.20,94.64),[],10),
  ("village_125","Llanidloes",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.36,86.50),[],35),
  ("village_126","Aberystwyth",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.14,99.38),[],160),
  ("village_127","Clac_Manau",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.17,-86.47),[],180),
  ("village_128","Merthyr_Cynog",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.95,112.87),[],0),

  ("village_129","Oratun",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.67,111.17),[],20),
  ("village_130","Cill_Chleite",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.76,13.14),[],60),
  ("village_131","Cill_Alaid",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.41,20.02),[],260),
  ("village_132","Eifionydd",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.15,70.43),[],15),
  ("village_135","Sliab_Culinn",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.98,27.93),[],90),
  ("village_134","Mag_Mucceda",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.57,18.08),[],180),
  ("village_135","Cogwy",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.89,81.67),[],160),
  ("village_136","Pen_Rhionydd",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.82,-0.95),[],180),
  ("village_137","Camus",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(129.97,57.45),[],180),
  ("village_138","Arderydd",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.67,-8.36),[],40),
#alrwic village formato usado, roman fort villages
  ("village_139","Mynyw",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.60,107.45),[],20),
  ("village_140","Llan_Docgwinn",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.02,124.33),[],60),
  ("village_141","Llangollen",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.51,71.17),[],55),
  ("village_142","Opergelei",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.76,59.99),[],15),
  ("village_143","Pillgwynllwg",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.18,124.24),[],10),
  ("village_144","Rhaeadr_Gwy",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.64,95.50),[],35),
  ("village_145","Cuil_Conaire",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.43,52.30),[],90),
  ("village_146","Pencaer",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.69,105.64),[],180),
  ("village_147","Mag_Tuired",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(119.53,43.90),[],45),
  ("village_148","Buireann",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.54,-17.12),[],240),
#alrwic village acaba
  ("village_149","Genouhalh",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.50,72.91),[],20),
  ("village_150","Dewyddwella",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.56,98.43),[],60),
  ("village_151","Helfeld",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.77,67.21),[],55),
  ("village_152","Bangor_Is_Coed",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.35,68.07),[],15),
  ("village_153","Cathures",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.23,-54.65),[],10),
  ("village_154","Essovre",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.30,76.94),[],35),
  ("village_155","LlangWern",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.85,92.70),[],160),
  ("village_156","Dwfr",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.16,54.69),[],180),
  ("village_157","Cill_Mic_Creannain",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.26,-6.51),[],60),

  ("village_158","Aebbercurnig",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.46,-82.47),[],90),
  ("village_159","Irrus_Domnann",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(130.09,28.63),[],180),
  ("village_160","Dyvnwtdd",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.35,-24.39),[],35),
  ("village_161","Raith_Bec",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(51.35,-1.84),[],180),
  ("village_162","Tuidhidhean",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.30,10.51),[],260),
  ("village_163","Aberlessic",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50.60,-86.19),[],240),
  ("village_164","Cluain_Meala",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.95,106.41),[],240),
  ("village_165","Urnaidhe",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.57,103.52),[],180),
  ("village_166","Anava",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.79,-6.29),[],45),

  ("village_167","Art_Muirchol",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.88,-121.53),[],90),
  ("village_168","Cuince",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(104.24,86.32),[],90),
  ("village_169","Ad_Cluanan",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.61,-154.41),[],35),
  ("village_170","Cliath",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.54,-196.70),[],45),
  ("village_171","Luimneach_Laighean",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.16,107.54),[],45),
  ("village_172","Ard_Macha",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.59,12.07),[],240),
  ("village_173","Beannchar",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.91,4.48),[],90),
  ("village_174","Both_Domhnaigh",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.46,5.62),[],80),
  ("village_175","Cathair_Chonroi",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.88,93.79),[],45),

  ("village_176","Luachair",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.57,87.57),[],90),
  ("village_177","Ached_Bou",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.73,82.12),[],80),
  ("village_178","Dol_Ais",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.13,-164.14),[],35),
  ("village_179","Lois_Mor",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.13,119.59),[],240),
  ("village_180","Mag_Liphi",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(55.78,71.64),[],260),
  ("village_181","Dol",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.29,-113.99),[],240),
  ("village_182","Tairpert_Boitir",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.76,-72.27),[],90),
  ("village_183","Ego",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.83,-149.21),[],80),
  ("village_184","Boand",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.98,44.47),[],45),

  ("village_185","Achadh_Fharcha",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.16,50.23),[],180),
  ("village_186","Ir_Ysgyn",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.56,-70.32),[],45),
  ("village_187","Boher_Bue",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.29,110.19),[],60),
  ("village_188","Achadh_Chuinnire",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.22,18.36),[],90),
  ("village_189","Sleamhain",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(51.52,55.23),[],80),
  ("village_190","Gobhann",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.09,-19.49),[],45),
  ("village_191","Huensis",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.40,-122.82),[],240),
  ("village_192","Yr_Wyn",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.51,-31.74),[],260),
  ("village_193","Ilea",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.89,-91.15),[],90),

  ("village_194","Doirad_Eilinn",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(55.04,-96.64),[],180),
  ("village_195","Baile_Loch",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.27,27.59),[],90),
  ("village_196","Cindgaradh",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.53,-57.13),[],90),
  ("village_197","Llanerch",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.53,-32.16),[],90),
  ("village_198","Druim_Dergblathiug",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.78,-121.85),[],80),
  ("village_199","Nisa",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.33,-167.77),[],45),
  ("village_200","Lugmud",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.91,35.55),[],240),
  ("village_201","Dumha_Aichir",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.74,93.09),[],260),
  ("village_202","Clogher_Mor",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(121.62,100.15),[],180),

  ("village_203","Imchlar",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.42,1.24),[],240),
  ("village_204","Cath_Atho_Dara",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(100.34,99.36),[],45),
  ("village_205","Mageduac",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.49,-72.49),[],90),
  ("village_206","Ached_Fobuir",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(115.54,36.94),[],90),
  ("village_207","Uaine",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.87,-129.77),[],80),
  ("village_208","Magh_Gals",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.71,90.45),[],240),
  ("village_209","Pabell",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.84,-40.18),[],240),
  ("village_210","Aillinn",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.54,78.56),[],260),
  ("village_211","Ruim",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.76,-171.80),[],90),
  ("village_212","Daire_Calgaich",  icon_village_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.55,-12.31),[],180),
  
  ("salt_mine","Salinae",icon_town_snow|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.08,79.95),[]),
##  ("iron_mine","Slieve Anierin",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.01,22.69),[]),

  ("four_ways_inn","Feotherestan_(inn)",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.42,41.42),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
##  ("test_scene","test_scene",icon_village_1|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -16.6),[]),
#plazas unicas chief sot
    ("celidon_forest","Ancient_Stones",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.88,78.56),[]),
  ("hidden_valley","Rare Ruins",icon_town_snow|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.91,47.69),[]),
  ("iniau_hideout","Sacred_Grove",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(91.28,89.86),[]),
    ("quarry1","Quarry",icon_town_snow|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.11,67.17),[]),
    ("hadrian_wall1","Hadrian Wall",icon_town_snow|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.83,1.26),[]),
    ("odin_cave","Cave",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.50,-122.85),[]),
###battlefiends unicos
    ("river_delta","River Delta",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.71,148.08),[]),
    ("quarry","Quarry",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.11,69.17),[]),
    ("tilting_at_windmills","Tilting at Windmills",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.51,-2.70),[]),
    ("multi_indigo_cradle","Cradle",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.17,24.78),[]),
    ("multi_indigo_frontier","Frontier",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50.06,59.24),[]),
    ("of_multi_caravan_ambush","Caravan ambush",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.67,34.65),[]),
    ("of_multi_crezy","Forest Pass",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.94,109.48),[]),
    ("of_multi_fjord","Fjord",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.22,117.01),[]),
    ("of_multi_hastings","Hastings",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-99.03,146.31),[]),
    ("of_multi_hot_gates","Hot Gates",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.86,-21.44),[]),
    ("of_multi_mini_circles","Circle",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.57,88.44),[]),
    ("of_multi_rock_valley","Rock Valley",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.06,-124.73),[]),
    ("of_multi_small_ruins","Ruins",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132.86,106.23),[]),
    ("of_multi_stone_circles","Stone Circles",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.43,106.43),[]),
    ("of_multi_thingvellir","Thingvellir",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.81,-62.64),[]),
    ("battle_stones","Stone Row",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.24,148.36),[]),
    ("circle_mystic","Circle Mystic",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.70,155.70),[]),
    ("roman_fort","Roman Fort",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.31,51.89),[]),
    ("hadrian_wall","Hadrian Wall",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.83,0.26),[]),
    ("farmland","Farmland",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.47,106.65),[]),
    ("stonemonumento","stonemonumento",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.68,15.20),[]),
    ("forestbattle","Forest Battle",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.27, 86.17),[]),
    ("multi_scene_dam_10","Dam",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.64, -50.41),[]),
#plazas unicas chief sot acaba
  
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56,-57),[]),

  ("training_ground","Training_Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.66,-91.68),[]),

  ("training_ground_1","Training_Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.79,-28.96),[],100),
  ("training_ground_2","Training_Village",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.30,62.73),[],100),
  ("training_ground_3","Training_Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.60,33.54),[],100), #chief quitada
  ("training_ground_4","Training_Lake",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.93,70.61),[],100),
  ("training_ground_5","Training_Camp",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.27,128.70),[],100),

###monasterios empieza
    ("monasterio1","Ad Candida Casam",icon_town_steppe|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.72,3.92),[]),
    ("monasterio2","Iona",icon_town_steppe|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.48,-112.83),[]),
    ("monasterio3","Cill Dara",icon_town_steppe|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.13,82.56),[]),
    ("monasterio4","Dommoc",icon_town_steppe|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-141.98,93.09),[]),
    ("monasterio5","Lindisfarne",icon_town_steppe|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.63,-54.08),[]),
    ("monasterio6","Mynyw",icon_town_steppe|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.29,110.53),[]),
    ("monasterio7","Ard Macha",icon_town_steppe|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.44,11.64),[]),
    ("monasterio8","Abbercurnig",icon_town_steppe|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.19,-79.05),[]),
#-## Outposts begin
  ("outpost_1","Outpost",icon_village_deserted_c|pf_disabled|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0, 0),[]),
  ("outpost_2","Outpost",icon_village_deserted_c|pf_disabled|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1, -1),[]),
  ("fort","My Lair",icon_village_snow_deserted_a|pf_disabled|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1, 1),[]),
#-## Outposts end

#TEMPERED ADDED PARTY FOR LOOT WAGON TROOP STORAGE  
  ("temp_loot_wagon","Supply Wagon",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#tempered acaba
  
#  bridge_a
  ("Bridge_1","{!}1",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.10,33.57),[],90),
  ("Bridge_2","{!}2",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.14,-143.73),[],64),
  ("Bridge_3","{!}3",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-78.79,78.50),[],10),
  ("Bridge_4","{!}4",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.03,106.28),[],90),
  ("Bridge_5","{!}5",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-89.92,131.42),[],135),
  ("Bridge_6","{!}6",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50.21,125.74),[],120),
  ("Bridge_7","{!}7",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.96,94.24),[],75),
  ("Bridge_8","{!}8",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.18,-58.18),[],55),
  ("Bridge_9","{!}9",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.57,139.15),[],60),
  ("Bridge_10","{!}10",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.43,-63.92),[],35),
  ("Bridge_11","{!}11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.36,7.54),[],90),
  ("Bridge_12","{!}12",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.11,126.35),[],135),
  ("Bridge_13","{!}13",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.41,112.36),[],90),
#  ("Bridge_14","{!}14",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145.19,143.25),[],75),
  ("Bridge_15","{!}15",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.42,83.18),[],15),
  ("Bridge_16","{!}16",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(88.03,44.52),[],35),
  ("Bridge_17","{!}17",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.49,50.25),[],15),
  ("Bridge_18","{!}18",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.53,91.60),[],90),
  ("Bridge_19","{!}19",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.30,94.14),[],120),

#  ("looter_spawn_point2"   ,"looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(6.31,111.66),[(trp_looter,15,0)]),
  ("looter_spawn_point"   ,"looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(2.79,92.01),[(trp_looter,15,0)]),
  ("looter_spawn_point3"   ,"looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(87.91,6.07),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"steppe_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(79.60,93.28),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(87.67,103.20),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"forest_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-3.88,-110.94),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point2"  ,"forest_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(93.02,54.61),[(trp_looter,15,0)]),
#  ("forest_bandit_spawn_point3"  ,"forest_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(55.07,60.35),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point4"  ,"forest_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-60.14,44.87),[(trp_looter,15,0)]),
#  ("mountain_bandit_spawn_point2","mountain_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(0.48,-81.33),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","mountain_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-35.79,-54.24),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point3","mountain_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-7.89,-13.68),[(trp_looter,15,0)]),
#  ("mountain_bandit_spawn_point4","mountain_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-46.23,16.38),[(trp_looter,15,0)]),
  ("new_sp"   ,"new_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.01,-75.39),[(trp_looter,15,0)]),
  ("new_sp2"   ,"new_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.31,109.39),[(trp_looter,15,0)]),
  ("new_sp3"   ,"new_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.31,50.39),[(trp_looter,15,0)]),
  ("new_sp4"   ,"new_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.31,142.39),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"sea_raider_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-116.54,151.02),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"sea_raider_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-93.61,86.14),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_3"   ,"sea_raider_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-28.67,159.38),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-24.93,109.88),[(trp_looter,15,0)]),
#puesto chief spam point 3 sea pirates
 ("ship_raider_spawn_point_1"   ,"sea_pirate_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(145.64,198.25),[(trp_looter,15,0)]), #scoti
 ("ship_raider_spawn_point_2"   ,"sea_pirate_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(129.39,-98.89),[(trp_looter,15,0)]), #frankish
 ("ship_raider_spawn_point_3"   ,"sea_pirate_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-199.27,166.67),[(trp_looter,15,0)]), #dena
 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ]
