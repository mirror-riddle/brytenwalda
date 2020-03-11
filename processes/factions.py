from modules.info import export_dir
from modules.factions import factions
from common import convert_to_identifier, replace_spaces, lf_open
from io_processor import IOProcessor

faction_name_pos = 0
faction_flags_pos = 2
faction_coherence_pos = 3
faction_relations_pos = 4
faction_ranks_pos = 5


def compile_relations():
    relations = [[0.0] * len(factions) for faction in factions]
    for (i_faction, faction) in enumerate(factions):
        relations[i_faction][i_faction] = faction[faction_coherence_pos]
        rels = factions[i_faction][faction_relations_pos]
        for rel in rels:
            rel_name = rel[0]
            other_pos = -1
            for j_f in range(len(factions)):
                if factions[j_f][faction_name_pos] == rel_name:
                    other_pos = j_f
            if other_pos == -1:
                print("ERROR faction not found: " + rel_name)
            else:
                relations[other_pos][i_faction] = rel[1]
                relations[i_faction][other_pos] = rel[1]
    return relations


def save_factions(file, relations, faction, i_faction):
    identifier = convert_to_identifier(faction[0])
    dashed_name = replace_spaces(faction[1])
    fac_color = faction[6] if len(faction) == 7 else 0xAAAAAA

    file.write("fac_%s %s %d %d \n" % (identifier, dashed_name, faction[2], fac_color))
    
    for reln in relations[i_faction]:
        file.write(" %f " % reln)
    file.write("\n")
    
    ranks = []
    if (len(faction) > faction_ranks_pos):
        ranks = faction[faction_ranks_pos]
    
    file.write("%d " % (len(ranks)))
    
    for rank in ranks:
        dashed_rank = replace_spaces(rank)
        file.write(" %s " % dashed_rank)


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

    relations = compile_relations()
    io_ids = IOIDs("../ids/factions.py")
    io_factions = IOFactions(export_dir + "factions.txt")
    
    for (index, faction) in enumerate(factions):
        io_ids.write(faction[0], index)
        io_factions.write(relations, faction, index)

    io_ids.close()   
    io_factions.close() 
