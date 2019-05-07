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

    grille_identite=np.eye(15,dtype=int)
    # complete = False, a_gagne = 0
    grille_diag=np.diag([1,1,1,2,2,2,2,1,2,1,2,1,0,1,0])
    # complete = False, a_gagne = 1
    grille_presque_complete = np.ones((15,15),int)
    grille_presque_complete[4][11] = 0
    # complete = False, a_gagne = 0
    grille_presque_vide = np.zeros((15,15),int)
    grille_presque_vide[7][1] = 1

    liste_grille_true=[grille_ones]
    liste_grille_false=[grille_zeros,grille_identite,grille_diag,grille_presque_complete,grille_presque_vide]

    for grille_true in liste_grille_false:
        assert(grille_complete(grille_true)==True)

    for grille_false in liste_grille_false:
        assert(grille_complete(grille_false)==False)

def test_grille_a_gagne():
    grille_gagne = [[2,1,0,2,1,2,2,1,2,1,1,1,0,1,0],[1,2,1,2,0,2,2,1,2,1,2,1,1,1,0],[1,2,1,2,2,1,0,1,2,1,2,0,0,1,0],[1,0,1,2,0,2,2,1,1,1,2,1,0,1,0],[2,2,1,2,0,0,2,1,0,1,2,1,0,1,0],[0,0,0,0,0,2,1,0,2,2,1,1,0,1,0],[1,1,1,2,2,2,2,1,2,1,2,1,0,1,0],[2,1,2,2,0,0,1,1,0,1,2,1,0,1,0],[2,0,1,2,1,1,0,1,2,1,2,1,0,1,0],[1,1,1,2,2,2,2,1,2,1,2,1,0,1,0],[1,1,1,2,2,2,2,1,2,1,2,1,0,1,0],[1,1,1,2,2,2,2,1,2,1,2,1,0,1,0],[1,1,0,2,0,0,2,1,2,1,2,0,0,1,0][1,1,1,2,1,2,2,1,2,1,2,1,1,1,1],[1,1,1,2,2,2,2,1,2,1,2,1,0,1,0]]

