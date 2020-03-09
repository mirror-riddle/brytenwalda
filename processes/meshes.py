# import string

# from headers.common import *
from modules.info import export_dir
from modules.meshes import meshes

from common import replace_spaces, lf_open


def save_meshes():
    ofile = open(export_dir + "meshes.txt", "w")
    ofile.write("%d\n" % len(meshes))
    for i_mesh in range(len(meshes)):
        mesh = meshes[i_mesh]
        ofile.write("mesh_%s %d %s %f %f %f %f %f %f %f %f %f\n" % (mesh[0], mesh[1], replace_spaces(
            mesh[2]), mesh[3], mesh[4], mesh[5], mesh[6], mesh[7], mesh[8], mesh[9], mesh[10], mesh[11]))
    ofile.close()


def save_python_header():
    ofile = lf_open("../ids/meshes.py", "w")
    for i_mesh in range(len(meshes)):
        ofile.write("mesh_%s = %d\n" % (meshes[i_mesh][0], i_mesh))
    ofile.write("\n\n")
    ofile.close()


print("Exporting meshes...")
save_python_header()
save_meshes()
