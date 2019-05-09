# -*- coding utf-8 -*-
"""
Projet IA, Gomoku (variante long pro), Groupe TD A
@author: Damien ALOUGES, Amine AGOUSSAL, Cécile AMSALLEM
"""

import numpy as np

user_char = None
IA_char = None


def conversion_pos_coord(position: str):
    '''
    Convertit une position entrée par l'utilisateur sous la forme "A4" en un tuple coordonnées d'une grille, sous la forme (0,3)

    :param position: string de la forme "A4", contenant une lettre suivie d'un nombre.
    :return: un tuple correspondant aux coordonnées sur la grille de la position fournie. Si l'entrée est invalide, l'un des membres de ce tuple est -1.
    '''

    (lettre, nombre) = (position[0], position[1:])
    # On recupere lettre (1er char du string) et nombre (chars au dela du premier) depuis le string position donné

    try:
        colonne = int(nombre) - 1  # On tente de convertir le string du nombre en entier
    except:
        colonne = -1  # Si le charactère n'a pu être converti en entier, on le passe à -1
    if (colonne < 0 | colonne >= 15):  # Si la colonne est supérieure ou égale à 15, ou inférieure à 0 elle est invalide
        colonne = -1  # On remplace alors la colonne par -1

    lettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    ligne = -1  # Coordonnée invalide par défaut
    for k in range(0, 15):
        if lettres[k] == lettre:
            ligne = k
            break  # Sortie de la boucle quand la lettre est trouvée

    return (ligne, colonne)


# La fonction suivante renvoie un booléen représentant si la grille est complète ou non.
def grille_complete(grille):
    # On compte les cases que l'on rempli
    cmpt = 0
    res = False
    for i in range(0, 15):
        for j in range(0, 15):
            # Toutes celles différentes de 0 contiennent une case jouée.
            if grille[i][j] != 0:
                cmpt = cmpt + 1
    # S'il y a 120 cases pleines alors la grille est complète puisqu'il n'y a plus de pions. (Chaque joueur en a 60)
    if cmpt >= 120:
        res = True
        print("La grille est complète, le jeu est fini.")
    # On renvoie le résultat
    return res


# Le but de la fonction suivante est de savoir si le joueur k a gagné.
# La fonction renvoie 0 si personne n'a gagné, 1 si le joueur 1 a gagné, 2 si le joueur 2 a gagné.
def a_gagne(grille):
    cmpt = 0
    # On regarde d'abord sur les colonnes.
    for i in range(0, 15):
        for j in range(0, 14):
            # On regarde si le symbole et le suivant sont égaux
            if grille[i][j] == grille[i][j + 1]:
                # On ajoute un au compteur si les deux symboles sont égaux
                cmpt = cmpt + 1
            else:
                # Sinon on remet le compteur à 0
                cmpt = 0
            # Si le compteur atteint 5, on regard si ce n'est pas 5 zéros d'affilés.
            if cmpt == 5:
                # Si le symbole est différent de 0 on renvoie le symbole, sinon on continue
                if grille[i][j] != 0:
                    print("Le jeu est fini, le joueur" + str(grille[i][j]) + "a gagné.")
                    return grille[i][j]
                # Si c'était 5 zéros à la suite on remet le compteur à 0
                else:
                    cmpt = 0
    # On remet le compteur à 0 pour s'il n'a pas trouvé de fin de jeu avant.
    cmpt = 0
    # On fait de même pour les lignes.
    for j in range(0, 15):
        for i in range(0, 14):
            if grille[i][j] == grille[i + 1][j]:
                cmpt = cmpt + 1
            else:
                cmpt = 0
            if cmpt == 5:
                if grille[i][j] != 0:
                    print("Le jeu est fini, le joueur" + grille[i][j] + "a gagné.")
                    return grille[i][j]
                else:
                    cmpt = 0
    # Il s'agit maintenant de tester sur les colonnes. On remet encore le compteur à zéros.
    cmpt = 0
    # On se limite à 0,11 car on ne doit pas dépasser les dimenseions de la grille !
    # On teste donc d'abord pour les diagonales allant d'en haut à gauche à en bas à droite.
    for i in range(0, 11):
        for j in range(0, 11):
            # On regarde si les 5 cases en diagonales (haut gauche vers bas droite) ont le même symbole
            if grille[i][j] == grille[i + 1][j + 1] and grille[i + 1][j + 1] == grille[i + 2][j + 2]:
                if grille[i + 2][j + 2] == grille[i + 3][j + 3] and grille[i + 3][j + 3] == grille[i + 4][j + 4]:
                    # Si c'est le cas on vérifie qu'il ne s'agit pas d'un zéro.
                    if grille[i][j] != 0:
                        print("Le jeu est fini, le joueur " + str(grille[i][j]) + " a gagné.")
                        return grille[i][j]
    # Maintenant on teste les diagonales allant du bas gauche vers le haut droit.
    for i in range(4, 15):
        for j in range(0, 11):
            # On regarde si les 5 cases en diagonales (haut gauche vers bas droite) ont le même symbole
            if grille[i][j] == grille[i - 1][j + 1] and grille[i - 1][j + 1] == grille[i - 2][j + 2]:
                if grille[i - 2][j + 2] == grille[i - 3][j + 3] and grille[i - 3][j + 3] == grille[i - 4][j + 4]:
                    # Si c'est le cas on vérifie qu'il ne s'agit pas d'un zéros.
                    if grille[i][j] != 0:
                        print("Le jeu est fini, le joueur " + str(grille[i][j]) + " a gagné.")
                        return grille[i][j]
    print("Le jeu n'est pas fini.")
    return grille[i][j]


def creation_plateau():
    plateau = np.zeros((15, 15), dtype=int)  # On crée une matrice 15x15 de 0
    return plateau


def demander_couleur():
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


def verif_tour3(grille, coordonnees):
    res = True
    (i, j) = coordonnees
    # La position est déjà converti en coordonnées dans la grille
    if grille[i][j] != 0:
        res = False
    else:
        # On vérifie la distance au centre de coordonnées (7,7)
        distance = abs(7 - i) + abs(7 - j)
        if distance < 7:
            res = False
    return res


def Gomoku():
    print("L'ordinateur sera le J%s. Vous serez le J%s. Veuillez patienter." % (IA_char, user_char))
    state_grille = creation_plateau()  # On initialise le plateau
    joueur_actif = 1  # On initialise le 1er joueur comme étant le joueur actif.
    tour_actif = 1  # On initialise le numéro du tour

    # Fonctionnement du Gomoku ici
    while terminal_test(state_grille) == False:  # Tant que le jeu n'est pas fini

        if joueur_actif == IA_char:  # tour IA :
            action_IA = minimax_modulable.minimax(state_grille, IA_char)[1]  # Action choisie par l'IA suite à l'algo du minimax
            state_grille = minimax_modulable.result(state_grille, action_IA, IA_char)  # On place le pion aux coordonnées demandées
            position_choisie_IA = conversion_coord_pos(action_IA)
            print("\nL'ordinateur a joué en %s.", position_choisie_IA)
            joueur_actif = user_char

        else:  # joueur_actif == user_char:
            # tour joueur
            position_valide = False
            while not position_valide:  # Tant qu'une position valide n'a pas été renseignée, on en redemande une
                print("Entrer une position valide ou placer votre pion :")
                position_choisie_user = input(">")
                action_user = conversion_pos_coord(position_choisie_user)  # On obtient les coordonnées correspondant à l'entrée utilisateur
                if action_user[0] != -1 and action_user[1] != -1:  # Si les deux coordonnées sont valides
                    position_valide = True
            state_grille = minimax_modulable.result(state_grille, action_user, user_char)  # On place le pion aux coordonnées demandées
            print("\nL'utilisateur a joué en %s.", position_choisie_user)
            joueur_actif = IA_char

        # Quelqu'un a joué, on affiche avant de passer au tour suivant
        afficher_plateau(state_grille)
        tour_actif += 1

    joueur_gagnant = terminal_test(state_grille)
    print("Fin du jeu !")
    if (joueur_gagnant == True):
        print("Egalité entre vous !")
    else:
        print("Le J%s a gagné." % joueur_gagnant)


if __name__ == '__main__':
    # Appeler main ici
    (user_char, IA_char) = demander_couleur()
    Gomoku()
# Ne pas mettre de fonctions ci dessous !
