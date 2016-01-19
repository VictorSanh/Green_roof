# -*- coding: utf-8 -*-

"""

CLASS DONNEES METEO - DONNEES JSON


"""

# Bibliothèques

import csv
import json
import math
from os import path
from .lambert93 import convert_coord

ressources_dir = path.join(path.dirname(__file__), 'ressources')
data_base_dir = path.join(path.dirname(__file__), 'data_base')

def detecte_IDstation():
    # Stock dans un dictionnaire les longitudes, latitues et les ID des 
    # stations correspondantes
    dico = {}
    with open(path.join(ressources_dir, 'postesSynop.json')) as file:
            doc=json.load(file)
            fichier_courant = doc["features"]
            for station in fichier_courant:
                element = station["properties"]
                (lati_converted, long_converted) = convert_coord(float(element["Latitude"]),float(element["Longitude"]))
                dico[lati_converted,long_converted] = element["ID"]
    return dico

def repere_station(lati, longi):
    #Repère la station la plus proche du point ou a cliqué l'utilisateur pour 
    #y extraire les données  
    
    diconaire = detecte_IDstation()
    L = list(diconaire.keys())
    lati_station = L[0][0]
    long_station = L[0][1]
    (lati_c,long_c) = convert_coord(lati,longi)
    minimum = math.sqrt((long_station - long_c)**2 + (lati_station - lati_c)**2)
    for cle in diconaire.keys():
        if math.sqrt((cle[1] - long_c)**2 + (cle[0] - lati_c)**2) <= minimum:
            lati_station = cle[0]
            long_station = cle[1]
            minimum = math.sqrt((cle[1] - long_c)**2 + (cle[0] - lati_c)**2)
    IDsolution = diconaire[lati_station,long_station]
    return IDsolution

class ValeurNonCommuniquee(Exception): 
    def __init__(self):
        super().__init__('La valeur demandée nest pas communiquée')

class DonneesMeteo(object):
    """
    La classe DonneesMeteo :

    récupère des données météo pour calculer l'isolement de l'installation
    """

    def __init__(self, latitude, longitude, mois, jour):
        """ Initialise l'environment avec la localisation et la date """
        self.mois = str(mois)
        if (jour < 10):
            self.jour = '0' + '{}'.format(jour)
        else:
            self.jour = str(jour)
        self.annee = str(2014)
        self.ID = repere_station(latitude, longitude)

    def get_t(self):
        """ Donne la température en Kelvin à un instant donné """
        annee = self.annee
        mois = self.mois
        jour = self.jour
        ID = self.ID
        s = 'synop.{}{}.csv.gz'.format(annee, mois)
        with open(path.join(data_base_dir, s)) as csvfile:
            doc = csv.reader(csvfile, delimiter = ';')
            temp = []
            for row in doc:
                for heure in range(8):
                    carac = int(3*heure)
                    if carac > 10:
                        strheure = str(carac) + '0000'
                    else:
                        strheure = '0' + str(carac) + '0000'
                    if row[1] == annee + mois + jour + strheure and row[0] == ID: 
                        if row[7] == 'mq':
                            raise ValeurNonCommuniquee
                        temp.append(row[7])
        return temp

    def get_pres(self):
        """ Donne la pression à un moment de la journée """
        annee = self.annee
        mois = self.mois
        jour = self.jour
        ID = self.ID
        s = 'synop.{}{}.csv.gz'.format(annee, mois)    
        with open(path.join(data_base_dir, s)) as csvfile:
            doc = csv.reader(csvfile, delimiter = ';')
            pres = []
            for row in doc:
                for heure in range(8):
                    carac = int(3*heure)
                    if carac > 10:
                        strheure = str(carac) + '0000'
                    else:
                        strheure = '0' + str(carac) + '0000'
                    if row[1] == annee + mois + jour + strheure and row[0] == ID:
                        if row[20] == 'mq':
                            raise ValeurNonCommuniquee
                        pres.append(row[20])
        return pres
        
    def get_humidite(self):
        """ Donne l'humidité ambiante à un instant donné """
        annee = self.annee
        mois = self.mois
        jour = self.jour
        ID = self.ID
        s = 'synop.{}{}.csv.gz'.format(annee, mois)
        with open(path.join(data_base_dir, s)) as csvfile:
            doc = csv.reader(csvfile, delimiter = ';')
            humidite = []
            for row in doc:
                for heure in range(8):
                    carac = int(3*heure)
                    if carac > 10:
                        strheure = str(carac) + '0000'
                    else:
                        strheure = '0' + str(carac) + '0000'
                    if row[1] == annee + mois + jour + strheure and row[0] == ID: 
                        if row[9] == 'mq':
                            raise ValeurNonCommuniquee
                        humidite.append(row[9])
        return humidite
