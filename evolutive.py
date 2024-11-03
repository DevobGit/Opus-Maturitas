import axelrod as axl
from stack import Betterplot
import matplotlib.pyplot as plt
from unnormed_ecosystem import Betterecosystem
import copy

def evolutive(players, steps, mutation):
    
    pop = []
    for _ in players:
        pop.append(1)
    print(len(pop), len(players))
    total_pop = [copy.deepcopy(pop)]

    tournament = axl.Tournament(players=players, turns=200)
    results = tournament.play()

    plot = axl.Plot(results)
    p = plot.boxplot()
    p.show()

    for step in range(steps):

        print(step)

        eco = Betterecosystem(results, population=pop)
        eco.reproduce(1)
        total_pop.append(copy.deepcopy(eco.population_sizes[-1]))
        pop = eco.population_sizes[-1]
        playerpop = {}
        
        for player in players:
            playerpop[player.name] = [i * pop[players.index(player)] for i in player.weights]
        
        pop = [sum(x) for x in zip(*list(playerpop.values()))]
        print("[sum(x) for x in zip(*list(playerpop.values()))]", pop)
        
        total_pop.append(copy.deepcopy(pop))

        plot = axl.Plot(results)
        p = plot.stackplot(eco)
        p.show()

        print(eco.population_sizes)

    eco.population_sizes = total_pop
    norm = 0
    for i in eco.population_sizes:
        for u in i:
            norm += u
    eco.population_sizes = [p / norm for p in eco.population_sizes]
    
    plot = axl.Plot(results)
    p = plot.stackplot(eco)
    p.show()








if __name__=="__main__":

    players = [axl.Cooperator(), axl.Defector(),
            axl.TitForTat(), axl.Grudger()]
    tournament = axl.Tournament(players=players, turns=200)
    results = tournament.play()
    eco = Betterecosystem(results)
    eco.reproduce(10)



    """
    fig, ax = plt.subplots()
    stacks = ax.stackplot(1, eco.population_sizes,
                colors=["dimgray", "lightgray", "lightcoral", "red", "tomato", "sienna", "orange", "darkgoldenrod", "gold", "darkkhaki", "olive", "yellow", "lawngreen", "darkgreen", "aquamarine", "lightseagreen", "darkslategray", "cyan", "dodgerblue", "navy", "indigo", "violet", "purple", "magenta", "deeppink"], alpha=0.8)
    ax.legend(loc=(1.04, 0), reverse=True)
    ax.set_title('Strategy Population')
    ax.set_xlabel('Generation')
    ax.set_ylabel('Cumulated Strategy Weights')
    """



    plot = Betterplot(results)
    p = plot.stackplot(eco)
    p.show()
    print(eco.population_sizes)
