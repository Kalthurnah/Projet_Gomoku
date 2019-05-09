from Projet_Gomoku import *
import pytest
import numpy as np

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
