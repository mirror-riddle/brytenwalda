###################################################
# headers.strings.py
# This file contains declarations for strings
# DO NOT EDIT THIS FILE!
###################################################


def find_string(strings, string_id):
    result = -1
    num_strings = len(strings)
    i_string = 0
    while (i_string < num_strings) and (result == -1):
        str = strings[i_string]
        if (str[0] == string_id):
            result = i_string
        i_string += 1
    return result
