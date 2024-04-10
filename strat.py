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
        
        
    def play(self, round):
        
        self.chosenstrat = random.choice(self.strategies)
        """ Choix aléatoire de la stratégie, le choix des pourcentages de chance de séléction reste à
            implémenter, mais n'est pas prioritaire puisque néscessaire uniquement à partir de la quatrième
            étape de travail.
        """
        self.action = self.chosenstrat.action(round)
        return self.action

# Définition des classes stratégies
class Strat():
    def __init__(self, name):
        
        self.name = name 
    
class Stratrandom(Strat):
    def __init__(self, name):
        super().__init__(name)
    
    def action(self, round): 
        """
        round est complétement inutile mais je ne sais comment gérer l'argument en trop donné par la classe player
        """
        return random.choice([0, 1])
        

class Stratlist(Strat):     
    def __init__(self, name, list):
        super().__init__(name)
        
        self.list = list
    
    def action(self, round):
        return self.list[round % len(self.list)]
        




nice_double_change = Stratlist("Nice Double Change", [0, 0, 1, 1])
mean_change = Stratlist("Mean Change", [1, 0])
roll_the_dice = Stratrandom("Roll The Dice")


Hoenn = Player("Hoenn", [nice_double_change, roll_the_dice])
Hisui = Player("Hisui", [nice_double_change, mean_change])      

match(Hoenn, Hisui, 10)

