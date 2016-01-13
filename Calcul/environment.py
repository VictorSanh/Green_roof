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

b = detecte_IDstation()
L = list(b.keys())

class ValeurNonCommuniquee(Exception): 
    def __init__(self):
        super().__init__('La valeur demandée nest pas communiquée')

def repere_station(long, lati):
    #Repère la station la plus proche du point ou a cliqué l'utilisateur pour 
    #y extraire les données

    diconaire = detecte_IDstation()
    L = list(diconaire.keys())
    long_station = float(L[0][0])
    lati_station = float(L[0][1])
    minimum = math.sqrt((long_station - long)**2 + (lati_station - lati)**2)
    for cle in diconaire:
        if math.sqrt((float(cle[0]) - long)**2 + (float(cle[1]) - lati)**2) <= minimum:
            long_station = cle[0]
            lati_station = cle[1]
    return(long_station, lati_station)

a = repere_station(54.520667,-15.887667)

def get_temp(annee, mois, jour, heure, ID):
    """ Donne la température en Kelvin à un instant donné """
    s = 'synop.{}{}.csv.gz'.format(annee, mois)
    with open(s) as csvfile:
        doc = csv.reader(csvfile, delimiter = ';')
        for row in doc:      
            if row[1] == annee+mois+jour+heure and row[0] == ID:              
                a = row[7]
        if a == 'mq':
            raise ValeurNonCommuniquee()
    return a

c = get_temp('2014', '12', '01', '060000', '07139')
print(c)

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

    def get_t(self, annee, mois, jour, heure, ID):
        """ Donne la température en Kelvin à un instant donné """
        s = 'synop.{}{}.csv.gz'.format(annee, mois)
        with open(s) as csvfile:
            doc = csv.reader(csvfile, delimiter = ';')
            for row in doc:      
                if row[1] == annee+mois+jour+heure and row[0] == ID:              
                    a = row[7]
            if a == 'mq':
                raise ValeurNonCommuniquee()
        return a

    def get_pres(self, annee, mois, jour, heure, ID):
        """ Donne la pression à un moment de la journée """
        s = 'synop.{}{}.csv.gz'.format(annee, mois)    
        with open(s) as csvfile:
            doc = csv.reader(csvfile, delimiter = ';')     
            for row in doc:      
                if row[1] == annee+mois+jour+heure and row[0] == ID:              
                    a = row[20]
            if a == 'mq':
                raise ValeurNonCommuniquee()
        return a
        
    def get_u(self, annee, mois, jour, heure, ID):
        """ Donne l'humidité ambiante à un instant donné """
        s = 'synop.{}{}.csv.gz'.format(annee, mois)
        with open(s) as csvfile:
            doc = csv.reader(csvfile, delimiter = ';')
            for row in doc:      
                if row[1] == annee+mois+jour+heure and row[0] == ID:              
                    a = row[9]
            if a == 'mq':
                raise ValeurNonCommuniquee()
        return a