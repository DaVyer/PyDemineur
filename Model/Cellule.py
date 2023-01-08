# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)

def isContenuCorrect(a : int) -> bool:
    """

    :param a:
    :return:
    """
    res = False
    if type(a) == int:
        if (a >= 0 and a < 9) or a == const.ID_MINE:
            res = True
    return res

print(isContenuCorrect(10))

def construireCellule(contenu : int = 0, visibilite : bool = False) -> dict:
    """

    :param contenu:
    :param visibilite:
    :return:
    """
    if not isContenuCorrect(contenu):
        raise ValueError(f"construireCellule : le contenu {contenu} n’est pas correct")
    if type(visibilite) != bool:
        raise TypeError(f"construireCellule : le second paramètre {visibilite} n’est pas un booléen ")
    return {const.CONTENU : contenu, const.VISIBLE : visibilite}

print(construireCellule(0, False))




