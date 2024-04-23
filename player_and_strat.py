import random

# Fixer la graine aléatoire pour des résultats reproductibles
random.seed(6436)

class Player():
    # Définition de la classe des joueurs
    def __init__(self, name, strategies): # Le joueur a un nom et une liste de stratégies

        self.name = name
        self.strategies = strategies
        self.memory = [] # Le joueur initie une liste vide comme mémoire des coups adverses passés
        self.score = 0 # Le joueur démarre avec un score de 0
        self.totalscore = 0 # Le joueur démarre avec un score total de 0       
    def play(self, tour):
        
        self.chosenstrat = random.choice(self.strategies)
        #Choix aléatoire de la stratégie, le choix des pourcentages de chance de séléction reste à
        #implémenter, mais n'est pas prioritaire puisque néscessaire uniquement à partir de la quatrième
        #étape de travail.

        if isinstance(self.chosenstrat, Stratlist): # Vérifie que la strat suit une liste, et lui indique le n. de tour
            self.action = self.chosenstrat.action(tour)
        elif isinstance(self.chosenstrat, Stratmemory): # Vérifie que la strat utilise la mémoire, et la lui donne
            self.action = self.chosenstrat.action(self.memory)
        else : # Sinon n'a pas besoin de lui donner plus d'infos
            self.action = self.chosenstrat.action()
        
        return self.action
    
    def memorize(self, move): # Ajoute un move à sa mémoire
        self.memory.append(move)
        
    def nullifyscore(self): # Reset son score à zéro
        self.score = 0
        
    def nullifytotalscore(self): # Reset son score total à zéro
        self.totalscore = 0
    
# Définition des classes stratégies, le nom des classes sera sûrement changé à l'avenir pour correspondre aux noms originaux

class Strat(): # Classe des stratégie, elle... porte un nom !
    def __init__(self, name):
        
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
    def __init__(self, name, liste):
        super().__init__(name)
        
        self.list = liste
    
    def action(self, tour):
        return self.list[tour % len(self.list)]

class Stratmemory(Strat): # Classe demandant une information "memory" pour sa méthode action
    
    def action(self, memory): 
        pass

class Stratcontrol(Stratlist, Stratmemory): # Classe suivant une liste et avec mémoire utilisée pour les contrôles
    pass

class Stratitat(Stratmemory): # Coopère puis repète l'action prècèdente de l'adversaire
    
    def action(self, memory): 
        if not memory or memory[-1] == 0:
            return 0
        return 1

class Stratotitat(Stratmemory): # Trahi uniquement si l'adversaire à trahi deux ou plus fois de suite
    
    def action(self, memory): 
        if len(memory) >= 2 and memory[-1] == 1 and memory[-2] == 1:
            return 1
        else:
            return 0
        
class Stratnoredemption(Stratmemory): # Coopère jusqu'à ce que l'adversaire trahi, ne fait alors plus que trahir
    
    def action(self, memory): 
        if 1 in memory:
            return 1
        else:
            return 0
        
class Stratdavis(Stratmemory): # Coopère les 10 premiers tours puis joue noredemption
    
    def action(self, memory): 
        if len(memory) >= 10 and 1 in memory :
            return 1
        return 0
       
# Créer objets strat

nice_double_change = Stratlist("Nice Double Change", [0, 0, 1, 1])
mean_change = Stratlist("Mean Change", [1, 0])
roll_the_dice = Stratrandom("Roll The Dice")
always_cooperate = Stratcooperation("Always Cooperate")
always_betray = Stratbetrayal("Always Betray")
tit_for_tat = Stratitat("Tit For Tat")
tit_for_two_tat = Stratotitat("Tit For Two Tat")
no_redemption = Stratnoredemption("No Redemption")
davis = Stratdavis("Davis")

# Créer objets joueurs

Hoenn = Player("Hoenn", [tit_for_tat, tit_for_two_tat, roll_the_dice])
Hisui = Player("Hisui", [no_redemption, tit_for_tat])
DavisLover = Player("Davis Lover", [davis])
Allrandom = Player("All Random", [roll_the_dice])
Ruben = Player("Ruben", [mean_change])
Zahibra = Player("Zahibra", [no_redemption, roll_the_dice])
Juliette = Player("Juliette", [davis, tit_for_tat])