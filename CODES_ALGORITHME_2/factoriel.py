""" de finition du factoriel"""
def is_factoriel(nb):
    if nb == 0 or nb == 1:
        return 1
    f=1
    for i in range(1,nb+1):
        f *=i
    return f

#print(is_factoriel(6))

def recursion_factoriel(n):
    if n == 0 or n == 1:
        return 1
    return n*recursion_factoriel(n-1)
            
#print(recursion_factoriel(6))
""" determination du nombre d'euler"""
def euler_number(nb):
    euler = 0
    for i in range(nb):
        euler += 1/is_factoriel(i)
    return euler
print(euler_number(10))