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
    player1.prepare_for_new_game_against(player2)
    player2.prepare_for_new_game_against(player1)
    for tour in range(rounds):
        choice1 = player1.play(tour)
        choice2 = player2.play(tour)
        outcome1, outcome2 = prisoner_dilemma(choice1, choice2)
        player1.handle(outcome1, choice2)
        player2.handle(outcome2, choice1)

    player1.totalscore += player1.score
    player2.totalscore += player2.score


# Définition des tournois
from collections import defaultdict
def tournament(players: list, rounds: int):
    results = defaultdict(dict)
    for i, player1 in enumerate(players):
        player2 = deepcopy(player1)
        match(player1, player2, rounds)
        results[player1.name][player2.name] = player1.score
        for player2 in players[i+1:]:
            match(player1, player2, rounds)
            results[player1.name][player2.name] = player1.score
            results[player2.name][player1.name] = player2.score

    print(24*" " + " ".join([p1.name[0:3] for p1 in players]))
    for p1 in players:
        out = f"{p1.name:<23}"
        for p2 in players:
            out += f" {results[p1.name][p2.name]:>3}"
        print(out)
