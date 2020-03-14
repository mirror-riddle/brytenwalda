# This module should ONLY be imported by operations.py, because another import
# will execure initialization again.

from common import retrieve_lines


# global variables init
quick_strings = []
variables = retrieve_lines("variables.txt")
variable_uses = [1] * len(variables)
