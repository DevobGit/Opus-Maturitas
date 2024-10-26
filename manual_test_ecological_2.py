import axelrod as axl

players = [axl.Cooperator(), axl.Defector(),
           axl.TitForTat(), axl.Grudger()]
tournament = axl.Tournament(players=players, turns=200)
results = tournament.play()
eco = axl.Ecosystem(results)
eco.reproduce(2)

plot = axl.Plot(results)
p = plot.stackplot(eco)
p.show()