import copy
import random
from axelrod.action import Action
from axelrod.player import Player
from axelrod.game import DefaultGame
C, D = Action.C, Action.D


class Evo(Player):
    """
    A player selects randomly a strategy at its disposal using
    the given weights. It can mutate to change its strategies
    and weights.
    Un joueur qui choisi aléatoirement l'une de ses stratégies à
    l'aide de poids. Il peut muter et changer ses poids. Créé à
    partir de la classe Player de la librairie Axelrod.
    https://github.com/Axelrod-Python/Axelrod/blob/dev/axelrod/player.py

    Names:

    - Evo
    """

    def __init__(self, strategies: list, weights: list):
        self.strategies = strategies
        self.weights = weights
        self.chosenstrategy = self.strategies[0]
        super().__init__()

    def mutate(self):
        new_weights = []
        for i in self.weights :
            if i == 0 and random.randint(1, 10) == 1 :
                i = 0.5
            elif i < 0.1 and random.randint(1, 10) == 1 :
                i = 0
            else :
                i *= random.uniform(0.8, 1.2)
            new_weights.append(i)
        # Vérifie qu'il existe au moins 1 élèment
        # non-nul dans la liste en remplaçant dans
        # le cas contraire un poid
        # aléatoire par sa valeur avant la mutation,
        # jusqu'à ce qu'un élèment ne soit plus nul.
        while new_weights.count(0) == len(new_weights):
            random_weight_to_restore = random.randint(0, len(new_weights) - 1)
            new_weights[random_weight_to_restore] = self.weights[random_weight_to_restore]
        self.weights = new_weights.copy()
        self.normalizeweights()

    def choosestrategy(self):
        self.chosenstrategy = random.choices(
            population=self.strategies,
            weights=self.weights,
            k=1
        )[0]

    def normalizeweights(self):
        total_of_weights = 0
        for i in self.weights :
            total_of_weights += i
        for i in self.weights :
            self.weights[self.weights.index(i)] /= total_of_weights

    name = "Evo"
    classifier = {
        "memory_depth": float("inf"),  # Long memory
        "stochastic": True,
        "long_run_time": True,
        "inspects_source": True,
        "manipulates_source": True,
        "manipulates_state": True,
    }

    def receive_match_attributes(self):
        for i in self.strategies:
            i.receive_match_attributes()
            
    def set_match_attributes(self, length=-1, game=None, noise=0):
        if not game:
            game = DefaultGame
        self.match_attributes = {"length": length, "game": game, "noise": noise}
        self.receive_match_attributes()
        
        for i in self.strategies:
            i.set_match_attributes()

    def strategy(self, opponent: Player) -> Action:
        """
        Choisi une stratégie au tour 1 et la garde pour le match
        """
        if len(self.history) == 0:
            self.choosestrategy()
        answer = self.chosenstrategy.strategy(opponent)
        return answer
    
    def clone(self):
        """Clones the player without history, reapplying configuration
        parameters as necessary. Et réapplique au joueur les effets de mutation."""

        cls = self.__class__
        new_player = cls(**self.init_kwargs)
        new_player.match_attributes = copy.copy(self.match_attributes)
        new_player.weights = self.weights
        return new_player

    def reset(self):
        for i in self.strategies:
            i.reset()

    def update_history(self, play, coplay):
        self.chosenstrategy.history.append(play, coplay)

    @property
    def history(self):
        return self.chosenstrategy._history

    # Properties maintained for legacy API, can refactor to self.history.X
    # in 5.0.0 to reduce function call overhead.
    @property
    def cooperations(self):
        return self.chosenstrategy._history.cooperations

    @property
    def defections(self):
        return self.chosenstrategy._history.defections

    @property
    def state_distribution(self):
        return self.chosenstrategy._history.state_distribution
