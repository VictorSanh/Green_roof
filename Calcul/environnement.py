# -*- coding: utf-8 -*-

from weather_data import DonneesMeteo
from weather_data import Irradiance

class Environnement(DonneesMeteo, Irradiance):
    """
    La classe Environnement :

    Les données environnementales pour faire le calcul de la consommation.
    """

    def __init__(self, longitude, latitude, mois, jour):
        """ Initialise l'environment avec la localisation et la date """
        DonneesMeteo.__init__(self, longitude, latitude, mois, jour)
        Irradiance.__init__(self, longitude, latitude, mois, jour)



if __name__ == "__main__":
    ev = Environnement(48.8534100, 2.3488000, 10, 10)
    print(ev.get_t())
    ev.extraire_irradiance()
    print(ev.irradiance)
