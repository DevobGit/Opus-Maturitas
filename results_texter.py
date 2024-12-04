def information_text(tournament_type: str, file_number: int, start_players : list, final_players: list, seed= None, special_notes=None):
    """_summary_

    Args:
        tournament_type (str): Type du tournoi ("Axelrod", "Remplacement_non_muté", "Remplacement_muté", "Moyenne", ou "Héritage)
        file_number (int): Numéro du tournoi, permettant de l'identifier et le différencier des autres. NE PAS UTILISER DE NUMÉRO DÉJÀ EXISTANT !
        start_players (list): Liste des joueurs tels qu'ils étaient au début du tournoi.
        final_players (list): Liste des joueurs à la dernière génération.
        seed (_type_, optional): Spécification possible d'une graine aléatoire utilisée. Defaults to None.
        special_notes (_type_, optional): Possibles notes sur le tournoi. Defaults to None.
    """
    
    with open(str("tournoi_de_type_" + str(tournament_type) + "_" + str(file_number) + ".txt").lower(), "w") as file:
        file.write((tournament_type) + "_" + str(file_number) + "\n" + "\n" + "Graine aléatoire : " + str(seed) + "\n" + "\n" + "Joueurs de départ :" + "\n")
        
        for player in start_players :
            file.write("\n" + "Joueur : " + str(player.name) + "\n")
            file.write("Stratégies : " + str(player.strategies) + "\n")
            file.write("Poids : " + str(player.weights) + "\n")
        
        file.write("\n" + "Joueurs Finaux :" + "\n")
        
        for player in final_players :
            file.write("\n" + "Joueur : " + str(player.name) + "\n")
            file.write("\n" + "Classement au dernier tournoi : " + str(player.rank) + "\n")
            file.write("Générations avec mutations " + str(player.generations_mutations) + "\n")
            file.write("Stratégies : " + str(player.strategies) + "\n")
            file.write("Poids : " + str(player.weights) + "\n")
        
        if tournament_type == "Axelrod" :
            file.write("\n" + "Type Axelrod :\nLe nombre de joueurs de type T dans la population au début de la génération G\nest égal au nombre total de points gagnés par les joueurs de type T dans la génération précédente G-1." + "\n")
        elif tournament_type == "Remplacement_non_muté" :
            file.write("\n" + "Type Remplacement_non_muté :\nÀ chaque nouvelle génération G, le joueur ayant gagné le moins\nde points en génération G-1 est remplacé par celui qui en a gagné le plus en génération G-1." + "\n")
        elif tournament_type == "Remplacement_muté" :
            file.write("\n" + "Type Remplacement_muté :\nÀ chaque nouvelle génération G, le joueur ayant gagné le moins de\npoints en génération G-1 est remplacé par une version de celui qui en a gagné le plus en génération G-1\ndont les poids ont subit une mutation aléatoire." + "\n")
        elif tournament_type == "Moyenne" :
            file.write("\n" + "Type Moyenne : À\nchaque nouvelle génération G, chaque joueur change ses poids en la moyenne\nde ses poids avec ceux du joueur ayant gagné le plus de points en génération G-1." + "\n")
        elif tournament_type == "Héritage" :
            file.write("\n" + "Type Héritage : À\nchaque nouvelle génération G, chaque joueur change son poid X en la moyenne\nde son poid avec celui du joueur ayant gagné le plus de points en génération G-1, le poid X étant\nle poid le plus élevé du gagnant, sont trait le plus spécifique" + "\n")
        elif tournament_type == "Remplacement_muté_x12" :
            file.write("\n" + "Type Remplacement_muté_x12 :\nÀ chaque nouvelle génération G, les 12 joueurs ayant gagné le moins de\npoints en génération G-1 sont remplacés par des versions des 12 qui en ont gagné le plus en génération G-1\ndont les poids ont subit une mutation aléatoire." + "\n")
        
        if special_notes is not None :
            file.write("\n" + "Notes particulières : " + "\n" + str(special_notes) + "\n")
        
        file.close()