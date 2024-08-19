from axelrod import Tournament, Cooperator, Defector, TitForTat, Grudger, Plot
from evolutive_strat import Evo


playerlist = [
    Evo([TitForTat(), Defector(), Cooperator(), Grudger()]
        ,[1, 0, 0, 0]),
    Evo([TitForTat(), Defector(), Cooperator(), Grudger()]
        ,[0, 1, 0, 0]),
    Evo([TitForTat(), Defector(), Cooperator(), Grudger()]
        ,[0, 0, 1, 0]),
    Evo([TitForTat(), Defector(), Cooperator(), Grudger()]
        ,[0, 0, 0, 1])
    ]


def evolutive_tournament(players: list, steps: int, reproduction_type: int):
    for _ in range(steps) :
        tournament = Tournament(players)
        results = tournament.play()


        plot = Plot(results)
        p = plot.boxplot()
        p.show()
        
        print(results.ranking)
        player_weights = []
        for i in results.ranking:
            player_weights.append(players[results.ranking[i]].weights)
        print(player_weights)
        
        best_player = players[results.ranking[0]]
        
        if reproduction_type == 0:
            offspring = best_player.clone()
            offspring.mutate()
            del players[results.ranking[-1]]
            players.append(offspring)
        elif reproduction_type == 1:
            for player in players :
                new_weights = []
                for i, weight in enumerate(player.weights):
                    # Calcul de la moyenne des éléments aux mêmes indices
                    moyenne = (weight + best_player.weights[i]) / 2
                    # Ajouter la moyenne à la nouvelle liste
                    new_weights.append(moyenne)
                player.weights = new_weights.copy()
                player.mutate()
        elif reproduction_type == 2:
            for player in players :
                player.weights[best_player.weights.index(max(best_player.weights))] = max(best_player.weights)
                player.mutate()

evolutive_tournament(playerlist, 5, 0)
