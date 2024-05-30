import random
import string
from scipy.stats import chisquare

# Fixer la graine aléatoire pour des résultats reproductibles
random.seed(6436)

class Player():
    # Définition de la classe des joueurs
    def __init__(self, name, strategies): # Le joueur a un nom et une liste de stratégies
        self.name = name
        self.strategies = strategies
        self.memory = [] # Le joueur initie une liste vide comme mémoire des coups adverses passés
        self.automemory = [] # Le joueur initie une liste vide comme mémoire de ses propres coups passés
        self.score = 0 # Le joueur démarre avec un score de 0
        self.totalscore = 0 # Le joueur démarre avec un score total de 0
        self.action = 0 # Cette variable correspond au dernier coup joué par le joueur
        self.chosenstrat = self.strategies[0] # Cette variable correspond à la dernière stratégie choisie
               
    def play(self, tour : int): 
        self.chosenstrat = random.choice(self.strategies)
        #Choix aléatoire de la stratégie, le choix des pourcentages de chance de séléction reste à
        #implémenter, mais n'est pas prioritaire puisque néscessaire uniquement à partir de la quatrième
        #étape de travail.

        if isinstance(self.chosenstrat, Stratlist): # Vérifie que la strat suit une liste, et lui indique le n. de tour
            self.action = self.chosenstrat.action(tour)
            return self.action
        if isinstance(self.chosenstrat , Stratmemory): # Vérifie que la strat utilise la mémoire, et la lui donne
            if isinstance(self.chosenstrat, Stratautomemory): # Vérifie que la strat utilise l' automémoire, et la lui donne
                self.action = self.chosenstrat.action(self.memory, self.automemory)
                return self.action
            self.action = self.chosenstrat.action(self.memory)
            return self.action
        # Sinon n'a pas besoin de lui donner plus d'infos
        self.action = self.chosenstrat.action()
        return self.action
            
    def memorize(self, move : int): # Ajoute un move à sa mémoire
        self.memory.append(move)
        
    def automemorize(self, move :int): # Ajoute un move à son automémoire
        self.automemory.append(move)
        
    def nullifyscore(self): # Reset son score à zéro
        self.score = 0
        
    def nullifytotalscore(self): # Reset son score total à zéro
        self.totalscore = 0
    
    def erasememory(self): # Reset sa mémoire
        self.memory.clear()
        
    def eraseautomemory(self): # Reset son automémoire
        self.automemory.clear()
    
# Définition des classes stratégies, le nom des classes sera sûrement changé à l'avenir pour correspondre aux noms originaux

class Strat(): # Classe des stratégie, elle... porte un nom !
    def __init__(self, name : string):
        
        self.name = name 

class Stratcooperation(Strat): # Coopère
    
    def action(self):
        return 0
        
class Stratbetrayal(Strat): # Trahi
    
    def action(self): 
        return 1
   
class Stratrandom(Strat): # Agit aléatoirement à 50% de coopération
    
    def action(self): 
        return random.choice([0, 1])

class Stratlist(Strat): # Suit la liste de coups donné, revient au début lorsque la fin est atteinte    
    def __init__(self, name : string, liste : list):
        super().__init__(name)
        
        self.list = liste
    
    def action(self, tour : int):
        return self.list[tour % len(self.list)]

class Stratmemory(Strat): # Classe demandant une information "memory" pour sa méthode action
    
    def action(self, memory : list): 
        pass

class Stratautomemory(Strat): # Classe demandant une information "automemory" correspondant à ses anciens coups pour sa méthode action
    
    def action(self, automemory : list): 
        pass

class Stratitat(Stratmemory): # Coopère puis repète l'action prècèdente de l'adversaire
    
    def action(self, memory : list): 
        if not memory or memory[-1] == 0:
            return 0
        return 1

class Stratotitat(Stratmemory): # Trahi uniquement si l'adversaire à trahi deux ou plus fois de suite
    
    def action(self, memory : list): 
        if len(memory) >= 2 and memory[-1] == 1 and memory[-2] == 1:
            return 1
        return 0
        
class Stratgrudger(Stratmemory): # Coopère jusqu'à ce que l'adversaire trahi, ne fait alors plus que trahir
    
    def action(self, memory : list): 
        if 1 in memory:
            return 1
        return 0
        
class Stratdavis(Stratmemory): # Coopère les 10 premiers tours puis joue grudger
    
    def action(self, memory : list): 
        if len(memory) >= 10 and 1 in memory :
            return 1
        return 0

class Stratgrofman(Stratmemory, Stratautomemory): # Si les joueurs ont agit différemment au dernier tour coopére avec 2/7 de probabilité, sinon coopère
    
    def action(self, memory : list, automemory : list):
        if len(memory) == 0 or memory[-1] == automemory[-1]:
            return 0
        return random.choices([0, 1], [2, 5])

class Stratjoss(Stratmemory): # joue tit for tat avec 90% de coopération au lieu de 100%
    
    def action(self, memory : list): 
        if (not memory or memory[-1] == 0) and random.uniform(0, 1) <= 0.9:
            return 0
        return 1

class Strattullock(Stratmemory): # Coopère les 11 premiers tours puis coopère 10% de moins que l'adversaire les 10 derniers tours
    
    def action(self, memory : list):
        if not len(memory) >= 11 :
            if random.randint(0, 10) <= (memory[-10:].count(1) / 10) - (memory[-10:].count(1) / 100):
                return 0
            return 1
        return 0

class Stratgraaskamp(Stratmemory, Stratautomemory):
    
    def __init__(self, name : string, alpha: float = 0.05) -> None:
        super().__init__(name)

        self.alpha = alpha
        self.opponent_is_random = False
        self.next_random_defection_turn = None
    
    def action(self, memory : list, automemory : list):
        if len(memory) < 56  : # Joue tit for tat les 55 premier tours sauf le 50 où il trahi
            if (not memory or memory[-1] == 0) and not len(memory) == 50:
                return 0
            return 1     
        # Vérifie si l'adversaire est aléatoire avec un Chi-squared test, auquel cas trahi toujours
        p_value = chisquare([memory.count(0), memory.count(1)]).pvalue
        self.opponent_is_random = (
            p_value >= self.alpha
        ) or self.opponent_is_random # Ne fait pas le test si l'adversaire a déjà été considéré comme random

        if self.opponent_is_random:
            return 1
        # Vérifie si l'adversaire est un "clone" de lui même ou s'il est tit for tat, auquel cas, joue tit for tat
        if (
            all(
                memory[i] == automemory[i - 1]
                for i in range(1, len(automemory))
            )
            or memory == automemory
        ):
            if memory[-1] == 1:
                return 1
            return 0
        
        if self.next_random_defection_turn is None: # Vérifie si le prochain tour aléatoir de trahison a déjà été choisi
            # Place la prochaine trahison à entre 5 et 15 tours plus loins que le nombre de tours actuel
            self.next_random_defection_turn = random.randint(5, 15) + len(
                automemory
                )
        
        if len(automemory) == self.next_random_defection_turn: # Vérifie s'il est le tour de trahison
            # Choisi le prochain tour de trahison
            self.next_random_defection_turn = random.randint(5, 15) + len(
                automemory
            )
            return 1
        return 0

class Stratsteinandrapoport(Stratmemory):
    
    def __init__(self, name : string, alpha: float = 0.05) -> None:
        super().__init__(name)

        self.alpha = alpha
        self.opponent_is_random = False
    
    def action(self, memory : list):
        if not len(memory) >= 3 :
            return 0
        
        """
        Dans un match de 200 tours, trahi les deux derniers tours. (Comportement en cas
        de matchs plus longs personnelement interprété, pourra changer plus tard, pour
        l'instant sans importance.
        """
        if len(memory) % 199 == 0 or len(memory) % 199 == -1 :
            return 1
        
        if len(memory) % 15 == -1 :
            p_value = chisquare(
                [memory.count(0), memory.count(1)]
            ).pvalue
            self.opponent_is_random = (p_value >= self.alpha)
        
        if self.opponent_is_random:
            return 1

        return memory[-1]