# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 18:24:19 2016

@author: srotc_000
"""


import urllib.parse
import urllib.request
import json 

class MonException(Exception):
    def __init__(self,valeur):
        self.valeur = valeur
    def __imprim__(self):
        return "MonException ({})".format(self.valeur)
        

    

#Requete html sur googleapis.com/maps sous la forme suivante :
#https://maps.googleapis.com/maps/api/geocode/json?address=avenue+blaise+pascal+champs+sur+marnes&sensor=false
#Ca renvoie un fichier json avec beaucoup de données sur l'adresse indiquée, dont notamment la lat et longitude.

def geocode(addr):
        """Renvoie un fichier json qui modélise la position indiquée par addr"""
        addr_formatee = addr.replace(' ','+')     
        url = ("https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % addr_formatee);        
        reponse = urllib.request.urlopen(url).read()
        #Problème: reponse est de type bytes, et donc json.load() ne peut le lire.        
        #On préfère donc le convertir avec la lecture sous json.        
        data = reponse.decode('utf-8')        
        return json.loads(data)
#
def resultat_trouve(fichier_json):
    """Va checker si le champ 'status' du fichier json est bien OK i.e.
    qu'une ville a été trouvée (même si c'est pas la bonne).
    Si le champs 'status' vaut ZERO_RESULTS, c'est qu'il y a rien de trouvé
    et qu'il faut revoir l'adresse entrée"""
    if fichier_json['results']

def addresse_formatee(fichier_json):
        """Va renvoyer l'adresse formatée selon les criètes de Google Maps 
        afin que l'utilisateur vérifie que ce soit bien la bonne adresse"""
        return fichier_json['results'][0]['formatted_address']
        
def lat_lng(fichier_json):
        """Si l'adresse est validée par l'utilisateur comme son adresse 
        (addresse_formatee), alors on renvoie réellement la latitude et 
        la longitude sous la forme d'un dictionaire 
        {'lat' : valeur_latitude, 'lng' : valeur_longitude}"""
        return fichier_json['results'][0]['geometry']['location']
        
        
fichier = geocode("avenue blaise pascal champss surre marnee")
print(addresse_formatee(fichier))
latlng = lat_lng(fichier)
print (latlng['lat'],latlng['lng'])

#Il faut donner de la robustesse au code et la gestion des erreurs
#Par exemple, il y a URLError
#HTTPError quand l'adresse n'est pas trouvée ou
#IndexError quand on veut accéder à un champ du fichier json alors que celui ci est vide.

#En fait regarder sur fichier_json['statuts']
#Vaut "OK" lorsque c'est bien trouvé
#Vaut "ZERO_RESULTS"
#En fait quand l'adresse est pas trouvée, c'est plutot "ZERO_RESULTS" qui est renvoyé.

#Autre possibilité alternative avec la libraire geopy.

#from geopy.geocoders import Nominatim
#geolocator = Nominatim()
#location = geolocator.geocode("aveenue blaise pascal, champs sur marne")
#print(location.address)
#print((location.latitude, location.longitude))

#COMMENTAIRE SUR CE DERNIER CODE

#Bien, renvoie rapidement MAIS ne gère pas vraiment les fautes d'orthographe.

