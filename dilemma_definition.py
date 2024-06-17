from player_and_strat import Player
from copy import deepcopy


def prisoner_dilemma(choice1: int, choice2: int):
    if choice1 == 0:
        if choice2 == 0:
            return (3, 3)
        return (0, 5)
    elif choice2 == 0:
        return (5, 0)
    return (1, 1)


def match(player1: Player, player2: Player, rounds: int):
    player1.opponent = player2
    player2.opponent = player1
    for tour in range(rounds):
        choice1 = player1.play(tour)
        choice2 = player2.play(tour)
        outcome1, outcome2 = prisoner_dilemma(choice1, choice2)
        player1.handle(outcome1, choice2)
        player2.handle(outcome2, choice1)

    player1.totalscore += player1.score
    player2.totalscore += player2.score


def match(player1 : Player, player2 : Player, rounds : int, comments : bool):
    if comments : # Vérifie si l'on souhaite les commentaires des matchs
        print("MATCH : Player", player1.name, "VERSUS Player", player2.name) # Print les infos du match
    
    if player1 == player2 :
        player2 = deepcopy(player1)
    
    # Informe les joueurs de leur adversaires
    player1.getopponent(player2)
    player2.getopponent(player1)
    
    for tour in range(rounds) : # Répète pendant le nombre de tours souhaité
        outcome_player1, outcome_player2 = prisoner_dilemma(player1, player2, tour)
        # Sauvegarde les résultats du tour en variable
        # Sauvegarde les coups de l'adversaire pour chaque joueur
        player1.memorize(player2.action)
        player1.automemorize(player1.action)
        player2.memorize(player1.action)
        player2.automemorize(player2.action)
        if comments : # Vérifie si l'on souhaite les commentaires du match
            # Print les infos du tour
            print("Round :", tour + 1)
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
def tournament(players: list, rounds: int):
    for i, player1 in enumerate(players):
        player1.reset_for_new_game()
        player2 = deepcopy(player1)
        player2.reset_for_new_game()
        match(player1, player2, rounds)
        for player2 in players[i+1:]:
            player1.reset_for_new_game()
            player2.reset_for_new_game()
            match(player1, player2, rounds)
