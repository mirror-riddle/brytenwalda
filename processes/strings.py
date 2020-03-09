# import string

# from headers.common import *
from modules.info import export_dir
from modules.strings import strings

from common import convert_to_identifier, replace_spaces, lf_open


def save_strings(strings):
    ofile = open(export_dir + "strings.txt", "w", -1, "utf-8")
    ofile.write("stringsfile version 1\n")
    ofile.write("%d\n" % len(strings))
    for i_string in range(len(strings)):
        str = strings[i_string]
        ofile.write("str_%s %s\n" % (convert_to_identifier(str[0]), replace_spaces(str[1])))
    ofile.close()


def save_python_header():
    ofile = lf_open("../ids/strings.py", "w")
    for i_string in range(len(strings)):
        ofile.write("str_%s = %d\n" % (convert_to_identifier(strings[i_string][0]), i_string))
    ofile.write("\n\n")
    ofile.close()


print("Exporting strings...")
save_python_header()
save_strings(strings)
