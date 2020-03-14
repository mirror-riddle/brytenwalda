from modules.sounds import sounds
from module_processor import ModuleProcessor


def compile_sounds(sounds):
  all_sounds = []
  for sound in sounds:
    sound_files = sound[2]
    sound_flags = sound[1]
    for i_sound_file in range(len(sound_files)):
      sound_file = sound_files[i_sound_file]
      if (type(sound_file) != type([])):
        sound_file = [sound_file, 0]
      sound_no = 0
      found = 0
      while (sound_no < (len(all_sounds))) and (not found):
        if all_sounds[sound_no][0] == sound_file[0]:
          found = 1
        else:
          sound_no += 1
      if not found:
        all_sounds.append((sound_file[0], sound_flags))
        sound_no = len(all_sounds) - 1
      sound_files[i_sound_file] = [sound_no, sound_file[1]]
  return all_sounds


def save_sound(ofile, sound):
  ofile.write("snd_%s %d %d " % (sound[0], sound[1], len(sound[2])))
  sample_list = sound[2]
  for s in sample_list:
    ofile.write("%d %d " % (s[0], s[1]))
  ofile.write("\n")


class SoundProcessor(ModuleProcessor):
  id_prefix = "snd_"
  id_name = "sounds.py"
  export_name = "sounds.txt"

  def after_open_export_file(self):
    self.export_file.write("soundsfile version 3\n")

  def write_export_file(self, sound):
    save_sound(self.export_file, sound)

  def write_sound_samples(self, sound_samples):
    self.export_file.write("%d\n" % len(sound_samples))
    for sound_sample in sound_samples:
      self.export_file.write(" %s %d\n" % sound_sample)
    self.export_file.write("%d\n" % len(sounds))


def process_sounds():
  print("exporting sounds...")
  processor = SoundProcessor()
  sound_samples = compile_sounds(sounds)
  processor.write_sound_samples(sound_samples)
  for index, sound in enumerate(sounds):
    processor.write(sound, index)
  processor.close()
