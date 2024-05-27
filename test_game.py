#python3 -m unittest
from dilemma_definition import match, prisoner_dilemma, tournament
from player_and_strat import (
    Player,
    Stratcooperation,
    Stratbetrayal,
    Stratitat,
)


from unittest import TestCase, main


class TestGame(TestCase):
    @classmethod
    def setUp(cls):
        cls.cooperator = Player("Cooperator", [Stratcooperation("Always Cooperate")])
        cls.betrayer = Player("Betrayer", [Stratbetrayal("Always Betray")])
        cls.tit_for_tat_lover = Player("Tit For Tat", [Stratitat("Tit For Tat")])

    def test_dilemma(self):
        self.assertEqual(
            prisoner_dilemma(self.cooperator, self.betrayer, 0),
            (0, 5), "L'une face à l'autre, la coopération ne gagne rien et la trahison 5 points."
        )

        self.assertEqual(
            prisoner_dilemma(self.betrayer, self.cooperator, 0),
            (5, 0), "L'une face à l'autre, la coopération ne gagne rien et la trahison 5 points."
        )

        # Vérifie que le coopérateur ne gagne rien et que le trahisseur gagne 5 points
        assert prisoner_dilemma(
            self.betrayer,
            self.betrayer,
            0) == (1, 1), "Quand chaque joueur trahit, ils ne reçoivent qu'un point."
        # Vérifie que les deux trahisseurs gagnent 1 point.
        assert prisoner_dilemma(
            self.cooperator,
            self.cooperator,
            0) == (3, 3), "Quand chaque joueur coopère, ils reçoivent trois points."
        # Vérifie que les deux cooperateurs gagnent 3 points.

    # Vérifie les résultats d'un match de vingt tours
    def test_match(self):
        match(self.cooperator, self.betrayer, 20, False)
        self.assertEqual(self.cooperator.score, 0, "coop. vs trahi. sur 20 tours a pour résultat 100-0 pour trahi.")
        self.assertEqual(self.betrayer.score, 100, "coop. vs trahi. sur 20 tours a pour résultat 100-0 pour trahi.")

    def test_tournament(self):
        expected_ranking = ['Betrayer', 'Tit For Tat', 'Cooperator']
        ranking = tournament([self.cooperator, self.betrayer, self.tit_for_tat_lover], 5, False)
        self.assertEqual(
            ranking,
            expected_ranking
        )

if __name__ == '__main__':
    main()

