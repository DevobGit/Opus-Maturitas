from axelrod import Tournament, TitForTat, Grudger, TitFor2Tats, FirstByDavis, FirstByDowning, FirstByNydegger, FirstByShubik, FirstBySteinAndRapoport, FirstByTidemanAndChieruzzi, SecondByBorufsen, SecondByColbert, SecondByGraaskampKatzen, SecondByGrofman, SecondByMikkelson, SecondByRichardHufford, SecondByRowsam, SecondByTester, SecondByTidemanAndChieruzzi, SecondByWeiner, SecondByWhite, SecondByYamachi, FirstByAnonymous, FirstByFeld, FirstByGraaskamp, FirstByTullock, Random, FirstByGrofman, FirstByJoss
from evolutive_strat import Evo

from unittest import TestCase

class TestEvo(TestCase):

    def test_evolutive_strat(self):
        
        stratlist = [
            TitForTat(),
            Random(),
            FirstByJoss(),
            FirstByGrofman(),
            FirstByTidemanAndChieruzzi(),
            FirstByNydegger(),
            FirstByShubik(),
            FirstBySteinAndRapoport(),
            Grudger(),
            FirstByDavis(),
            FirstByGraaskamp(),
            FirstByDowning(),
            FirstByFeld(),
            FirstByTullock(),
            FirstByAnonymous(),
            SecondByBorufsen(),
            SecondByGraaskampKatzen(),
            SecondByWeiner(),
            SecondByTidemanAndChieruzzi(),
            SecondByWhite(),
            SecondByYamachi(),
            SecondByColbert(),
            SecondByMikkelson(),
            SecondByRowsam(),
            TitFor2Tats(),
            SecondByGrofman(),
            SecondByTester(),
            SecondByRichardHufford()
        ]

        weightlist = []
        
        playerlist = [
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy()),
            Evo(stratlist
                ,weightlist.copy())
        ]
        
        for i in playerlist:
            for _ in stratlist :
                if len(i.weights) == playerlist.index(i) :
                    i.weights.append(1)
                elif (len(stratlist) != len(playerlist)) and (playerlist.index(i) > len(stratlist)) and(len(i.weights) == 0):
                    i.weights.append(1)
                else :
                    i.weights.append(0)
            print(i.weights)

        repet = 10
        
        tournament = Tournament(stratlist, repetitions=repet)
        results = tournament.play()

        evo_tournament = Tournament(playerlist, repetitions=repet)
        evo_results = evo_tournament.play()
        
        for i, score in enumerate(results.scores):
            for u in range(repet):
                self.assertAlmostEqual(score[u]/10000, evo_results.scores[i][u]/10000, delta=0.2)