# -*- coding: utf-8 -*-

import donnees_json
import irradiance

class Environnement(object):
    """
    La classe Environnement :

    On a toutes les données environnementales pour faire le calcul de la consommation.
    """

    def __init__(self, longitude, latitude, mois, jour):
        """ Initialise l'environment avec la localisation et la date """
        self.longitude = longitude
        self.latitude = latitude
        self.mois = mois
        self.jour = jour
    def extraire_temp(self):
        d = donnees_json.DonneesMeteo(self.latitude, self.longitude, self.mois, self.jour)
        return d.get_t()
    def extraire_pres(self):
        d = donnees_json.DonneesMeteo(self.latitude, self.longitude, self.mois, self.jour)
        return d.get_pres()
    def extraire_humi(self):
        d = donnees_json.DonneesMeteo(self.latitude, self.longitude, self.mois, self.jour)
        return d.get_humidite()
    def extraire_irr(self):
        i = irradiance.Irradiance(self.longitude, self.latitude, self.jour, self.mois)
        return i.extraire_irradiance()