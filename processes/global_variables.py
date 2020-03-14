from common import retrieve_lines, save_variables, save_quick_strings


# global variables init
quick_strings = []
variables = retrieve_lines("variables.txt")
variable_uses = [1] * len(variables)


def save_global_variables():
  save_quick_strings(quick_strings)
  save_variables(variables, variable_uses)