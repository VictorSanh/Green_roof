# -*- coding: utf-8 -*-
import os

class Irradiance():
    """ La classe irradiance va permettre d'extraire l'irradiance au point donné"""

    def __init__(self, longitude, latitude, jour, mois):
        """ Initialise l'environment avec la localisation et la date """
        self.longitude = longitude
        self.latitude = latitude
        self.jour = jour
        self.mois = mois
        self. irradiance = [] #on va stocker les irradiances pour les 24h de la journée

    def heure(self):
        """Donne l'heure de l'année correspondant au jour et au mois"""
        return 0

    def point(self):
        """Detecte le numéro du point où l'on est par rapport 
        à la liste des points donnée"""
        point = 0
        with open("coord_points.txt", 'r') as fichier:
            for ligne in fichier:
                mots = ligne.split()
                if (float(mots[2]) == self.longitude) and (float(mots[3]) == self.latitude):
                    point = int(mots[1])
        return point

    def creation_fichier(self):
        """cree le fichier .txt qui contient les irradiances
        au point qui nous interresse"""
        s = '{}'.format(self.point())
        # os.execl(".\plot_variable.exe", s) : cette commande ne fonctionne pas chez moi
        # elle signifie exectuer le ficher machin avec le paramètre s 
        # (c'est exactement ce qu'on veut je crois)

    def extraire_irradiance(self):
        """Permet de stocker les données voulues au point donné
        dans le vecteur self.irradiance"""
        # self.creation_fichier()
        heure = self.heure()
        doc = "irradiance_totale_point_{}.txt".format(self.point())
        with open(doc, 'r') as fichier:
            i = 1
            for ligne in fichier:
                if (i >= heure) and (i < heure + 25):
                    mots = ligne.split()
                    self.irradiance.append(float(mots[0]))
                i = i + 1
        self.irradiance = self.irradiance[::-1]
        return self.irradiance

# les fonctions marchent une fois qu'on a exectué le bon excecutable 
# (vous pouvez tester pour la point 1)
# Néanmoins je n'arrive pas à excécuter le .exe directement dans python...