"""
Produit un tournoi écologique avec la librairie Axelrod
à des fins de comparaison.
"""
import axelrod as axl

players = [axl.Cooperator(), axl.Defector(),
           axl.TitForTat(), axl.Grudger()]
tournament = axl.Tournament(players=players, turns=200)
results = tournament.play()
eco = axl.Ecosystem(results)
eco.reproduce(20)

plot = axl.Plot(results)
p = plot.stackplot(eco)
p.show()
print(eco.population_sizes)