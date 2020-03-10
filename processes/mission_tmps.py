from modules.info import export_dir
from modules.mission_templates import mission_templates
from operations import *
from common import convert_to_identifier, lf_open

mission_template_name_pos = 0
mission_template_flags_pos = 1
mission_template_types_pos = 2
mission_template_desc_pos = 3
mission_template_groups_pos = 4
mission_template_triggers_pos = 5


def save_triggers(file, template_name, triggers, variable_list, variable_uses, tag_uses, quick_strings):
    file.write("%d\n" % len(triggers))
    for i in range(len(triggers)):
        trigger = triggers[i]
        file.write("%f %f %f " % (trigger[trigger_check_pos], trigger[trigger_delay_pos], trigger[trigger_rearm_pos]))
        save_statement_block(file, 0, 1, trigger[trigger_conditions_pos],
                             variable_list, variable_uses, tag_uses, quick_strings)
        save_statement_block(file, 0, 1, trigger[trigger_consequences_pos],
                             variable_list, variable_uses, tag_uses, quick_strings)
        file.write("\n")
    file.write("\n")


def save_mission_template_group(file, entry, tag_uses):
    if (len(entry[5]) > 8):
        print("ERROR: Too many item_overrides!")
    file.write("%d %d %d %d %d %d  " % (entry[0], entry[1], entry[2], entry[3], entry[4], len(entry[5])))
    for item_override in entry[5]:
        add_tag_use(tag_uses, tag_item, item_override)
        file.write("%d " % (item_override))
    file.write("\n")


def save_mission_templates(variables, variable_uses, tag_uses, quick_strings):
    file = open(export_dir + "mission_templates.txt", "w")
    file.write("missionsfile version 1\n")
    file.write(" %d\n" % (len(mission_templates)))
    for mission_template in mission_templates:
        file.write("mst_%s %s %d " % (
            convert_to_identifier(mission_template[mission_template_name_pos]), 
            convert_to_identifier(mission_template[mission_template_name_pos]),
            mission_template[mission_template_flags_pos]
        ))
        file.write(" %d\n" % (mission_template[mission_template_types_pos]))
        file.write("%s \n" % (mission_template[mission_template_desc_pos].replace(" ", "_")))
        file.write("\n%d " % len(mission_template[mission_template_groups_pos]))
        for group in mission_template[mission_template_groups_pos]:
            save_mission_template_group(file, group, tag_uses)
        save_triggers(file, 
            convert_to_identifier(mission_template[mission_template_name_pos]),
            mission_template[mission_template_triggers_pos], 
            variables, variable_uses, tag_uses, quick_strings
        )
        file.write("\n")
    file.close()


def save_python_header():
    file = lf_open("../ids/mission_templates.py", "w")
    for i_mission_template in range(len(mission_templates)):
        file.write("mst_%s = %d\n" % (mission_templates[i_mission_template][0], i_mission_template))
    file.close()


def process_mission_tmps():
    print("Exporting mission_template data...")
    save_python_header()
    variable_uses = []
    variables = load_variables(export_dir, variable_uses)
    tag_uses = load_tag_uses(export_dir)
    quick_strings = load_quick_strings(export_dir)
    save_mission_templates(variables, variable_uses, tag_uses, quick_strings)
    save_variables(export_dir, variables, variable_uses)
    save_tag_uses(export_dir, tag_uses)
    save_quick_strings(export_dir, quick_strings)
