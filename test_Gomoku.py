from Projet_Gomoku import *


def test_conversion_pos_coord():
    assert conversion_pos_coord(("A",4)) == (0,3)
    assert conversion_pos_coord(("B",7)) == (1,6)
    assert conversion_pos_coord(("O",1)) == (14,0)
