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

    def __init__(self, l1=0.3, l2=0.1, l3=0.05, lai=5, tin=275):
        """ Initialise le toit végétal """
        # Les tailles caracteristiques du toit
        self._epaisseur_beton = l1
        self._epaisseur_terre = l2
        self._taille_plantes = l3

        # Parametre de densite de la vegetation
        self._lai = lai

        # Discretisation du toit
        self._nl = (l1 + l2)/DZ
        self._nl1 = l1/DZ
        self._nl2 = l2/DZ

        # Initialise la temperature dans le toit
        self.temperature = np.ones(self._nl+1)
        # Pour l'instant temperature uniforme (A CHANGER)
        
        # temperature 
        self.temperature_interieure = tin
        # Parametres de conduction
        
        

    def __getitem__(self, hauteur):
        """ Retourne la valeur de la temperature a une hauteur donnee """
        return self.temperature(round(hauteur/DZ))
    
    def calcule_diff_finies(self, Environment, time1, time2):
        """ Calcule la consommation d'energie par la methode des 
        differences finies """
        consommation = 0
        # Boucle principale
        for s in np.linspace(time1, time2, 10000):
            temperature[1:_nl1] += coeff1 * dt/ dz**2 *(temperature[0:_nl1-1]
                                                        + temperature[2:_nl1+1]
                                                        - 2*temperature[1:_nl1])
            
            temperature[_nl1+1:_nl2] = temperature[_nl1+1:_nl2]
            + coeff2 * dt / dz**2 *(temperature[_nl1:_nl2-1] + T[_nl1+2:_nl2+1]
                                    - 2 * temperature[_nl1+1:_nl2])

            temperature[0] = (temperature[1] + h * dz * Tin) / (1 + h * dz)


        return consommation

    def calcule_fourier(self, Environment, time1, tim2):
        """ Calcule la consommation d'energie par une méthode de Fourier """
        consommation = 0
        # Boucle principale
        for s in np.linspace(time1, time2, 10000):
    
        return consommation

    def calcule_volumes_finis(self, Environment, time1, tim2):
        """" Calcule la consommation d'energie par une méthode des volumes 
        finis """
        consommation = 0
        # Boucle principale
        for s in np.linspace(time1, time2, 10000):

        return consommation

    def calcule_elements_finis(self, Environment, time1, tim2):
        """" Calcule la consommation d'energie par une méthode des elements 
        finis """
        consommation = 0
        # Boucle principale
        for s in np.linspace(time1, time2, 10000):

        return consommation
    
    
    
