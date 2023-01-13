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
    Cette fonction permet de renvoyer le contenu d'une cellule.

    Si le paramètre ne correspond pas à une cellule, la fonction renvoies une TypeError, sinon elle renvoies le contenu de la case.

    :param cell: Dictionnaire dans lequel les clés const.CONTENU et const.VISIBLE sont passé en paramètre.
    :return: Retourne le contenu de la cellule.
    """
    if not type_cellule(cell):
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return cell.get(const.CONTENU)

def isVisibleCellule(cell : dict) -> bool:
    """
    Cette fonction permet de renvoyer si la cellule est visible ou non.

    Si le paramètre ne correspond pas à une cellule, la fonction renvoies une TypeError, sinon la fonction renvoies un bolléen, \
        True si la case est visible, False sinon.

    :param cell: Dictionnaire dans lequel les clés const.CONTENU et const.VISIBLE sont passé en paramètre.
    :return: Retourne un booléen, True si la case est visible, False sinon.
    """
    if not type_cellule(cell):
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return cell.get(const.VISIBLE)

def setContenuCellule(cell : dict, x : int) -> None:
    """
    Cette fonction permet de modifier le contenu d'une cellule passé en paramètre par un nombre passé en paramètre. Elle ne renvoies rien

    Si le paramètre 'cell' passé en paramètre ne correspond pas à une cellule, la fonction renvoies une TypeError. Si le type du paramètre 'x' \
        ne correspond pas à un int, la fonction renvoies une TypeError. Si le contenu de x n'est pas correcte (ex : -3), la fonction renvoies une ValueError \
        sinon la fonction remplace le contenu de la cellule par le nombre passé en paramètre.

    :param cell: Dictionnaire dans lequel les clés const.CONTENU et const.VISIBLE sont passé en paramètre.
    :param x: Entier passé en paramètre
    :return: La fonction ne retourne rien
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
    Cette fonction permet de modifier la visibilité d'une cellule passé en paramètre par un bolléen passé en paramètre. Elle ne renvoies rien.

    Si le paramètre 'cell' passé en paramètre ne correspond pas à une cellule, la fonction renvoies une TypeError. Si le type du paramètre 'visible' \
        ne correspond pas à un booléen, la fonction renvoies une TypeError. Sinon la fonction remplace la visibilité de \
        la cellule par la nouvelle visibilité passé en paramètre.

    :param cell: Dictionnaire dans lequel les clés const.CONTENU et const.VISIBLE sont passé en paramètre.
    :param visible: booléen passé en paramètre.
    :return: Cette fonction ne retourne rien.
    """
    if not type_cellule(cell):
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if not type(visible) == bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen.")
    cell[const.VISIBLE] = visible
    return None

def contientMineCellule(cell : dict) -> bool:
    """
    Cette fonction permet de savoir si une cellule contient une mine ou non.

    Si le paramètre 'cell' passé en paramètre ne correspond pas à une cellule, la fonction renvoies une TypeError. Si le contenu de la cellule \
        est égal à const.ID_MINE la fonction renvoies True, sinon la fonction renvies False.

    :param cell: Dictionnaire dans lequel les clés const.CONTENU et const.VISIBLE sont passé en paramètre.
    :return: La fonction renvoies un booléen, si le contenu de la cellule correspond à l'id dune mine (-1), elle renvoies True, sinon elle renvoies False.
    """
    res = False
    if not type_cellule(cell):
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule.")
    if getContenuCellule(cell) == const.ID_MINE:
        res = True
    return res

def isAnnotationCorrecte(annotation : str) -> bool:
    """
    Cette fonction permet de vérifier si l'annotation d'une cellule correspond bien à None, const.DOUTE ou const.FLAG.

    Si le paramètre passé ne correspond pas à None, const.Doute ou const.FLAG, la fonction renvoies False, sinon la fonction renvoies True.

    :param annotation: Chaine de charactère passé en paramètre correspondant à 'Doute', 'Flag' ou None.
    :return: La fonction renvoies un booléen.
    """
    res = False
    if annotation == None or annotation == const.DOUTE or annotation == const.FLAG:
        res = True
    return res

def getAnnotationCellule(cell : dict) -> str:
    """
    Cette fonction permet de récupérer l'annotation d'une cellule.

    Si le paramètre 'cell' ne correspond pas à une cellule, la fonction renvoies une TypeError, si const.ANNOTATION dans la cell n'ai pas correcte, \
        la fonction renvoies None. Sinon la fonction renvoies l'annotation du paramètre.

    :param cell: Dictionnaire dans lequel les clés const.CONTENU, const.VISIBLE et const.ANNOTATION sont passé en paramètre.
    :return: la fonction retourne res, correspondant soit à l'annotation de la cellule, soit à None.
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
    Cette fonction change l'annotation d'une cellule.

    Si le poaramètre 'cell' ne correspond pas à une cellule, la fonction renvoies un TypeError. Si l'annotation de la cellule correspond à None, elle est \
        remplacé par const.Flag, si l'annotation de la cellule correspond à const.Flag, elle est remplacé par const.Doute, enfin, si l'annotation de la \
        cellule correspond à const.Doute, elle est remplacé par None.

    :param cell: Dictionnaire dans lequel les clés const.CONTENU, const.VISIBLE et const.ANNOTATION sont passé en paramètre.
    :return: La fonction ne renvoies rien.
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

def reinitialiserCellule(cell : dict) -> None:
    """
    Cette fonction permet de réintialiser une cellule.

    La fonction met à False const.VISIBLE, 0 const.CONTENU et si l'annotation correspond à const.FLAG ou const.DOUTE elle le remplace par None.

    :param cell: Dictionnaire dans lequel les clés const.CONTENU, const.VISIBLE et const.ANNOTATION sont passé en paramètre.
    :return: La fonction ne renvoies rien.
    """
    setVisibleCellule(cell, False)
    setContenuCellule(cell, 0)
    if getAnnotationCellule(cell) == const.FLAG or const.DOUTE:
        cell[const.ANNOTATION] = None
    return None
