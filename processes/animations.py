from modules.info import export_dir
from modules.animations import animations
from common import lf_open


def init_actions_file():
    file = open(export_dir + "actions.txt", "w")
    file.write("%d\n" % len(animations))
    return file


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


def init_ids_file():
    file = lf_open("../ids/animations.py", "w")    
    return file


def write_ids_file(file, name, index):
    file.write("anim_%s = %d\n" % (name, index))


def close_ids_file(file):
    file.write("\n\n")
    file.close()


def process_animations():
    print("Exporting animations...")
    ids_file = init_ids_file()
    actions_file = init_actions_file()
    for (index, animation) in enumerate(animations):
        write_ids_file(ids_file, animation[0], index)
        write_actions_file(actions_file, animation)
    actions_file.close()
    close_ids_file(ids_file)
