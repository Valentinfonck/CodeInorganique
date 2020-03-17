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
#courant    = courant * 10**(-3) #en Amperes
#print(courant)

plt.figure("1")
plt.title("The linear regression of the link between the overvoltage and log(I)")
plt.plot(np.log(courant),voltage-1.23,'o-',color='red',label = "Experimental datas")
plt.xlabel('log(I) [A]')
plt.ylabel('Overvoltage [V]')
results1 = np.polyfit(np.log(courant[4:]),voltage[4:]-1.23,1)
print(results1)
logcourantfit = np.linspace(-8,0.5,3000)
surtensionfit = results1[0]*logcourantfit + results1[1]
plt.plot(logcourantfit,surtensionfit, label = "eta = 0.31*log(I) + 2.424")
plt.legend()
plt.show()