"""
affiche d'un triangle inverse en 5
exemple:
    5 5 5 5 5
    5 5 5 5
    5 5 5
    5 5
    5  
"""
rows = 6
for i in range(rows,1,-1):
    for j in range(1,i):
        print(5,end=" ")
    print(" ")