from dilemma_definition import tournament, match
from player_and_strat import (
    Player,
    Stratanonymous,
    Stratdowning,
    Stratfeld,
    Stratgraaskamp,
    Stratgrofman,
    Stratgrudger,
    Stratjoss,
    Stratlist,
    Stratnydegger,
    Stratrandom,
    Stratcooperation,
    Stratbetrayal,
    Stratitat,
    Stratotitat,
    Stratdavis,
    Stratshubik,
    Stratsteinandrapoport,
    Strattidemanandchieruzzi,
    Strattullock
)

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
nydegger = Stratnydegger("Nydegger")
downing = Stratdowning("Downing")

# Créer objets joueurs

hoenn = Player("Hoenn", [tit_for_tat, tit_for_two_tat, roll_the_dice])
hisui = Player("Hisui", [grudger, tit_for_tat])
davis_lover = Player("Davis", [davis])
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
nydegger_lover = Player("Nydegger", [nydegger])
downing_lover = Player("Downing", [downing])


"""
Tournoi avec les participants du premier tournoi d'Axelrod, ceux suivis d'un #!
sont soumis à de possibles erreurs dans l'interprétation du fonctionnement de
leur stratégie.  Fait 5 répétitions du tournoi pour lisser les effets
aléatoires, tel que dans le premier tournoi d'Axelrod.
"""
players = [
    tit_for_tat_lover,
    tideman_and_chieruzzi_lover,  # !
    nydegger_lover,
    grofman_lover,
    shubik_lover,  # !
    stein_and_rapoport_lover,
    grudger_lover,
    davis_lover,
    graaskamp_lover,
    downing_lover,
    feld_lover,  # !
    joss_lover,
    tullock_lover,
    anonymous_lover,  # !
    all_random,
]

n_players = len(players)
n_tournaments = 5
n_rounds = 200
for _ in range(n_tournaments):
    tournament(players, n_rounds)


# trie les joueurs par ordre décroissant des scores
players = sorted(players, key=lambda player: player.totalscore, reverse=True)
print("Classement par scores:")
for player in players:  # Donne le score de chaque joueur dans l'ordre de la liste triée
    print(player.totalscore, int(player.totalscore/n_players/n_tournaments), player.name)