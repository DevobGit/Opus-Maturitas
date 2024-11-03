"""Tools for simulating population dynamics of immutable players.

An ecosystem runs in the context of a previous tournament, and takes the
results as input. That means no matches are run by the ecosystem, and a
tournament needs to happen before it is created. For example:

players = [axelrod.Cooperator(), axlerod.Defector()]
tournament = axelrod.Tournament(players=players)
results = tournament.play()
ecosystem = axelrod.Ecosystem(results)
ecosystem.reproduce(100)


Code tu tournoi ecologique de la librairie Axelrod, modifié pour fonctionner
aussi comme tournoi évolutif.
https://github.com/Axelrod-Python/Axelrod/blob/dev/axelrod/ecosystem.py

"""

import random
import copy
from typing import Callable, List

from axelrod.result_set import ResultSet


class Iamsleepy(object):
    """An ecosystem based on the payoff matrix from a tournament.

    Attributes
    ----------
    num_players: int
        The number of players
    """

    def __init__(
        self,
        results: ResultSet,
        #players, (utile uniquement dans le code mis en commentaire plus loin)
        mutation = False,
        fitness: Callable[[float], float] = None,
        population: List[int] = None,
    ) -> None:
        """Create a new evolutive ecosystem.
        
        Notez que la payoff matrix correspondant au résultats
        de chaque joueurs lors du tournoi généré précèdemment
        et dont les résultats sont prit en argument par cette
        classe, il faut pour que la payoff matrix soit réutilisable
        dans le calcul de chaque génération que les joueurs participants
        au tournoi soient tous initialement mono-stratégiques.
        Les joueurs-stratgégies de la librairie axelrod sont alors
        parfaitement utilisables pour cette forme de tournoi évolutif.
        
        Plus de détail dans les commentaires du code de la méthode
        de classe reproduce().
        
        

        Parameters
        ----------
        results: ResultSet
            The results of the tournament run beforehand to use.
        fitness: List of callables
            The reproduction rate at which populations reproduce.
        population: List of ints.
            The initial populations of the players, corresponding to the
            payoff matrix in results.
        """
        self.mutation = mutation
        # self.players = players
        self.results = results
        self.num_players = self.results.num_players
        self.payoff_matrix = self.results.payoff_matrix
        self.payoff_stddevs = self.results.payoff_stddevs

        # Population sizes will be recorded in this nested list, with each
        # internal list containing strategy populations for a given turn. The
        # first list, representing the starting populations, will by default
        # have all equal values, and all population lists will be normalized to
        # one. An initial population vector can also be passed. This will be
        # normalised, but must be of the correct size and have all non-negative
        # values.
        if population:
            if min(population) < 0:
                raise TypeError(
                    "Minimum value of population vector must be non-negative"
                )
            elif len(population) != self.num_players:
                print(len(population), self.num_players)
                raise TypeError(
                    "Population vector must be same size as number of players"
                )
            else:
                norm = sum(population)
                self.population_sizes = [[p / norm for p in population]] # Division entière la version du code en commentaire
        else:
            self.population_sizes = [
                [1 / self.num_players for _ in range(self.num_players)]
            ]

        # This function is quite arbitrary and probably only influences the
        # kinetics for the current code.
        if fitness:
            self.fitness = fitness
        else:
            self.fitness = lambda p: p

    def reproduce(self, turns: int):
        """Reproduce populations according to the payoff matrix.
        
        Notez que la payoff matrix correspondant au résultats
        de chaque joueurs lors du tournoi généré précèdemment
        et dont les résultats sont prit en argument par cette
        classe, il faut pour que la payoff matrix soit réutilisable
        dans le calcul de chaque génération que les joueurs participants
        au tournoi soient tous initialement mono-stratégiques.
        Les joueurs-stratgégies de la librairie axelrod sont alors
        parfaitement utilisables pour cette forme de tournoi évolutif.
        
        Plus de détail dans les commentaires du code de la méthode
        de classe reproduce().

        Parameters
        ----------
        turns: int
            The number of turns to run.
        """
        for iturn in range(turns):
            print(iturn)
            plist = list(range(self.num_players))
            pops = self.population_sizes[-1]

            # The unit payoff for each player in this turn is the sum of the
            # payoffs obtained from playing with all other players, scaled by
            # the size of the opponent's population. Note that we sample the
            # normal distribution based on the payoff matrix and its standard
            # deviations obtained from the iterated PD tournament run
            # previously.
            payoffs = [0.0 for ip in plist]
            for ip in plist:
                for jp in plist:
                    avg = self.payoff_matrix[ip][jp]
                    dev = self.payoff_stddevs[ip][jp]
                    p = int(random.normalvariate(avg, dev))
                    payoffs[ip] += p * pops[jp]

            # The fitness should determine how well a strategy reproduces. The
            # new populations should be multiplied by something that is
            # proportional to the fitness, but we are normalizing anyway so
            # just multiply times fitness.
            #int(self.fitness(p)) dans la version du code en commentaire
            fitness = [self.fitness(p) for p in payoffs]
            newpops = [p * f for p, f in zip(pops, fitness)]
            
            # La première population n'est pas une population de stratégie, mais
            # une population de joueurs mono-stratégiques. Cela revient au même
            # pour la première génération, mais par la suite les mutations sur
            # les joueurs leur fais avoir plusieurs stratégies et il faut faire
            # la distinction.
            # Pour avoir la population de chaque stratégies, il
            # faut prendre pour chaque joueur sa liste des poids associés à
            # leurs stratégies dont on multiplie chaque poid par la population du
            # joueur. La liste de population des stratégies sera une liste où
            # chaque element est la somme des elements à la même position dans les
            # listes créées à l'étape d'avant. Ceci ne fonctionne que si chaque
            # joueur a les mêmes stratégies et que les poids à une position X
            # dans leur liste correspondent toujours à la même stratégie pour
            # chaque joueur.
            # Le code ci-dessous permet d'obtenir la nouvelle population.
            
            #playerpop = {}
            
            #for player in self.players:
            #    playerpop[player.name] = [i * newpops[self.players.index(player)] for i in player.weights]
            
            #newpops = [int(sum(x)) for x in zip(*list(playerpop.values()))]
            
            # Cependant il se trouve que ce code n'est utile que lorsque les
            # joueurs ont plusieurs stratégie différentes (sinon, comme dit plus
            # tôt, cela revient au même que la population de chaque stratégie).
            # Mais dans ce cas là, la payoff matrix utilisée pour reproduire la
            # population ne correspond pas aux résultat de chaques stratégies
            # au 1er tournoi, mais aux résultats de chaque joueurs de 1ere génération.
            # Elle n'est donc pas applicable sur les stratégies (ce qui rend la
            # conversion de joueur à stratégie codée ci-dessus inutile), mais pas
            # non plus sur les joueurs, car la matrice ne prend on compte que les
            # joueur de 1ere génération avec les choix aléatoire de stratégies à
            # utiliser qu'ils en fait au premier tournoi, toute mutation et changement
            # dans le choix de stratégie que le joueur ferait plus tard n'est pas prit
            # en compte.
            
            
            # Au final, l'effet de mutation sur le joueur n'aurait d'effet que de changer
            # légèrement et aléatoirement les poids de chaque stratégie du joueur (et donc
            # la population de la stratégie), un effet qui peut être simulé simplement en
            # applicant la "mutation" directement sur la population de stratégies.
            # En effet, des mutation aléatoires qui ont pour effet de changer une stratégie
            # vont avoir sur la population totale une légère variation aléatoire des
            # population de stratégies, avec notamment la possibilité de faire réapparaître
            # une stratégie dont la population a été éteinte.
            # De ce fait, il n'y a pad de besoin d'utiliser les joueurs Evo(),
            # les joueurs-stratégies de la librairie Axelrod sont parfaitement compatible
            # avec cette forme de tournoi évolutif qui n'est qu'une légère modification
            # du tournoi écologique de la librairie.
            # Notez que puisqu'il n'y a pas besoin de faire muter des joueurs de manière
            # individuelle, les populations peuvent être normées.
            
            if self.mutation:
                newpopulations = []
                for pop in newpops :
                    newpop = pop * random.uniform(0.8, 1.2)
                    if pop == 0 and random.randint(1, 10) == 1 :
                        pop = 0.1
                    newpopulations.append(newpop)
                newpops = copy.deepcopy(newpopulations)
            
            norm = sum(newpops)
            newpops = [p / norm for p in newpops]
            
            self.population_sizes.append(newpops)