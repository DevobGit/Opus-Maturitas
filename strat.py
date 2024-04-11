"""
https://note.nkmk.me/en/python-issubclass-mro-bases-subclasses/#:~:text=In%20Python%2C%20you%20can%20use,the%20__subclasses__()%20method.
https://stackoverflow.com/questions/2225038/determine-the-type-of-an-object
"""


import random
# Fixer la graine aléatoire pour des résultats reproductibles
random.seed(6436)

def prisoner_dilemma(player1, player2, round):
    outcomes = {
        (0, 0): (3, 3),
        (0, 1): (0, 5),
        (1, 0): (5, 0),
        (1, 1): (1, 1)
    }

    outcome_player1, outcome_player2 = outcomes[(player1.play(round), player2.play(round))]
    return(outcome_player1, outcome_player2)

def match(player1, player2, rounds):
    score1, score2 = 0, 0
    print("MATCH : Player", player1.name, "VERSUS Player", player2.name)
    for round in range(rounds) :
        outcome_player1, outcome_player2 = prisoner_dilemma(player1, player2, round)
        
        # Sauvegarder les coups de l'adversaire pour chaque joueur
        player1.memorize(player2.action)
        player2.memorize(player1.action)
        
        # Print les infos du tour
        print("Round :", round + 1)
        for player in ([player1, player2]):
            print(player.name, "uses", player.chosenstrat.name)
            if  player.action == 0 :
                print(player.name, "cooperates !")
            else :
                print(player.name, "betrays !")
        print("Previous scores :", score1, score2)
        print("Gains :", outcome_player1, outcome_player2)
        
        # Effectuer réelement les changements des scores
        score1 += outcome_player1
        score2 += outcome_player2
        
        print("Present scores :", score1, score2)
        
        
    print("This is their final scores !")

# Définition de la classe des joueurs

class Player():
    def __init__(self, name, strategies):
        
        self.name = name
        self.strategies = strategies
        self.memory = []
            
    def play(self, round):
        
        self.chosenstrat = random.choice(self.strategies)
        """ Choix aléatoire de la stratégie, le choix des pourcentages de chance de séléction reste à
            implémenter, mais n'est pas prioritaire puisque néscessaire uniquement à partir de la quatrième
            étape de travail.
        """
        if isinstance(self.chosenstrat, Stratlist):
            self.action = self.chosenstrat.action(round)
        elif isinstance(self.chosenstrat, Stratmemory):
            self.action = self.chosenstrat.action(self.memory)
        else :
            self.action = self.chosenstrat.action()
        
        return self.action
    
    def memorize(self, move):
        self.memory.append(move)
    

# Définition des classes stratégies
class Strat():
    def __init__(self, name):
        
        self.name = name 

class Stratcooperation(Strat):
    def __init__(self, name):
        super().__init__(name)
    
    def action(self):
        """
        round est complétement inutile mais je ne sais comment gérer l'argument en trop donné par la classe player
        """ 
        return 0
        
class Stratbetrayal(Strat):
    def __init__(self, name):
        super().__init__(name)
    
    def action(self): 
        return 1
   
class Stratrandom(Strat):
    def __init__(self, name):
        super().__init__(name)
    
    def action(self): 
        return random.choice([0, 1])

class Stratlist(Strat):     
    def __init__(self, name, list):
        super().__init__(name)
        
        self.list = list
    
    def action(self, round):
        return self.list[round % len(self.list)]

class Stratmemory(Strat):
    def __init__(self, name):
        super().__init__(name)
    
    def action(self, memory): 
        pass
        




nice_double_change = Stratlist("Nice Double Change", [0, 0, 1, 1])
mean_change = Stratlist("Mean Change", [1, 0])
roll_the_dice = Stratrandom("Roll The Dice")
always_cooperate = Stratcooperation("Always Cooperate")
always_betray = Stratbetrayal("Always Betray")


Hoenn = Player("Hoenn", [nice_double_change, roll_the_dice])
Hisui = Player("Hisui", [nice_double_change, mean_change])      

match(Hoenn, Hisui, 10)

