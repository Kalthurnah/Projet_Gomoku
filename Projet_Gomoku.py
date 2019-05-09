# -*- coding utf-8 -*-
"""
Projet IA, Gomoku, Groupe TD A
@author: Damien ALOUGES, Amine AGOUSSAL, Cécile AMSALLEM
"""

import numpy as np


def grille_complete(grille: {np.ndarray}):
    '''
    La fonction suivante renvoie un booléen représentant si la grille est complète ou non.

    :param grille: grille np.array d'entiers correspondant au plateau de jeu
    :return: Booléen True si la grille est complète, false sinon
    '''
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
        print("La grille est complète, le jeu est fini.")
    # On renvoie le résultat
    return res


#

def grille_a_gagne(grille: {np.ndarray}):
    '''
    Fonction indiquant si un joueur k a gagné.
    :param grille: grille np.array d'entiers correspondant au plateau de jeu
    :return: 0 si personne n'a gagné, 1 si le joueur 1 a gagné, 2 si le joueur 2 a gagné.
    '''
    cmpt = 0

    # Verification des gains par colonne, si qqn a 5 pions adjacents sur une même ligne
    for i in range(0, 15):
        for j in range(0, 14):
            # On regarde si la case et la suivante sont égales
            if grille[i][j] == grille[i][j + 1]:
                cmpt = cmpt + 1  # On incrémente le compteur si elles sont égales
            else:
                cmpt = 0  # Sinon on remet le compteur à 0
            # Si le compteur atteint 4, donc si on a 5 cases adjacentes identiques, on regarde si ce ne sont pas 5 zéros d'affilés.
            if cmpt == 4:
                # Si le symbole est différent de 0, quelqu'un a gagné, et on renvoie donc le gagnant, sinon on continue
                if grille[i][j] != 0:
                    print("Le jeu est fini, le joueur " + str(grille[i][j]) + " a gagné.")
                    return grille[i][j]
                # Si c'était 5 zéros à la suite, personne a gagné on remet le compteur à 0
                else:
                    cmpt = 0
    # On remet le compteur à 0 pour s'il n'a pas trouvé de fin de jeu avant.
    cmpt = 0

    # On vérifie de même les gains par lignes, ie si 5 cases adjacentes sont trouvées sur la même colonne
    for j in range(0, 15):
        for i in range(0, 14):
            if grille[i][j] == grille[i + 1][j]:
                cmpt = cmpt + 1
            else:
                cmpt = 0
            if cmpt == 4:
                if grille[i][j] != 0:
                    print("Le jeu est fini, le joueur " + str(grille[i][j]) + " a gagné.")
                    return grille[i][j]
                else:
                    cmpt = 0

    # Il s'agit maintenant de tester sur les diagonales. On remet encore le compteur à zéro.
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
    return 0


def conversion_pos_coord(position):
    (lettre, chiffre) = position  # On recupere lettre et chiffre depuis notre tuple position
    j = chiffre - 1
    L = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    i = -1
    for k in range(0, 15):
        if L[k] == lettre:
            i = k
    return (i, j)


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
    return (IA_char, user_char)


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
    print(user_char)
    # Fonctionnement du Gomoku ici


if __name__ == '__main__':
    # Appeler main ici
    (IA_char, user_char) = demander_couleur()
    Gomoku()
# Ne pas mettre de fonctions ci dessous !
