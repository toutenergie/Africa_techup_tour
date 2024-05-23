"""
inversion du triangle patern
exemple:
    5 5 5 5 5
    4 4 4 4
    3 3 3
    2 2
    1    
"""
rows = 6
for i in range(rows,0,-1):
    for j in range(i):
        print(i,end=" ")
    print(" ")