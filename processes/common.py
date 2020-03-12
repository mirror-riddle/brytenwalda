from pathlib import Path
from modules.info import export_dir
from headers.common import tags_end
from headers.operations import (
    try_begin,
    try_end,
    try_for_range,
    try_for_range_backwards,
    try_for_parties,
    try_for_agents,
    try_for_attached_parties,
    try_for_active_players,
    try_for_prop_instances,

    call_script,

    store_script_param,
    store_script_param_1,
    store_script_param_2,

    can_fail_operations
)

try_operations = (
    try_begin,
    try_for_range,
    try_for_range_backwards,
    try_for_parties,
    try_for_agents,
    try_for_attached_parties,
    try_for_active_players,
    try_for_prop_instances
)


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


def save_statement_block(
    ofile, statement_name, can_fail_statement, statements, variable_list, variable_uses, quick_strings
):
    local_vars = []
    local_var_uses = []
    ofile.write("%d " % len(statements))
    store_script_param_1_uses = 0
    store_script_param_2_uses = 0
    current_depth = 0
    can_fail = 0
    for index, statement in enumerate(statements):
        if isinstance(statement, list) or isinstance(statement, tuple):
            opcode = statement[0]
            no_variables = 0
        else:
            opcode = statement
            no_variables = 1
        if (opcode in try_operations):
            current_depth += 1
        elif (opcode == try_end):
            current_depth -= 1
        elif (opcode == store_script_param_1 or (opcode == store_script_param and statement[2] == 1)):
            store_script_param_1_uses += 1
        elif (opcode == store_script_param_2 or (opcode == store_script_param and statement[2] == 2)):
            store_script_param_2_uses += 1
        elif (can_fail_statement == 0 and current_depth == 0 and (opcode in can_fail_operations or (
                (opcode == call_script) and (statement[1].startswith("cf_", 7))
            )) and ( not statement_name.startswith("cf_"))):
            print("WARNING: Script can fail at operation #%d. Use cf_ at the beginning of its name: %s"
                %(index, statement_name)
            )
        save_statement(ofile, opcode, no_variables, statement, variable_list,
                       variable_uses, local_vars, local_var_uses, [], quick_strings)
    if (store_script_param_1_uses > 1):
        print("WARNING: store_script_param_1 is used more than once:" + statement_name)
    if (store_script_param_2_uses > 1):
        print("WARNING: store_script_param_2 is used more than once:" + statement_name)
    i = 0
    while (i < len(local_vars)):
        if (local_var_uses[i] == 0 and not(local_vars[i].startswith("unused"))):
            print("WARNING: Local variable never used: " + local_vars[i] + ", at: " + str(statement_name))
        i = i + 1
    if (len(local_vars) > 128):
        print("WARNING: Script uses more than 128 local wariables: " +
              str(statement_name) + "variables count:" + str(len(local_vars)))


def save_simple_triggers(ofile, triggers, variable_list, variable_uses, quick_strings):
    ofile.write("%d\n" % len(triggers))
    for trigger in triggers:
        ofile.write("%f " % (trigger[0]))
        save_statement_block(ofile, 0, 1, trigger[1], variable_list, variable_uses, quick_strings)
        ofile.write("\n")
