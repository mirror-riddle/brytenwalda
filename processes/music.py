from modules.music import tracks
from module_processor import ModuleProcessor


def save_track(file, track):
  file.write("%s %d %d\n" % (track[1], track[2], (track[2] | track[3])))


class MusicProcessor(ModuleProcessor):
  id_prefix = "track_"
  id_name = "music.py"
  export_name = "music.txt"

  def after_open_export_file(self):
    self.export_file.write("%d\n" % len(tracks))

  def write_export_file(self, track):
    save_track(self.export_file, track)


def process_musics():
  print("exporting tracks...")
  processor = MusicProcessor()
  for index, track in enumerate(tracks):
    processor.write(track, index)
  processor.close()