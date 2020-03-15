# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:58:10 2020

@author: pierr
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import math


#==============================================================================
#                  Expérience 1
#==============================================================================

#FAIRE EN LOGARITHMIQUE
#ou alors plot en fonction de la surtension, voire faire des droites de tafel

Resistance = np.array([0,0.1,0.33,1,3.3,10,33,100,330,1000000]) #10000=infini
voltage    = np.array([0.065,0.169,0.433,1.34,3.17,3.51,3.66,3.7,3.71,3.72])
courant    = np.array([0.,0.,0.,0.,0.2,0.79,1.03,1.10,1.13,1.14]) #en mA
courant    = courant * 10**(-3) #en Amperes
#print(courant)

def ButlerVolmer(surtension):
    T = 20.+273.15 #température du labo en Kelvin
    z = 2.         #electrons echanges
    R = 8.314
    F = 96500.
    
    facteur = z*F*surtension / (R*T)
    terme1 = np.exp( 0.5 * facteur)
    terme2 = np.exp(-0.5 * facteur)
    
    return (terme1 - terme2)

Evaluation = ButlerVolmer(voltage-1.23)
print(Evaluation)

A = np.dot(Evaluation,courant)
B = np.dot(courant,courant)
print(A)
print(B)

print(A/B)



 


plt.figure("1")
plt.title("Evolution de l'intensité en fonction du voltage")
plt.plot(courant,voltage-1.23,'o-',color='red')
plt.xlabel('Intensité [mA]')
plt.ylabel('Surtension [V]')


surtension = voltage - 1.23
print(surtension)

plt.figure("1bis")
plt.title("Sous forme Butler-Volmer")
plt.plot(surtension,np.log(courant),'o-',color='red')
plt.xlabel('surtension')
plt.ylabel('courant')
#plt.xlim(-3., 3)



#==============================================================================
#                  Expérience 2
#==============================================================================
#faire en log askip

Temps         = np.linspace(25,225,9)
VolumeProduit = np.array([5,10,15,21,26,31,36,41,47])

plt.figure("2")
plt.title("Evolution du volume de H2 produit en fonction du temps")
plt.plot(Temps,VolumeProduit,'o-',color='red')
plt.xlabel('Temps [sec]')
plt.ylabel('Volume produit [cm³(?)]')


#==============================================================================
#                  Expérience 3
#==============================================================================


Voltage = np.array([0.006,0.008,0.015,0.03,0.10,0.30,0.58,0.66,0.71,0.74])
Courant = np.array([0.03,0.03,0.03,0.03,0.03,0.03,0.02,0.,0.,0.])

plt.figure("3")
plt.title("Evolution du potentiel dans la cellule en fonction du courant")
plt.plot(Courant,Voltage,'o-',color='red')
plt.xlabel('Courant [mA]')
plt.ylabel('Voltage [mV]')


#==============================================================================
#                  Expérience 4
#==============================================================================


Temps  = np.linspace(25,1000,40)
Volume = np.array([0.03,0.03,0.03,0.03,0.03,0.03,0.02,0.,0.,0.])

#matplotlib.rcParams['toolbar'] = 'None'
#plt.rcParams['figure.facecolor'] = 'None'
'''
plt.figure("4")
plt.title("Consommatiuon du volume de H2 en fonction du temps")
plt.plot(Courant,Voltage,'-r')
plt.xlabel('Courant [mA]')
plt.ylabel('Voltage [mV]')
'''


#==============================================================================
#                  Butler-Volmer théorique
#==============================================================================

def ButlerVolmer(I0,alpha,surtension):
    T = 20.+273.15 #température du labo en Kelvin
    z = 2.         #electrons echanges
    R = 8.314
    F = 96500.
    
    facteur = z*F*surtension / (R*T)
    terme1 = np.exp( (1-alpha) * facteur)
    terme2 = np.exp(   -alpha  * facteur)
    
    return I0 * (terme1 - terme2)

surtension = np.linspace(0.,2.,1000)
I0         = 45.92 #10**(-3.6)*20  #on a 20 cm² avec Platine
alpha      = 0.5   #valeur à trouver
CourantTheorique = ButlerVolmer(I0,alpha,surtension)

plt.figure("1bisbis")
plt.title("Sous forme Butler-Volmer théorique")
plt.plot(surtension,CourantTheorique,color='red')
plt.xlabel('surtension')
plt.ylabel('log courant théorique')

#plt.show()

