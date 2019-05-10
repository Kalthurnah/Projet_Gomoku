from Projet_Gomoku import *

import pytest
from dataclasses import dataclass
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

    # Grille 0
    grille_zeros = np.zeros((15, 15), int)
    liste_infos_grilles.append(InfosGrille(grille=grille_zeros, est_complete=False, a_gagne=0))

    # Grille 1
    grille_ones = np.ones((15, 15), int)
    liste_infos_grilles.append(InfosGrille(grille=grille_ones, est_complete=True, a_gagne=1))

    # Grille 2
    grille_identite = np.eye(15, dtype=int)
    liste_infos_grilles.append(InfosGrille(grille=grille_identite, est_complete=False, a_gagne=1))

    # Grille 3
    grille_diag = np.diag([1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 0, 1, 0])
    liste_infos_grilles.append(InfosGrille(grille=grille_diag, est_complete=False, a_gagne=0))

    # Grille 4
    grille_presque_pleine = np.ones((15, 15), int)
    grille_presque_pleine[4][11] = 0
    liste_infos_grilles.append(InfosGrille(grille=grille_presque_pleine, est_complete=True, a_gagne=1))

    # Grille 5
    grille_presque_vide = np.zeros((15, 15), int)
    grille_presque_vide[7][1] = 1
    liste_infos_grilles.append(InfosGrille(grille=grille_presque_vide, est_complete=False, a_gagne=0))

    # Grille 6
    grille_gagne1_ligne = np.zeros((15, 15), int)
    grille_gagne1_ligne[14][14] = 1
    grille_gagne1_ligne[14][13] = 1
    grille_gagne1_ligne[14][12] = 1
    grille_gagne1_ligne[14][11] = 1
    grille_gagne1_ligne[14][10] = 1
    liste_infos_grilles.append(InfosGrille(grille=grille_gagne1_ligne, est_complete=False, a_gagne=1))

    # Grille 7
    grille_gagne2_colonne = np.zeros((15, 15), int)
    grille_gagne2_colonne[14][14] = 2
    grille_gagne2_colonne[13][14] = 2
    grille_gagne2_colonne[12][14] = 2
    grille_gagne2_colonne[11][14] = 2
    grille_gagne2_colonne[10][14] = 2
    liste_infos_grilles.append(InfosGrille(grille=grille_gagne2_colonne, est_complete=False, a_gagne=2))

    # Grille 8
    grille_gagne2_diag_bas_droite = np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, ],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, ], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, ],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, ], ], dtype=int)
    liste_infos_grilles.append(
        InfosGrille(grille=grille_gagne2_diag_bas_droite, est_complete=False, a_gagne=2))  # Grille 8

    # Grille 9
    grille_gagne1_diag_haut_gauche = np.array(
        [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, ], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, ],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, ], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, ],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], ], dtype=int)
    liste_infos_grilles.append(InfosGrille(grille=grille_gagne1_diag_haut_gauche, est_complete=False, a_gagne=1))

    # Grille 10
    grille_gagne2_diag_haut_droit = np.array(
        [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, ], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, ],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, ], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], ], dtype=int)
    liste_infos_grilles.append(InfosGrille(grille=grille_gagne2_diag_haut_droit, est_complete=False, a_gagne=2))

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
    grille = infos_grille.grille
    a_gagne = infos_grille.a_gagne
    assert grille_a_gagne(grille) == a_gagne
    print()


# Coordonnées à tester pour le test de verif_tour3, ainsi que leur resultat attendu
valeurs_tests_verif_tour3 = [((1, 3), False),
                             ((6, 4), False),
                             ((0, 0), True)]


@pytest.mark.parametrize('coordonnee, resultat_attendu', valeurs_tests_verif_tour3)
def test_verif_tour3(coordonnee, resultat_attendu):
    grille = np.zeros((15, 15), int)
    grille[1][3] = 2
    grille[7][7] = 1
    # Grille à un état de 3e tour

    assert verif_tour3(grille, coordonnee) == resultat_attendu


# Positions à tester pour le test de verif_tour3, ainsi que leur resultat attendu
valeurs_tests_conversion_pos_coord = [("A4", (0, 3)),
                                      ("B7", (1, 6)),
                                      ("O15", (14, 14)),
                                      ("D1", (3, 0))]


@pytest.mark.parametrize('position, resultat_attendu', valeurs_tests_conversion_pos_coord)
def test_conversion_pos_coord(position, resultat_attendu):
    assert conversion_pos_coord(position) == resultat_attendu


@pytest.mark.parametrize('entree_utilisateur, resultat_attendu', [("1", (1, 2)), ("2", (2, 1))])
def test_demander_couleur(monkeypatch, entree_utilisateur, resultat_attendu):
    # This simulates the user entering "Mark" in the terminal:
    monkeypatch.setattr('builtins.input', lambda x: entree_utilisateur)

    assert demander_couleur() == resultat_attendu


def test_creation_plateau():
    assert np.all(creation_plateau() == 0)
