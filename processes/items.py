from functools import reduce
from modules.info import export_dir
from modules.items import items, get_item_status
from module_processor import ModuleProcessor
from operations import save_quick_strings, save_simple_triggers, load_quick_strings
from common import (
    convert_to_identifier, lf_open, load_variables, replace_spaces, save_variables
)


def variations_reducer(base, variation):
    variation_string = ("%s %d " % (variation[0], variation[1]))
    return ("%s%s" % (base, variation_string))


def factions_reducer(base, faction):
    return ("%s%d " % (base, faction))


def write_items(ofile, item):
    identity = convert_to_identifier(item[0])
    name = replace_spaces(item[1])
    status = get_item_status(item)
    variations_info = reduce(variations_reducer, item[2], "")
    info = (item[3], item[4], item[5], item[7]) + status
    ofile.write("itm_%s %s %s %d %s " % (identity, name, name, len(item[2]), variations_info))
    ofile.write("%d %d %d %d %f %d %d %d %d %d %d %d %d %d %d %d %d\n" % info)
    if (len(item) > 9):
        factions_info = reduce(factions_reducer, item[9], "")
        ofile.write("%d \n%s \n" % (len(item[9]), factions_info))
    else:
        ofile.write("0 \n")


class ItemProcessor(ModuleProcessor):
    id_prefix = "itm_"
    id_name = "items.py"
    export_name = "item_kinds1.txt"

    def after_open_export_file(self):
        self.export_file.write("itemsfile version 3\n")
        self.export_file.write("%d\n" % len(items))

    def write_export_file(self, item):
        write_items(self.export_file, item)

    def write_triggers(self, item, variables, variable_uses, quick_strings):
        if (len(item) > 8):
            save_simple_triggers(
                self.export_file, item[8], variables, variable_uses, [], quick_strings
            )


def process_items():
    print("Exporting item...")
    variable_uses = []
    variables = load_variables(variable_uses)
    quick_strings = load_quick_strings(export_dir)

    processor = ItemProcessor()
    for index, item in enumerate(items):
        processor.write(item, index)
        processor.write_triggers(item, variables, variable_uses, quick_strings)
    processor.close()

    save_variables(variables, variable_uses)
    save_quick_strings(export_dir, quick_strings)
