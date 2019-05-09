# -*- coding utf-8 -*-
"""
Projet IA, Variante du minimax adaptable. Remplacer actions, terminal_test, et heuristic.
@author:Amine AGOUSSAL, Groupe TD A
"""

import numpy as np
import math

IA_char = None
user_char = None
vide_char = None


def actions(state_grille, tour=0):
    '''
    Retourne les actions possibles d'un joueur sur une grille de jeu. Modèle, à remplacer par une fonction spécifique au jeu !

    :param state_grille: grille du jeu
    :param tour: numero du tour actuel pour les jeux dont le tour influe sur les actions possibles
    :return: liste des actions possibles du joueur, sous la forme de tuple de coordonnées
    '''

    return [(-1, -1)]


def terminal_test(state_grille):
    '''
    Teste si une grille donnée est en fin de jeu. Modèle, à remplacer par une fonction spécifique au jeu !

    :param state_grille:  état de la grille
    :return: Soit le caractere du gagnant, soit True si il y a une égalité, soit False si l'état n'est pas terminal
    '''

    return False


def heuristic(state_grille):
    '''
    Fournit une heuristique évaluant approximativement l'état de la grille. Modèle, à remplacer par une heuristique spécifique au jeu!
    :param state_grille:  état de la grille
    :return: Entier entre -99 et 99 représentant le gain approximatif de la grille
    '''

    return 0


def result(state_grille, action, joueur):
    '''
    Applique une action d'un joueur à une grille de jeu
    :param state_grille: grille de l'état
    :param action: coordonnées de la case à jouer. Doit être jouable (vide) avant tout.
    :param joueur: joueur qui place la case
    :return: Nouvelle grille résultant de l'action appliquée
    '''
    result_grille = np.copy(state_grille)
    result_grille[action[0]][action[1]] = joueur
    return result_grille


def utility(state_grille):
    '''
    Fournit une évaluation de l'état de la grille. 100/-100 si l'un des joueurs gagne, et une valeur entre les deux si une heuristique est utilisée
    :param state_grille:  état de la grille
    :return: entier representant l'évaluation de la grille. Gain minimum si le joueur gagne, maximum si l'IA gagne
    '''
    fin = terminal_test(state_grille)

    if not fin:
        if fin == user_char:
            return -100  # Adversaire gagne : gain minimum
        if fin == IA_char:
            return 100  # IA gagne : gain maximum
        # Grille pleine sans gagnant :
        return 0

    else:
        # Si l'état n'est pas terminal, on utilise une heuristique
        return heuristic(state_grille)


def minimax(grille_state, joueur, tour=0, profondeur=5, borne_min=-math.inf, borne_max=math.inf):
    '''
    Algorithme principal du minimax. Vérifier que les fonctions heuristic, terminal_test, actions

    :param grille_state: grille de l'état actuel du jeu
    :param joueur: joueur lors de l'état actuel du jeu
    :param profondeur: maximum de profondeur de recherche du minimax
    :param tour: tour actuel du jeu, dans les jeux ou le tour influe sur les actions possibles
    :param borne_min:
    :param borne_max:
    :return:
    '''
    if terminal_test(grille_state) or profondeur == 0:
        return (utility(grille_state), None)

    if joueur == IA_char:
        # On initialise le maximum d'utilité trouvé, par défaut - l'infini, et l'action associée (None par défaut)
        (utility_max, action_max) = (-math.inf, None)

        for action in actions(grille_state, tour):
            grille_state_action = result(grille_state, action, joueur)
            utility_action = minimax(grille_state_action, user_char, tour + 1, profondeur - 1, borne_min, borne_max)[0]
            new_maxi = max(utility_max, utility_action)  # nouveau maximum entre le maximum et l'utilité de cette action
            if new_maxi != utility_max:  # Si le nouveau maximum est supérieur à l'ancien
                (utility_max, action_max) = (new_maxi, action)  # on met à jour l'utilité max et son action associée

            # Elagage alpha-beta v

            if (utility_max >= borne_max):
                # Si l'utilité trouvée est supérieure à la borne max, on sait qu'on a pas interet à ce qu'un tel coup
                # soit joué car on a déja trouvé de meilleures alternatives. On arrete donc la recherche de cet arbre
                return (utility_max, action_max)

            # Sinon, on change la borne minimale pour indiquer que l'on ignorera tous les résultats d'utilité inférieure à celui obtenu ici
            borne_min = max(borne_min, utility_max)

        return (utility_max, action_max)

    else:  # donc si joueur == User_Char:
        # On initialise le minimum d'utilité trouvé, par défaut + l'infini, et l'action associée (None par défaut)
        (utility_min, action_min) = (math.inf, None)

        for action in actions(grille_state, tour):
            grille_state_action = result(grille_state, action, joueur)
            utility_action = minimax(grille_state_action, IA_char, tour + 1, profondeur - 1, borne_min, borne_max)[0]
            new_mini = min(utility_min, utility_action)  # nouveau minimum entre le minimum et l'utilité de cette action
            if new_mini != utility_min:  # Si le nouveau minimum est inférieur à l'ancien,
                (utility_min, action_min) = (new_mini, action)  # on met à jour l'utilité min et son action associée

            # Elagage alpha-beta v

            if (utility_min <= borne_min):
                # Si l'utilité trouvée est inférieure à la borne min, on sait qu'on a pas interet à ce qu'un tel coup
                # soit joué car on a déja trouvé de meilleures alternatives. On arrete donc la recherche de cet arbre
                return (utility_min, action_min)

            # Sinon, on change la borne maximale pour indiquer que l'on ignorera tous les résultats d'utilité supérieure à celui obtenu ici
            # Car on considère que le joueur jouera le coup d'utilité la plus basse possible et ignorera les coups d'utilité supérieure
            borne_max = min(borne_max, utility_min)
        return (utility_min, action_min)