from modules.animations import animations
from common import lf_open
from io_processor import ModuleProcessor


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


class AnimationProcessor(ModuleProcessor):
    id_name = "animations.py"
    export_name = "actions.txt"

    def after_open_export_file(self):
        self.export_file.write("%d\n" % len(animations))
    
    def write_id_file(self, animation, index):
        self.id_file.write("anim_%s = %d\n" % (animation[0], index))

    def write_export_file(self, animation):
        write_actions_file(self.export_file, animation)

    def before_close_id_file(self):
        self.id_file.write("\n\n")


def process_animations():
    print("Exporting animations...") 
    processor = AnimationProcessor()
    for (index, animation) in enumerate(animations):
        processor.write(animation, index)
    processor.close()