from headers.skills import num_skill_words
from headers.troops import level_bits, level_mask, num_weapon_proficiencies
from modules.troops import troops
from common import convert_to_identifier, replace_spaces
from module_processor import ModuleProcessor


def save_troops(file, troop):
  troop_len = len(troop)
  if troop_len == 11:
    troop[11:11] = [0, 0, 0, 0, 0]
  elif troop_len == 12:
    troop[12:12] = [0, 0, 0, 0]
  elif troop_len == 13:
    troop[13:13] = [0, 0, 0]
  elif troop_len == 14:
    troop[14:14] = [0, 0]
  elif troop_len == 15:
    troop[15:15] = [0]
  if (troop[4] > 0):
    pass
  troop_info = (
      convert_to_identifier(troop[0]),
      replace_spaces(troop[1]),
      replace_spaces(troop[2]),
      replace_spaces(str(troop[13])),
      troop[3],
      troop[4],
      troop[5],
      troop[6],
      troop[14],
      troop[15]
  )
  file.write("\ntrp_%s %s %s %s %d %d %d %d %d %d\n  " % troop_info)
  inventory_list = troop[7]
  for inventory_item in inventory_list:
    file.write("%d 0 " % inventory_item)
  for i in range(64 - len(inventory_list)):
    file.write("-1 0 ")
  file.write("\n ")
  attrib = troop[8]
  strength = (attrib & 0xff)
  agility = ((attrib >> 8) & 0xff)
  intelligence = ((attrib >> 16) & 0xff)
  charisma = ((attrib >> 24) & 0xff)
  starting_level = (attrib >> level_bits) & level_mask

  file.write(" %d %d %d %d %d\n" % (strength, agility, intelligence, charisma, starting_level))
  wp_word = troop[9]
  for wp in range(num_weapon_proficiencies):
    wp_level = wp_word & 0x3FF
    file.write(" %d" % wp_level)
    wp_word = wp_word >> 10
  file.write("\n")

  skill_array = troop[10]
  for i in range(num_skill_words):
    file.write("%d " % ((skill_array >> (i * 32)) & 0xffffffff))
  file.write("\n  ")

  face_keys = [troop[11], troop[12]]

  for fckey in (face_keys):
    word_keys = []
    for word_no in range(4):
      word_keys.append((fckey >> (64 * word_no)) & 0xFFFFFFFFFFFFFFFF)
    for word_no in range(4):
      file.write("%d " % (word_keys[(4 - 1) - word_no]))

  file.write("\n")


class TroopProcessor(ModuleProcessor):
  id_prefix = "trp_"
  id_name = "troops.py"
  export_name = "troops.txt"

  def after_open_export_file(self):
    self.export_file.write("troopsfile version 2\n")
    self.export_file.write("%d " % len(troops))

  def write_export_file(self, troop):
    save_troops(self.export_file, troop)


def process_troops():
  print("exporting troops...")
  processor = TroopProcessor()
  for index, troop in enumerate(troops):
    processor.write(troop, index)
  processor.close()
