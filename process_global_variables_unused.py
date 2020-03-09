from module_info import export_dir
from process_operations import load_variables


print("Checking global variable usages...")
variable_uses = []
variables = load_variables(export_dir, variable_uses)
i = 0
while (i < len(variables)):
    if (variable_uses[i] == 0):
        print("WARNING: Global variable never used: " + variables[i])
    i = i + 1
