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
        player1.memory.append(choice2)
        player2.memory.append(choice1)
        player1.score += outcome1
        player2.score += outcome2


# Définition des tournois
def tournament(players: list, rounds: int):
    for i, player1 in enumerate(players):
        player1.reset_for_new_game()
        player2 = deepcopy(player1)
        player2.reset_for_new_game()

        match(player1, player2, rounds)
        player1.totalscore += player1.score

        for player2 in players[i+1:]:
            player1.reset_for_new_game()
            player2.reset_for_new_game()
            match(player1, player2, rounds)

            player1.totalscore += player1.score
            player2.totalscore += player2.score
