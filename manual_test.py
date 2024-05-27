import random
from tkinter import TRUE
from dilemma_definition import match, tournament
from player_and_strat import Allrandom, Betrayer, Cooperator, DavisLover, Hisui, Hoenn, Juliette, Ruben, TitForTatLover, Zahibra
# Fixer la graine aléatoire pour des résultats reproductibles
random.seed(6436)

# Faire un match
match(Hoenn,
      DavisLover,
      20,
      True)
#df.match(ps.Hoenn, ps.DavisLover, 20, True)

# Faire un tournoi

tournament(
    [
        DavisLover,
        Hisui,
        Hoenn, 
        Allrandom,
        Ruben,
        Zahibra,
        Juliette
    ], 
    20, 
    True
)

#match(TitForTatLover, TitForTatLover, 20, True)
print(tournament([Cooperator, Betrayer, TitForTatLover], 20, True))