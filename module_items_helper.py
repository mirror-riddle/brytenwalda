from header_common import *
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

def create_items(prefixs, subfix):
  return [create_item(prefix, subfix) for prefix in prefixs]

def create_horse_prefix(id, name, extra_mesh=[]):
  mesh = [(id[1], 0)] + extra_mesh
  return [id[0], name, mesh]

def create_draft_horse_prefix(id):
  return create_horse_prefix(id, "Draft Horse")

def create_north_horse_prefix(id):
  return create_horse_prefix(id, "North Horse", [("horse_c",imodbits_horse_good)])

def create_paraveredus_horse_prefix(id):
  return create_horse_prefix(id, "Paraveredus", [("hunting_horse",imodbits_horse_good)])

def create_horses(ids, subfix, create_horse_prefix):
  return [create_item(create_horse_prefix(id), subfix) for id in ids]
