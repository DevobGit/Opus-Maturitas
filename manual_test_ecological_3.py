from axelrod import Cooperator, Defector, TitForTat, Grudger, Tournament, Plot
from unnormed_ecosystem2 import Iamsleepy
from evolutive_strat import Evo
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
random.seed(1)
tournament = Tournament(players=stratlist, turns=200)
results = tournament.play()
eco = Iamsleepy(results, mutation= False)

eco.reproduce(20)

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

print("OK")