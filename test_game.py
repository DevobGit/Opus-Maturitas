from dilemma_definition import match, prisoner_dilemma, tournament
from player_and_strat import (
    Player,
    Stratcooperation,
    Stratbetrayal,
    Stratitat,
)


from unittest import TestCase


class TestGame(TestCase):
    @classmethod
    def setUp(cls):
        cls.cooperator = Player("Cooperator", [Stratcooperation("Always Cooperate")])
        cls.betrayer = Player("Betrayer", [Stratbetrayal("Always Betray")])
        cls.tit_for_tat_lover = Player("Tit For Tat", [Stratitat("Tit For Tat")])

    def test_dilemma(self):
        self.assertEqual(
            prisoner_dilemma(self.cooperator, self.betrayer, 0),
            (0, 5)
        )

        self.assertEqual(
            prisoner_dilemma(self.betrayer, self.cooperator, 0),
            (5, 0)
        )

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

    # Vérifie les résultats d'un match de vingt tours
    def test_match(self):
        match(self.cooperator, self.betrayer, 20, False)
        self.assertEqual(self.cooperator.score, 0)
        self.assertEqual(self.betrayer.score, 100)

    def test_tournament(self):
        expected_ranking = [self.tit_for_tat_lover, self.cooperator, self.betrayer]
        ranking = tournament([self.cooperator, self.betrayer, self.tit_for_tat_lover], 100, False)
        self.assertEqual(
            ranking,
            expected_ranking
        )
