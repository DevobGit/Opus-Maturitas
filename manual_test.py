import random
from dilemma_definition import tournament, match
from player_and_strat import Player, Stratanonymous, Stratfeld, Stratgraaskamp, Stratgrofman, Stratgrudger, Stratjoss, Stratlist, Stratrandom, Stratcooperation, Stratbetrayal, Stratitat, Stratotitat, Stratdavis, Stratshubik, Stratsteinandrapoport, Strattidemanandchieruzzi, Strattullock

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
tullock = Strattullock("Tullock")
graaskamp = Stratgraaskamp("Graaskamp")
stein_and_rapoport = Stratsteinandrapoport("Stein and Rapoport")
tideman_and_chieruzzi = Strattidemanandchieruzzi("Tideman and Chieruzzi")
shubik = Stratshubik("Shubik")
feld = Stratfeld("Feld")
anonymous = Stratanonymous("Anonymous")

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
tullock_lover = Player("Tullock", [tullock])
graaskamp_lover = Player("Graaskamp", [graaskamp])
stein_and_rapoport_lover = Player("Stein and Rapoport", [stein_and_rapoport])
tideman_and_chieruzzi_lover = Player("Tideman and Chieruzzi", [tideman_and_chieruzzi])
shubik_lover = Player("Shubik", [shubik])
feld_lover = Player("Feld", [feld])
anonymous_lover = Player("Anonymous", [anonymous])

# Fixer la graine aléatoire pour des résultats reproductibles
#random.seed(6436)
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

"""
Tournoi avec les participants du premier tournoi d'Axelrod, ceux suivis d'un #! sont soumis à de
possibles erreurs dans l'interprétation du fonctionnement de leur stratégie.
Fait 5 répétitions du tournoi pour lisser les effets aléatoires, tel que dans
le premier tournoi d'Axelrod.
"""

for _ in range(5) :
    tournament(
        [
            tit_for_tat_lover,
            tideman_and_chieruzzi_lover, #!
            #nydegger_lover,
            grofman_lover,
            shubik_lover, #!
            stein_and_rapoport_lover,
            grudger_lover,
            davis_lover,
            graaskamp_lover,
            #downing_lover,
            feld_lover, #!
            joss_lover,
            tullock_lover,
            anonymous_lover, #!
            all_random,
            
        ], 
        200, 
        True
    )
"""
anonymous_lover.nullifyscore()
anonymous_lover.nullifytotalscore()
tideman_and_chieruzzi_lover.nullifytotalscore()
tideman_and_chieruzzi_lover.nullifyscore()
tideman_and_chieruzzi_lover.erasememory()
match(anonymous_lover, tit_for_tat_lover, 200, True)
"""