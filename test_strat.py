from dilemma_definition import match
from player_and_strat import (
    Player,
    Stratanonymous,
    Stratcooperation,
    Stratbetrayal,
    Stratdavis,
    Stratfeld,
    Stratgraaskamp,
    Stratgrudger,
    Stratitat,
    Stratjoss,
    Stratlist,
    Stratgrofman,
    Stratnydegger,
    Stratrandom,
    Stratshubik,
    Stratsteinandrapoport,
    Strattidemanandchieruzzi,
    Strattullock
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
        match(shubik_lover, opponent, 20)
        self.assertEqual(
            opponent.memory,
            [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        )

    def test_joss(self):
        joss_lover = Player("Joss", [Stratjoss("Joss")])
        joss_lover.opponent = Player("Opponent", [Stratcooperation("Coop")])
        n = 10000
        match(joss_lover, self.cooperator, n)
        m = self.cooperator.memory.count(0)
        # la limite de m/n quand n tend vers l'infini devrait être 9/10
        self.assertTrue(m/n < 0.95)
        self.assertTrue(m/n > 0.85)

    def test_tullock(self):
        tullock_lover = Player("Tullock", [Strattullock("Tullock")])
        tullock_lover.opponent = Player("Opponent", [Stratcooperation("Coop")])
        n = 10000
        match(tullock_lover, self.cooperator, n)
        # les premiers 11 coups de tullock doivent être des coopérations
        for i in range(11):
            self.assertTrue(self.cooperator.memory[i] == 0)
        # compte le nombre de coopérations de tullock après les 11 premiers coups
        m = self.cooperator.memory[11:].count(0)
        # après les 11 premiers coups, tullock devrait coopérer à 90% de chance (dans la situation unique contre coop)
        self.assertTrue(m/(n-11) < 0.95)
        self.assertTrue(m/(n-11) > 0.85)

    def test_random(self):
        random_lover = Player("Random", [Stratrandom("Random")])
        random_lover.opponent = Player("Opponent", [Stratcooperation("Coop")])
        n = 10000
        match(random_lover, self.cooperator, n)
        m = self.cooperator.memory.count(0)
        # la limite de m/n quand n tend vers l'infini devrait être 1/2
        self.assertTrue(m/n < 0.55)
        self.assertTrue(m/n > 0.45)

    def test_feld(self):
        feld_lover = Player("Feld", [Stratfeld("Feld")])
        feld_lover.opponent = Player("Opponent", [Stratcooperation("Coop")])
        n = 200
        match(feld_lover, self.cooperator, n)
        # puisque les chances de coopérer baissent, il y aura plus de coopération la première moitié du match que la deuxième
        self.assertTrue(self.cooperator.memory[:int(n/2)].count(0) > (self.cooperator.memory[int(n/2):].count(0)))

    def test_grudger(self):
        grudger = Stratgrudger("Grudger")
        grudger_lover = Player("Grudger", [grudger])
        opponent = Player("Opponent", [Stratlist("TestGrudger", [0, 0, 0, 0, 0, 1, 1, 0, 0, 0])])
        match(grudger_lover, opponent, 10)
        self.assertEqual(
            opponent.memory,
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        )

    def test_davis(self):
        davis = Stratdavis("Davis")
        davis_lover = Player("Davis", [davis])
        opponent = Player("Opponent", [Stratlist("TestDavis", [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
        match(davis_lover, opponent, 20)
        self.assertEqual(
            opponent.memory,
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        )

    def test_graaskamp(self):
        graaskamp = Stratgraaskamp("Graaskamp")
        graaskamp_lover = Player("Graaskamp", [graaskamp])
        opponent = Player("Opponent", [Stratlist("TestGraaskamp", [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
        match(graaskamp_lover, opponent, 200)
        # pylint veut utiliser enumerate, mais cela retourne un tuple dont je ne souhaite que le 1er elmt
        for i in range(len(graaskamp_lover.memory)):
            # commence par coopérer
            if i == 0:
                self.assertEqual(opponent.memory[0], 0)
            # puis joue tit for tat jusqu'au 50e tour inclu
            elif i < 50:
                self.assertEqual(opponent.memory[i], graaskamp_lover.memory[(i-1)])
            # trahi au tour 51
            elif i == 50:
                self.assertEqual(opponent.memory[i], 1)
            # puis joue 5 tours de tit for tat
            elif i < 56:
                self.assertEqual(opponent.memory[i], graaskamp_lover.memory[(i-1)])

        # si graaskamp ne considère pas son adversaire random, et que son adversaire n'est pas son double
        # ou tit for tat, graaaskamp trahi tout les 5 à 15 tours, ce qui laisse le rapport de trahisons
        # par coopération dans l'intervalle [1/15: 1/5]
        if not graaskamp_lover.chosenstrat.opponent_is_random:
            self.assertTrue((opponent.memory[55:].count(1) / opponent.memory[55:].count(0)) <= (1/5))
            self.assertTrue((opponent.memory[55:].count(1) / opponent.memory[55:].count(0)) >= (1/15))

        # testons avec un adversaire consideré random:
        opponent2 = Player("Opponent2", [Stratlist("TestGraaskamp2", [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])])
        match(graaskamp_lover, opponent2, 200)
        for i in range(len(graaskamp_lover.memory)):
            # commence par coopérer
            if i == 0:
                self.assertEqual(opponent2.memory[0], 0)
            # puis joue tit for tat jusqu'au 50e tour inclu
            elif i < 50:
                self.assertEqual(opponent2.memory[i], graaskamp_lover.memory[(i-1)])
            # trahi au tour 51
            elif i == 50:
                self.assertEqual(opponent2.memory[i], 1)
            # puis joue 5 tours de tit for tat
            elif i < 56:
                self.assertEqual(opponent2.memory[i], graaskamp_lover.memory[(i-1)])
            elif graaskamp_lover.chosenstrat.opponent_is_random:
                self.assertEqual(opponent2.memory[i], 1)

        # testons avec tit for tat
        opponent3 = self.tit_for_tat_lover
        match(graaskamp_lover, opponent3, 200)
        for i in range(len(graaskamp_lover.memory)):
            # commence par coopérer
            if i == 0:
                self.assertEqual(opponent3.memory[0], 0)
            # puis joue tit for tat jusqu'au 50e tour inclu
            elif i < 50:
                self.assertEqual(opponent3.memory[i], graaskamp_lover.memory[(i-1)])
            # trahi au tour 51
            elif i == 50:
                self.assertEqual(opponent3.memory[i], 1)
            # puis joue tit for tat à jamais
            else:
                self.assertEqual(opponent3.memory[i], graaskamp_lover.memory[(i-1)])

        # testons avec un clone de lui-même
        opponent4 = Player("Opponent4", [graaskamp])
        match(graaskamp_lover, opponent4, 200)
        for i in range(len(graaskamp_lover.memory)):
            # commence par coopérer
            if i == 0:
                self.assertEqual(opponent4.memory[0], 0)
            # puis joue tit for tat jusqu'au 50e tour inclu
            elif i < 50:
                self.assertEqual(opponent4.memory[i], graaskamp_lover.memory[(i-1)])
            # trahi au tour 51
            elif i == 50:
                self.assertEqual(opponent4.memory[i], 1)
            # puis joue tit for tat à jamais
            else:
                self.assertEqual(opponent4.memory[i], graaskamp_lover.memory[(i-1)])

    def test_steinandrapoport(self):
        steinandrapoport_lover = Player("Tullock", [Stratsteinandrapoport("Steinandrapoport")])
        steinandrapoport_lover.opponent = Player("Opponent", [Stratcooperation("Coop")])
        match(steinandrapoport_lover, self.cooperator, 200)
        # les 4 premiers coups de Stein and Rapoport doivent être des
        # coopérations
        for i in range(len(steinandrapoport_lover.memory)):
            # commence par coopérer
            if i < 4:
                self.assertEqual(self.cooperator.memory[i], 0)
            elif i < 198:
                self.assertEqual(self.cooperator.memory[i], 0)
            else:
                self.assertEqual(self.cooperator.memory[i], 1)

        # testons avec random / une séquence alternante
        opponent = Player("Opponent", [Stratlist("Alternator", [0, 1])])
        match(steinandrapoport_lover, opponent, 200)
        # les 4 premiers coups de Stein and Rapoport doivent être des coopérations
        for i in range(len(steinandrapoport_lover.memory)):
            # commence par coopérer
            if i < 4:
                self.assertEqual(opponent.memory[i], 0)
            # joue tit for that avant le premier test
            elif i < 15:
                self.assertEqual(opponent.memory[i], steinandrapoport_lover.memory[(i-1)])
            else:
                self.assertEqual(opponent.memory[i], 1)

    def test_nydegger(self):
        nydegger = Stratnydegger("Nydegger")
        nydegger_lover = Player("Nydegger", [nydegger])
        opponent = Player("Opponent", [Stratlist("TestNydegger", [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])])
        match(nydegger_lover, opponent, 20)
        self.assertEqual(
            opponent.memory,
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        )
        opponent2 = Player("Opponent2", [Stratlist("TestNydegger2", [1, 0, 1])])
        match(nydegger_lover, opponent2, 3)
        self.assertEqual(opponent2.memory, [0, 1, 1])

    def test_tidemanandchieruzzi(self):
        tidemanandchieruzzi = Strattidemanandchieruzzi("Tideman and Chieruzzi")
        tidemanandchieruzzi_lover = Player("Tideman and Chieruzzi", [tidemanandchieruzzi])
        opponent = Player("Opponent", [Stratlist("TestTideman and Chieruzzi", [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0])])
        match(tidemanandchieruzzi_lover, opponent, 200)
        self.assertEqual(
            opponent.memory[:30],
            [0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
        )
        # trahi les deux derniers tours
        self.assertEqual(opponent.memory[-1], 1)
        self.assertEqual(opponent.memory[-2], 1)

    def test_anonymous(self):
        # Puisque anonymous a à chaque tour un pourcentage de chance de coopération
        # aléatoire entre 30% et 70%, cette stratégie aléatoire n'est biaisé
        # ni d'un coté ni de l'autre, et donc les résultats devraient être similaire
        # à un simple générateur aléatoire 50/50
        anonymous_lover = Player("Anonymous", [Stratanonymous("Anonymous")])
        anonymous_lover.opponent = Player("Opponent", [Stratcooperation("Coop")])
        n = 10000
        match(anonymous_lover, self.cooperator, n)
        m = self.cooperator.memory.count(0)
        # la limite de m/n quand n tend vers l'infini devrait être 1/2
        self.assertTrue(m/n < 0.55)
        self.assertTrue(m/n > 0.45)
