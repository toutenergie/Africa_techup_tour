# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:21:23 2024

@author: ABDOULAHI FAYE
"""

# =============================================================================
fichier = open("hello.txt", "w")
fichier.write("Hello, world! je veux metriser le traitement des fichier en python")
fichier.close()
with open("hello.txt") as fichier:
    for ligne in fichier:
        # faire quelque chose avec une ligne
        print(ligne)
# =============================================================================
