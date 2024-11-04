from axelrod import TitForTat, Grudger, TitFor2Tats, FirstByDavis, FirstByDowning, FirstByNydegger, FirstByShubik, FirstBySteinAndRapoport, FirstByTidemanAndChieruzzi, SecondByBorufsen, SecondByColbert, SecondByGraaskampKatzen, SecondByGrofman, SecondByMikkelson, SecondByRichardHufford, SecondByRowsam, SecondByTester, SecondByTidemanAndChieruzzi, SecondByWeiner, SecondByWhite, FirstByAnonymous, FirstByFeld, FirstByGraaskamp, FirstByTullock, Random, FirstByGrofman, FirstByJoss, SecondByHarrington, SecondByChampion, SecondByCave, SecondByWmAdams, SecondByLeyvraz, SecondByBlack, SecondByEatherley, SecondByGetzler, SecondByKluepfel
from ecological import evolutive_tournament
from evolutive_strat import Evo
from results_texter import information_text
import copy
import random

stratlist = [
    # les 24 premières sont NICE
    TitForTat(),
    FirstByNydegger(),
    FirstByGrofman(),
    FirstByShubik(),
    FirstBySteinAndRapoport(),
    Grudger(),
    FirstByDavis(),
    SecondByGrofman(),
    SecondByTidemanAndChieruzzi(),
    SecondByGraaskampKatzen(),
    SecondByWeiner(),
    TitFor2Tats(),
    SecondByRowsam(),
    SecondByMikkelson(),
    SecondByBorufsen(),
    SecondByWhite(),
    
    SecondByChampion(),
    SecondByWmAdams(),
    SecondByCave(),
    SecondByKluepfel(),
    SecondByGetzler(),
    SecondByLeyvraz(),
    SecondByEatherley(),
    SecondByBlack(),
    
    # Les 12 dernières sont NASTY
    
    FirstByTidemanAndChieruzzi(),
    FirstByGraaskamp(),
    FirstByDowning(),
    FirstByFeld(),
    FirstByJoss(),
    FirstByTullock(),
    FirstByAnonymous(),
    Random(),
    SecondByColbert(),
    SecondByTester(),
    SecondByRichardHufford(),
    SecondByHarrington()


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

random.seed(6)

evolutive_tournament(playerlist, 248, TOURNAMENT_TYPE)

information_text(TOURNAMENT_TYPE, 6, saved_players, playerlist, seed=random_seed)
print("OK")
