import player_and_strat as ps
import dilemma_definition as df

def test_always_cooperate():
    test = ps.Player("Player", [ps.always_cooperate])
    # Crée un joueur coopérant toujours
    for n in range(10) :
        assert test.play(n) == 0, "always_cooperate coopère toujours."
        # Vérifie sur 10 tours que le joueur coopère

def test_always_betray():
    test = ps.Player("Player", [ps.always_betray])
    # Crée un joueur trahissant toujours
    for n in range(10) :
        assert test.play(n) == 1, "always_cooperate coopère toujours."
        # Vérifie sur 10 tours que le joueur trahi

def test_tit_for_tat():
    test = ps.Player("Player", [ps.tit_for_tat])
    # Crée un joueur utilisant tit for tat
    control_list = ps.Stratlist("Control List", [0, 0, 1, 1, 0, 1, 0, 1, 1, 1])
    # Crée une strat suivant une liste de contrôle
    control = ps.Player("Control", [control_list])
    # Crée un joueur suivant la strat de contrôle
    df.match(test, control, 10, False)
    # Fait un match entre tit for tat et le contrôle
    assert control.memory == [0, 0, 0, 1, 1, 0, 1, 0, 1, 1], "[0, 0, 0, 1, 1, 0, 1, 0, 1, 1] est la liste attendue des coups joués par tit for tat contre [0, 0, 1, 1, 0, 1, 0, 1, 1, 1]."
    # Vérifie que les coups de tit for tat correspondent aux résultats attendus

test_always_cooperate()
test_always_betray()
test_tit_for_tat()