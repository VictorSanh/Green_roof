# -*- coding: utf-8 -*-

"""

CLASS GREEN ROOF

"""

# Bibliothèque

import numpy as np
from environnement import Environnement

# Pas d'espace
DZ = 5e-3

""" Concrete physic parameters """
rho_su = 2600  #density of concrete kg/m^3
c_su = 960 #specific heat concrete J/kg K
lambda_su = 0.2 #thermal conductivity concrete W/(m K)

coeff1 = lambda_su / c_su / rho_su

""" Soil physic parameters """
rho_soil = 1200 #density of soil kg / m^3
c_soil = 840 # specific heat soil : J/kg K
lambda_soil = 1.0 #thermal conductivity soil with organic matter 0.15 - 2 W/(m K)
LAMBDA = 2.257e06 # J/kg, latent heat of vaporization
Dvt  = 2e-06 # vapor diffusivity m^2/s choose as an a constant

coeff2 = (lambda_soil + LAMBDA * Dvt) / c_soil / rho_soil

# Heat transfert coefficient between air and concrete
h = 4 # W m-2 K-1

# Convective coeficient of vapor transport
hg = 3 # W m-2 K-1

# Stefan Boltzmann constant
sigma = 5.670373e-08 # W m-2 K-4

# Average leaves thickness
d = 1e-03 # m

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


    def __getitem__(self, hauteur):
        """ Retourne la valeur de la temperature a une hauteur donnee """
        return self.temperature(round(hauteur/DZ))
    
    def calcule_diff_finies_lentes(self, env, time1=0, time2=24):
        """ Calcule la consommation d'energie par la methode des 
        differences finies et Euler explicite"""
        
        # Donnees fournies par l'environnement exterieur
        t_ext = env.get_t()
        irr_ext = env.get_irradiance()
        hum_ext = env.get_humidite()
        pres_ext = env.get_pres()

        # Inititalisation de la consommation a 0
        consommation = 0

        _nl1 = self._nl1
        _nl2 = self._nl2
        _nl = self._nl

        dt = (time2 - time1)/1000

        # Boucle principale
        for s in np.linspace(time1, time2, 1000):
            self.temperature[1:_nl1] = self.temperature[1:_nl1]
            + (self.temperature[0:_nl1-1]
               + self.temperature[2:_nl1+1]
               - 2*self.temperature[1:_nl1]) * coeff1 * dt/ DZ**2
            
            self.temperature[_nl1+1:_nl2] = self.temperature[_nl1+1:_nl2]
            + coeff2 * dt / DZ**2 *(self.temperature[_nl1:_nl2-1] 
                                    + self.temperature[_nl1+2:_nl2+1]
                                    - 2 * self.temperature[_nl1+1:_nl2])

            self.temperature[0] = (h * DZ * self.temperature_interieure + 
                                   self.temperature[1])/(1 + h * DZ)
            consommation += 0.1

        return consommation

    def calcule_diff_finies_rapides(self, env, time1=0, time2=24):
        """ Calcule la consommation d'energie par la methode des 
        differences finies et Euler implicite"""

        # Donnees fournies par l'environnement exterieur
        t_ext = env.get_t()
        irr_ext = env.get_irradiance()
        hum_ext = env.get_humidite()
        pres_ext = env.get_pres()

        # Inititalisation de la consommation a 0
        consommation = 0

        # Boucle principale
        for s in np.linspace(time1, time2, 10000):
            consommation += 0

        return consommation

    def calcule_fourier(self, env, time1=0, time2=24):
        """ Calcule la consommation d'energie par une méthode de Fourier """
        consommation = 0
        # Boucle principale
        for s in np.linspace(time1, time2, 10000):
            consommation += 0

        return consommation

    def calcule_volumes_finis(self, env, time1 = 0, time2 = 24):
        """" Calcule la consommation d'energie par une méthode des volumes 
        finis """

        # Donnees fournies par l'environnement exterieur
        t_ext = env.get_t()
        irr_ext = env.get_irradiance()
        hum_ext = env.get_humidite()
        pres_ext = env.get_pres()

        # Inititalisation de la consommation a 0
        consommation = 0

        # Boucle principale
        for s in np.linspace(time1, time2, 10000):
            consommation += 0

        return consommation

    def calcule_elements_finis(self, env, time1=0, time2=24):
        """" Calcule la consommation d'energie par une méthode des elements 
        finis """

        # Donnees fournies par l'environnement exterieur
        t_ext = env.get_t()
        irr_ext = env.get_irradiance()
        hum_ext = env.get_humidite()
        pres_ext = env.get_pres()

        # Inititalisation de la consommation a 0
        consommation = 0

        # Boucle principale
        for s in np.linspace(time1, time2, 10000):
            consommation += 0

        return consommation

if __name__ == "__main__":
    env = Environnement(48.8534100, 2.3488000, 10, 10)
    roof = GreenRoof()
    print(roof.calcule_diff_finies_lentes(env))
