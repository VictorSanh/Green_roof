# -*- coding: utf-8 -*-

from .weather_data import DonneesMeteo
from .weather_data import Irradiance

class Environnement(DonneesMeteo, Irradiance):
    """
    La classe Environnement :

    Les données environnementales pour faire le calcul de la consommation.
    """

    def __init__(self, longitude, latitude, mois, jour):
        """ Initialise l'environment avec la localisation et la date """
        DonneesMeteo.__init__(self, longitude, latitude, mois, jour)
        Irradiance.__init__(self, longitude, latitude, mois, jour)

    def get_irradiance(self):
        self.extraire_irradiance()
        return self.irradiance



if __name__ == "__main__":
    ev = Environnement(48.8534100, 2.3488000, 2, 15)
    print("Temperature : ")
    print(ev.get_t())
    print("Pression : ")
    print(ev.get_pres())
    print("Irradiance : ")
    print(ev.get_irradiance())
