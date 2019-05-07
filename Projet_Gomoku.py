# -*- coding utf-8 -*-
"""
Projet IA, Gomoku, Groupe TD A
@author: Damien ALOUGES, Amine AGOUSSAL, Cécile AMSALLEM
"""
vide_char = 0
def Gomoku():
    (IA_char,user_char)=demander_couleur()


def demander_couleur():
    print("Les noirs commencent. Veux tu être :")
    print("1 - Les noirs")
    print("2 - Les blancs")
    choix = input(">")

    if choix == 1:
        user_char= 1
        IA_char= 2
    else:
        user_char = 2
        IA_char = 1
    return (IA_char,user_char)


if __name__ == '__main__':
    # Appeler main ici
    exit()
