from modules.info import export_dir
from modules.animations import animations
from common import lf_open
from io_processor import IOProcessor


def write_actions_file(file, action):
    file.write(" %s %d %d " % (action[0], action[1], action[2]))
    file.write(" %d\n" % (len(action) - 3))
    for elem in action[3:]:
        file.write("  %f %s %d %d %d " % (elem[0], elem[1], elem[2], elem[3], elem[4]))
        if (len(elem) > 5):
            file.write("%d " % elem[5])
        else:
            file.write("0 ")
        if (len(elem) > 6):
            file.write("%f %f %f  " % elem[6])
        else:
            file.write("0.0 0.0 0.0 ")
        if (len(elem) > 7):
            file.write("%f \n" % (elem[7]))
        else:
            file.write("0.0 \n")


class AnimationIOIDs(IOProcessor):
    
    def write(self, name, index):
        self.file.write("anim_%s = %d\n" % (name, index))

    def before_close(self):
        self.file.write("\n\n")


class AnimationIOActions(IOProcessor):

    def after_open(self):
        self.file.write("%d\n" % len(animations))

    def write(self, action):
        write_actions_file(self.file, action)


def process_animations():
    print("Exporting animations...")
    
    io_ids = AnimationIOIDs("../ids/animations.py")
    io_actions = AnimationIOActions(export_dir + "actions.txt")
    
    for (index, animation) in enumerate(animations):
        io_ids.write(animation[0], index)
        io_actions.write(animation)
    
    io_ids.close()
    io_actions.close()
