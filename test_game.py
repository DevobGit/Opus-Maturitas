from dilemma_definition import (
    match,
    prisoner_dilemma,
    tournament
)
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
        cls.cooperator = Player("Cooperator", [Stratcooperation()])
        cls.betrayer = Player("Betrayer", [Stratbetrayal()])
        cls.tit_for_tat_lover = Player("Tit For Tat", [Stratitat()])

    def test_dilemma(self):
        self.assertEqual(
            prisoner_dilemma(0, 1),
            (0, 5),
        )
        self.assertEqual(
            prisoner_dilemma(1, 0),
            (5, 0),
        )
        self.assertEqual(
            prisoner_dilemma(1, 1),
            (1, 1)
        )
        self.assertEqual(
            prisoner_dilemma(0, 0),
            (3, 3)
        )

    def test_match(self):
        match(self.cooperator, self.betrayer, 20)
        self.assertEqual(self.cooperator.score, 0)
        self.assertEqual(self.betrayer.score, 100)

    def test_tournament(self):
        expected_ranking = ['Betrayer', 'Tit For Tat', 'Cooperator']
        players = [self.cooperator, self.betrayer, self.tit_for_tat_lover]
        tournament(players, 5)
        players = sorted(players, key=lambda player: player.totalscore, reverse=True)
        ranking = [p.name for p in players]
        self.assertEqual(ranking, expected_ranking)
