import random
import dilemma_definition as df
import player_and_strat as ps
# Fixer la graine aléatoire pour des résultats reproductibles
random.seed(6436)

# Faire un match

df.match(ps.Hoenn, ps.DavisLover, 20, True)

# Faire un tournoi

df.tournament([ps.DavisLover, ps.Hisui, ps.Hoenn, ps.Allrandom, ps.Ruben, ps.Zahibra, ps.Juliette], 20, True)