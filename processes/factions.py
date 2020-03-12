from functools import reduce
from modules.info import export_dir
from modules.factions import factions
from common import convert_to_identifier, replace_spaces, lf_open
from io_processor import IOProcessor

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


def save_factions(file, faction, i_faction, faction_names):
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
        file.write("%d %s" % (len(ranks), ranks_string))
    else:
        file.write("0 ")

    file.write("\n")


class IOFactions(IOProcessor):

    def after_open(self):
        self.file.write("factionsfile version 1\n")
        self.file.write("%d\n" % len(factions))

    def write(self, relations, faction, index):
        save_factions(self.file, relations, faction, index)


class IOIDs(IOProcessor):

    def write(self, id, index):
        self.file.write("fac_%s = %d\n" % (id, index))

    def before_close(self):
        self.file.write("\n\n")


def process_factions():
    print("Exporting factions...")

    faction_names = [faction[0] for faction in factions]
    io_ids = IOIDs("../ids/factions.py")
    io_factions = IOFactions(export_dir + "factions.txt")

    for (index, faction) in enumerate(factions):
        io_ids.write(faction[0], index)
        io_factions.write(faction, index, faction_names)

    io_ids.close()
    io_factions.close()
