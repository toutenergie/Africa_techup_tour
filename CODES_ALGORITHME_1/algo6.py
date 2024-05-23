"""
half inversion:
              exemple:
                    0 1 2 3 4 5
                    0 1 2 3 4
                    0 1 2 3
                    0 1 2
                    0 1
"""
rows = 6
for i in range(rows,0,-1):
    for j in range(i):
        print(j,end=" ")
    print(" ")