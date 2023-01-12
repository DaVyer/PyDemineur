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
    Cette fonction permet de vérifier si l'entier rentré en paramètre représente bien le contenu d'une cellule.

    Si le contenu de la cellule représente bien un entier, la fonction renvoie True, sinon elle renvoie False.

    :param a: Entier passé en paramètre
    :return: Renvoie True si la cellule est bien comprise entre 0 et 8 compris ou si elle correspond à la constante ID_MINE
    """
    res = False
    if type(a) == int:
        if (a >= 0 and a < 9) or a == const.ID_MINE:
            res = True
    return res

def construireCellule(contenu : int = 0, visible : bool = False) -> dict:
    """
    Cette fonction permet de renvoyer un dictionnaire comprenant le contenu de la case et sa visibilité.

    Si le contenu n'est pas compris entre 0 et 8 inclus, une erreur de type ValueError apparait, et si la visibilité ne correspond pas à un
    booléen, la fonction renvoie une erreur de type TypeError.

    :param contenu: Variable représentant la valeur de la case, initialisé à 1.
    :param visibilite: Variable représentant la visibilité de la case, initialisé à False.
    :return: La fonction retourne un dictionnaire avec comme clé le contenu qui vaut au départ 0, visible qui au départ vaut False \
                    et annotation qui vaut None.
    """
    if not isContenuCorrect(contenu):
        raise ValueError(f"construireCellule : le contenu {contenu} n’est pas correct")
    if type(visible) != bool:
        raise TypeError(f"construireCellule : le second paramètre {type(visible)} n’est pas un booléen ")
    return {const.CONTENU : contenu, const.VISIBLE : visible, const.ANNOTATION : None}

def getContenuCellule(cell : dict) -> int:
    """

    :param cell:
    :return:
    """
    if not type_cellule(cell):
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return cell.get(const.CONTENU)

def isVisibleCellule(cell : dict) -> bool:
    """

    :param cell:
    :return:
    """
    if not type_cellule(cell):
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return cell.get(const.VISIBLE)

def setContenuCellule(cell : dict, x : int) -> None:
    """

    :param cell:
    :param x:
    :return:
    """
    if not type_cellule(cell):
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")
    if not type(x) == int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    if not isContenuCorrect(x):
        raise ValueError(f"setContenuCellule : la valeur du contenu {x} n’est pas correcte.")

    cell[const.CONTENU] = x
    return None

def setVisibleCellule(cell : dict, visible : bool) -> None:
    """

    :param cell:
    :param visible:
    :return:
    """
    if not type_cellule(cell):
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if not type(visible) == bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen.")
    cell[const.VISIBLE] = visible
    return None

def contientMineCellule(cell : dict) -> bool:
    """

    :param cell:
    :return:
    """
    res = False
    if not type_cellule(cell):
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule.")
    if getContenuCellule(cell) == const.ID_MINE:
        res = True
    return res

def isAnnotationCorrecte(annotation : str) -> bool:
    """

    :param annotation:
    :return:
    """
    res = False
    if annotation == None or annotation == const.DOUTE or annotation == const.FLAG:
        res = True
    return res

def getAnnotationCellule(cell : dict) -> str:
    """

    :param cell:
    :return:
    """
    if not type_cellule(cell):
        raise TypeError(f"getAnnotationCellule : le paramètre {cell} n’est pas une cellule")
    if isAnnotationCorrecte(cell):
        res = None
    else:
        res = cell.get(const.ANNOTATION)
    return res

def changeAnnotationCellule(cell : dict) -> None:
    """

    :param cell:
    :return:
    """
    if not type_cellule(cell):
        raise TypeError("changeAnnotationCellule : le paramètre n’est pas une cellule")
    if getAnnotationCellule(cell) == None:
        cell[const.ANNOTATION] = const.FLAG
    elif getAnnotationCellule(cell) == const.FLAG:
        cell[const.ANNOTATION] = const.DOUTE
    elif getAnnotationCellule(cell) == const.DOUTE:
        cell[const.ANNOTATION] = None
    return None

