# cette algorithme a pour objectif d'afficher 
# le triangle en chiffres evolutifs
"""
exemple:
       1
       1 2
       1 2 3
       1 2 3 4
       1 2 3 4 5
       ...
"""
line = 6
for i in range(line):
    for j in range(i):
        print(j+1,end=" ")
    print(" ")
