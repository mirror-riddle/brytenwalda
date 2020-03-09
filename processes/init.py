import os

from modules.info import export_dir
from processes.common import save_variables, is_file_exist, read_variables


def remove_file(file):
    if is_file_exist(file):
        os.remove(file)
    else:
        print(file, 'not exist !')


def retrieve_variables(file):
    variables = []
    variable_uses = []
    var_list = read_variables(file)
    for var in var_list:
        striped_var = var.strip()
        if striped_var:
            variables.append(striped_var)
            variable_uses.append(1)
    return (variables, variable_uses)


def process_init():
    print("Initializing...")

    files = ['tag_uses.txt', 'quick_strings.txt', 'variables.txt', 'variable_uses.txt']
    [remove_file(export_dir + file) for file in files]

    variables_file = 'variables.txt'
    if is_file_exist(variables_file):
        save_variables(*retrieve_variables(variables_file))
    else:
        print("variables.txt not found. Creating new variables.txt file")
