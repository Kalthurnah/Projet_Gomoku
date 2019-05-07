from Projet_Gomoku import *
import numpy as np

def test_vide():
    # Exemple de test unitaire, à supprimer
    #Pour plus d'infos, cf pytest
    assert 0 == 0
    # assert distance([1,3],[4,3])==3

def test_grille_complete():
    grille_zeros=np.zeros((15,15),int)
    grille_ones=np.ones((15,15),int)
    grille_completes01=np.ones((15,15),int)
    grille_identite=np.eye((15),int)
    #grille_diag=np.diag([1,1,1,2,2,,])

    assert(grille_complete(grille_zeros)==False)
    assert(grille_complete(grille_ones)==True)


