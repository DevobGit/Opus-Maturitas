import random
from dilemma_definition import match, tournament
from player_and_strat import Player, Stratgrofman, Stratgrudger, Stratjoss, Stratlist, Stratrandom, Stratcooperation, Stratbetrayal, Stratitat, Stratotitat, Stratdavis

nice_double_change = Stratlist("Nice Double Change", [0, 0, 1, 1])
mean_change = Stratlist("Mean Change", [1, 0])
nice_change = Stratlist("Nice Change", [0, 1])
roll_the_dice = Stratrandom("Roll The Dice")
always_cooperate = Stratcooperation("Always Cooperate")
always_betray = Stratbetrayal("Always Betray")
tit_for_tat = Stratitat("Tit For Tat")
tit_for_two_tat = Stratotitat("Tit For Two Tat")
grudger = Stratgrudger("Grudger")
davis = Stratdavis("Davis")
grofman = Stratgrofman("Grofman")
joss = Stratjoss("Joss")

# Créer objets joueurs

hoenn = Player("Hoenn", [tit_for_tat, tit_for_two_tat, roll_the_dice])
hisui = Player("Hisui", [grudger, tit_for_tat])
davis_lover = Player("Davis Lover", [davis])
all_random = Player("All Random", [roll_the_dice])
ruben = Player("Ruben", [mean_change])
zahibra = Player("Zahibra", [grudger, roll_the_dice])
juliette = Player("Juliette", [davis, tit_for_tat])
cooperator = Player("Cooperator", [always_cooperate])
betrayer = Player("Betrayer", [always_betray])
tit_for_tat_lover = Player("Tit For Tat", [tit_for_tat])
alternator = Player("Alternator", [nice_change])
grudger_lover = Player("Grudger", [grudger])
grofman_lover = Player("Grofman", [grofman])
joss_lover = Player("Joss", [joss])
# Fixer la graine aléatoire pour des résultats reproductibles
random.seed(6436)

# Faire un match
"""
match(hoenn,
      davis_lover,
      20,
      True)
match(hoenn, davis_lover, 20, True)
"""
# Faire un tournoi
"""
tournament(
    [
        davis_lover,
        hisui,
        hoenn, 
        all_random,
        ruben,
        zahibra,
        juliette
    ], 
    20, 
    True
)
"""
#match(TitForTatLover, TitForTatLover, 20, True)
#print(tournament([Cooperator, Betrayer, TitForTatLover], 20, True))

#tournoi avec les joueur d'Axelrod
tournament(
    [
        tit_for_tat_lover,
        #tideman_and_chieruzzi_lover,
        #nydegger_lover,
        grofman_lover,
        #shubik_lover
        #stein_and_rapoport_lover,
        grudger_lover,
        davis_lover,
        #graaskamp_lover,
        #downing_lover,
        #feld_lover,
        joss_lover,
        #tullock_lover,
        #anonymous_lover,
        all_random,
        
    ], 
    20, 
    True
)
