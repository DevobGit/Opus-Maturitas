"""
from dilemma_definition import match
from player_and_strat import Player, always_cooperate, always_betray, tit_for_tat, Stratlist

def test_always_cooperate():
    test = Player("Player", [always_cooperate])
    # Crée un joueur coopérant toujours
    for n in range(10) :
        assert test.play(n) == 0, "always_cooperate coopère toujours."
        # Vérifie sur 10 tours que le joueur coopère

def test_always_betray():
    test = Player("Player", [always_betray])
    # Crée un joueur trahissant toujours
    for n in range(10) :
        assert test.play(n) == 1, "always_cooperate coopère toujours."
        # Vérifie sur 10 tours que le joueur trahi

def test_tit_for_tat():
    test = Player("Player", [tit_for_tat])
    # Crée un joueur utilisant tit for tat
    control_list = Stratlist("Control List", [0, 0, 1, 1, 0, 1, 0, 1, 1, 1])
    # Crée une strat suivant une liste de contrôle
    control = Player("Control", [control_list])
    # Crée un joueur suivant la strat de contrôle
    match(test, control, 10, False)
    # Fait un match entre tit for tat et le contrôle
    assert control.memory == [0, 0, 0, 1, 1, 0, 1, 0, 1, 1], "[0, 0, 0, 1, 1, 0, 1, 0, 1, 1] est la liste attendue des coups joués par tit for tat contre [0, 0, 1, 1, 0, 1, 0, 1, 1, 1]."
    # Vérifie que les coups de tit for tat correspondent aux résultats attendus

test_always_cooperate()
test_always_betray()
test_tit_for_tat()
"""

#python3 -m unittest
from dilemma_definition import match, prisoner_dilemma, tournament
from player_and_strat import (
    Player,
    Stratcooperation,
    Stratbetrayal,
    Stratitat,
    Stratlist,
)


from unittest import TestCase, main


class TestStrat(TestCase):
    @classmethod
    def setUp(cls):
        cls.cooperator = Player("Cooperator", [Stratcooperation("Always Cooperate")])
        cls.betrayer = Player("Betrayer", [Stratbetrayal("Always Betray")])
        cls.tit_for_tat_lover = Player("Tit For Tat", [Stratitat("Tit For Tat")])
        cls.control_tit_for_tat_list = Player("Control", [Stratlist("Control List", [0, 0, 1, 1, 0, 1, 0, 1, 1, 1])])

    def test_always_cooperate(self):
        for n in range(10) :
            self.assertEqual(
                self.cooperator.play(n),
                0 , "always_cooperate coopère toujours."
            )
            # Vérifie sur 10 tours que le joueur coopère
    
    def test_always_betray(self):
        for n in range(10) :
            self.assertEqual(
                self.betrayer.play(n),
                1 , "always_betray trahi toujours."
            )
            # Vérifie sur 10 tours que le joueur trahi
            
    def test_tit_for_tat(self):
        match(self.tit_for_tat_lover, self.control_tit_for_tat_list, 10, False)
        # Fait un match entre tit for tat et le contrôle
        self.assertEqual(
            self.control_tit_for_tat_list.memory,
            [0, 0, 0, 1, 1, 0, 1, 0, 1, 1], "[0, 0, 0, 1, 1, 0, 1, 0, 1, 1] est la liste attendue des coups joués par tit for tat contre [0, 0, 1, 1, 0, 1, 0, 1, 1, 1]."
        )
        # Vérifie que les coups de tit for tat correspondent aux résultats attendus
    

if __name__ == '__main__':
    main()

