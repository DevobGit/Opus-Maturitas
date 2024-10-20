from axelrod import Tournament, Plot
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.ticker as mticker


def evolutive_tournament(players: list, steps: int, reproduction_type: int):
    # Stocke les infos le 1ere generation
    generation = [0]
    strats = {}
    for player in players :
        player.normalizeweights()
        for strat in player.strategies :
            if not (strat.name in strats):
                strats[strat.name] = [player.weights[player.strategies.index(strat)]]
            else :
                strats[strat.name][0] += player.weights[player.strategies.index(strat)]
    
    for g in range(steps) :
        print(g)
        tournament = Tournament(players)
        results = tournament.play()


        #plot = Plot(results)
        #p = plot.boxplot()
        #p.show()
        
        #print(results.ranking)
        player_weights = []
        for i in results.ranking:
            player_weights.append(players[results.ranking[i]].weights)
        #print(player_weights)
        
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
    
        #stocke les infos de la dernière generation
        generation.append(g+1)
        for player in players :
            for strat in player.strategies :
                if (len(strats[strat.name]) == g + 1):
                    strats[strat.name].append(player.weights[player.strategies.index(strat)])
                else :
                    strats[strat.name][g + 1] += player.weights[player.strategies.index(strat)]

    fig, ax = plt.subplots()
    stacks = ax.stackplot(generation, strats.values(),
                labels=strats.keys(),colors=["dimgray", "lightgray", "lightcoral", "red", "tomato", "sienna", "orange", "darkgoldenrod", "gold", "darkkhaki", "olive", "yellow", "lawngreen", "darkgreen", "aquamarine", "lightseagreen", "darkslategray", "cyan", "dodgerblue", "navy", "indigo", "violet", "purple", "magenta", "deeppink"], alpha=0.8)
    ax.legend(loc=(1.04, 0), reverse=True)
    ax.set_title('Strategy Population')
    ax.set_xlabel('Generation')
    ax.set_ylabel('Cumulated Strategy Weights')
    # add tick at every 200 million people
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(.1))
    
    #hatches=['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*', '/o', '\\|', '|*', '-\\', '+o', 'x*', 'o-', 'O|', 'O.', '*-', 'xx', 'oo', 'OO', '..', '**']
    #for stack, hatch in zip(stacks, hatches):
    #    stack.set_hatch(hatch)

    plt.show()    
