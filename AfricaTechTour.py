# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:03:04 2024

@author: ABDOULAHI FAYE
"""
# =============================================================================
# cours sur les fichiers python
# with open('zoo.txt', 'r') as fichier:
#     for ligne in fichier:
#         print(ligne)

# fichier.close()
# =============================================================================
# =============================================================================
# # ECRITUR DANS UN FICHIER PYTHON
# animaux2 = [" poisson ", " abeille ", " chat "]
# with open('zoo2.txt','w') as file:
#     for animal in animaux2:
#         file.write("C'est un {}\n".format(animal))
        
        
#     file.close()
# =============================================================================
# creation d'un fichier de calcul des coordonnées d'un spirale
import math
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
angles =np.arange(0,16*math.pi,0.01)
rayon=np.arange(0.5,len(angles),0.01)
print(len(angles))
print(len(rayon))
# calcul des coordonées x ,y
x=[]
y=[]
for r,a in zip(rayon,angles):
    x.append(r*math.cos(a))
    y.append(r*math.sin(a))
with open('spirat.txt','w') as file:
    for i,j in zip(x,y):
        file.write("{:0.5f}   {:0.5f}\n".format(i,j))
    file.close()
# =============================================================================
# 
xx = []
yx = []
with open ("spirat.txt", "r") as f_in :
    for line in f_in :
     coords = line . split ()
     xx. append ( float ( coords [0]))
     yx. append ( float ( coords [1]))
    
plt.figure ( figsize =(8 ,8))
mini = min (x+y) * 1.2
maxi = max (x+y) * 1.2
plt.xlim (mini , maxi )
plt.ylim (mini , maxi )
plt.plot (x, y)
# =============================================================================
                   