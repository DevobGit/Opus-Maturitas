# Fichier définissant les fonctions pour exécuter un tournoi de dilemmes du prisonnier itérés
# semblable à celui d'Axelrod.
# Ceci n'est pas utilisé pour produire les graphiques présentés dans le dossier TM.


# import de la classe defaultdict
from collections import defaultdict

# import de deepcopy, permettant de créer des copies d'objets utilisant une autre place en
# mémoire que les objets originaux.
from copy import deepcopy

# import de la classe Player définie dans player_and_strat
from player_and_strat import Player

def prisoner_dilemma(choice1: int, choice2: int):
    """_summary_

    Args:
        choice1 (int): choix du joueur 1. 0 = coopérer, 1 = trahir
        choice2 (int): choix du joueur 2. 0 = coopérer, 1 = trahir

    Returns:
        un tuple des gains en score de chaque joueur
    """
    if choice1 == 0:
        if choice2 == 0:
            return (3, 3)
        return (0, 5)
    elif choice2 == 0:
        return (5, 0)
    return (1, 1)


def match(player1: Player, player2: Player, rounds: int):
    """_summary_

    Args:
        player1 (Player): joueur 1, une instance de la classe Player
        player2 (Player): joueur 2, une instance de la classe Player
        rounds (int): nombre de fois que le dilemme du prisonnier est itéré entre les joueurs 1 et 2.
    """
    # utilise la méthode de classe prepare_for_new_game_against()
    # sur chaque joueur
    player1.prepare_for_new_game_against(player2)
    player2.prepare_for_new_game_against(player1)
    for tour in range(rounds):
        # fais jouer chaque joueur
        choice1 = player1.play(tour)
        choice2 = player2.play(tour)
        # utilise la fonction prisoner_dilemma pour obtenir les
        # gains de chaque joueur selon leur choix pendant le tour
        outcome1, outcome2 = prisoner_dilemma(choice1, choice2)
        # donne à chaque joueur ses gains et l'information du
        # choix de l'adversaire
        player1.handle(outcome1, choice2)
        player2.handle(outcome2, choice1)
    # ajoute à la fin du match les scores gagnés pendant le match
    # aux scores totaux, qui peuvent être conservés après les matchs
    player1.totalscore += player1.score
    player2.totalscore += player2.score



def tournament(players: list, rounds: int):
    """_summary_

    Args:
        players (list): liste des joueurs participants aux tournois
        rounds (int): nombre de fois que le dilemme du prisonnier est itéré entre les joueurs 1 et 2 à chaque match
    """
    results = defaultdict(dict)
    for i, player1 in enumerate(players):
        # commence par faire un match entre le joueur et lui-même
        player2 = deepcopy(player1)
        match(player1, player2, rounds)
        # garde en mémoire les scores obtenus par les joueurs lors
        # de leur matchs
        results[player1.name][player2.name] = player1.score
        # fais les matchs avec les joueurs suivants de la liste
        for player2 in players[i+1:]:
            match(player1, player2, rounds)
            # garde en mémoire les scores obtenus par les joueurs lors
            # de leur matchs
            results[player1.name][player2.name] = player1.score
            results[player2.name][player1.name] = player2.score
    # affiche les résultats dans un tableau de scores obtenus par chaques
    # joueur face à chaque autres joueurs
    print(24*" " + " ".join([p1.name[0:3] for p1 in players]))
    for p1 in players:
        out = f"{p1.name:<23}"
        for p2 in players:
            out += f" {results[p1.name][p2.name]:>3}"
        print(out)
