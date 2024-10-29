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
        ,[0.25,0.25,0.25,0.25],
        "Evo1"),
    Evo(stratlist
        ,[0.25,0.25,0.25,0.25],
        "Evo2"),
    Evo(stratlist
        ,[0.25,0.25,0.25,0.25],
        "Evo3"),
    Evo(stratlist
        ,[0.25,0.25,0.25,0.25],
        "Evo4")
    ]

print("playerlist", playerlist)

saved_players = copy.deepcopy(playerlist)

# Types possibles sont "Axelrod", "Remplacement_non_muté", "Remplacement_muté", "Moyenne", et "Héritage."
TOURNAMENT_TYPE = "Remplacement_muté"

random_seed = 10

random.seed(random_seed)

evolutive_tournament(playerlist, 200, TOURNAMENT_TYPE)

information_text(TOURNAMENT_TYPE, 2, saved_players, playerlist, seed=random_seed, special_notes="Tournoi créé dans l'unique but de vérifier la fonction écrivant ce fichier d'infos supplémentaires.")
print("OK")
