# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import *
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
    Cette fonction permet de construire une grille avec x nbLignes et y nbCollones qui sont des entiers et elle renvoies une liste.

    Si le nb de lignes est inférieur à 1 ou que le nb de collones est inférieur à 1, la fonction renvoies une ValueError. Si le type du paramètre nbLignes \
        ou le type du paramètre nbCollones ne sont pas des entiers, la fonction renvoies une TypeError. Sinon la fonction crée une grille de n collones et n lignes \
        et renvoies une grille, un tableau de tableau.

    :param nbLignes: Entier passé en paramètre.
    :param nbCollones: Entier passé en paramètre
    :return: retourne un tableau.
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
    Cette fonction récupère le nombre de ligne d'une grille.

    Si le paramètre 'grille' n'est pas du bon type, la fonction renvoies une TypeError, sinon elle renvoies le nombre de ligne de la grille.

    :param grille: Dictionnaire passé en paramètre.
    :return: Un entier correspondant au nombre de lignes dans le tableau.
    """
    if not type_grille_demineur(grille):
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille.")
    return len(grille)

def getNbColonnesGrilleDemineur(grille : list) -> int:
    """
    Cette fonction récupère le nombre de collone d'une grille.

    Si le paramètre 'grille' n'est pas du bon type, la fonction renvoies une TypeError, sinon elle renvoies le nombre de collone de la grille.

    :param grille: Dictionnaire passé en paramètre.
    :return: Un entier correspondant au nombre de collones dans le tableau.
    """
    if not type_grille_demineur((grille)):
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille.")
    return len(grille[0])


def isCoordonneeCorrecte(grille : list, coord : tuple) -> bool:
    """
    Cette fonction permet de vérifier si une coordonnée est correcte.

    Si le type de la grille n'est pas une liste ou que le type de la coord n'est pas un tuple la fonction renvoies une typeError. \
        Si la coord[0] est plus petit que le nombre de ligne et que la coord[1] est plus petit que le nombre de collones dans le tableau \
        et que le nombre de ligne passé en paramètre est supérieur ou égale à 0 et que le nombre de collone est supérieur ou égale à 0, la fonction renvoies True \
        sinon elle renvoies False.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :param coord: Coordonnée de la case cliqué passé en paramètre et correspondant à un tuple.
    :return: Retourne un booléen.
    """
    if not type(grille) == list or not type(coord) == tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")

    res = False
    if coord[0] < len(grille) and coord[1] < len(grille[0]) and coord[0] >= 0 and coord[1] >= 0:
        res = True
    return res

def getCelluleGrilleDemineur(grille : list, coord : tuple) -> dict:
    """

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :param coord: Coordonnée de la case cliqué passé en paramètre et correspondant à un tuple.
    :return: Retourne un dictionnaire.
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

def placerMinesGrilleDemineur(grille : list, nb : int, coord : tuple) -> None:
    """

    :param grille:
    :param nb:
    :param coord:
    :return:
    """
    if nb < 0 or (getNbColonnesGrilleDemineur(grille)) * (getNbLignesGrilleDemineur(grille)) - 1 < nb:
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorrect.")
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille.")

    h = 0
    while nb > h:
        coordCellule = construireCoordonnee(randint(0, getNbLignesGrilleDemineur(grille)-1), randint(0, getNbColonnesGrilleDemineur(grille)-1))
        if coordCellule != coord and isCoordonneeCorrecte(grille, coordCellule) and getContenuGrilleDemineur(grille, coordCellule) != const.ID_MINE:
            setContenuGrilleDemineur(grille, coordCellule, const.ID_MINE)
            h += 1
    compterMinesVoisinesGrilleDemineur(grille)
    return None

def compterMinesVoisinesGrilleDemineur(grille : list) -> None:
    """

    :param grille:
    :return:
    """
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            coord = construireCoordonnee(i, j)
            if getContenuGrilleDemineur(grille, coord) != const.ID_MINE:
                nbrMines = 0
                for h in getCoordonneeVoisinsGrilleDemineur(grille, coord):
                    if getContenuGrilleDemineur(grille, h) == const.ID_MINE:
                        nbrMines += 1
                setContenuGrilleDemineur(grille, coord, nbrMines)
    return None

def getNbMinesGrilleDemineur(grille : list) -> int:
    """

    :param grille:
    :return:
    """
    if not type_grille_demineur(grille):
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n’est pas une grille.")
    nbrMines = 0
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            coord = construireCoordonnee(i, j)
            if getContenuGrilleDemineur(grille, coord) == const.ID_MINE:
                nbrMines += 1
    return nbrMines

def getAnnotationGrilleDemineur(grille : list, coord : tuple) -> str:
    """

    :param grille:
    :param coord:
    :return:
    """
    return getAnnotationCellule(getCelluleGrilleDemineur(grille, coord))

def getMinesRestantesGrilleDemineur(grille : list) -> int:
    """

    :param grille:
    :return:
    """
    nbrFlag = 0
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            coord = construireCoordonnee(i, j)
            if getAnnotationGrilleDemineur(grille, coord) == const.FLAG:
                nbrFlag += 1
    return getNbMinesGrilleDemineur(grille) - nbrFlag

def gagneGrilleDemineur(grille : list) -> bool: #Test optionnel fait précédemment
    """

    :param grille:
    :return:
    """
    res = True
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if contientMineGrilleDemineur(grille, (i,j)) and isVisibleGrilleDemineur(grille, (i, j)) or contientMineGrilleDemineur(grille, (i, j)) and \
                    getAnnotationGrilleDemineur(grille, (i, j)) != const.FLAG or not contientMineGrilleDemineur(grille, (i, j)) and not isVisibleGrilleDemineur(grille, (i ,j)):
                res = False
    return res

def perduGrilleDemineur(grille : list) -> bool:
    """

    :param grille:
    :return:
    """
    res = False
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if isVisibleGrilleDemineur(grille, (i, j)) and contientMineGrilleDemineur(grille ,(i, j)):
                res = True
    return res

def reinitialiserGrilleDemineur(grille : list) -> None:
    """

    :param grille:
    :return:
    """
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            reinitialiserCellule(getCelluleGrilleDemineur(grille, (i, j)))
    return None

def decouvrirGrilleDemineur(grille : list, coord : tuple) -> set:
    """

    :param grille:
    :param coord:
    :return:
    """
    case = []
    case.append(coord)
    ensemble = set()
    while not len(case) == 0:
        if not isVisibleGrilleDemineur(grille, case[0]):
            setVisibleGrilleDemineur(grille, case[0], True)
            ensemble.add(case[0])
            if getContenuGrilleDemineur(grille, case[0]) == 0:
                voisins = getCoordonneeVoisinsGrilleDemineur(grille, case[0])
                case += voisins
                voisins.clear()
        case.remove(case[0])
    return ensemble


def simplifierGrilleDemineur(grille : list, coord : tuple) -> set:
    """

    :param grille:
    :param coord:
    :return:
    """
    case = []
    case.append(coord)
    ensemble = set()
    while not len(case) == 0:
        coord = case.pop()
        nbrFlag = 0
        if isVisibleGrilleDemineur(grille, coord) == True:
            lstVoisin = getCoordonneeVoisinsGrilleDemineur(grille, coord)
            for coordVoisin in lstVoisin:
                if getAnnotationGrilleDemineur(grille, coordVoisin) == const.FLAG:
                    nbrFlag += 1
            if getContenuGrilleDemineur(grille, coord) == nbrFlag:
                for coordVoisin in lstVoisin:
                    if not isVisibleGrilleDemineur(grille, coordVoisin):
                        if getAnnotationGrilleDemineur(grille, coordVoisin) == None:
                            setVisibleGrilleDemineur(grille, coordVoisin, True)
                            ensemble.add(coordVoisin)
                            case.append(coordVoisin)
    return ensemble

