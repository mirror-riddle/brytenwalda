import re
from inspect import isfunction
from pathlib import Path
from modules.info import export_dir
from headers.common import tags_end


def convert_to_identifier_with_no_lowercase(s0):
  s1 = re.sub(r"[ '`()-]", "_", s0)
  s2 = re.sub(r"[,|]", '', s1)
  return s2


def convert_to_identifier(s0):
  s1 = convert_to_identifier_with_no_lowercase(s0)
  return s1.lower()


def replace_spaces(s0):
  return re.sub(r" ", "_", s0)


def lf_open(file, mode):
  return open(file, mode, -1, "utf-8", None, '\n')


def is_file_exist(file):
  return Path(file).is_file()


def read_lines(path):
  if not is_file_exist(path):
    print(path, "not found :(")
    return []

  with open(path, "r") as f:
    lines = f.readlines()
  return lines


def retrieve_lines(file, transformer=None):
  lines = read_lines(file)
  solid_lines = []
  for line in lines:
    striped_line = line.strip()
    if striped_line:
      solid_lines.append(striped_line)
  if isfunction(transformer):
    return [*map(transformer, solid_lines)]
  else:
    return solid_lines


def load_variables():
  variables = retrieve_lines(export_dir + "variables.txt")
  variable_uses = retrieve_lines(export_dir + "variable_uses.txt", lambda x: int(x))
  return (variables, variable_uses)


def save_varbs(varbs, file):
  with open(export_dir + file, "w") as f:
    for varb in varbs:
      f.write("%s\n" % varb)


def save_variables(variables, variable_uses):
  save_varbs(variables, "variables.txt")
  save_varbs(variable_uses, "variable_uses.txt")


def load_quick_strings():
  lines = retrieve_lines(export_dir + "quick_strings.txt", lambda x: x.split(" "))
  quick_strings = filter(lambda x: len(x) == 2, lines)
  return [*quick_strings]


def save_quick_strings(quick_strings):
  with open(export_dir + "quick_strings.txt", "w") as file:
    file.write("%d\n" % len(quick_strings))
    for string in quick_strings:
      content = replace_spaces(string[1])
      file.write("%s %s\n" % (string[0], content))
