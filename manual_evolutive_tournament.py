from axelrod import TitForTat, Grudger, TitFor2Tats, FirstByDavis, FirstByDowning, FirstByNydegger, FirstByShubik, FirstBySteinAndRapoport, FirstByTidemanAndChieruzzi, SecondByBorufsen, SecondByColbert, SecondByGraaskampKatzen, SecondByGrofman, SecondByMikkelson, SecondByRichardHufford, SecondByRowsam, SecondByTester, SecondByTidemanAndChieruzzi, SecondByWeiner, SecondByWhite, FirstByAnonymous, FirstByFeld, FirstByGraaskamp, FirstByTullock, Random, FirstByGrofman, FirstByJoss, SecondByHarrington, SecondByChampion, SecondByCave, SecondByWmAdams, SecondByLeyvraz, SecondByBlack, SecondByEatherley, SecondByGetzler, SecondByKluepfel, Cooperator
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
    
    #alwais cooperate
    #Cooperator(),
    
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
        ,weightlist.copy()
        ,"01"),
    Evo(stratlist
        ,weightlist.copy()
        ,"02"),
    Evo(stratlist
        ,weightlist.copy()
        ,"03"),
    Evo(stratlist
        ,weightlist.copy()
        ,"04"),
    Evo(stratlist
        ,weightlist.copy()
        ,"05"),
    Evo(stratlist
        ,weightlist.copy()
        ,"06"),
    Evo(stratlist
        ,weightlist.copy()
        ,"07"),
    Evo(stratlist
        ,weightlist.copy()
        ,"08"),
    Evo(stratlist
        ,weightlist.copy()
        ,"09"),
    Evo(stratlist
        ,weightlist.copy()
        ,"10"),
    Evo(stratlist
        ,weightlist.copy()
        ,"11"),
     Evo(stratlist
        ,weightlist.copy()
        ,"12"),
    Evo(stratlist
        ,weightlist.copy()
        ,"13"),
    Evo(stratlist
        ,weightlist.copy()
        ,"14"),
    Evo(stratlist
        ,weightlist.copy()
        ,"15"),
    Evo(stratlist
        ,weightlist.copy()
        ,"16"),
    Evo(stratlist
        ,weightlist.copy()
        ,"17"),
    Evo(stratlist
        ,weightlist.copy()
        ,"18"),
    Evo(stratlist
        ,weightlist.copy()
        ,"19"),
    Evo(stratlist
        ,weightlist.copy()
        ,"20"),
    Evo(stratlist
        ,weightlist.copy()
        ,"21"),
    Evo(stratlist
        ,weightlist.copy()
        ,"22"),
    Evo(stratlist
        ,weightlist.copy()
        ,"23"),
    Evo(stratlist
        ,weightlist.copy()
        ,"24"),
    Evo(stratlist
        ,weightlist.copy()
        ,"25"),
    Evo(stratlist
        ,weightlist.copy()
        ,"26"),
    Evo(stratlist
        ,weightlist.copy()
        ,"27"),
    Evo(stratlist
        ,weightlist.copy()
        ,"28"),
    Evo(stratlist
        ,weightlist.copy()
        ,"29"),
    Evo(stratlist
        ,weightlist.copy()
        ,"30"),
    Evo(stratlist
        ,weightlist.copy()
        ,"31"),
    Evo(stratlist
        ,weightlist.copy()
        ,"32"),
    Evo(stratlist
        ,weightlist.copy()
        ,"33"),
    Evo(stratlist
        ,weightlist.copy()
        ,"34"),
    Evo(stratlist
        ,weightlist.copy()
        ,"35"),
    #Evo(stratlist
    #    ,weightlist.copy()
    #    ,"05")
    Evo(stratlist
        ,weightlist.copy()
        ,"36")
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

# Types possibles sont "Axelrod", "Remplacement_non_muté", "Remplacement_muté", "Remplacement_muté_x12", "Moyenne", et "Héritage."
TOURNAMENT_TYPE = "Remplacement_muté"

random_seed = 7

random.seed(random_seed)

evolutive_tournament(playerlist, 248, TOURNAMENT_TYPE)

information_text(TOURNAMENT_TYPE, 11, saved_players, playerlist, seed=random_seed, special_notes="Tournoi avec le même code que ceux des remplacements mutés, mais avec plus d'informations sur les joueurs de fin.")
print("OK")
