from axelrod import Cooperator, Defector, TitForTat, Grudger
from ecological import evolutive_tournament
from evolutive_strat import Evo

stratlist = [
    Cooperator(),
    Defector(),
    TitForTat(),
    Grudger(),
]

weightlist = []

playerlist = [
    Evo(stratlist
        ,[1,0,0,0],
        "Cooperator"),
    Evo(stratlist
        ,[0,1,0,0],
        "Defector"),
    Evo(stratlist
        ,[0,0,1,0],
        "TirForTat"),
    Evo(stratlist
        ,[0,0,0,1],
        )
    ]

print("playerlist", playerlist)

evolutive_tournament(playerlist, 2, "Axelrod")
