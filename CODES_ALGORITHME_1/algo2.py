# dans cette partie nous allons inverser le triangle
"""
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
"""
row = 6
for i in range(row,0,-1):
    b = (1+row)-i
    for j in range(1,i+1):
        print(b,end=" ")
    print(" ")
         
     