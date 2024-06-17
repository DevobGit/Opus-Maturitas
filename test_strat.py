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
        self.assertEqual(grofman_lover.play(0), 0)

        grofman_lover.memory.append(1)
        grofman_lover.automemory.append(1)

        n = 10000
        m = 0
        for _ in range(n):
            choice = grofman_lover.play(0)
            grofman_lover.handle(0, 1)
            if choice == 0:
                m += 1

        self.assertTrue(m/n < 0.59)
        self.assertTrue(m/n > 0.58)

    def test_shubik(self):
        shubik = Stratshubik("Shubik")
        shubik_lover = Player("Shubik", [shubik])
        print("choice", shubik_lover.play(0))
        shubik_lover.handle(1, 1)
        print("choice", shubik_lover.play(1))
        shubik_lover.handle(1, 1)
        print("choice", shubik_lover.play(2))
        shubik_lover.handle(1, 1)
        print("choice", shubik_lover.play(3))
        shubik_lover.handle(1, 1)
        print("choice", shubik_lover.play(4))
        shubik_lover.handle(1, 1)
