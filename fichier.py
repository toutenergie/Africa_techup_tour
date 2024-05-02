# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:21:23 2024

@author: ABDOULAHI FAYE
"""

# =============================================================================
fichier = open("hello.txt", "w")
fichier.write("Hello, world!")
fichier.close()
with open("file.txt") as fichier:
    for ligne in fichier:
        # faire quelque chose avec une ligne
        print(ligne)
# =============================================================================
