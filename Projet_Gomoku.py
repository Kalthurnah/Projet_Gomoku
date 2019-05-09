# -*- coding utf-8 -*-
"""
Projet IA, Gomoku, Groupe TD A
@author: Damien ALOUGES, Amine AGOUSSAL, Cécile AMSALLEM
"""

import numpy as np

# La fonction suivante renvoie un booléen représentant si la grille est complète ou non.
def grille_complete(grille):
    # On compte les cases que l'on rempli
    cmpt = 0
    res = False
    for i in range(0,15):
        for j in range(0,15):
            # Toutes celles différentes de 0 contiennent une case jouée.
            if grille[i][j] != 0 :
                cmpt = cmpt + 1
    # S'il y a 120 cases pleines alors la grille est complète puisqu'il n'y a plus de pions.
    if cmpt == 120 :
        res = True
        print("La grille est complète, le jeu est fini.")
    # On renvoie le résultat
    return res

# Le but de la fonction suivante est de savoir si le joueur k a gagné.
# La fonction renvoie 0 si personne n'a gagné, 1 si le joueur 1 a gagné, 2 si le joueur 2 a gagné.
def a_gagne(grille):
    cmpt = 0
    # On regarde d'abord sur les colonnes.
    for i in range (0,15):
        for j in range(0,14):
            # On regarde si le symbole et le suivant sont égaux
            if grille[i][j] == grille[i][j+1] :
                # On ajoute un au compteur si les deux symboles sont égaux
                cmpt = cmpt + 1
            else :
                # Sinon on remet le compteur à 0
                cmpt = 0
            # Si le compteur atteint 5, on regard si ce n'est pas 5 zéros d'affilés.
            if cmpt == 5 :
                # Si le symbole est différent de 0 on renvoie le symbole, sinon on continue
                if grille[i][j] != 0 :
                    print("Le jeu est fini, le joueur" + str(grille[i][j]) + "a gagné.")
                    return grille[i][j]
                # Si c'était 5 zéros à la suite on remet le compteur à 0
                else :
                    cmpt = 0
    # On remet le compteur à 0 pour s'il n'a pas trouvé de fin de jeu avant.
    cmpt = 0
    # On fait de même pour les lignes.
    for j in range(0,15) :
        for i in range(0,14) :
            if grille[i][j] == grille[i+1][j] :
                cmpt = cmpt + 1
            else :
                cmpt = 0
            if cmpt == 5:
                if grille[i][j] != 0 :
                    print("Le jeu est fini, le joueur" + grille[i][j] + "a gagné.")
                    return grille[i][j]
                else :
                    cmpt = 0
    # Il s'agit maintenant de tester sur les colonnes. On remet encore le compteur à zéros.
    cmpt = 0
    # On se limite à 0,11 car on ne doit pas dépasser les dimenseions de la grille !
    # On teste donc d'abord pour les diagonales allant d'en haut à gauche à en bas à droite.
    for i in range(0,11):
        for j in range(0,11):
            # On regarde si les 5 cases en diagonales (haut gauche vers bas droite) ont le même symbole
            if grille[i][j] == grille[i+1][j+1] and grille[i+1][j+1] == grille[i+2][j+2] :
                if grille[i+2][j+2] == grille[i+3][j+3] and grille[i+3][j+3]== grille[i+4][j+4] :
                    # Si c'est le cas on vérifie qu'il ne s'agit pas d'un zéro.
                    if grille[i][j] != 0:
                        print("Le jeu est fini, le joueur " + str(grille[i][j]) + " a gagné.")
                        return grille[i][j]
    # Maintenant on teste les diagonales allant du bas gauche vers le haut droit.
    for i in range(4,15):
        for j in range(0,11):
            # On regarde si les 5 cases en diagonales (haut gauche vers bas droite) ont le même symbole
            if grille[i][j] == grille[i-1][j+1] and grille[i-1][j+1] == grille[i-2][j+2] :
                if grille[i-2][j+2] == grille[i-3][j+3] and grille[i-3][j+3]== grille[i-4][j+4] :
                    # Si c'est le cas on vérifie qu'il ne s'agit pas d'un zéros.
                    if grille[i][j] != 0:
                        print("Le jeu est fini, le joueur " + str(grille[i][j]) + " a gagné.")
                        return grille[i][j]
    print("Le jeu n'est pas fini.")
    return grille[i][j]


vide_char = 0


def demander_couleur():
    print("Les noirs commencent. Veux tu être :")
    print("1 - Les noirs")
    print("2 - Les blancs")
    choix = input(">")

    if choix == 1:
        user_char= 1
        IA_char= 2
    else:
        user_char = 2
        IA_char = 1
    return (IA_char,user_char)


def Gomoku():
    (IA_char,user_char)=demander_couleur()


if __name__ == '__main__':
    # Appeler main ici
    exit()

