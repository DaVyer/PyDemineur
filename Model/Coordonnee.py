# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0

def construireCoordonnee(num_ligne : int, num_colonne : int) -> tuple:
    """
    Récupère des coordonnées données.

    Cette fonction teste si les valeurs données sont bien des entiers et si ils sont positifs. Dans le cas contraire, si l'un des paramètres n'est pas un entier,
    la fonction retourne un TypeError, et dans le cas ou l'un des paramètres n'est pas positifs, la fonction retourne une ValueError. La fonction retourne
    un tuple.

    :param num_ligne: numéro de ligne passé en paramètre
    :param num_colonne: numéro de colonne passé en paramètre
    :return: retourne un tuple composé du numéro de la ligne et le numéro de la colonne.
    """
    if not isinstance(num_ligne, int) and isinstance(num_colonne, int) :
        raise TypeError(f"construireCoordonnee : Le numéro de ligne {num_ligne} ou le numéro de colonne {num_colonne} ne sontpas des entiers")
    elif num_ligne < 0 or num_colonne < 0:
        raise ValueError(f"construireCoordonnee : Le numéro de ligne {num_ligne} ou de colonne {num_colonne} ne sont pas positifs")
    else:
        return (num_ligne, num_colonne)

def getLigneCoordonnee(coordL : tuple) -> int:
    """
    Récupère le numéro de ligne contenu dans la coordonnée passée en paramètre

    La fonction teste si le paramètre correspond bien à des coordonnées. Si ce n'est pas le cas, la fonction retourne une TypeError.
    Retourne le premier élément du couple, correspondant à la ligne.

    :param coordL: couple représentant le numéro de la ligne et de la colonne, tout deux commençant à 0.
    :return: Retourne la première valeur du couple correspondant à la ligne.
    """
    if not isinstance(coordL, tuple):
        raise TypeError("getLigneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coordL[0]

def getColonneCoordonnee(coordC : tuple) -> int:
    """
    Récupère le numéro de colonne contenu dans la coordonnée passée en paramètre

    La fonction teste si le paramètre correspond bien à des coordonnées. Si ce n'est pas le cas, la fonction retourne une TypeError.
    Retourne le deuxième élément du couple, correspondant à la colonne.

    :param coordC: couple représentant le numéro de la ligne et de la colonne, tout deux commençant à 0.
    :return: Retourne la deuxième valeur du couple correspondant à la colonne.
    """
    if not isinstance(coordC, tuple):
        raise TypeError("getColonneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coordC[1]