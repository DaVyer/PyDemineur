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
    if not type_grille_demineur((grille)):
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille.")
    return len(grille[1])


def isCoordonneeCorrecte(grille : list, coord : tuple) -> bool:
    if not type(grille) == list or not type(coord) == tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")

    res = False
    for i in grille:
        if coord == grille[i]:
            res = True
    return res




