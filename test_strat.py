from dilemma_definition import match
from player_and_strat import (
    Player,
    Stratcooperation,
    Stratbetrayal,
    Stratitat,
    Stratlist,
    Stratgrofman,
    Stratshubik
)

from unittest import TestCase


class TestStrat(TestCase):
    @classmethod
    def setUp(cls):
        cls.cooperator = Player("Cooperator", [Stratcooperation("Always Cooperate")])
        cls.betrayer = Player("Betrayer", [Stratbetrayal("Always Betray")])
        cls.tit_for_tat_lover = Player("Tit For Tat", [Stratitat("Tit For Tat")])
        cls.control_tit_for_tat_list = Player("Control", [Stratlist("Control List", [0, 0, 1, 1, 0, 1, 0, 1, 1, 1])])

    def test_always_cooperate(self):
        for n in range(10):
            self.assertEqual(self.cooperator.play(n), 0)

    def test_always_betray(self):
        for n in range(10):
            self.assertEqual(self.betrayer.play(n), 1)

    def test_tit_for_tat(self):
        match(self.tit_for_tat_lover, self.control_tit_for_tat_list, 10)
        self.assertEqual(
            self.control_tit_for_tat_list.memory,
            [0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
        )

    def test_grofman(self):
        grofman = Stratgrofman("Grofman")
        grofman_lover = Player("Grofman", [grofman])
        grofman_lover.opponent = Player("Opponent", [Stratcooperation("Coop")])
        self.assertEqual(grofman_lover.play(0), 0)

        grofman_lover.memory.append(1)
        grofman_lover.opponent.memory.append(0)

        n = 1000000
        m = 0
        for _ in range(n):
            grofman_lover.handle(0, 1)
            choice = grofman_lover.play(0)
            if choice == 0:
                m += 1
        # la limite de m/n quand n tend vers l'infini devrait être 2/7 ≈ 0,2857 
        self.assertTrue(m/n < 0.29)
        self.assertTrue(m/n > 0.27)

    def test_shubik(self):
        shubik = Stratshubik("Shubik")
        shubik_lover = Player("Shubik", [shubik])
        opponent = Player("Opponent", [Stratlist("TestShubik", [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0])])
        shubik_lover.opponent = opponent
        match(shubik_lover, opponent, 20)
        self.assertEqual(
            opponent.memory,
            [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        )
