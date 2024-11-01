from axelrod import Cooperator, Defector, TitForTat, Grudger, TitFor2Tats, FirstByDavis, FirstByDowning, FirstByJoss, FirstByNydegger, FirstByShubik, FirstBySteinAndRapoport, FirstByTidemanAndChieruzzi, SecondByBorufsen, SecondByColbert, SecondByGladstein, SecondByGraaskampKatzen, SecondByGrofman, SecondByMikkelson, SecondByRichardHufford, SecondByRowsam, SecondByTester, SecondByTidemanAndChieruzzi, SecondByWeiner, SecondByWhite, SecondByYamachi, FirstByAnonymous
from ecological import evolutive_tournament
from evolutive_strat import Evo
from results_texter import information_text
import copy
import random

stratlist = [
    FirstByAnonymous(),
    Defector(),
    TitForTat(),
    Grudger(),
    TitFor2Tats(),
    FirstByDavis(),
    FirstByDowning(),
    FirstByJoss(),
    FirstByNydegger(),
    FirstByShubik(),
    FirstBySteinAndRapoport(),
    FirstByTidemanAndChieruzzi(),
    SecondByBorufsen(),
    SecondByColbert(),
    SecondByGladstein(),
    SecondByGraaskampKatzen(),
    SecondByGrofman(),
    SecondByMikkelson(),
    SecondByRichardHufford(),
    SecondByRowsam(),
    SecondByTester(),
    SecondByTidemanAndChieruzzi(),
    SecondByWeiner(),
    SecondByWhite(),
    SecondByYamachi()
]

weightlist = []
# Pour donner à chaque joueur le même poid à toutes les strats
for _ in stratlist :
    weightlist.append(1)  

playerlist = [
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy()),
    Evo(stratlist
        ,weightlist.copy())
    ]

# Pour que chaque joueur n'ait initialement qu'une strat disponible (différente pour chaque joueur)
"""
for i in playerlist:
    for _ in stratlist :
        if len(i.weights) == playerlist.index(i) :
            i.weights.append(1)
        elif (len(stratlist) != len(playerlist)) and (playerlist.index(i) > len(stratlist)) and(len(i.weights) == 0):
            i.weights.append(1)
        else :
            i.weights.append(0)
    print(i.weights)
"""
saved_players = copy.deepcopy(playerlist)

# Types possibles sont "Axelrod", "Remplacement_non_muté", "Remplacement_muté", "Moyenne", et "Héritage."
TOURNAMENT_TYPE = "Remplacement_muté"

random_seed = None

random.seed(random_seed)

evolutive_tournament(playerlist, 1, TOURNAMENT_TYPE)

information_text(TOURNAMENT_TYPE, 1, saved_players, playerlist, seed=random_seed)
print("OK")
