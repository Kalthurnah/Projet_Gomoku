from Projet_Gomoku import *
import numpy as np

def test_vide():
    # Exemple de test unitaire, à supprimer
    #Pour plus d'infos, cf pytest
    assert 0 == 0
    # assert distance([1,3],[4,3])==3
    
def test_verif_tour3():
    grille = np.zeros((15,15),int)
    grille[1][3] = 2
    grille[7][7] = 1
    assert verif_tour3(grille, (1,3)) == False
    assert verif_tour3(grille,(6,4)) == False
    assert verif_tour3(grille,(0,0)) == True

    
def test_conversion_pos_coord():
    assert conversion_pos_coord(("A",4)) == (0,3)
    assert conversion_pos_coord(("B",7)) == (1,6)
    assert conversion_pos_coord(("O",1)) == (14,0)