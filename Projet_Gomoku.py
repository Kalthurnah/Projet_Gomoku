# -*- coding utf-8 -*-
"""
Projet IA, Gomoku, Groupe TD A
@author: Damien ALOUGES, Amine AGOUSSAL, Cécile AMSALLEM
"""

import numpy as np


def conversion_pos_coord(position):
    '''
    Convertit une position entrée par l'utilisateur sous la forme "A4" en un tuple coordonnées d'une grille, sous la forme (0,3)
    :param position: string de la forme "A4", contenant une lettre et un chiffre.
    :return: un tuple correspondant aux coordonnées sur la grille de la position fournie. Si l'entrée est invalide, l'un des membres de ce tuple est -1.
    '''

    (lettre, chiffre) = (position[0], position[1])  # On recupere lettre et chiffre depuis le string position donné

    try:
        colonne = int(chiffre) - 1
    except:
        colonne = -1  # Si le charactère n'a pu être converti en entier, on le passe à -1
    if (colonne >= 15):  # Si la colonne est supérieure ou égale à 15, elle est invalide
        colonne = -1  # On remplace j par -1

    lettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    ligne = -1  # Coordonnée invalide par défaut
    for k in range(0, 15):
        if lettres[k] == lettre:
            ligne = k
            break  # Sortie de la boucle quand la lettre est trouvée

    return (ligne, colonne)
    # TODO : Verif à l'utilisation si (i==-1 ou j == -1), auquel cas la position fournie par l'utilisateur est invalide.


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
