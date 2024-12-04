# Fichier définissant des fonctions de tests pour les fonctions définies
# dans dilemma_definition

# import de la classe TestCase, classe parent des classes de tests
# définies dans ce fichier
from unittest import TestCase

# importe les fonctions à tester
from dilemma_definition import (
    match,
    prisoner_dilemma,
    tournament
)
# importe la classe joueur et trois classes de stratégies en provenance
# de player_and_strat, qui seront utilisées pour les tests
from player_and_strat import (
    Player,
    Stratcooperation,
    Stratbetrayal,
    Stratitat,
)

class TestGame(TestCase):
    """ Classe pour les tests des fonctions liées aux mécaniques
    du tournoi de dilemmes du prisonier itérés.

    Args:
        TestCase (_type_): classe parent des classes de tests
    """
    @classmethod
    def setUp(cls):
        # Crée des objets joueurs pouvant être utilisés dans toutes
        # les méthodes de classes
        cls.cooperator = Player("Cooperator", [Stratcooperation()])
        cls.betrayer = Player("Betrayer", [Stratbetrayal()])
        cls.tit_for_tat_lover = Player("Tit For Tat", [Stratitat()])

    def test_dilemma(self):
        """Teste si test_dilemma retourne les nombres de points gagnés
        correctes pour chaque couple de choix possibles.
        """
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
        """Teste si la fonction match donne les totaux de scores
        correct lors d'un match simple sur 20 tours entre
        cooperator et betrayer.
        """
        match(self.cooperator, self.betrayer, 20)
        self.assertEqual(self.cooperator.score, 0)
        self.assertEqual(self.betrayer.score, 100)

    def test_tournament(self):
        """Teste si la fonction tournament donne le classement de joueurs
        correct lors d'un tournoi entre betrayer, tit for tat, et cooperator,
        avec des matcsh sur 5 tours.
        """
        expected_ranking = ['Betrayer', 'Tit For Tat', 'Cooperator']
        players = [self.cooperator, self.betrayer, self.tit_for_tat_lover]
        tournament(players, 5)
        players = sorted(players, key=lambda player: player.totalscore, reverse=True)
        ranking = [p.name for p in players]
        self.assertEqual(ranking, expected_ranking)
