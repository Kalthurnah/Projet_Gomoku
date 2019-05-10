# -*- coding utf-8 -*-
"""
Projet IA, Gomoku (variante long pro), Groupe TD A
@author: Damien ALOUGES, Amine AGOUSSAL, Cécile AMSALLEM
"""

import minimax_modulable
import numpy as np

user_char = None
IA_char = None


def actions(state_grille, tour):
    '''
    Retourne les actions possibles d'un joueur à une grille de jeu, pour le Gomoku

    :param state_grille: grille du jeu
    :param tour: numero du tour actuel
    :return:actions possibles du joueur
    '''
    actions_possibles = []
    for j in range(0, 15):
        for i in range(0, 15):
            # Pour chaque case du jeu, si l'action est valide, on l'ajoute aux actions possibles
            if verif_validite_action(state_grille, (i, j), tour):
                actions_possibles.append((i, j))

    return actions_possibles


def terminal_test(state_grille):
    '''
    Teste si une grille donnée est en fin de jeu, pour le Gomoku

    :param state_grille:  état de la grille
    :return: soit le caractère du gagnant, soit 0 si il y a une égalité, soit -1 si l'état n'est pas terminal
    '''
    if grille_complete(state_grille):  # Grille complète, égalité
        return 0
    gagnant = grille_a_gagne(state_grille)
    if gagnant != 0:
        return gagnant  # Si quelqu'un a gagné, on retourne son caractère

    # Sinon, le jeu n'est pas fini, on retourne -1
    return -1


def heuristic(state_grille):
    '''
    Fournit une heuristique évaluant approximativement l'état de la grille pour le Gomoku

    :param state_grille:  état de la grille
    :return:Entier entre -99 et 99 représentant le gain approximatif de la grille
    '''
    # TODO
    return 0


def creation_plateau():
    plateau = np.zeros((15, 15), dtype=int)  # On crée une matrice 15x15 de 0
    return plateau


def afficher_plateau(grille):
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
        print(lettres[i], end='')
        for j in range(0, 15):
            # Puis on affiche toute la ligne de la grille
            if grille[i][j] == 0:
                print(' - ', end='')
            elif grille[i][j] == 1:  # Le joueur 1 joue les pions noir
                # Nous avons choisi ce symbole comme rond noir par rapport aux couleurs de la console
                # La console étant sur fond noir, la police est blanche et le rond apparait donc noir
                print(' ○ ', end='')
            else:
                # Et celui ci comme pion blanc
                print(' • ', end='')
            if j != 14:
                # On sépare deux cases par une barre verticale
                print('|', end='')
        print()
    return


def conversion_pos_coord(position: str):
    '''
    Convertit une position entrée par l'utilisateur sous la forme "A4" en un tuple coordonnées d'une grille, sous la forme (0,3)

    :param position: string de la forme "A4", contenant une lettre suivie d'un nombre.
    :return: un tuple correspondant aux coordonnées sur la grille de la position fournie. Si l'entrée est invalide, l'un des membres de ce tuple est -1.
    '''

    try:
        # On recupere lettre (1er char du string) et nombre (chars au dela du premier) depuis le string position donné
        (lettre, nombre) = (position[0], position[1:])
        colonne = int(nombre) - 1  # On tente de convertir le string du nombre en entier
    except:
        return (-1, -1)  # Si le caractère n'a pu être converti en entier ou pas pu être obtenu, on retourne -1,-1

    if (colonne < 0 | colonne >= 15):  # Si la colonne est supérieure ou égale à 15, ou inférieure à 0 elle est invalide
        colonne = -1  # On remplace alors la colonne par -1

    lettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    ligne = -1  # Coordonnée invalide par défaut
    for k in range(0, 15):
        if lettres[k] == lettre:
            ligne = k
            break  # Sortie de la boucle quand la lettre est trouvée

    return (ligne, colonne)


def grille_complete(grille: np.ndarray):
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
    # On renvoie le résultat
    return res


def grille_a_gagne(grille: np.ndarray):
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
                cmpt = cmpt + 1 # On incrémente le compteur si elles sont égales
            else:
                cmpt = 0   # Sinon on remet le compteur à 0
            # Si le compteur atteint 4, donc si on a 5 cases adjacentes identiques, on regarde si ce ne sont pas 5 zéros d'affilés.
            if cmpt == 4:
                # Si le symbole est différent de 0, quelqu'un a gagné, et on renvoie donc le gagnant, sinon on continue
                if grille[i][j] != 0:
                    return grille[i][j]
                # Si c'était 5 zéros à la suite, personne a gagné on remet le compteur à 0
                else:
                    cmpt = 0
            if j==13 :
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
                    return grille[i][j]
                else:
                    cmpt = 0
            if i == 13 :
                cmpt = 0

    # Il s'agit maintenant de tester sur les diagonales. On remet encore le compteur à zéro.
    cmpt = 0
    # On se limite à 0,11 car on ne doit pas dépasser les dimensions de la grille !
    # On teste donc d'abord pour les diagonales allant d'en haut à gauche à en bas à droite.
    for i in range(0, 11):
        for j in range(0, 11):
            # On regarde si les 5 cases en diagonales (haut gauche vers bas droite)sont identiques
            if grille[i][j] == grille[i + 1][j + 1] and grille[i + 1][j + 1] == grille[i + 2][j + 2] \
                    and grille[i + 2][j + 2] == grille[i + 3][j + 3] and grille[i + 3][j + 3] == grille[i + 4][j + 4]:
                # Si c'est le cas on vérifie qu'il ne s'agit pas d'un zéro.
                if grille[i][j] != 0:
                    return grille[i][j]
    # Maintenant on teste les diagonales allant du bas gauche vers le haut droit.
    for i in range(4, 15):
        for j in range(0, 11):
            # On regarde si les 5 cases en diagonales (bas gauche vers haut droite) sont identiques
            if grille[i][j] == grille[i - 1][j + 1] and grille[i - 1][j + 1] == grille[i - 2][j + 2] \
                    and grille[i - 2][j + 2] == grille[i - 3][j + 3] and grille[i - 3][j + 3] == grille[i - 4][j + 4]:
                # Si c'est le cas on vérifie qu'il ne s'agit pas d'un zéro.
                if grille[i][j] != 0:
                    return grille[i][j]
    return 0


def verif_tour3(grille, coordonnees):
    '''
    Fonction verifiant si un pion peut être placé à une coordonnée donnée lors du tour 3
    :param grille: grille du jeu
    :param coordonnees: coordonnées à jouer
    :return:
    '''
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


def verif_validite_action(grille, coordonnees, tour):
    if coordonnees[0] == -1 or coordonnees[1] == -1:  # Si les coordonnées ne sont pas valides, l'action non plus
        return False
    # Le premier tour est géré en dur dans le jeu, puisque le joueur n'a qu'un choix.
    if tour == 3:  # Si on est au tour 3 on vérifie la validité conformément au règles du tour 3
        if not verif_tour3(grille, coordonnees):
            return False
    # Si la coordonnée est valide jusqu'à maintenant, on vérifie si la case est bien vide
    return grille[coordonnees[0]][coordonnees[1]] == 0  # On retourne donc le booléen correspondant à cette égalité


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


def Gomoku():
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
            position_choisie_IA = 'undef'  # TODO : conversion_coord_pos(action_IA)
            print("\nL'ordinateur a joué en %s." %position_choisie_IA)
            joueur_actif = user_char

        else:  # joueur_actif == user_char:
            # tour joueur
            position_valide = False
            while not position_valide:  # Tant que la position n'est pas valide on en redemande une
                print("Entrer une position valide où placer votre pion :")
                position_choisie_user = input(">")
                action_user = conversion_pos_coord(position_choisie_user)  # On obtient les coordonnées correspondant à l'entrée utilisateur
                position_valide = verif_validite_action(grille_jeu, action_user, tour_actif)  # On vérif si elles sont valides et jouables
            grille_jeu = minimax_modulable.result(grille_jeu, action_user, user_char)  # On place le pion aux coordonnées demandées
            print("\nL'utilisateur a joué en %s." %position_choisie_user)
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
    '''
    Fonction chargeant le module minimax modulable et remplacant ses fonctions dépendant du jeu par celles du Gomoku.
    '''

    # On affecte les caractères des joueurs
    minimax_modulable.user_char = user_char
    minimax_modulable.IA_char = IA_char
    minimax_modulable.vide_char = 0
    # On affecte les fonctions spécifiques au jeu pour qu'elles soient utilisées par le minimax modulable
    minimax_modulable.actions = actions
    minimax_modulable.terminal_test = terminal_test
    minimax_modulable.heuristic = heuristic


grille_non_gagnante = np.array(
        [[2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], ], dtype=int)
    
grille_a_gagne(grille_non_gagnante)

if __name__ == '__main__':
    #Appeler main ici
    (user_char, IA_char) = demander_couleur()
    charger_minimax()

    Gomoku()
# Ne pas mettre de fonctions ci dessous !
