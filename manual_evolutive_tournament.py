from axelrod import Cooperator, Defector, TitForTat, Grudger, TitFor2Tats, FirstByDavis, FirstByDowning, FirstByJoss, FirstByNydegger, FirstByShubik, FirstBySteinAndRapoport, FirstByTidemanAndChieruzzi, SecondByBorufsen, SecondByColbert, SecondByGladstein, SecondByGraaskampKatzen, SecondByGrofman, SecondByMikkelson, SecondByRichardHufford, SecondByRowsam, SecondByTester, SecondByTidemanAndChieruzzi, SecondByWeiner, SecondByWhite, SecondByYamachi
from ecological import evolutive_tournament
from evolutive_strat import Evo

stratlist = [
    Cooperator(),
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
#for _ in stratlist :
#    weightlist.append(1)  

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
for i in playerlist:
    for _ in stratlist :
        if len(i.weights) == playerlist.index(i) :
            i.weights.append(1)
        elif (len(stratlist) != len(playerlist)) and (playerlist.index(i) > len(stratlist)) and(len(i.weights) == 0):
            i.weights.append(1)
        else :
            i.weights.append(0)
    print(i.weights)

evolutive_tournament(playerlist, 100, 0)
