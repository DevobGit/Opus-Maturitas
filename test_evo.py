from axelrod import Tournament, Cooperator, Defector, TitForTat, Grudger
from evolutive_strat import Evo

from unittest import TestCase

class TestEvo(TestCase):
    @classmethod
    def setUp(cls):
        cls.cooperator = Evo([Cooperator()],[1], "Cooperator")
        cls.defector = Evo([Defector()],[1], "Defector")
        cls.titfortat = Evo([TitForTat()],[1], "TitForTat")
        cls.grudger = Evo([Grudger()],[1], "Grudger")

    def test_evolutive_strat(self):
        players = [Cooperator(), Defector(), TitForTat(), Grudger()]
        tournament = Tournament(players)
        results = tournament.play()

        evo_players = [self.cooperator, self.defector, self.titfortat, self.grudger]

        evo_tournament = Tournament(evo_players)
        evo_results = evo_tournament.play()
        
        self.assertEqual(results.scores, evo_results.scores)