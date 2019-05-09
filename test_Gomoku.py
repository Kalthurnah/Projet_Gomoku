import pytest
from dataclasses import dataclass
from Projet_Gomoku import *
import numpy as np


@dataclass
class InfosGrille:
    """
    classe pour stocker une grille et les résultats qu'on attends d'elle
    """
    grille: np.ndarray
    est_complete: bool
    a_gagne: int


def generer_grilles_tests():
    liste_infos_grilles = []

    #Grille 0
    grille_zeros = np.zeros((15, 15), int)
    liste_infos_grilles.append(InfosGrille(grille=grille_zeros, est_complete=False, a_gagne=0))

    #Grille 1
    grille_ones = np.ones((15, 15), int)
    liste_infos_grilles.append(InfosGrille(grille=grille_ones, est_complete=True, a_gagne=1))

    #Grille 2
    grille_identite = np.eye(15, dtype=int)
    liste_infos_grilles.append(InfosGrille(grille=grille_identite, est_complete=False, a_gagne=1))

    #Grille 3
    grille_diag = np.diag([1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 0, 1, 0])
    liste_infos_grilles.append(InfosGrille(grille=grille_diag, est_complete=False, a_gagne=0))

    #Grille 4
    grille_presque_complete = np.ones((15, 15), int)
    grille_presque_complete[4][11] = 0
    liste_infos_grilles.append(InfosGrille(grille=grille_presque_complete, est_complete=False, a_gagne=1))

    #Grille 5
    grille_presque_vide = np.zeros((15, 15), int)
    grille_presque_vide[7][1] = 1
    liste_infos_grilles.append(InfosGrille(grille=grille_presque_vide, est_complete=False, a_gagne=0))

    # Pour ajouter une grille à la liste, la créer ci-dessous, et ajouter à liste_infos_grilles l'objet InfosGrille correspondant, cf exemples existants
    return liste_infos_grilles


liste_infos_grilles = generer_grilles_tests()


@pytest.mark.parametrize('infos_grille', liste_infos_grilles)
def test_grille_complete(infos_grille):
    grille = infos_grille.grille
    est_complete = infos_grille.est_complete
    assert (grille_complete(grille) == est_complete)


@pytest.mark.parametrize('infos_grille', liste_infos_grilles)
def test_a_gagne(infos_grille):
    # grille_gagne = np.array([[2, 1, 0, 2, 1, 2, 2, 1, 2, 1, 1, 1, 0, 1, 0],
    #                          [1, 2, 1, 2, 0, 2, 2, 1, 2, 1, 2, 1, 1, 1, 0],
    #                          [1, 2, 1, 2, 2, 1, 0, 1, 2, 1, 2, 0, 0, 1, 0],
    #                          [1, 0, 1, 2, 0, 2, 2, 1, 1, 1, 2, 1, 0, 1, 0],
    #                          [2, 2, 1, 2, 0, 0, 2, 1, 0, 1, 2, 1, 0, 1, 0],
    #                          [0, 0, 0, 0, 0, 2, 1, 0, 2, 2, 1, 1, 0, 1, 0],
    #                          [1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 0, 1, 0],
    #                          [2, 1, 2, 2, 0, 0, 1, 1, 0, 1, 2, 1, 0, 1, 0],
    #                          [2, 0, 1, 2, 1, 1, 0, 1, 2, 1, 2, 1, 0, 1, 0],
    #                          [1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 0, 1, 0],
    #                          [1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 0, 1, 0],
    #                          [1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 0, 1, 0],
    #                          [1, 1, 0, 2, 0, 0, 2, 1, 2, 1, 2, 0, 0, 1, 0],
    #                          [1, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1],
    #                          [1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 0, 1, 0],], dtype=int)
    grille = infos_grille.grille
    grille_a_gagne = infos_grille.a_gagne
    assert a_gagne(grille) == grille_a_gagne
    print()
