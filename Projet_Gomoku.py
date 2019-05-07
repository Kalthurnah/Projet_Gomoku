# -*- coding utf-8 -*-
"""
Projet IA, Gomoku, Groupe TD A
@author: Damien ALOUGES, Amine AGOUSSAL, Cécile AMSALLEM
"""

import numpy as np

def creation_plateau():
    plateau = np.zeros((15,15),dtype=int)
    return plateau

def Gomoku():
    (IA_char,user_char)=demander_couleur()


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
    return (IA_char, user_char)

def Gomoku():

    print(user_char)

if __name__ == '__main__':
    # Appeler main ici
    (IA_char, user_char) = demander_couleur()
    Gomoku()
