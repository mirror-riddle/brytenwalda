import os

from modules.info import export_dir
from processes.common import (
    save_variables, is_file_exist, retrieve_lines
)


def remove_file(file):
  if is_file_exist(file):
    os.remove(file)
  else:
    print(file, 'not exist !')


def process_init():
  print("Initializing...")

  files = ['tag_uses.txt', 'quick_strings.txt', 'variables.txt', 'variable_uses.txt']

  for file in files:
    remove_file(export_dir + file)

  variables_file = 'variables.txt'
  variables = retrieve_lines(variables_file)
  variable_uses = [1] * len(variables)
  print(variables[0], len(variables[0]))
  save_variables(variables, variable_uses)
