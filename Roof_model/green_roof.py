# -*- coding: utf-8 -*-

"""

CLASS GREEN ROOF

"""

# Bibliothèque

import numpy as np
import random as rand
from scipy.optimize import fsolve
from .environnement import Environnement

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

""" Canopy physics parameters """
rho_c = 1000
c_c = 1.2

# Canopy air
rho_a = 1.2 # density of air
c_a = 1000 # specific heat of air

rho_infinite = 1.2

# Heat transfert coefficient between air and concrete
h = 4 # W m-2 K-1

# Convective coeficient of vapor transport
hg = 3 # W m-2 K-1

# Stefan Boltzmann constant
sigma = 5.670373e-08 # W m-2 K-4

# Average leaves thickness
d = 1e-03 # m

# Sky temperature
Tsky = 250

# Other coefficients
ks = 1.0
k1 = 1.0
re = 1000
epsilon = 0.004
ha = 2


class GreenRoof(object):
    """
    La classe toit vegetal :

    Contient les paramètres du toit
    """

    def __init__(self, l1=0.3, l2=0.1, l3=0.05, lai=5, tin=275, surf=10):
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
        self.temperature = 320 * np.ones(self._nl+1)
        # Pour l'instant temperature uniforme (A CHANGER)
        
        # temperature 
        self.temperature_interieure = tin

        # Surface
        self.surface = surf


    def __getitem__(self, hauteur):
        """ Retourne la valeur de la temperature a une hauteur donnee """
        return self.temperature(round(hauteur/DZ))

    def Boundary(self, Tg, Tg_, phi_s, Tc, Ta):
        """ Calcul des conditions aux limites """
        tau_s = np.exp(-ks*self._lai)
        tau_1 = np.exp(-k1*self._lai)
        return -(lambda_soil + LAMBDA * Dvt) * (Tg - Tg_)/DZ - tau_s * phi_s - sigma * (tau_1*Tsky**4 + (1 - tau_1)*Tc**4 - Tg**4) + hg * (Tg - Ta)
    
    def calcule_diff_finies_lentes(self, env, time1=0, time2=24):
        """ Calcule la consommation d'energie par la methode des 
        differences finies et Euler explicite"""
        
        # Donnees fournies par l'environnement exterieur
        t_ext = np.array(list(map(float, env.get_t())))
        #print(env.get_irradiance())
        irr_ext = np.array(env.get_irradiance())
        hum_ext = np.array(list(map(float, env.get_humidite())))
        pres_ext = np.array(list(map(float, env.get_pres())))

        # Inititalisation de la consommation a 0
        consommation = 0

        # Raccourcis
        _nl1 = self._nl1
        _nl2 = self._nl2
        _nl = self._nl

        # Intervalle de temps de calcul
        dt = (time2 - time1)/1000

        # Initialisation 
        Tc = t_ext[0]
        Ta = t_ext[0]

        tau_s = np.exp(-ks*self._lai)
        tau_1 = np.exp(-k1*self._lai)

        # Random process : the wall
        consommation += rand.randint(20, 50)    

        # Boucle principale
        for s in np.linspace(time1, time2, 1000):
            
            # Green Roof Equation
            self.temperature[1:_nl1] = self.temperature[1:_nl1]
            + (self.temperature[0:_nl1-1]
               + self.temperature[2:_nl1+1]
               - 2*self.temperature[1:_nl1]) * coeff1 * dt/ DZ**2
            
            self.temperature[_nl1+1:_nl2] = self.temperature[_nl1+1:_nl2]
            + coeff2 * dt / DZ**2 *(self.temperature[_nl1:_nl2-1] 
                                    + self.temperature[_nl1+2:_nl2+1]
                                    - 2 * self.temperature[_nl1+1:_nl2])

            consommation += epsilon * h * abs(self.temperature[0] - self.temperature_interieure) * dt * self.surface

            self.temperature[0] = (h * DZ * self.temperature_interieure + 
                                   self.temperature[1])/(1 + h * DZ)

            self.temperature[_nl1] = ((lambda_soil + LAMBDA * Dvt) * self.temperature[_nl1+1] +
                                      lambda_su * self.temperature[_nl1-1]) / (lambda_su + lambda_soil + LAMBDA*Dvt)

            # Canopy Equations
            Tc_old = Tc
            Tc = Tc + dt * ((1 - tau_1) * sigma * (Tsky**4 + self.temperature[_nl2]**4 - 2*Tc**4) - 2 * self._lai * rho_c * c_c * (Tc - Ta)/re
                            + (1 - tau_s - (1 - tau_s) * rho_infinite)* irr_ext[s*(irr_ext.size - 1)/24]) / rho_c / d / c_c

            Ta = Ta + dt * (2*self._lai*rho_a*c_a/re*(Tc_old - Ta) + hg * (self.temperature[_nl2] - Ta) + ha * (t_ext[s*(t_ext.size - 1)/24] - Ta)) / rho_a / c_a / self._taille_plantes

            self.temperature[_nl2] = fsolve(self.Boundary, self.temperature[_nl2], args=(self.temperature[_nl2-1], irr_ext[s/24*(irr_ext.size - 1)], Tc, Ta))[0]

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
