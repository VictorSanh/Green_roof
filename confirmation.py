# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 18:24:19 2016

@author: srotc_000
"""


import urllib.parse
import urllib.request
from urllib.error import URLError, HTTPError
import json 
from unidecode import unidecode

class ZeroResult(Exception):
    def __init__(self,valeur):
        self.valeur = valeur
    def __imprim__(self):
        return "{}".format(self.valeur)

class ZeroResultFrance(Exception):
    def __init__(self,valeur):
        self.valeur = valeur
    def __imprim__(self):
        return "{}".format(self.valeur)

#Requete html sur googleapis.com/maps sous la forme suivante :
#https://maps.googleapis.com/maps/api/geocode/json?address=avenue+blaise+pascal+champs+sur+marnes&sensor=false
#Ca renvoie un fichier json avec beaucoup de données sur l'adresse indiquée, dont notamment la lat et longitude.

def geocode(addr):
        """Renvoie un fichier json qui modélise la position indiquée par addr"""
        
        addr_formatee = addr.replace(' ','+')     
        url = ("https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % addr_formatee);        
        #Gestion des accents : é, à,...        
        url = unidecode(url)
        reponse = urllib.request.urlopen(url).read()
        #Problème: reponse est de type bytes, et donc json.load() ne peut le lire.        
        #On préfère donc le convertir avant la lecture sous json.        
        data = reponse.decode('utf-8')        
        return json.loads(data)
#
def trouve_en_france(fichier):
    """Va checker si le champ 'status' du fichier json est bien OK i.e.
    qu'une ville a été trouvée (même si c'est pas la bonne).
    Si le champs 'status' vaut ZERO_RESULTS, c'est qu'il y a rien de trouvé
    et qu'il faut revoir l'adresse entrée. On lève dans ce cas un exception."""
    
    if fichier['status']=="ZERO_RESULTS":
        raise ZeroResult("Pas de résultat")
    else:
        liste_results=fichier['results']
        position=-1
        for i, element in enumerate(liste_results):
            for ss_element in element['address_components']:
                if ss_element['short_name']=="FR":
                    position=i
        if position==-1:
            raise ZeroResultFrance("Pas de résultat en France")
        else:
            return position


def addresse_formatee(fichier, position):
        """Va renvoyer l'adresse formatée selon les criètes de Google Maps 
        afin que l'utilisateur vérifie que ce soit bien la bonne adresse."""
        
        return fichier['results'][position]['formatted_address']
        

def lat_lng(fichier, position):
        """Si l'adresse est validée par l'utilisateur comme son adresse 
        (addresse_formatee), alors on renvoie réellement la latitude et 
        la longitude sous la forme d'un dictionaire 
        {'lat' : valeur_latitude, 'lng' : valeur_longitude}"""
        
        return fichier['results'][position]['geometry']['location']
        
        
#def main(adresse_rentree):
#    try:
#        fichier = geocode(adresse_rentree)
#        pos = trouve_en_france(fichier)
#    except MonException as erreur:
#        print(erreur)
#        erreur.__imprim__()
#    except HTTPError as erreur:
#        print(erreur)
#        erreur.__str__()
#    except URLError as erreur:
#        print(erreur)
#        erreur.__str__()
#    except:
#        print("Something went wrong")        
#    else:
#        print(addresse_formatee(fichier, pos))
#        latlng = lat_lng(fichier, pos)
#        print (latlng['lat'],latlng['lng'])

#
#if __name__=="__main__":
#    main()
    

#Il faut donner de la robustesse au code et la gestion des erreurs
#Par exemple, il y a URLError quand il n'y a pas de connexion internet :
#<urlopen error [Errno 11001] getaddrinfo failed>
#HTTPError quand l'adresse n'est pas trouvée ou
#IndexError quand on veut accéder à un champ du fichier json alors que celui ci est vide.


#Autre possibilité alternative avec la libraire geopy.

#from geopy.geocoders import Nominatim
#geolocator = Nominatim()
#location = geolocator.geocode("aveenue blaise pascal, champs sur marne")
#print(location.address)
#print((location.latitude, location.longitude))

#COMMENTAIRE SUR CE DERNIER CODE

#Bien, renvoie rapidement MAIS ne gère pas vraiment les fautes d'orthographe.

