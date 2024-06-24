import random
import string
from scipy.stats import chisquare
from math import sqrt


class Player():
    # Définition de la classe des joueurs
    def __init__(self, name, strategies) -> None:
        # Le joueur a un nom et une liste de stratégies
        self.name = name
        self.strategies = strategies
        self.memory = []  # Le joueur initie une liste vide comme mémoire des coups adverses passés
        self.score = 0  # Le joueur démarre avec un score de 0
        self.totalscore = 0  # Le joueur démarre avec un score total de 0
        self.action = 0  # Cette variable correspond au dernier coup joué par le joueur
        self.chosenstrat = self.strategies[0]  # Cette variable correspond à la dernière stratégie choisie
        self.opponent = None

    def play(self, tour: int):
        """print()
        print("----")
        print("tour: ", tour)"""
        self.chosenstrat = random.choice(self.strategies)
        # Choix aléatoire de la stratégie, le choix des pourcentages de chance
        # de séléction reste à implémenter, mais n'est pas prioritaire puisque
        # néscessaire uniquement à partir de la quatrième étape de travail.
        if isinstance(self.chosenstrat, Stratlist):
            # Vérifie que la strat suit une liste, et lui indique le n. de tour
            self.action = self.chosenstrat.action(tour)
            return self.action
        self.action = self.chosenstrat.action(self)
        return int(self.action)

    def handle(self, outcome: int, choice: int):
        self.memory.append(choice)
        self.score += outcome

    def reset_for_new_game(self, opponent):
        self.score = 0
        self.opponent = opponent
        self.memory.clear()
        for i in self.strategies:
            i.reset_for_new_game()


# Définition des classes stratégies, le nom des classes sera sûrement changé à
# l'avenir pour correspondre aux noms originaux
class Strat():  # Classe des stratégie, elle... porte un nom !
    def __init__(self, name: string) -> None:
        self.name = name
        self.player = None

    def reset_for_new_game(self):
        pass


class Stratcooperation(Strat):
    # Coopère
    def action(self, player: Player):
        return 0


class Stratbetrayal(Strat):
    # Trahi
    def action(self, player: Player):
        return 1


class Stratrandom(Strat):
    # Agit aléatoirement à 50% de coopération
    def action(self, player: Player):
        return random.choice([0, 1])


class Stratlist(Strat):
    # Suit la liste de coups donné, revient au début lorsque la fin est atteinte
    def __init__(self, name: string, liste: list) -> None:
        super().__init__(name)
        self.list = liste

    def action(self, tour: int):
        return self.list[tour % len(self.list)]


class Stratitat(Strat):
    # Coopère puis repète l'action prècèdente de l'adversaire
    def action(self, player: Player):
        if not player.memory:
            return 0
        return player.memory[-1]


class Stratotitat(Strat):
    # Trahi uniquement si l'adversaire à trahi deux ou plus fois de suite
    def action(self, player: Player):
        if len(player.memory) >= 2 and player.memory[-1] == 1 and player.memory[-2] == 1:
            return 1
        return 0


class Stratgrudger(Strat):
    # Coopère jusqu'à ce que l'adversaire trahi, ne fait alors plus que trahir
    def action(self, player: Player):
        if 1 in player.memory:
            return 1
        return 0


class Stratdavis(Strat):
    # Coopère les 10 premiers tours puis joue grudger
    def action(self, player: Player):
        if len(player.memory) >= 10 and 1 in player.memory:
            return 1
        return 0


class Stratgrofman(Strat):
    # Si les joueurs ont agit différemment au dernier tour coopére avec 2/7 de
    # probabilité, sinon coopère
    def action(self, player: Player):
        if not player.memory or player.memory[-1] == player.opponent.memory[-1]:
            return 0
        return random.choices([0, 1], [2, 5])[0]


class Stratjoss(Strat):
    # joue tit for tat avec 90% de coopération au lieu de 100%
    def action(self, player: Player):
        if (not player.memory or player.memory[-1] == 0) and random.uniform(0, 1) <= 0.9:
            return 0
        return 1


class Strattullock(Strat):
    # Coopère les 11 premiers tours puis coopère 10% de moins que l'adversaire
    # les 10 derniers tours
    def action(self, player: Player):
        if len(player.memory) <= 10:
            return 0
        if random.randint(0, 100) <= (player.memory[-10:].count(0) * 10) - 10:
            return 0
        return 1


class Stratgraaskamp(Strat):
    # de https://axelrod.readthedocs.io/en/dev/_modules/axelrod/strategies/axelrod_first.html#FirstByGraaskamp
    def __init__(self, name: string, alpha: float = 0.05) -> None:
        super().__init__(name)

        self.alpha = alpha
        self.opponent_is_random = False
        self.next_random_defection_turn = None

    def reset_for_new_game(self):
        self.opponent_is_random = False
        self.next_random_defection_turn = None

    def action(self, player: Player):
        # Joue tit for tat les 55 premier tours sauf le 50 où il trahi
        if len(player.memory) < 56:
            if (not player.memory or player.memory[-1] == 0) and len(player.memory) != 50:
                return 0
            return 1
        """
        Vérifie si l'adversaire est aléatoire avec un Chi-squared test,
        facilement réalisable avec le module scipy, auquel cas trahi toujours
        """
        p_value = chisquare([player.memory.count(0), player.memory.count(1)]).pvalue
        # Ne fait pas le test si l'adversaire a déjà été considéré comme random
        self.opponent_is_random = (p_value >= self.alpha) or self.opponent_is_random
        # Vérifie si l'adversaire est un "clone" de lui même ou s'il est tit
        # for tat, auquel cas, joue tit for tat
        if (
            all(
                player.memory[i] == player.opponent.memory[i - 1]
                for i in range(1, len(player.opponent.memory))
            )
            or player.memory == player.opponent.memory
        ):
            if player.memory[-1] == 1:
                return 1
            return 0

        # trahi si adversaire random
        if self.opponent_is_random:
            return 1
        if self.next_random_defection_turn is None:
            # Vérifie si le prochain tour aléatoir de trahison a déjà été
            # choisi puis place la prochaine trahison à entre 4 et 14 tours
            # plus loins que le nombre de tours actuel (pour "trahir tout les 5
            # à 15 tours")
            self.next_random_defection_turn = random.randint(4, 14) + len(player.opponent.memory)

        if len(player.opponent.memory) == self.next_random_defection_turn:
            # Vérifie s'il est le tour de trahison puis choisi le prochain tour
            # de trahison
            self.next_random_defection_turn = random.randint(4, 14) + len(
                player.opponent.memory
            )
            return 1
        return 0


class Stratsteinandrapoport(Strat):
    # de https://axelrod.readthedocs.io/en/dev/_modules/axelrod/strategies/axelrod_first.html#FirstBySteinAndRapoport
    def __init__(self, name: string, alpha: float = 0.05) -> None:
        super().__init__(name)

        self.alpha = alpha
        self.opponent_is_random = False

    def reset_for_new_game(self):
        self.opponent_is_random = False

    def action(self, player: Player):
        """
        Dans un match de 200 tours, trahi les deux derniers tours.
        (Comportement en cas de matchs plus longs personnelement interprété,
        pourra changer plus tard, pour l'instant sans importance.
        """
        if not len(player.memory) >= 3:
            return 0

        if len(player.memory) % 199 == 0 or len(player.memory) % 199 == 198:
            return 1

        if len(player.memory) % 15 == 14:
            p_value = chisquare(
                [
                    player.memory.count(0),
                    player.memory.count(1)
                ]
            ).pvalue
            self.opponent_is_random = (p_value >= self.alpha)

        if self.opponent_is_random:
            return 1

        return player.memory[-1]


class Strattidemanandchieruzzi(Strat):
    # de https://axelrod.readthedocs.io/en/dev/_modules/axelrod/strategies/axelrod_first.html#FirstByTidemanAndChieruzzi
    def __init__(self, name: string) -> None:
        super().__init__(name)

        self.betraying = False
        self.betraying_turns = 0
        self.remaining_betrayals = 0
        # Alzheimer fait oublier les précédentes trahisons et recommencer comme au début du match
        self.last_alzheimer = -20
        self.alzheimer = False
        self.remembered_betrayals = 0

    def reset_for_new_game(self):
        self.betraying = False
        self.betraying_turns = 0
        self.remaining_betrayals = 0
        self.last_alzheimer = -20
        self.alzheimer = False
        self.remembered_betrayals = 0

    def decrease_remaining_betrays(self):
        # Réduit le compteur de trahisons, cesse de trahir s'il est nul
        if self.betraying:
            self.remaining_betrayals -= 1
            if self.remaining_betrayals == 0:
                self.betraying = False

    def forget(self):
        # Oublie tout pour redémarrer, partir loin et commencer une nouvelle
        # vie
        self.betraying = False
        self.betraying_turns = 0
        self.remaining_betrayals = 0
        self.remembered_betrayals = 0

    def action(self, player: Player):
        """
        Dans un match de 200 tours, trahi les deux derniers tours.
        (Comportement en cas de matchs plus longs personnelement interprété,
        pourra changer plus tard, pour l'instant sans importance.
        """
        if not player.memory:
            return 0

        if len(player.memory) % 199 == 0 or len(player.memory) % 199 == 198:
            return 1

        if player.memory[-1] == 1:
            self.remembered_betrayals += 1

        # Vérifie s'il y a eu alzheimer le tour précédent, pour offrir un
        # second tour de coopération
        if self.alzheimer:
            self.alzheimer = False
            return 0

        # Vérifie s'il faut tout oublier
        current_round = len(player.memory) + 1
        # Peut alzheimer s'il n'y en a pas encore eu
        if self.last_alzheimer == 0:
            valid_alzheimer = True
        # Il faut s'être passé au moins 20 tour depuis le dernier alzheimer
        else:
            valid_alzheimer = (current_round - self.last_alzheimer >= 20)

        # Il faut avoir au moins 10 points de plus que l'adversaire pour alzheimer
        if valid_alzheimer:
            valid_points = (player.score - player.opponent.score >= 10)
            valid_rounds = (current_round % 200 <= 190)
            """
            Dans un match de 200 tours, ne lance pas alzheimer s'il reste moins
            de 10 tours.  (Comportement en cas de matchs plus longs
            personnelement interprété, pourra changer plus tard, pour l'instant
            sans importance.
            """
            opponent_is_cooperating = (player.memory[-1] == 0)
            if valid_points and valid_rounds and opponent_is_cooperating:
                """
                La dernière condition pour donner une nouvelle chance à
                l'adversaire est:

                " if the number of defections differs from a 50-50 random
                generator by at least 3.0 standard deviations. "

                """
                # 50-50 split is based off the binomial distribution.
                N = len(player.memory)
                # std_dev = sqrt(N*p*(1-p)) where p is 1 / 2.
                std_deviation = sqrt(N) / 2
                lower = N / 2 - 3 * std_deviation
                upper = N / 2 + 3 * std_deviation
                if (
                    self.remembered_betrayals <= lower
                    or self.remembered_betrayals >= upper
                ):
                    # L'adversaire mérite que l'on oublie ses trahisons
                    self.last_alzheimer = current_round
                    self.forget()
                    self.alzheimer = True
                    return 0  # Première coopération après le redémmarage

        # Vérifie si la stratégie est dans une chaîne de trahison

        if self.betraying:
            self.decrease_remaining_betrays()
            return 1
        """
        Si l'adversaire vient de trahir, commence une chaîne de trahisons
        (dont le nombre augmente à chaque trahison adverse).
        """
        if player.memory[-1] == 1:
            self.betraying = True
            self.betraying_turns += 1
            self.remaining_betrayals = self.betraying_turns
            self.decrease_remaining_betrays()
            return 1

        return 0


class Stratshubik(Strat):
    def __init__(self, name: string) -> None:
        super().__init__(name)
        self.betraying = False
        self.betraying_turns = 0
        self.remaining_betrayals = 0

    def reset_for_new_game(self):
        self.betraying = False
        self.betraying_turns = 0
        self.remaining_betrayals = 0

    def decrease_remaining_betrays(self):
        # Réduit le compteur de trahisons, cesse de trahir s'il est nul
        if self.betraying:
            self.remaining_betrayals -= 1
            if self.remaining_betrayals == 0:
                self.betraying = False

    def action(self, player: Player):
        if not player.memory:
            return 0

        if self.betraying:
            # Vérifie si la stratégie est dans une chaîne de trahison
            self.decrease_remaining_betrays()
            return 1

        if player.memory[-1] == 1 and player.opponent.memory[-1] == 0:
            """
            Si l'adversaire a trahi au dernier tour alors que le joueur avait
            coopéré, commence une nouvelle chaîne de trahisons, plus longue que
            la dernière de une trahison
            """
            self.betraying = True
            self.betraying_turns += 1
            self.remaining_betrayals = self.betraying_turns
            self.decrease_remaining_betrays()
            return 1

        return 0


class Stratfeld(Strat):
    def __init__(
        self,
        name,
        start_coop_prob: float = 1.0,
        end_coop_prob: float = 0.5,
        rounds_of_decay: int = 200,
    ) -> None:
        super().__init__(name)
        self.start_coop_prob = start_coop_prob
        self.end_coop_prob = end_coop_prob
        self.rounds_of_decay = rounds_of_decay
        self.coop_prob = start_coop_prob

    def reset_for_new_game(self):
        self.coop_prob = self.start_coop_prob

    def reduce_prob(self):
        """
        Réduction de probabilité de coopération à chaque tour pour respecter le
        taux de dépard, de fin, et le nombre de tours sur lequel le taux baisse
        """
        self.coop_prob -= ((self.start_coop_prob - self.end_coop_prob) / (self.rounds_of_decay - 1))

    def action(self, player: Player):
        if not player.memory:
            self.reduce_prob()
            return 0
        if player.memory[-1] == 1:
            self.reduce_prob()
            return 1
        choice = random.choices([0, 1], weights=[self.coop_prob, 1 - self.coop_prob])[0]
        self.reduce_prob()
        return choice


class Stratanonymous(Strat):
    """
    Informations sur la stratégie quasi non-existantes, effet connu: la
    probabilité de coopération tombait fréquemment entre 30% et 70%.
    """
    def action(self, player: Player):
        r = random.uniform(3, 7)
        return random.choices([0, 1], cum_weights=[r, r + (10 - r)])[0]


class Stratnydegger(Strat):
    def __init__(self, name) -> None:
        self.abetray = [
            1, 6, 7, 17, 22, 23, 26, 29, 30, 31, 33, 38, 39, 45, 49, 54, 55,
            58, 61,
        ]
        super().__init__(name)

    def atotal(self, player: Player):
        first = 16*(player.opponent.memory[-1] + 2 * player.memory[-1])
        second = 4*(player.opponent.memory[-2] + 2 * player.memory[-2])
        third = player.opponent.memory[-1] + 2 * player.memory[-1]
        return first + second + third

    def action(self, player: Player):
        if len(player.memory) == 0:
            return 0
        if len(player.memory) == 1:
            return player.memory[-1]
        if len(player.memory) == 2:
            if player.memory[0:2] == [1, 0]:
                return 1
            else:
                return player.memory[-1]
        if self.atotal(player) in self.abetray:
            return 1
        return 0


class Stratdowning(Strat):
    # de https://axelrod.readthedocs.io/en/dev/_modules/axelrod/strategies/axelrod_first.html#FirstByDowning
    def __init__(self, name) -> None:
        super().__init__(name)
        self.number_opponent_cooperations_in_response_to_c = 0
        self.number_opponent_cooperations_in_response_to_d = 0

    def reset_for_new_game(self):
        self.number_opponent_cooperations_in_response_to_c = 0
        self.number_opponent_cooperations_in_response_to_d = 0

    def action(self, player: Player):
        round_number = len(player.memory) + 1

        if round_number == 1:
            return 1
        if round_number == 2:
            if player.memory[-1] == 0:
                self.number_opponent_cooperations_in_response_to_c += 1
            return 1

        if player.opponent.memory[-2] == 0 and player.memory[-1] == 1:
            self.number_opponent_cooperations_in_response_to_c += 1
        if player.opponent.memory[-2] == 0 and player.memory[-1] == 1:
            self.number_opponent_cooperations_in_response_to_d += 1

        alpha = self.number_opponent_cooperations_in_response_to_c / (
            player.opponent.memory.count(0) + 1
        )
        beta = self.number_opponent_cooperations_in_response_to_d / max(
            player.opponent.memory.count(1), 2
        )

        R, P, S, T = 3, 1, 0, 5
        expected_value_of_cooperating = alpha * R + (1 - alpha) * S
        expected_value_of_defecting = beta * T + (1 - beta) * P

        if expected_value_of_cooperating > expected_value_of_defecting:
            return 0
        if expected_value_of_cooperating < expected_value_of_defecting:
            return 1
        return ((player.opponent.memory[-1] + 1) % 2)
