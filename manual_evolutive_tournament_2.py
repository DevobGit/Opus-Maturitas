from axelrod import TitForTat, Grudger, TitFor2Tats, FirstByDavis, FirstByDowning, FirstByNydegger, FirstByShubik, FirstBySteinAndRapoport, FirstByTidemanAndChieruzzi, SecondByBorufsen, SecondByColbert, SecondByGraaskampKatzen, SecondByGrofman, SecondByMikkelson, SecondByRichardHufford, SecondByRowsam, SecondByTester, SecondByTidemanAndChieruzzi, SecondByWeiner, SecondByWhite, FirstByAnonymous, FirstByFeld, FirstByGraaskamp, FirstByTullock, Random, FirstByGrofman, FirstByJoss, SecondByHarrington, SecondByChampion, SecondByCave, SecondByWmAdams, SecondByLeyvraz, SecondByBlack, SecondByEatherley, SecondByGetzler, SecondByKluepfel, Tournament, Plot
from ecological_axl import Secondevolutive
import matplotlib.pyplot as plt

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

gen = 1000
generations = []
for i in range(gen + 1):
    generations.append(i + 1)

tournament = Tournament(players=stratlist, turns=200)
results = tournament.play()
eco = Secondevolutive(results, mutation= False)

eco.reproduce(gen)

strats = {}
for player in stratlist :
    strats[str(player)] = []
    for i in eco.population_sizes :
        strats[str(player)].append(i[stratlist.index(player)])
    
    
    #if not (player in strats):
    #    strats[player] = [player.weights[player.strategies.index(strat)]]
    #else :
    #    strats[player][0] += player.weights[player.strategies.index(strat)]
    
plot = Plot(results)
p = plot.stackplot(eco)
p.show()
print(eco.population_sizes)


fig, ax = plt.subplots()
stacks = ax.stackplot(generations, strats.values(),
            labels=strats.keys(),colors=["#73ff00", "#9aff47", "#bcff85", "#9bff85", "#71ff52", "#2eff00", "#00ff80", "#57ffab", "#8affc4", "#64b58c", "#3bbf7d", "#00b85c", "#00b806", "#60b563", "#8cb560", "#5bb000", "#73ff00", "#9aff47", "#bcff85", "#9bff85", "#71ff52", "#2eff00", "#00ff80", "#57ffab", "#ff0000", "#ff6e6e", "#ff906e", "#ff004c", "#cc003d", "#c44168", "#bd6542", "#f07f51", "#ff4a00", "#cf3c00", "#8c0303", "#8c033c"], alpha=0.8)
ax.legend(loc=(1.04, 0), reverse=True)
ax.set_title('Strategy Population')
ax.set_xlabel('Generation')
ax.set_ylabel('Cumulated Strategy Weights')
