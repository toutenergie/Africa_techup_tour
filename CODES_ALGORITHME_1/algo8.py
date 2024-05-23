"""
mirrode pyramide
exemple:
    1 2
  1 2 3
1 2 3 4
...
"""
rows = 6
for i in range(1,rows+1):
  for j in range(1,rows-i+1):
    print(" ",end=" ")
  for j in range(1,i+1):
    print(j,end=" ")
  print(" ")
#------------------------------------------------------------------------
