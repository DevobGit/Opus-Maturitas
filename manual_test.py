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

roll_the_dice = Stratrandom()
tit_for_tat = Stratitat()
tit_for_two_tat = Stratotitat()
grudger = Stratgrudger()
davis = Stratdavis()
grofman = Stratgrofman()
joss = Stratjoss()
tullock = Strattullock()
graaskamp = Stratgraaskamp()
stein_and_rapoport = Stratsteinandrapoport()
tideman_and_chieruzzi = Strattidemanandchieruzzi()
shubik = Stratshubik()
feld = Stratfeld()
anonymous = Stratanonymous()
nydegger = Stratnydegger()
downing = Stratdowning()

# Créer objets joueurs
davis_lover = Player("Davis", [davis])
all_random = Player("Random", [roll_the_dice])
tit_for_tat_lover = Player("Tit For Tat", [tit_for_tat])
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
leur stratégie. Fait 5 répétitions du tournoi pour lisser les effets
aléatoires, tel que dans le premier tournoi d'Axelrod.
"""
players = [
    tit_for_tat_lover, # tested
    tideman_and_chieruzzi_lover,  # !
    nydegger_lover, # tested
    grofman_lover, # tested
    shubik_lover,  # ! # tested
    stein_and_rapoport_lover, # tested
    grudger_lover, # tested
    davis_lover, # tested
    graaskamp_lover, # tested
    downing_lover,
    feld_lover,  # ! # tested
    joss_lover, # tested
    tullock_lover, # tested
    anonymous_lover,  # !
    all_random, # tested
]

n_players = len(players)
n_tournaments = 1
n_rounds = 200
for _ in range(n_tournaments):
    tournament(players, n_rounds)


# trie les joueurs par ordre décroissant des scores
players = sorted(players, key=lambda player: player.totalscore, reverse=True)
print("Classement par scores:")
for player in players:  # Donne le score de chaque joueur dans l'ordre de la liste triée
    print(player.totalscore, int(player.totalscore/n_players/n_tournaments), player.name)
