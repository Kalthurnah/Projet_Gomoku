from Projet_Gomoku import *
import numpy as np

def test_vide():
    # Exemple de test unitaire, à supprimer
    #Pour plus d'infos, cf pytest
    assert 0 == 0
    # assert distance([1,3],[4,3])==3

def test_grille_complete():
    # Complète = False, a_gagne = 0
    grille_zeros=np.zeros((15,15),int)
    # complete = True, a_gagne = 1
    grille_ones=np.ones((15,15),int)
    # complete = False, a_gagne = 1
    grille_identite=np.eye((15),int)
    
    #grille_diag=np.diag([1,1,1,2,2,,])
    
    # complete = False, a_gagne = 1
    grille_presque_complete = np.ones((15,15),int)
    grille_presque_complete[4][11] = 0
    # complete = False, a_gagne = 0
    grille_presque_vide = np.zeros((15,15),int)
    grille_presque_vide[7][1] = 1
    

    assert(grille_complete(grille_zeros)==False)
    assert(grille_complete(grille_ones)==True)

g

