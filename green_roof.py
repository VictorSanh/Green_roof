# -*- coding: utf-8 -*-

"""

CLASS GREEN ROOF

"""

# Bibliothèque

import numpy as np

# Pas d'espace
DZ = 5e-3

class GreenRoof(object):
    """
    La classe toit vegetal :

    Contient les paramètres du toit
    """

    def __init__(self, l1=0.3, l2=0.1, l3=0.05, lai=5):
        """ Initialise le toit végétal """
        # Les tailles caracteristiques du toit
        self._epaisseur_beton = l1
        self._epaisseur_terre = l2
        self._taille_plantes = l3

        # Parametre de densite de la vegetation
        self._lai = lai

        # Discretisation du toit
        self._nl = (l1 + l2)/DZ

        # Initialise la temperature dans le toit
        self.temperature = np.ones(self._nl+1)
        # Pour l'instant temperature uniforme (A CHANGER)

    def __getitem__(self, hauteur):
        """ Retourne la valeur de la temperature a une hauteur donnee """
        return self.temperature(int(hauteur/DZ))
