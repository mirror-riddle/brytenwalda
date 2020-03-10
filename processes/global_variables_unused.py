from modules.info import export_dir
from processes.common import load_variables


def process_global_variables_unused():
    print("Checking global variable usages...")
    variable_uses = []
    variables = load_variables(variable_uses)
    for index, variable in enumerate(variables):
        if (variable_uses[index] == 0):
            print("WARNING: Global variable never used: ", variable)
