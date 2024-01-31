<div align="center">
    <a href="https://iut-info.univ-reims.fr/gitlab/bayf0001/ms103"><img src="https://www.univ-reims.fr/media-images/4748/logo-urca-impression.jpg" alt="URCA logo" height="128" style="border-radius: 10%"></a>
    <h1>SAÉ 2.01 - Demineur</h1>
    <h2>PyDemineur</h2>
    <strong><p>Réalisé par : Gwendal RODRIGUES</p></strong>
</div>

## Sommaire :

- But du projet [↓](#but-du-projet-)
- Préparer l'environnement Python [↓](#préparer-lenvironnement-python--)
  - Remarque [↓](#remarque-)
- Documentation [↓](#documentation-)
  - Configurer la documentation [↓](#configurer-la-documentation-)
    - Le ficheier `conf.py` [↓](#le-fichier-confpy-)
      - Les options [↓](#les-options-)
      - Emplacements des modules [↓](#emplacement-des-modules-)
    - Le fichier index.rst [↓](#le-fichier-indexrst-)

## But du projet :

L'objectif de ce projet a été de programmer une application en partant du besoin d'un client et qui nécessite une 
interface graphique, celui-ci consiste donc en la création d'un démineur en Python utilisant la librairie PyGame.

## Préparer l'environnement Python :

Vérifier que PyGame est bien installé sur le système utilisé. Le plus simple est
de lancer la commande d'installation : 
```sh
pip install pygame
```
Si la commande est refusée (vous n'avez pas les droits administrateur par exemple),
il faudra peut-être créer son environnement de développement.

Commencez par vérifier que PyGame est installé ou non avec la commande : 
```shell
pip freeze | grep pygame
```
> Sous Windows : 
> ```shell
> pip freeze | findstr pygame
> ```

Si PyGame n'est pas installé et que vous n'êtes pas administrateur de la machine, 
créez votre environnement de développement avec la commande :
```shell
python -m venv venv
```
Cette commande crée un répertoire `venv/` contenant une "copie" de l'environnement Python.

Placez-vous dans l'environnement de développement `venv/` en tapant
la commande :
```shell
source venv/bin/activate
```
> Sous Windows
> ```Shell
> venv\Scripts\activate
> ```
Dans cet environnement, vous pouvez alors installer PyGame avec la commande : 
```shell
pip install pygame
```

Pour quitter l'environnement `venv/`, il suffit de taper la commande :
```shell
deactivate
```

### Remarque :

Pour mettre à jour le package PyGame, il faut taper la commande : 
```shell
pip install pygame --upgrade
```

## Documentation :

Pour mettre en place les outils de documentation **Sphinx**, suivre les étapes 
suivantes.

Installer **Sphinx** : 
```shell
pip install sphinx
```

Vérifier que l'installation est correcte : 
```shell
sphinx-build --version
```

### Configurer la documentation :

Pour configurer la documentation, il faut exécuter la commande suivante dans le répertoire
de base.
```shell
sphinx-quickstart
```

Cette commande crée les fichiers suivants : 
- `Makefile` : Permet de générer la documentation
- `make.bat`: Pour Windows, remplace la commande `make` de linux.

La commande crée également les répertoires suivants : 
- `build/` : répertoire qui contiendra la documentation générée par __Sphinx__ (_à exclure du dépôt Git_).
- `source`: répertoire qui contient les fichiers de configuration `conf.py` et `index.rst`.

#### Le fichier `conf.py` :

Dans ce fichier, on retrouve les paramètres entrés lors de la configuration de la documentation.

On peut notamment ajouter dans ce fichier des options pour "_enjoliver_" la documentation.

Un thème souvent utilisé est le thème [sphinx-rtd-theme](https://pypi.org/project/sphinx-rtd-theme/). Pour l'installer,
il faut lancer la commande : 
```shell
pip install sphinx-rtd-theme
```
Enfin, dans le fichier `source\conf.py`, on ajoute la ligne : 
```python
html_theme = "phinx_rtd_theme"
```

##### Les options :
Une option utile est (toujours dans le fichier `source/conf.py`) : 
```python
extensions = [
    'sphinx.ext.autodoc',
]
```
Cette option permet d'inclure la documentation au format _docstring_ utilisé dans les 
fichiers python.

Par contre, dans la "_docstring_", il faut séparer la description de la méthode de celle des
paramètres par une ligne vide : 
```text
    """
    Retourne la colonne de la coordonnée donnée en paramètre

    :param coord: Coordonnée
    :return: Colonne de la coordonnée
    :raise TypeError: s'il ne s'agit pas d'une coordonnée
```
Ne pas oublier d'ajouter les ':' derrière le type des exceptions, sinon l'option `raise:` n'est pas 
reconnue.

Si vous voulez inclure le type des paramètres dans la documentation, il faut installer le module
`sphinx-autodoc-typehints` : 
```shell
pip install sphinx-autodoc-typehints
```
Sans oublier de l'ajouter dans les extensions (fichier `conf.py`) : 
```python
extensions = [
    ...,
    "sphinx_autodoc_typehints",
]
```

> __Remarque__ : Pour le typage en Python, on peut améliorer le typage grâce au module `typing` :
> ```python
> from typing import Union
>
> def format_unit(value: Union[float, int], unit: str) -> str:
>    ...
> ```

##### Emplacement des modules :

Si les modules ne se trouvent pas dans le même répertoire que le fichier `conf.py`, il 
faut préciser le chemin en décommentant les lignes : 
```python
import os
import sys
sys.path.insert(0, os.path.abspath('..')) # Mettre le bon chemin...
```

#### Le fichier `index.rst` :

Dans ce fichier, on ajoute les documents que l'on veut voir apparaître dans la documentation.

Ceci se fait dans le paragraphe `toctree``: 
```text
.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   ./Fichier01.rst
   ./Fichier02.rst
```
Les fichiers `Fichier0x.rst` commencent par une présentation de leur contenu, puis les
classes à documenter, les éventuelles notes et les fonctions associées : 
```text
view.Canvas
===========

    Classe permettant de créer et gérer une fenêtre.

    Exemple d'utilisation :

    .. code-block:: python

        from view.Canvas import Canvas

        # Création de la fenêtre
        cv = Canvas( (640, 480) )
        # Afficher/mettre à jour la fenêtre
        cv.display()

.. autoclass:: view.Canvas.Canvas
   :members:

.. NOTE::

    Fonction attachée à la fenêtre

.. autofunction:: view.Canvas.waitClick
.. autofunction:: view.Canvas.pause
```