from dilemma_definition import match, prisoner_dilemma, tournament
from player_and_strat import Betrayer, Cooperator, TitForTatLover

def test_dilemma():
    assert prisoner_dilemma(
        Cooperator, 
        Betrayer, 
        0) == (0, 5), "L'une face à l'autre, la coopération ne gagne rien et la trahison 5 points."
    # Vérifie que le coopérateur ne gagne rien et que le trahisseur gagne 5 points
    assert prisoner_dilemma(
        Betrayer, 
        Cooperator, 
        0) == (5, 0), "L'une face à l'autre, la coopération ne gagne rien et la trahison 5 points."
    # Vérifie que le coopérateur ne gagne rien et que le trahisseur gagne 5 points
    assert prisoner_dilemma(
        Betrayer, 
        Betrayer, 
        0) == (1, 1), "Quand chaque joueur trahit, ils ne reçoivent qu'un point."
    # Vérifie que les deux trahisseurs gagnent 1 point.
    assert prisoner_dilemma(
        Cooperator,
        Cooperator,
        0) == (3, 3), "Quand chaque joueur coopère, ils reçoivent trois points."
    # Vérifie que les deux cooperateurs gagnent 3 points.

def test_match():
    match(Cooperator, Betrayer, 20, False)
    assert Cooperator.score == 0, "coop. vs trahi. sur 20 tours a pour résultat 100-0 pour trahi."
    assert Betrayer.score == 100, "coop. vs trahi. sur 20 tours a pour résultat 100-0 pour trahi."
    # Vérifie les résultats d'un match de vingt tours

def test_tournament():
    tournament([Cooperator, Betrayer, TitForTatLover], 100, True)

test_dilemma()
test_match()
test_tournament()