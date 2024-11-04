from axelrod import Cooperator, Defector, TitForTat, Grudger, Tournament, Plot
from ecological_axl import Secondevolutive
from evolutive_strat import Evo
import random
import matplotlib.pyplot as plt

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


gen = 4
generations = []
for i in range(gen):
    generations.append(i + 1)

print("playerlist", playerlist)
random.seed(1)
tournament = Tournament(players=stratlist, turns=200)
results = tournament.play()
eco = Secondevolutive(results, mutation= False)

eco.reproduce(gen)

#print(eco.population_sizes) tout ce code ne sert que si le tournoi ne fait pas déjà la norme
#for i in eco.population_sizes:
#    norm = 0
#    for u in i:
#        norm += u
#    for u in i:
#        eco.population_sizes[eco.population_sizes.index(i)][i.index(u)] = u/norm

#print(eco.population_sizes)

plot = Plot(results)
p = plot.stackplot(eco)
p.show()
print(eco.population_sizes)

fig, ax = plt.subplots()
stacks = ax.stackplot(generations, eco.population_sizes,
            labels=stratlist,colors=["#73ff00", "#9aff47", "#bcff85", "#9bff85", "#71ff52", "#2eff00", "#00ff80", "#57ffab", "#8affc4", "#64b58c", "#3bbf7d", "#00b85c", "#00b806", "#60b563", "#8cb560", "#5bb000", "#73ff00", "#9aff47", "#bcff85", "#9bff85", "#71ff52", "#2eff00", "#00ff80", "#57ffab", "#ff0000", "#ff6e6e", "#ff906e", "#ff004c", "#cc003d", "#c44168", "#bd6542", "#f07f51", "#ff4a00", "#cf3c00", "#8c0303", "#8c033c"], alpha=0.8)
ax.legend(loc=(1.04, 0), reverse=True)
ax.set_title('Strategy Population')
ax.set_xlabel('Generation')
ax.set_ylabel('Cumulated Strategy Weights')
