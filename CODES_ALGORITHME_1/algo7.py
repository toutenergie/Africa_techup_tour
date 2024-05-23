"""
Creer un pyrimide avec des nobres
exemple:
    1
    1 2 3
    4 5 6 7
    ... 
"""
rows = 6
for i in range(rows):
    for j in range(i):
        print(i+j,end=" ")
    print(" ")