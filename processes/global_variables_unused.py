from global_variables import variables, variable_uses

def process_global_variables_unused():
    print("Checking global variable usages...")
    for index, variable in enumerate(variables):
        if (variable_uses[index] == 0):
            print("WARNING: Global variable never used: ", variable)
