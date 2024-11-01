from axelrod import Cooperator, Defector, TitForTat, Grudger
from ecological import evolutive_tournament
from evolutive_strat import Evo
from results_texter import information_text
import copy
import random

stratlist = [
    Cooperator(),
    Defector(),
    TitForTat(),
    Grudger(),
]

weightlist = []

playerlist = [
    Evo(stratlist
        ,[1,0,0,0],
        "Cooperator"),
    Evo(stratlist
        ,[0,1,0,0],
        "Defector"),
    Evo(stratlist
        ,[0,0,1,0],
        "TitForTat"),
    Evo(stratlist
        ,[0,0,0,1],
        "Grudger")
    ]

print("playerlist", playerlist)

saved_players = copy.deepcopy(playerlist)

# Types possibles sont "Axelrod", "Remplacement_non_muté", "Remplacement_muté", "Moyenne", et "Héritage."
TOURNAMENT_TYPE = "Axelrod"

random_seed = None

random.seed(random_seed)

evolutive_tournament(playerlist, 4, TOURNAMENT_TYPE)

information_text(TOURNAMENT_TYPE, 2, saved_players, playerlist, seed=random_seed, special_notes="Type 'Axelrod' modifié. Utilise les scores normés à la place des scores.\nles scores normés correspondent aux scores divisés par le nombre d'adversaires\net de tours joués.")
print("OK")
