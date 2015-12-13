# -*- coding: utf-8 -*-

"""

CLASS ENVIRONMENT

"""

# Bibliothèques

import csv
import json
import math

     
def detecte_IDstation():
    # Stock dans un dictionnaire les longitudes, latitues et les ID des 
    # stations correspondantes
    dico = {}
    with open('postesSynop.json') as file:
            doc=json.load(file)
            fichier_courant = doc["features"]
            for station in fichier_courant:
                element = station["properties"]
                dico[element["Longitude"],element["Latitude"]] = element["ID"]
    return dico

a=detecte_IDstation()
for cle in a:
    print(cle[0])

def repere_station(long, lati):
    #Repère la station la plus proche du point ou a cliqué l'utilisateur pour 
    #y extraire les données
    #c'est pas encore fini!!
    diconaire = detecte_IDstation()
    list_vector = []
    for cle in diconaire:
        list_vector.append(math.sqrt((cle[0] - long)**2 + (cle[1] - lati)**2))


class Environment(object):
    """
    La classe environment :

    récupère des données météo pour calculer l'isolement de l'installation
    """

    def __init__(self, longitude, latitude, date):
        """ Initialise l'environment avec la localisation et la date """
        self.longitude = longitude
        self.latitude = latitude
        self.date = date

    def get_t(self, time):
        """ Donne la température à un instant donné """
        
        return 0

    def irradiance(self, time):
        """ Donne les radiations solaires (W/m^2) à un moment de la journée """
        return 0

    def get_pres(self, time):
        """ Donne la pression à un moment de la journée """
        return 0
        
    def get_u(self,time):
        """ Donne l'humidité ambiante à un instant donné """
        return 0