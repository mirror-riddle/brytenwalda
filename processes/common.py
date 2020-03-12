from pathlib import Path
from headers.common import tags_end
from modules.info import export_dir


def convert_to_identifier_with_no_lowercase(s0):
    s1 = s0.replace(" ", "_")
    s2 = s1.replace("'", "_")
    s3 = s2.replace("`", "_")
    s4 = s3.replace("(", "_")
    s5 = s4.replace(")", "_")
    s6 = s5.replace("-", "_")
    s7 = s6.replace(",", "")
    s8 = s7.replace("|", "")
    s9 = s8.replace("\t", "_")  # Tab
    return s9


def convert_to_identifier(s0):
    s1 = convert_to_identifier_with_no_lowercase(s0)
    return s1.lower()


def replace_spaces(s0):
    s1 = s0.replace("\t", "_")
    return s1.replace(" ", "_")


def lf_open(file, mode):
    return open(file, mode, -1, "utf-8", None, '\n')


def is_file_exist(file):
    return Path(file).is_file()


def read_variables(file):
    with open(file, "r") as file:
        var_list = file.readlines()
    return var_list


def retrieve_variables(file, is_variables_use=False):
    if not is_file_exist(file):
        print(file, "not found. Creating new variables.txt file")
        return []

    variables = []
    var_list = read_variables(file)
    for var in var_list:
        striped_var = var.strip()
        if striped_var:
            var = int(striped_var) if is_variables_use else striped_var
            variables.append(var)
    return variables


def load_variables(variable_uses):
    variables_file = export_dir + "variables.txt"
    variables = retrieve_variables(variables_file)

    variable_uses_file = export_dir + "variable_uses.txt"
    variable_uses += retrieve_variables(variable_uses_file, True)

    return variables


def save_varbs(varbs, file):
    with open(export_dir + file, "w") as file:
        [file.write("%s\n" % varb) for varb in varbs]


def save_variables(variables, variable_uses):
    save_varbs(variables, "variables.txt")
    save_varbs(variable_uses, "variable_uses.txt")


def load_tag_uses():
    tag_uses = [ [] ] * tags_end
    # for i in range(tags_end):
    #     sub_tag_uses = []
    #     tag_uses.append(sub_tag_uses)

    try:
        file = open(export_dir + "tag_uses.txt", "r")
        var_list = file.readlines()
        file.close()
        for v in var_list:
            vv = v.strip().split(';')
            if vv:
                for v2 in vv:
                    vvv = v2.split(' ')
                    if len(vvv) >= 3:
                        ensure_tag_use(tag_uses, int(vvv[0]), int(vvv[1]))
                        tag_uses[int(vvv[0])][int(vvv[1])] = int(vvv[2])
    except:
        print("Creating new tag_uses.txt file...")
    return tag_uses
