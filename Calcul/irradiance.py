# -*- coding: utf-8 -*-
import subprocess
import math


"""
CLASSE IRRADIANCE - UTILISEE DANS ENVIRONNEMENT
"""

"""Tranformation des longitudes et latitudes par Lambert 93"""
#Definition de constantes
def degreeToRadian(deg):
    return float(deg/180*math.pi)
    
a = 6378137     # semi-major axis of the ellipsoid
e = 0.08181919106 # first eccentricity of the ellipsoid
lc = degreeToRadian(3)
l0 = degreeToRadian(3)
phi1 = degreeToRadian(44) # 1st automecoic parallel
phi2 = degreeToRadian(49) # 2nd automecoic parallel
phi0 = degreeToRadian(46.3) # latitude of origin
X0 = 700000 # x coordinate at origin
Y0 = 6600000 # y coordinate at origin
gN1 = a/math.sqrt(1-e*e*math.sin(phi1)*math.sin(phi1))
gN2 = a/math.sqrt(1-e*e*math.sin(phi2)*math.sin(phi2))
gl1 = math.log(math.tan(math.pi/4+phi1/2)*pow((1-e*math.sin(phi1))/(1+e*math.sin(phi1)),e/2))
gl2 = math.log(math.tan(math.pi/4+phi2/2)*pow((1-e*math.sin(phi2))/(1+e*math.sin(phi2)),e/2))
gl0 = math.log(math.tan(math.pi/4+phi0/2)*pow((1-e*math.sin(phi0))/(1+e*math.sin(phi0)),e/2))
n = (math.log((gN2*math.cos(phi2))/(gN1*math.cos(phi1))))/(gl1-gl2)
c = ((gN1*math.cos(phi1))/n)*math.exp(n*gl1)
ys = Y0 + c*math.exp(-n*gl0)

def convert_coord(lati,long):
    phi = degreeToRadian(lati)
    l   = degreeToRadian(long)
    gl  = math.log(abs(math.tan(math.pi/4+phi/2)*pow((1-e*math.sin(phi))/(1+e*math.sin(phi)),e/2)))
    x93 = X0 + c*(math.exp(-n*gl))*(math.sin(n*(l-lc)))
    y93 = ys - c*math.exp(-n*gl)*math.cos(n*(l-lc))
    return (x93/1000,y93/1000)	

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