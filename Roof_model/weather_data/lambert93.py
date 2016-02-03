# -*- coding: utf-8 -*-

"""

PROJECTION LAMBERT 93

"""

import math

def degreeToRadian(deg):
    return float(deg/180*math.pi)

#Definition des constantes
a = 6378137     
e = 0.08181919106 
lc = degreeToRadian(3)
l0 = degreeToRadian(3)
phi1 = degreeToRadian(44) 
phi2 = degreeToRadian(49) 
phi0 = degreeToRadian(46.3) 
X0 = 700000 
Y0 = 6600000 
gN1 = a/math.sqrt(1-e*e*math.sin(phi1)*math.sin(phi1))
gN2 = a/math.sqrt(1-e*e*math.sin(phi2)*math.sin(phi2))
gl1 = math.log(math.tan(math.pi/4+phi1/2)*pow((1-e*math.sin(phi1))/(1+e*math.sin(phi1)),e/2))
gl2 = math.log(math.tan(math.pi/4+phi2/2)*pow((1-e*math.sin(phi2))/(1+e*math.sin(phi2)),e/2))
gl0 = math.log(math.tan(math.pi/4+phi0/2)*pow((1-e*math.sin(phi0))/(1+e*math.sin(phi0)),e/2))
n = (math.log((gN2*math.cos(phi2))/(gN1*math.cos(phi1))))/(gl1-gl2)
c = ((gN1*math.cos(phi1))/n)*math.exp(n*gl1)
ys = Y0 + c*math.exp(-n*gl0)

# Conversion latitude/longitude en coordonnées cartésiennes
def convert_coord(lati,long):
    phi = degreeToRadian(lati)
    l   = degreeToRadian(long)
    gl  = math.log(abs(math.tan(math.pi/4+phi/2)*pow((1-e*math.sin(phi))/(1+e*math.sin(phi)),e/2)))
    x93 = X0 + c*(math.exp(-n*gl))*(math.sin(n*(l-lc)))
    y93 = ys - c*math.exp(-n*gl)*math.cos(n*(l-lc))
    return (x93/1000,y93/1000)
