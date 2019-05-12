# -*- coding utf-8 -*-
"""
Projet IA, Gomoku (variante long pro), Groupe TD A
@author: Damien ALOUGES, Amine AGOUSSAL, Cécile AMSALLEM
"""

import minimax_modulable
import numpy as np
from random import randint

user_char = None
IA_char = None



def actions_opti(state_grille: np.ndarray, tour: int, rayon=3):
    """
    Retourne les actions possibles d'un joueur à une grille de jeu, pour le Gomoku, en ne prenant en compte que les cas les plus probables,
    c'est à dire les cases comportant un pion dans un rayon donné aux alentours


    :param state_grille: grille du jeu
    :param rayon: rayon dans lequel on doit trouver des pions autour d'une case pour qu'elle soit jugée probable d'être jouée
    :param tour: numero du tour actuel
    :return: actions possibles du joueur
    """


    actions_possibles = []

    # Si on est en début de jeu, et que le tour est <=3 (c'est donc le premier tour jouable de l'IA ou du joueur),
    # Alors on ne peut pas vraiment prédire son jeu : On prend donc une action au hasard que l'on peut jouer selon les règles.
    if tour <= 3:
        (i, j) = (randint(0, 14), randint(0, 14))
        while not verif_validite_action(state_grille, (i, j), tour):
            # Tant que le coup n'est pas valide on reprend des nouvelles coordonnées
            (i, j) = (randint(0, 14), randint(0, 14))
        actions_possibles.append((i, j))

    # Sinon, on suppose que le joueur ne joue que dans des cases qui sont dans un rayon donné d'un pion déja joué.
    else:
        for i in range(0, 15):
            for j in range(0, 15):
                if state_grille[i][j] != 0:  # Si un pion est dans cette case
                    # On ajoute toutes les cases jouables dans un rayon de 4 cases autour de lui aux actions possibles,
                    # Ligne : On prend un intervalle de valeurs entre i-rayon et i+rayon inclus, en excluant les valeurs hors de la grille
                    for dist in range(0, rayon):
                        # pour chaque coordonnée de point à cette distance du point i,j en diagonale, colonne et ligne
                        for coordonnee in [(i - dist, j - dist), (i - dist, j + dist), (i + dist, j - dist), (i + dist, j + dist),
                                           (i + dist, j), (i - dist, j), (i, j - dist), (i, j + dist)]:
                            if verif_validite_action(state_grille, coordonnee, tour) and coordonnee not in actions_possibles:
                                actions_possibles.append(coordonnee)
                                # Si la coordonnées n'est pas déja dans la liste et est jouable, on la marque comme une action possible
    return actions_possibles


def actions(state_grille: np.ndarray, tour: int):
    """
    Retourne les actions possibles d'un joueur à une grille de jeu, pour le Gomoku

    :param state_grille: grille du jeu
    :param tour: numero du tour actuel
    :return: actions possibles du joueur
    """

    actions_possibles = []
    for i in range(0, 15):
        for j in range(0, 15):
            # Pour chaque case du jeu, si l'action est valide, on l'ajoute aux actions possibles
            if verif_validite_action(state_grille, (i, j), tour):
                actions_possibles.append((i, j))

    return actions_possibles


def terminal_test(state_grille: np.ndarray):
    """
    Teste si une grille donnée est en fin de jeu, pour le Gomoku

    :param state_grille:  état de la grille
    :return: soit le caractère du gagnant, soit 0 si il y a une égalité, soit -1 si l'état n'est pas terminal
    """
    if grille_complete(state_grille):  # Grille complète, égalité
        return 0
    gagnant = grille_a_gagne(state_grille)
    if gagnant != 0:
        return gagnant  # Si quelqu'un a gagné, on retourne son caractère

    # Sinon, le jeu n'est pas fini, on retourne -1
    return -1


def heuristic(state_grille: np.ndarray):
    """
    Fournit une heuristique évaluant approximativement l'état de la grille pour le Gomoku
    Ici, on compte le nombre de pions avantageux par joueur, c'est à dire le nombre de pions sur une ligne, colonne ou diagonale de 5 cases,
    qui ne sont pas bloqués par l'adversaire.

    :param state_grille:  état de la grille
    :return: Entier entre -infini et +infini exclus représentant le gain approximatif de la grille (son intêret, donc)
    """

    total_pions_gains_potentiels_IA = 0  # Total des pions avantageux pour l'IA, initialisé à 0
    total_pions_gains_potentiels_user = 0

    rayon = 5  # Rayon de test au dela duquel on arrete de compter les pions non bloqués.

    for i in range(0, 11):
        for j in range(0, 11):
            # On parcourt la grille de gauche à droite puis de bas en haut.
            # Il ne suffit donc de verifier que les 5 cases sur les lignes vers la droite, colonnes vers le bas, et diagonales vers la droite

            joueur_case = state_grille[i][j]  # Le joueur dont le pion est sur la case parcourue, ou 0 si la case est vide
            if joueur_case != 0:  # Si un pion est dans cette case

                # On initialise les compteur de pions potentiellements gagnants dans tous les sens

                compteur_pions_gains_potentiels_ligne = 1
                compteur_pions_gains_potentiels_col = 1
                compteur_pions_gains_potentiels_diaghd = 1
                compteur_pions_gains_potentiels_diagbd = 1
                # On compte toutes les cases dans un rayon de 4 cases autour de lui

                # Ligne : On prend un intervalle de valeurs entre i-rayon et i+rayon inclus, en excluant les valeurs hors de la grille
                for dist in range(1, rayon):
                    # On compte le nombre de pions sur les 5 prochaines cases de la diagonale vers le haut à droite
                    if i - dist >= 0 and j + dist < 15:  # Si la coordonnées est valide
                        if state_grille[i - dist][j + dist] == joueur_case:
                            # Si il y a un pion du joueur, on l'ajoute au compteur,
                            compteur_pions_gains_potentiels_diaghd += 1
                        elif state_grille[i - dist][j + dist] != 0:
                            # Si il y a un pion de son adversaire, on réinitialise le compteur à 0 car la diagonale est "inexploitable"
                            compteur_pions_gains_potentiels_diaghd = 0
                            break  # Et on arrete de chercher cette diagonale

                for dist in range(1, rayon):
                    # De meme, sur la diagonale bas droite
                    if i + dist < 15 and j + dist < 15:  # Si la coordonnées est valide
                        if state_grille[i + dist][j + dist] == joueur_case:
                            compteur_pions_gains_potentiels_diagbd += 1
                        elif state_grille[i + dist][j + dist] != 0:
                            compteur_pions_gains_potentiels_diagbd = 0
                            break

                for dist in range(1, rayon):
                    # De meme, sur la colonne descendante
                    if i + dist < 15:  # Si la coordonnées est valide
                        if state_grille[i + dist][j] == joueur_case:
                            compteur_pions_gains_potentiels_col += 1
                        elif state_grille[i + dist][j] != 0:
                            compteur_pions_gains_potentiels_col = 0
                            break

                for dist in range(1, rayon):
                    # De meme, sur la ligne vers la droite
                    if j + dist < 15:  # Si la coordonnées est valide
                        if state_grille[i][j + dist] == joueur_case:
                            compteur_pions_gains_potentiels_ligne += 1
                        elif state_grille[i][j + dist]:
                            compteur_pions_gains_potentiels_ligne = 0
                            break

                # Maintenant qu'on a fini de compter les pions potentiellement avantageux sur lignes colonnes diagonales, on les ajoute au compteur total de l'utilisateur
                if joueur_case == IA_char:
                    total_pions_gains_potentiels_IA += compteur_pions_gains_potentiels_ligne + compteur_pions_gains_potentiels_col + compteur_pions_gains_potentiels_diagbd + compteur_pions_gains_potentiels_diaghd
                else:
                    total_pions_gains_potentiels_user += compteur_pions_gains_potentiels_ligne + compteur_pions_gains_potentiels_col + compteur_pions_gains_potentiels_diagbd + compteur_pions_gains_potentiels_diaghd

            # Si pas de pion sur cette case, on continue

    return total_pions_gains_potentiels_IA - total_pions_gains_potentiels_user


def creation_plateau():
    """
    Initialise un plateau vide

    :return: Matrice numpy 15x15 remplie de 0
    """
    plateau = np.zeros((15, 15), dtype=int)  # On crée une matrice 15x15 de 0
    return plateau


def afficher_plateau(grille: np.ndarray):
    """
    Affiche un plateau donné sur la console

    :param grille: matrice du plateau à afficher
    """
    # On commence par afficher les numéros des colonnes
    print(' ', end='')
    for k in range(1, 16):
        if k < 10:  # On espace les chiffres plus que les nombres, pour qu'ils soient correctement placés au dessus de la grille
            # Le end='' permet de ne pas faire de retour à la ligne avant un print vide
            print(' ', end='')
        print(k, end='')
        print('  ', end='')
    print()
    # On stocke toutes les lettres dont on a besoin pour indexer le plateau
    lettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    for i in range(0, 15):
        # Pour chaque ligne, on affiche d'abord la lettre correspondante
        print(lettres[i], end=' |')
        for j in range(0, 15):
            # Puis on affiche toute la ligne de la grille
            if grille[i][j] == 0:
                print('   ', end='')
            elif grille[i][j] == 1:  # Le joueur 1 joue les pions noir
                # Nous avons choisi ce symbole comme rond noir par rapport aux couleurs de la console
                # La console étant sur fond noir, la police est blanche et le rond apparait donc noir
                print(' ○ ', end='')
            else:
                # Et celui ci comme pion blanc
                print(' • ', end='')
            # On sépare deux cases par une barre verticale
            print('|', end='')
        print()
    return


def conversion_pos_coord(position: str):
    """
    Convertit une position entrée par l'utilisateur sous la forme "A4" en un tuple coordonnées d'une grille, sous la forme (0,3)

    :param position: string de la forme "A4", contenant une lettre suivie d'un nombre.
    :return: un tuple correspondant aux coordonnées sur la grille de la position fournie. Si l'entrée est invalide, l'un des membres de ce tuple est -1.
    """

    try:
        # On recupere lettre (1er char du string) et nombre (chars au dela du premier) depuis le string position donné
        (lettre, nombre) = (position[0], position[1:])
        colonne = int(nombre) - 1  # On tente de convertir le string du nombre en entier
    except:
        return (-1, -1)  # Si le caractère n'a pu être converti en entier ou pas pu être obtenu, on retourne -1,-1

    if (colonne < 0 or colonne >= 15):  # Si la colonne est supérieure ou égale à 15, ou inférieure à 0 elle est invalide
        colonne = -1  # On remplace alors la colonne par -1

    lettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    ligne = -1  # Coordonnée invalide par défaut
    for k in range(0, 15):
        if lettres[k] == lettre:
            ligne = k
            break  # Sortie de la boucle quand la lettre est trouvée

    return (ligne, colonne)



def conversion_coord_pos(coordonnees: (int, int)):
    """
    Fonction qui pour un tuple de coordonnées retourne une position lisible

    :param coordonnees: tuple de coordonnées sous la forme (0,3)
    :return: chaine lisible sous la forme "A4"

    """
    
    coord1 = str(0)
    coord2 = 0

    coord1 = chr(coordonnees[0] + 65)
    coord2 = str((coordonnees[1] + 1))

    position = coord1 + coord2

    return position


def grille_complete(grille: np.ndarray):
    """
    La fonction suivante renvoie un booléen représentant si la grille est complète ou non.

    :param grille: grille np.array d'entiers correspondant au plateau de jeu
    :return: Booléen True si la grille est complète, false sinon
    """
    # On compte les cases déja jouées
    cmpt = 0
    res = False
    for i in range(0, 15):
        for j in range(0, 15):
            # Toutes celles différentes de 0 contiennent une case jouée.
            if grille[i][j] != 0:
                cmpt = cmpt + 1

    # S'il y a 120 cases pleines alors la grille est complète puisqu'il n'y a plus de pions.
    # Le cas ou l'on a plus de pions que 120 n'est pas supposé arriver, mais on vérifie quand même au cas ou quelque chose tourne mal, et pour pouvoir tester plus facilement
    if cmpt >= 120:
        res = True
    # On renvoie le résultat
    return res


def grille_a_gagne(grille: np.ndarray):
    """
    Fonction indiquant si un joueur k a gagné.

    :param grille: grille np.array d'entiers correspondant au plateau de jeu
    :return: 0 si personne n'a gagné, 1 si le joueur 1 a gagné, 2 si le joueur 2 a gagné.
    """

    # Verification des gains par colonne, si qqn a 5 pions adjacents sur une même ligne
    for i in range(0, 15):
        for j in range(0, 11):
            case = grille[i][j]
            if case != 0 and case == grille[i][j + 1] and case == grille[i][j + 2] and case == grille[i][j + 3] and case == grille[i][
                j + 4]:
                return case

    # On vérifie de même les gains par lignes, ie si 5 cases adjacentes sont trouvées sur la même colonne
    for j in range(0, 15):
        for i in range(0, 11):
            case = grille[i][j]
            if case != 0 and case == grille[i + 1][j] and case == grille[i + 2][j] and case == grille[i + 3][j] and case == grille[i + 4][
                j]:
                return case

    # Il s'agit maintenant de tester sur les diagonales.
    # On se limite à 0,11 car on ne doit pas dépasser les dimensions de la grille !
    # On teste donc d'abord pour les diagonales allant d'en haut à gauche à en bas à droite.
    for i in range(0, 11):
        for j in range(0, 11):
            # On regarde si les 5 cases en diagonales (haut gauche vers bas droite)sont identiques
            case = grille[i][j]
            if case != 0 and case == grille[i + 1][j + 1] and case == grille[i + 2][j + 2] \
                    and case == grille[i + 3][j + 3] and case == grille[i + 4][j + 4]:
                return case
    # Maintenant on teste les diagonales allant du bas gauche vers le haut droit.
    for i in range(4, 15):
        for j in range(0, 11):
            # On regarde si les 5 cases en diagonales (bas gauche vers haut droite) sont identiques
            case = grille[i][j]
            if case != 0 and case == grille[i - 1][j + 1] and case == grille[i - 2][j + 2] \
                    and case == grille[i - 3][j + 3] and case == grille[i - 4][j + 4]:
                return case
    return 0


def verif_tour3(grille: np.ndarray, coordonnees: (int, int)):
    """
    Fonction verifiant si un pion peut être placé à une coordonnée donnée lors du tour 3

    :param grille: grille du jeu
    :param coordonnees: coordonnées à jouer
    :return:
    """
    res = True
    (i, j) = coordonnees
    # La position est déjà convertie en coordonnées dans la grille
    if grille[i][j] != 0:
        res = False
    else:
        # On vérifie la distance au centre de coordonnées (7,7)
        distance = abs(7 - i) + abs(7 - j)
        if distance < 7:
            res = False
    return res


def verif_validite_coordonnees(coordonnees):
    """
    Indique si un tuple de coordonnées et valide (ie dans la grille) ou pas

    :param coordonnees: coordonnées à verifier
    :return: booléen vrai si les coordonnées sont valides
    """
    # Les coordonnées sont valides si elles sont entre 0 et 14 inclus, puisque la grille est 15x15
    return coordonnees[0] >= 0 and coordonnees[0] <= 14 and coordonnees[1] >= 0 and coordonnees[1] <= 14


def verif_validite_action(grille: np.ndarray, coordonnees: (int, int), tour: int = 0):
    """
    Vérifie si une action est valide ou pas

    :param grille: grille de jeu actuelle
    :param coordonnees: coordonnées de l'action que l'on veut jouer
    :param tour: numéro du tour actuel
    :return: booléen indiquant si l'action est valide
    """

    # Booléen indiquant si les conditions de validité sont respectées : Donc si les coordonnées sont valides et qu'il n'y a pas de pion ici
    validite_action = verif_validite_coordonnees(coordonnees) and grille[coordonnees[0]][coordonnees[1]] == 0

    # Le premier tour est géré en dur dans le jeu, puisque le joueur n'a qu'un choix.
    if tour == 3:  # Si on est au tour 3 on vérifie également la validité conformément au règles du tour 3
        # Si les règles du tour 3 ne sont pas respectées, l'action n'est pas valide, on ajoute donc au booléen la condition de validité du tour 3
        validite_action = validite_action and verif_tour3(grille, coordonnees)

    return validite_action  # On retourne donc le booléen correspondant à la réalisation de toutes les conditions  nécessaire


def demander_couleur():
    """
    Demande la couleur de son choix à l'utilisateur (les noirs ou les blancs)
    :return: tuple d'entiers correspondant respectivement au numéro de joueur de l'utilisateur, et au numéro de l'ordinateur.
    """
    print("Les noirs commencent. Veux tu être :")
    print("1 - Les noirs")
    print("2 - Les blancs")
    choix = input(">")

    if choix == "1":
        user_char = 1
        IA_char = 2
    else:
        user_char = 2
        IA_char = 1
    return (user_char, IA_char)


def Gomoku():
    """
    Fonction principale du jeu de Gomoku

    """
    
    print("Bienvenue. Pour gagner, il faut réussir à aligner 5 pions. Bonne chance 😏 !")

    print("Au premier tour, il n'est possible de jouer qu'au centre H8 - le 1er joueur voit donc son pion placé de force")
    print("L'ordinateur sera le J%s. Vous serez le J%s. " % (IA_char, user_char))
    grille_jeu = creation_plateau()  # On initialise le plateau
    grille_jeu[7][7] = 1  # On place un pion du premier joueur au centre
    afficher_plateau(grille_jeu)
    tour_actif = 2  # On initialise le numéro du tour à 2, le premier tour ayant été joué ci dessus
    joueur_actif = 2  # On initialise le 2eme joueur comme étant le joueur actif, le premier ayant joué de force ci dessus.

    print("Au 3e tour, il est possible de jouer n’importe où excepté dans un carré de taille 7 cases sur 7 cases de centre H8.")
    # Fonctionnement du Gomoku ici
    while terminal_test(grille_jeu) == -1:  # Tant que le jeu n'est pas fini

        if joueur_actif == IA_char:  # tour IA :
            print("L'ordinateur réfléchit.. Veuillez patienter.")
            action_IA = minimax_modulable.minimax(grille_jeu, IA_char, tour_actif)[1]  # Action choisie par l'IA suite à l'algo du minimax
            grille_jeu = minimax_modulable.result(grille_jeu, action_IA, IA_char)  # On place le pion aux coordonnées demandées
            position_choisie_IA = conversion_coord_pos(action_IA)
            print("\nL'ordinateur a joué en %s." % position_choisie_IA)
            joueur_actif = user_char

        else:  # joueur_actif == user_char:
            # tour joueur
            position_valide = False
            while not position_valide:  # Tant que la position n'est pas valide on en redemande une
                print("Entrer une position valide où placer votre pion :")
                position_choisie_user = input(">")
                action_user = conversion_pos_coord(position_choisie_user)  # On obtient les coordonnées correspondant à l'entrée utilisateur
                position_valide = verif_validite_action(grille_jeu, action_user, tour_actif)  # Vérif si les coord sont valides & jouables
            grille_jeu = minimax_modulable.result(grille_jeu, action_user, user_char)  # On place le pion aux coordonnées demandées
            print("\nL'utilisateur a joué en %s." % position_choisie_user)
            joueur_actif = IA_char

        # Quelqu'un a joué, on affiche avant de passer au tour suivant
        afficher_plateau(grille_jeu)
        tour_actif += 1
        print("Tour %s" % tour_actif)

    joueur_gagnant = terminal_test(grille_jeu)
    print("Fin du jeu !")
    if joueur_gagnant == 0:
        print("Egalité entre vous !")
    else:
        print("Le J%s a gagné." % joueur_gagnant)


def charger_minimax():
    """
    Fonction chargeant le module minimax modulable et remplacant ses fonctions dépendant du jeu par celles spécifiques au Gomoku.
    (Nos heuristiques, actions, et terminal_test customisés pour ce jeu, donc)
    """

    # On affecte les caractères des joueurs
    minimax_modulable.user_char = user_char
    minimax_modulable.IA_char = IA_char
    minimax_modulable.vide_char = 0
    # On affecte les fonctions spécifiques au jeu pour qu'elles soient utilisées par notre minimax modulable
    minimax_modulable.actions = actions_opti
    minimax_modulable.terminal_test = terminal_test
    minimax_modulable.heuristic = heuristic


if __name__ == '__main__':
    (user_char, IA_char) = demander_couleur()
    charger_minimax()  # Après le choix des couleurs, car on passe au minimax les chaines user_char et IA_char !
    Gomoku()
