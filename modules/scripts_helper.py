from headers.operations import troop_set_slot
from modules.constants import slot_troop_cur_center


custom_scripts = [
    # script_gather_companion_candidates_to_starting_town
    # INPUT: none
    # OUTPUT: none
    ("gather_companion_candidates_to_starting_town", [
        (troop_set_slot, "trp_npc2", slot_troop_cur_center, "$g_starting_town"),
        (troop_set_slot, "trp_npc3", slot_troop_cur_center, "$g_starting_town"),
        (troop_set_slot, "trp_npc7", slot_troop_cur_center, "$g_starting_town"),
        (troop_set_slot, "trp_npc11", slot_troop_cur_center, "$g_starting_town"),
        (troop_set_slot, "trp_npc_backwoodsharry", slot_troop_cur_center, "$g_starting_town"),
    ]),

]
