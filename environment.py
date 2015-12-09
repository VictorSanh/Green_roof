# -*- coding: utf-8 -*-

"""

CLASS ENVIRONMENT

"""

# Bibliothèques

class Environment(object):
    """
    La classe environment :

    récupère des données météo pour calculer l'isolement de l'installation
    """

    def __init__(self, localisation, date):
        """ Initialise l'environment avec la localisation et la date """
        self.loc = localisation
        self.date = date

    def temperature(self, time):
        """ Donne la température à un instant donné """
        return 0

    def irradiance(self, time):
        """ Donne les radiations solaires (W/m^2) à un moment de la journée """
        return 0

    def pression(self, time):
        """ Donne la pression à un moment de la journée """
        return 0