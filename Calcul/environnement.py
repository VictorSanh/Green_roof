# -*- coding: utf-8 -*-

from weather_data import DonneesMeteo
from weather_data import Irradiance

class Environnement(object):
    """
    La classe Environnement :

    Les données environnementales pour faire le calcul de la consommation.
    """

    def __init__(self, longitude, latitude, mois, jour):
        """ Initialise l'environment avec la localisation et la date """
        self.longitude = longitude
        self.latitude = latitude
        self.mois = mois
        self.jour = jour
        self.donnees = DonneesMeteo(self.latitude, self.longitude,
                                    self.mois, self.jour)

    def extraire_temp(self):
        """ Extrait les donnes meteos sur la temperature """
        return donnees.get_t()

    def extraire_pres(self):
        """ Extrait les donnes meteos sur la temperature """
        return donnees.get_pres()

    def extraire_humi(self):
        """ Extrait les donnes meteos sur la temperature """
        return donnees.get_humidite()

    def extraire_irr(self):
        """ Extrait les donnes meteos sur l'irradiance """
        i = irradiance.Irradiance(self.longitude, self.latitude,
                                  self.jour, self.mois)
        return i.extraire_irradiance()

if __name__ == "__main__":
    ev = Environnement(5.75, 45.1333, 11, 10)
    print(ev.extraire_temp)
