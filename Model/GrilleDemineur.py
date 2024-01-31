# GrilleDemineur.py

from itertools import filterfalse
from random import *

from Model.Cellule import *
from Model.Coordonnee import *
import Model.Constantes
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
    Cette fonction permet de récupérer une cellule du tableau.

    Si le type de la grille n'est pas bon ou que le type de la coord n'est pas bon, la fonction renvoies une RaiseError. Si la coordonnée n'est pas correcte \
        La fonction renvoies une IndexError. Sinon la fonction renvoies la coordonnée, étant un tuple, de la case sur laquelle on vient de cliquer.

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
    Cette fonction permet de récupérer le contenu d'une cellule.

    La fonction renvoies le contenu de la cellule.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :param coord: Coordonnée de la case cliqué passé en paramètre et correspondant à un tuple.
    :return: Retourne un dictionnaire.
    """
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord))

def setContenuGrilleDemineur(grille : list, coord : tuple, contenu : int) -> None:
    """
    La fonction permet de modifier le contenu de la cellule.

    La fonction ne retourne rien mais modifie quand même le contenu de la case sur laquelle on a cliqué par l'entier passé en paramètre.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :param coord: Coordonnée de la case cliqué passé en paramètre et correspondant à un tuple.
    :param contenu: Contenu de la cellule correspondant à un entier.
    :return: Cette fonction ne retourne rien.
    """
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    return None

def isVisibleGrilleDemineur(grille : list, coord : tuple) -> bool:
    """
    Cette fonction détermine si la case sur laquelle on a cliqué est visible ou non.

    Si la case sur laquelle on a cliqué est Visible, soit que const.VISIBLE soit égale à True, la fonction renvoie True, sinon elle renvoies False.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :param coord: Coordonnée de la case cliqué passé en paramètre et correspondant à un tuple.
    :return: Cette fonction rentourne un booléen.
    """
    res = False
    if isVisibleCellule(getCelluleGrilleDemineur(grille, coord)) == True:
        res = True
    return res

def setVisibleGrilleDemineur(grille : list, coord : tuple, visibilite : bool) -> None:
    """
    Cette fonction permet de modifier la visibilité de la cellule par la visibilité passé en paramètre.

    La fonction ne renvoies rien mais modifie la valeur const.VISIBLE de la cellule par le paramètre passé.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :param coord: Coordonnée de la case cliqué passé en paramètre et correspondant à un tuple.
    :param visibilite: La visibilité correspond à un booléen qui correspond à si la case est visible ou non
    :return: Cette fonction ne retourne rien
    """
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visibilite)
    return None

def contientMineGrilleDemineur(grille : list, coord : tuple) -> bool:
    """
    Cette fonction permet de déterminer si une cellule contient une mine.

    Si la cellule contient une mine, la fonction renvoies True, sinon elle renvoies False.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :param coord: Coordonnée de la case cliqué passé en paramètre et correspondant à un tuple.
    :return: Cette fonction ne retourne un booléen.
    """
    res = False
    if contientMineCellule(getCelluleGrilleDemineur(grille, coord)):
        res = True
    return res

def getCoordonneeVoisinsGrilleDemineur(grille : list, coord : tuple) -> list:
    """
    Cette fonction permet de récupérer les coordonnées de tous les voisins d'une cellule.

    Si la la coordonnée passé en paramètre n'est pas correcte, la fonction renvoies un IndexError. Si la type de la grille n'est pas correcte \
        et que le type de la coord n'est pas un tuple, la fonction renvoies une TypeError. Sinon la fonction renvoies une liste des coordonnées des voisins \
        de la cellule passé en paramètre.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :param coord: Coordonnée de la case cliqué passé en paramètre et correspondant à un tuple.
    :return: Cette fonction retourne une liste.
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
    Cette fonction permet de placer le nombre exacte de bombe passé en paramètre dans la grille.

    Si le nombre passé en paramètre est inférieur à 0 et que la taille de la grille - 1 est inférieur au nombre passé en paramètre, la fonction renvoies \
        une ValueError. Si la coordonné n'est pas correcte, la fonction renvoies une IndexError. Sinon la fonction place le nombre de mine exacte dans le tableau.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :param nb: Le paramètre est un entier correspondant au nombre de mine que l'on veut placer dans la grille.
    :param coord: Coordonnée de la case passé en paramètre et correspondant à un tuple.
    :return: Cette fonction ne retourne rien.
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
    Cette fonction permet de compter le nombre de mine voisines pour chaque case du tableau.

    La fonction ne renvoies rien.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :return: Cette fonction ne retourne rien.
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
    Cette fonction permet de savoir combien de mine sont contenu dans la grille (ça affiche le résultat quand on lance le jeu).

    Si la grille n'est pas du bon type, la fonction renvoies une ValueError. Sinon elle renvoies le nombre de mine contenu dans la grille.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :return: Cette fonction retourne un entier correspondant au nombre de mine.
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
    Cette fonction permet de récupérer l'annotation contenu dans une cellule sur un case donné.

    Elle renvoies l'annotation contenu dans la cellule.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :param coord: Coordonnée de la case cliqué passé en paramètre et correspondant à un tuple.
    :return: Cette fonction renvoies un str correspondant à l'annotation de la cellule sur laquelle on a cliqué.
    """
    return getAnnotationCellule(getCelluleGrilleDemineur(grille, coord))

def getMinesRestantesGrilleDemineur(grille : list) -> int:
    """
    Cette fonction permet de récupérer le nombre de mines restantes dans le jeu.

    La fonction renvoies le nombre de mines restant dans la grille.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :return: La fonction renvoies un entier correspondant au nombres de mines restantes dans la grille.
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
    Cette fonction permet de déterminer si l'on a gagner la partie ou non.

    Si l'on a déterminer toute les bombes et que toutes les cases ont été révélées, la fonction renvoies False, sinon elle renvoies True.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :return: Cette fonction renvoies un booléen correspondant à si on a gagner la partie ou non.
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
    Cette fonction permet de déterminer si l'on a perdu la partie ou non.

    Si l'on a révélé une cellule contenant une bombe, la fonction renvoies True, sinon la fonction renvoies False.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :return: Cette fonction renvoies un booléen correspondant à si on a perdu la partie ou non.
    """
    res = False
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if isVisibleGrilleDemineur(grille, (i, j)) and contientMineGrilleDemineur(grille ,(i, j)):
                res = True
    return res

def reinitialiserGrilleDemineur(grille : list) -> None:
    """
    Cette fonction permet de réinitialiser toutes les cases de la grille.

    Elle ne renvoies rien et modifie toutes les cases de la grille.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :return: Cette fonction ne renvoies rien.
    """
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            reinitialiserCellule(getCelluleGrilleDemineur(grille, (i, j)))
    return None

def decouvrirGrilleDemineur(grille : list, coord : tuple) -> set:
    """
    Cette fonction permet de découvrir les cellule voisines de la grille quand celle-ci vaut 0.

    Elle renvoies un ensemble.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :param coord: Coordonnée de la case cliqué passé en paramètre et correspondant à un tuple.
    :return: Cette fonction renvoies un ensemble.
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
    Cette fonction permet de simplifier automatiquement les zones "sûrs" alentours à une cellule donnée.

    Cette fonction renvoies aussi un ensemble.

    :param grille: Tableau correspondant à une liste passé en paramètre.
    :param coord: Coordonnée de la case cliqué passé en paramètre et correspondant à un tuple.
    :return: Cette fonction renvoies un ensemble.
    """
    celluleDecouverte = set()
    celluleADecouvrir = {coord}
    compteurFlag = 0
    while len(celluleADecouvrir) > 0:
        coord = celluleADecouvrir.pop()
        if isVisibleGrilleDemineur(grille, coord):
            celluleDecouverte.add(coord)
            for voisins in getCoordonneeVoisinsGrilleDemineur(grille, coord):
                if getAnnotationGrilleDemineur(grille, voisins) == const.FLAG:
                    compteurFlag += 1
            if compteurFlag == getContenuGrilleDemineur(grille, coord):
                setVisibleGrilleDemineur(grille, coord, True)
                for voisins in getCoordonneeVoisinsGrilleDemineur(grille, coord):
                    if (getAnnotationGrilleDemineur(grille, voisins) != const.FLAG) and not isVisibleGrilleDemineur(
                            grille, voisins) \
                            and not contientMineGrilleDemineur(grille, voisins):
                        setVisibleGrilleDemineur(grille, voisins, True)
                        celluleDecouverte.add(voisins)
    return celluleDecouverte

#En pratique je pense que la fonction simplifierToutGrilleDecouvert fonctionne mais je ne vois pas comment faire ajouterFlagsGrilleDemineur et je n'ai plus le temps.

def ajouterFlagsGrilleDemineur(grille: list, coordonnee: tuple) -> set:
    """
     La fonction reçoit en paramètre une grille de démineur et la coordonnée de la cellule à vérifier.
     Si le contenu de la cellule correspond au nombre de cases non découvertes dans le voisinage, alors la
    fonction place un drapeau sur celles qui n’en n’ont pas.
    La fonction retourne l’ensemble des coordonnées des cellules sur lesquelles elle a placé un drapeau.

    :param grille: Une grille de démineur (de type list).
    :param coordonnee: Une coordonnée (de type tuple).
    :return:  La fonction retourne l’ensemble des coordonnées des cellules sur lesquelles elle a placé un drapeau.
    """
    celluleMarque = set()
    if isVisibleGrilleDemineur(grille, coordonnee):
        celluleADecouvrir = 0
        ListeVoisins = []
        for voisins in getCoordonneeVoisinsGrilleDemineur(grille, coordonnee):
            if not isVisibleGrilleDemineur(grille, voisins):
                celluleADecouvrir += 1
                ListeVoisins.append(voisins)
        if celluleADecouvrir == getContenuGrilleDemineur(grille, coordonnee):
            for voisins in ListeVoisins:
                if (not isVisibleGrilleDemineur(grille, voisins)) and (getAnnotationGrilleDemineur(grille, voisins) == None):
                    changeAnnotationCellule(getCelluleGrilleDemineur(grille, voisins))
                    celluleMarque.add(voisins)
    return celluleMarque

def simplifierToutGrilleDemineur(grille: list) -> tuple:
    """
    La fonction reçoit en paramètre une grille de démineur et qui retourne un tuple
    contenant en premier l’ensemble des coordonnées des cellules rendues visible
    et en second l’ensemble des coordonnées des cellules sur lesquelles a été ajouté un drapeau.
    Cette fonction parcourt toutes les cellules de la grille et tente de les simplifier en appelant
    simplifierGrilleDemineur et ajouterFlagsGrilleDemineur. Tant qu’il y a des
    modifications, la fonction reparcourt les cellules pour trouver des simplifications.

    :param grille: Une grille de démineur (de type list).
    :return: La fonction retourne un tuple contenant en premier l’ensemble des coordonnées des cellules rendues visible
    et en second l’ensemble des coordonnées des cellules sur lesquelles a été ajouté un drapeau.
    """
    flag = set()
    visible = set()
    for y in range(0, getNbLignesGrilleDemineur(grille) - 1):
        for x in range(0, getNbColonnesGrilleDemineur(grille) - 1):
            coordonnes = (y, x)
            visible.update(simplifierGrilleDemineur(grille, coordonnes))
            flag.update(ajouterFlagsGrilleDemineur(grille, coordonnes))
    return (visible, flag)

