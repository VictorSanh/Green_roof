# -*- coding: utf-8 -*-

class Irradiance():
    """ La classe irradiance va permettre d'extraire l'irradiance au point donné"""

    def __init__(self, longitude, latitude, date):
        """ Initialise l'environment avec la localisation et la date """
        self.longitude = longitude
        self.latitude = latitude
        self.date = date

    def point(self):
        point = 0
        with open("coord_points.txt", 'r') as fichier:
            for ligne in fichier:
                mots = ligne.split()
                if (float(mots[2]) == self.longitude) and (float(mots[3]) == self.latitude):
                    point = int(mots[1])
        return point

    def extraire_LW(self):
        