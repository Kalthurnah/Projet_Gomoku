from Projet_Gomoku import *
import numpy as np


def test_verif_tour3():
    grille = np.zeros((15, 15), int)
    grille[1][3] = 2
    grille[7][7] = 1
    # Grille au 3e tour

    assert verif_tour3(grille, (1, 3)) == False
    assert verif_tour3(grille, (6, 4)) == False
    assert verif_tour3(grille, (0, 0)) == True


def test_conversion_pos_coord():
    assert conversion_pos_coord("A4") == (0, 3)
    assert conversion_pos_coord("B7") == (1, 6)
    assert conversion_pos_coord("O15") == (14, 14)
    assert conversion_pos_coord("D1") == (3, 0)
