# -*- coding: utf-8 -*-

"""

CLASSE IRRADIANCE - UTILISEE DANS ENVIRONNEMENT


"""

# Biliothèques

import subprocess
import math
from os import path


code_fortran_dir = path.join(path.dirname(__file__), 'code_fortran')

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
        mois = int(self.mois)
        jour = int(self.jour)
        nbjours = 0
        nbheures = 0
        dic = {'1':'31', '2':'28', '3':'31', '4':'30', '5':'31', '6':'30', '7':'31','8':'31','9':'30','10':'31','11':'30','12':'31'}
        for i in range(1, mois):
            nbjours += int(dic['{}'.format(i)])
        nbjours += jour
        nbheures = 24*nbjours
        return nbheures

    def point(self):
        """Detecte le numéro du point où l'on est par rapport 
        à la liste des points donnée"""
        (x_lieu,y_lieu) = convert_coord(self.latitude, self.longitude)
        point = 0
        dist_min = 10000
        with open("coord_points.txt", 'r') as fichier:
            for ligne in fichier:
                mots = ligne.split()
                (x,y) = convert_coord(float(mots[3]), float(mots[2]))
                distance = math.sqrt((x - x_lieu)**2 + (y - y_lieu)**2)
                if distance <= dist_min:
                    point = int(mots[1])
                    dist_min = distance
        return point

    def creation_fichier(self):
        """cree le fichier .txt qui contient les irradiances
        au point qui nous interresse"""
        s = '{}'.format(self.point())
        proc = subprocess.Popen([".\plot_variable.exe"], stdin=subprocess.PIPE)
        proc.stdin.write(code
        proc.stdin.write((s + "\n").encode())
        proc.stdin.close()
        proc.wait()

    def extraire_irradiance(self):
        """Permet de stocker les données voulues au point donné
        dans le vecteur self.irradiance"""
        self.creation_fichier()
        heure = self.heure()
        doc = "irradiance_totale_point_{}.txt".format(self.point())
        with open(doc, 'r') as fichier:
            i = 1
            for ligne in fichier:
                if (i >= heure) and (i < heure + 25):
                    mots = ligne.split()
                    self.irradiance.append(float(mots[0]))
                i = i + 1
        return self.irradiance

# problème pour le 31 décembre !!
