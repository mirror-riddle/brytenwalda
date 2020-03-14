from functools import reduce
from modules.factions import factions
from common import convert_to_identifier, replace_spaces
from module_processor import ModuleProcessor


def get_faction_relations(faction, faction_names):
    relations = faction[4]
    faction_relations = [0.0] * len(faction_names)
    for relation in relations:
        try:
            index = faction_names.index(relation[0])
            faction_relations[index] = relation[1]
        except ValueError:
            print("ERROR faction not found: " + relation[0])
    return faction_relations


def relations_reducer(x, y):
    return "%s%f " % (x, y)


def ranks_reducer(x, y):
    return ("%s%s " % (x, replace_spaces(y)))


def save_factions(file, faction, faction_names):
    identifier = convert_to_identifier(faction[0])
    dashed_name = replace_spaces(faction[1])
    fac_color = faction[6] if len(faction) == 7 else 0xAAAAAA

    file.write("fac_%s %s %d %d \n" % (identifier, dashed_name, faction[2], fac_color))

    relations = get_faction_relations(faction, faction_names)
    relations_string = reduce(relations_reducer, relations, "")
    file.write(relations_string + "\n")

    if (len(faction) > 5):
        ranks = faction[5]
        ranks_string = reduce(ranks_reducer, ranks, "")
        file.write("%d %s\n" % (len(ranks), ranks_string))
    else:
        file.write("0 \n")


class FactionProcessor(ModuleProcessor):
    id_prefix = "fac_"
    id_name = "factions.py"
    export_name = "factions.txt"

    def after_open_export_file(self):
        self.export_file.write("factionsfile version 1\n")
        self.export_file.write("%d\n" % len(factions))

    def write_export_file(self, faction, faction_names):
        save_factions(self.export_file, faction, faction_names)


def process_factions():
    print("exporting factions...")
    processor = FactionProcessor()
    faction_names = [faction[0] for faction in factions]
    for index, faction in enumerate(factions):
        processor.write(faction, index, faction_names)
    processor.close()
