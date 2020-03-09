###################################################
# header_scene_props.py
# This file contains declarations for scene props
# DO NOT EDIT THIS FILE!
###################################################

sokf_type_container        = 0x0000000000000005
sokf_type_ai_limiter       = 0x0000000000000008
sokf_type_barrier          = 0x0000000000000009
sokf_type_barrier_leave    = 0x000000000000000a
sokf_type_ladder           = 0x000000000000000b
sokf_type_barrier3d        = 0x000000000000000c
sokf_type_player_limiter   = 0x000000000000000d
sokf_type_mask             = 0x00000000000000FF
sokf_add_fire              = 0x0000000000000100
sokf_add_smoke             = 0x0000000000000200
sokf_add_light             = 0x0000000000000400
sokf_show_hit_point_bar    = 0x0000000000000800    
sokf_place_at_origin       = 0x0000000000001000
sokf_dynamic               = 0x0000000000002000
sokf_invisible             = 0x0000000000004000
sokf_destructible          = 0x0000000000008000
sokf_moveable              = 0x0000000000010000
sokf_face_player           = 0x0000000000020000
sokf_dynamic_physics       = 0x0000000000040000
sokf_missiles_not_attached = 0x0000000000080000 #works only for dynamic mission objects
sokf_enforce_shadows       = 0x0000000000100000
sokf_dont_move_agent_over  = 0x0000000000200000
sokf_handle_as_flora       = 0x0000000001000000
sokf_static_movement       = 0x0000000002000000


spbf_hit_points_mask       = 0x00000000000000FF
spbf_hit_points_bits       = 20
spbf_init_use_time_mask    = 0x00000000000000FF
spbf_use_time_bits         = 28

def spr_hit_points(x):
  return ((x & spbf_hit_points_mask) << spbf_hit_points_bits)

def get_spr_hit_points(y):
  return (y >> spbf_hit_points_bits) & spbf_hit_points_mask

def spr_use_time(x):
  return ((x & spbf_init_use_time_mask) << spbf_use_time_bits)

def get_spr_use_time(y):
  return (y >> spbf_use_time_bits) & spbf_init_use_time_mask

#Animation Mode

spanim_linear              = 0
spanim_loop_linear         = 4
