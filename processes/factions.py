from functools import reduce
from modules.factions import factions
from common import convert_to_identifier, replace_spaces, lf_open
from io_processor import ModuleProcessor

faction_name_pos = 0
faction_flags_pos = 2
faction_coherence_pos = 3
faction_relations_pos = 4
faction_ranks_pos = 5


def get_faction_relations(faction, faction_names):
    relations = faction[faction_relations_pos]
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

    if (len(faction) > faction_ranks_pos):
        ranks = faction[faction_ranks_pos]
        ranks_string = reduce(ranks_reducer, ranks, "")
        file.write("%d %s\n" % (len(ranks), ranks_string))
    else:
        file.write("0 \n")


class FactionProcessor(ModuleProcessor):
    id_name = "factions.py"
    export_name = "factions.txt"

    def after_open_export_file(self):
        self.export_file.write("factionsfile version 1\n")
        self.export_file.write("%d\n" % len(factions))

    def write_id_file(self, faction, index):
        self.id_file.write("fac_%s = %d\n" % (faction[0], index))

    def write_export_file(self, faction, faction_names):
        save_factions(self.export_file, faction, faction_names)

    def before_close_id_file(self):
        self.id_file.write("\n\n")


def process_factions():
    print("Exporting factions...")
    processor = FactionProcessor()
    faction_names = [faction[0] for faction in factions]
    for (index, faction) in enumerate(factions):
        processor.write(faction, index, faction_names)
    processor.close()
