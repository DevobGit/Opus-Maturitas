from player_and_strat import Player

# Définition des manches

def prisoner_dilemma(player1 : Player, player2 : Player, tour : int):

    choice1 = player1.play(tour)
    choice2 = player2.play(tour)

    if choice1 == 0:
        if choice2 == 0:
            return (3, 3)
        return (0, 5)
    elif choice2 == 0:
        return (5, 0)
    return (1, 1)

# Retourne les résultat/gains du tour en utilisant le prècèdent dictionnaire pour assigner des gains
# en fonction de l'action du joueur obtenue par sa méthode play, auquelle l'on indique le tour du tournoi

# Définition des matchs

def match(player1 : Player, player2 : Player, rounds : int, comments : bool):
    if comments : # Vérifie si l'on souhaite les commentaires des matchs
        print("MATCH : Player", player1.name, "VERSUS Player", player2.name) # Print les infos du match
    for tour in range(rounds) : # Répète pendant le nombre de tours souhaité
        outcome_player1, outcome_player2 = prisoner_dilemma(player1, player2, tour)
        # Sauvegarde les résultats du tour en variable
        # Sauvegarde les coups de l'adversaire pour chaque joueur
        player1.memorize(player2.action)
        player2.memorize(player1.action)
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

def tournament(players : list, rounds : int, comments : bool):
    allplayers = players.copy() # Crée une liste de chaque joueurs, qu'ils aient joués ou non
    while players : # Répéter tant qu'il reste des joueurs à ne pas avoir joués tout leurs matchs
        for player2 in players : # Répéter pour chaque adversaire dans la liste des joueurs
            # Efface la mémoire
            players[0].erasememory()
            player2.erasememory()
            # Réinitialise les scores
            players[0].nullifyscore()
            player2.nullifyscore()
            match(players[0], player2, rounds, False)
            # Fait un match entre le premier joueur et son adversaire
            if not players[0] == player2 :
                player2.totalscore += player2.score
            players[0].totalscore += players[0].score # Ajoute les scores du matchs aux totaux
            if comments : # Vérifie si l'on souhaite les commentaires du tournoi
                print("match entre", players[0].name, "et", player2.name)
                print(players[0].score, player2.score)
                print(players[0].totalscore, player2.totalscore)
        players.remove(players[0])# Supprime de la liste le joueur ayant fini tout ses matchs
    allplayers = sorted(allplayers, key=lambda player: player.totalscore, reverse = True)
    # trie les joueurs par ordre décroissant des scores
    if comments : # Vérifie si l'on souhaite les commentaires du tournoi
        print("Classement par scores :")
        for player in allplayers : # Donne le score de chaque joueur dans l'ordre de la liste triée
            print(player.totalscore, player.name)
