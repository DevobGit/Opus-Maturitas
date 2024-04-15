"""
https://pybit.es/articles/python-subclasses/
https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
https://note.nkmk.me/en/python-issubclass-mro-bases-subclasses/#:~:text=In%20Python%2C%20you%20can%20use,the%20__subclasses__()%20method.
https://stackoverflow.com/questions/2225038/determine-the-type-of-an-object
Sources donnant les stratégies du premier tournoi d'Axelrod, le manque de détail pose un problème encore à résoudre :
https://axelrod.readthedocs.io/en/dev/tutorials/running_axelrods_first_tournament/index.html
https://axelrod.readthedocs.io/en/dev/reference/strategy_index.html
"""


import random
# Fixer la graine aléatoire pour des résultats reproductibles
random.seed(6436)

# Définition des manches

def prisoner_dilemma(player1, player2, round):
    outcomes = { # Créer un dictionnaire assignant chaque doublet d'action à son doublet de gains pour l'acteur
        (0, 0): (3, 3),
        (0, 1): (0, 5),
        (1, 0): (5, 0),
        (1, 1): (1, 1)
    }

    return(outcomes[(player1.play(round), player2.play(round))])
""" 
Retourne les résultat/gains du tour en utilisant le prècèdent dictionnaire pour assigner des gains
en fonction de l'action du joueur obtenue par sa méthode play, auquelle l'on indique le tour du tournoi
"""

# Définition des matchs

def match(player1, player2, rounds, comments):
    if comments : # Vérifie si l'on souhaite les commentaires des matchs
        print("MATCH : Player", player1.name, "VERSUS Player", player2.name) # Print les infos du match
    for round in range(rounds) : # Répète pendant le nombre de tours souhaité
        outcome_player1, outcome_player2 = prisoner_dilemma(player1, player2, round) # Sauvegarde les résultats du tour en variable
        
        # Sauvegarde les coups de l'adversaire pour chaque joueur
        player1.memorize(player2.action)
        player2.memorize(player1.action)
        if comments : # Vérifie si l'on souhaite les commentaires du match
            # Print les infos du tour
            print("Round :", round + 1)
            for player in ([player1, player2]): # Donne les actions pour les deux joueurs
                print(player.name, "uses", player.chosenstrat.name)
                if  player.action == 0 :
                    print(player.name, "cooperates !")
                else :
                    print(player.name, "betrays !")
            print("Previous scores :", player1.score, player2.score)
            print("Gains :", outcome_player1, outcome_player2)
        
        # Effectuer réelement les changements des scores
        player1.score += outcome_player1
        player2.score += outcome_player2
        if comments : # Vérifie si l'on souhaite les commentaires des matchs
            print("Present scores :", player1.score, player2.score) # Print les résultats totaux après le tour
    if comments : # Vérifie si l'on souhaite les commentaires des matchs
        # Print les résultats finaux    
        print("MATCH : Player", player1.name, "VERSUS Player", player2.name)   
        print("FINAL RESULTS :", player1.score, player2.score)
    
# Définition des tournois

def tournament(players, rounds, comments):
    allplayers = players.copy() # Crée une liste de chaque joueurs, qu'ils aient joués ou non
    while players : # Répéter tant qu'il reste des joueurs à ne pas avoir joués tout leurs matchs
        for player2 in players : # Répéter pour chaque adversaire dans la liste des joueurs
            match(players[0], player2, rounds, False) # Fait un match entre le premier joueur et son adversaire
            if comments : # Vérifie si l'on souhaite les commentaires du tournoi
                print("match entre", players[0].name, "et", player2.name)
            # Ajoute les scores du matchs aux totaux
            players[0].totalscore += players[0].score
            player2.totalscore += player2.score
            # Réinitialise les scores
            players[0].nullifyscore()
            player2.nullifyscore()
        players.remove(players[0])# Supprime de la liste le joueur ayant fini tout ses matchs
    allplayers = sorted(allplayers, key=lambda player: player.totalscore, reverse = True) # trie les joueurs par ordre décroissant des scores
    if comments : # Vérifie si l'on souhaite les commentaires du tournoi
        print("Classement par scores :")
        for player in allplayers : # Donne le score de chaque joueur dans l'ordre de la liste triée
            print(player.totalscore, player.name)

# Définition de la classe des joueurs

class Player():
    def __init__(self, name, strategies): # Le joueur a un nom et une liste de stratégies
        
        self.name = name
        self.strategies = strategies
        self.memory = [] # Le joueur initie une liste vide comme mémoire des coups adverses passés
        self.score = 0 # Le joueur démarre avec un score de 0
        self.totalscore = 0 # Le joueur démarre avec un score total de 0
            
    def play(self, round):
        
        self.chosenstrat = random.choice(self.strategies)
        """ Choix aléatoire de la stratégie, le choix des pourcentages de chance de séléction reste à
            implémenter, mais n'est pas prioritaire puisque néscessaire uniquement à partir de la quatrième
            étape de travail.
        """
        if isinstance(self.chosenstrat, Stratlist): # Vérifie que la strat suit une liste, et lui indique le n. de tour
            self.action = self.chosenstrat.action(round)
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
    def __init__(self, name):
        super().__init__(name)
    
    def action(self):
        return 0
        
class Stratbetrayal(Strat): # Trahi
    def __init__(self, name):
        super().__init__(name)
    
    def action(self): 
        return 1
   
class Stratrandom(Strat): # Agit aléatoirement à 50% de coopération
    def __init__(self, name):
        super().__init__(name)
    
    def action(self): 
        return random.choice([0, 1])

class Stratlist(Strat): # Suit la liste de coups donné, revient au début lorsque la fin est atteinte    
    def __init__(self, name, list):
        super().__init__(name)
        
        self.list = list
    
    def action(self, round):
        return self.list[round % len(self.list)]

class Stratmemory(Strat): # Classe demandant une information "memory" pour sa méthode action
    def __init__(self, name):
        super().__init__(name)
    
    def action(self, memory): 
        pass
    
class Stratitat(Stratmemory): # Coopère puis repète l'action prècèdente de l'adversaire
    def __init__(self, name):
        super().__init__(name)
    
    def action(self, memory): 
        if not memory or memory[-1] == 0:
            return 0
        else:
            return 1

class Stratotitat(Stratmemory): # Trahi uniquement si l'adversaire à trahi deux ou plus fois de suite
    def __init__(self, name):
        super().__init__(name)
    
    def action(self, memory): 
        if len(memory) >= 2 and memory[-1] == 1 and memory[-2] == 1:
            return 1
        else:
            return 0
        
class Stratnoredemption(Stratmemory): # Coopère jusqu'à ce que l'adversaire trahi, ne fait alors plus que trahir
    def __init__(self, name):
        super().__init__(name)
    
    def action(self, memory): 
        if 1 in memory:
            return 1
        else:
            return 0
        
class Stratdavis(Stratmemory): # Coopère les 10 premiers tours puis joue noredemption
    def __init__(self, name):
        super().__init__(name)
    
    def action(self, memory): 
        if len(memory) >= 10 and 1 in memory :
            return 1
        else :
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

# Faire un match

# match(Hoenn, DavisLover, 20, True)

# Faire un tournoi

# tournament([DavisLover, Hisui, Hoenn, Allrandom, Ruben, Zahibra, Juliette], 20, True)