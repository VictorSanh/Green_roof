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

ressources_dir = path.join(path.dirname(__file__), 'data/data_towns')
data_base_dir = path.join(path.dirname(__file__), 'data/data_other')

def detecte_IDstation():
    # Stocke dans un dictionnaire les longitudes, latitudes et les ID des 
    # stations correspondantes
	
    detection = {}
	
    with open(path.join(ressources_dir, 'postesSynop.json')) as file:
            doc = json.load(file)
            fichier_courant = doc["features"]
            for station in fichier_courant:
                element = station["properties"]
                (lati_converted, long_converted) = convert_coord(float(element["Latitude"]),float(element["Longitude"]))
                detection[lati_converted,long_converted] = element["ID"]
    return detection

def repere_station(lati, longi):
    #Repère la station la plus proche du point ou a cliqué l'utilisateur pour 
    #y extraire les données  
    
    dictionnaire = detecte_IDstation()
    L = list(dictionnaire.keys())
    lati_station = L[0][0]
    long_station = L[0][1]
    (lati_c,long_c) = convert_coord(lati,longi)
    minimum = math.sqrt((long_station - long_c)**2 + (lati_station - lati_c)**2)
	
    for cle in dictionnaire.keys():
        if math.sqrt((cle[1] - long_c)**2 + (cle[0] - lati_c)**2) <= minimum:
            lati_station = cle[0]
            long_station = cle[1]
            minimum = math.sqrt((cle[1] - long_c)**2 + (cle[0] - lati_c)**2)
    IDsolution = dictionnaire[lati_station,long_station]
    return IDsolution

class ValeurNonCommuniquee(Exception): 
    def __init__(self):
        super().__init__('La valeur demandée nest pas communiquée')

class DonneesMeteo(object):
    """
    La classe DonneesMeteo :

    récupère des données météo pour calculer l'isolement de l'installation
    """

    def __init__(self, longitude, latitude, mois, jour):
        """ Initialise l'environment avec la localisation et la date """
        
        # conversion mois
        if (mois < 10):
            self.strmois = '0' + '{}'.format(mois)
        else:
            self.strmois = str(mois)

        #conversion jour
        if (jour < 10):
            self.strjour = '0' + '{}'.format(jour)
        else:
            self.strjour = str(jour)

        self.strannee = str(2014)
        self.ID = repere_station(latitude, longitude)

    def get_t(self):
        """ Donne la température en Kelvin à un instant donné """
		
        strannee = self.strannee
        strmois = self.strmois
        strjour = self.strjour
        ID = self.ID
        s = 'synop.{}{}.csv'.format(strannee, strmois)
		
        with open(path.join(data_base_dir, s)) as csvfile:
            doc = csv.reader(csvfile, delimiter = ';')
            temp = []
            for row in doc:
                for heure in range(8):
                    valeur_heure = int(3*heure)
                    #Puisqu'on travaille avec une base de données, il faut gérer les cas des nombres
                    #inférieurs à 10: on doit rajouter un 0 au string correspondant
                    if valeur_heure > 10:
                        strheure = str(valeur_heure) + '0000'
                    else:
                        strheure = '0' + str(valeur_heure) + '0000'
                    if row[1] == strannee + strmois + strjour + strheure and row[0] == ID: 
                        #On repère l'instant précis ou l'on veut récupérer la donnée puis on la stocke
                        if row[7] == 'mq':
                            raise ValeurNonCommuniquee
                        temp.append(row[7])
        #On retourne un tableau un tableau à 8 valeurs car il y a 8 mesures effectuées, à chaque
        #intervalle de 3h
        return temp

    def get_pres(self):
        """ Donne la pression à un moment de la strjournée """
		
        strannee = self.strannee
        strmois = self.strmois
        strjour = self.strjour
        ID = self.ID
        s = 'synop.{}{}.csv'.format(strannee, strmois)  
		
        with open(path.join(data_base_dir, s)) as csvfile:
            doc = csv.reader(csvfile, delimiter = ';')
            pres = []
            for row in doc:
                for heure in range(8):
                    valeur_heure = int(3*heure)
                    #Puisqu'on travaille avec une base de données, il faut gérer les cas des nombres
                    #inférieurs à 10: on doit rajouter un 0 au string correspondant
                    if valeur_heure > 10:
                        strheure = str(valeur_heure) + '0000'
                    else:
                        strheure = '0' + str(valeur_heure) + '0000'
                    if row[1] == strannee + strmois + strjour + strheure and row[0] == ID:
                        #On repère l'instant précis ou l'on veut récupérer la donnée puis on la stocke
                        if row[20] == 'mq':
                            raise ValeurNonCommuniquee
                        pres.append(row[20])
        #On retourne un tableau un tableau à 8 valeurs car il y a 8 mesures effectués, à chaque
        #intervalle de 3h
        return pres
        
    def get_humidite(self):
        """ Donne l'humidité ambiante à un instant donné """
		
        strannee = self.strannee
        strmois = self.strmois
        strjour = self.strjour
        ID = self.ID
        s = 'synop.{}{}.csv'.format(strannee, strmois)
		
        with open(path.join(data_base_dir, s)) as csvfile:
            doc = csv.reader(csvfile, delimiter = ';')
            humidite = []
            for row in doc:
                for heure in range(8):
                    valeur_heure = int(3*heure)
                    #Puisqu'on travaille avec une base de données, il faut gérer les cas des nombres
                    #inférieurs à 10: on doit rajouter un 0 au string correspondant
                    if valeur_heure > 10:
                        strheure = str(valeur_heure) + '0000'
                    else:
                        strheure = '0' + str(valeur_heure) + '0000'
                    if row[1] == strannee + strmois + strjour + strheure and row[0] == ID:
                        #On repère l'instant précis ou l'on veut récupérer la donnée puis on la stock
                        #dans un tableau						
                        if row[9] == 'mq':
                            raise ValeurNonCommuniquee
                        humidite.append(row[9])
        #On retourne un tableau un tableau à 8 valeurs car il y a 8 mesures effectués, à chaque
        #intervalles de 3h
        return humidite
