# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


def construireGrilleDemineur(nbLignes : int, nbCollones : int) -> list:
    """

    :param nbLignes:
    :param nbCollones:
    :return:
    """
    if nbLignes < 1 or nbCollones < 1:
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes {nbLignes} \
         ou de colonnes {nbCollones} est négatif ou nul.")
    if not type(nbLignes) == int or not type(nbCollones) == int:
        raise TypeError(f"construireGrilleDemineur : Le nombre de lignes {nbLignes} ou de colonnes {nbCollones} n’est pas un entier.")

    grille = []
    for i in range(nbLignes):
        Lignes = []
        for j in range(nbCollones):
            Lignes.append(construireCellule())
        grille.append(Lignes)
    return grille

def getNbLignesGrilleDemineur(grille : list) -> int:
    """

    :param grille:
    :return:
    """
    if not type_grille_demineur(grille):
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille.")
    return len(grille)

def getNbColonnesGrilleDemineur(grille : list) -> int:
    """

    :param grille:
    :return:
    """
    if not type_grille_demineur((grille)):
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille.")
    return len(grille[0])


def isCoordonneeCorrecte(grille : list, coord : tuple) -> bool:
    """

    :param grille:
    :param coord:
    :return:
    """
    if not type(grille) == list or not type(coord) == tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")

    res = False
    if coord[0] < len(grille) and coord[1] < len(grille[0]) and coord[0] >=0 and coord[1] >= 0:
        res = True
    return res

def getCelluleGrilleDemineur(grille : list, coord : tuple) -> dict:
    """

    :param grille:
    :param coord:
    :return:
    """
    if not type_grille_demineur(grille) or not type(coord) == tuple:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")
    return grille[coord[0]][coord[1]]

def getContenuGrilleDemineur(grille : list, coord : tuple) -> dict:
    """

    :param grille:
    :param coord:
    :return:
    """
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord))

def setContenuGrilleDemineur(grille : list, coord : tuple, contenu : int) -> None:
    """

    :param grille:
    :param coord:
    :param contenu:
    :return:
    """
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    return None

def isVisibleGrilleDemineur(grille : list, coord : tuple) -> bool:
    """

    :param grille:
    :param coord:
    :return:
    """
    res = False
    if isVisibleCellule(getCelluleGrilleDemineur(grille, coord)) == True:
        res = True
    return res

def setVisibleGrilleDemineur(grille : list, coord : tuple, visibilite : bool) -> None:
    """

    :param grille:
    :param coord:
    :param visibilite:
    :return:
    """
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visibilite)
    return None

def contientMineGrilleDemineur(grille : list, coord : tuple) -> bool:
    """

    :param grille:
    :param coord:
    :return:
    """
    res = False
    if contientMineCellule(getCelluleGrilleDemineur(grille, coord)):
        res = True
    return res

def getCoordonneeVoisinsGrilleDemineur(grille : list, coord : tuple) -> list:
    """

    :param grille:
    :param coord:
    :return:
    """
    lstCoordVoisin = []
    x = getLigneCoordonnee(coord)
    y = getColonneCoordonnee(coord)

    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")
    if not type_grille_demineur(grille) or not type(coord) == tuple:
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")

    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if isCoordonneeCorrecte(grille, (i, j)):
                lstCoordVoisin.append((i, j))
    lstCoordVoisin.remove((x, y))
    return lstCoordVoisin


