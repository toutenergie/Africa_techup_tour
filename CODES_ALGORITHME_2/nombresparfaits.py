"""
cette fonction donne l'ensembles des diviseurs d'un nombre donner
"""
def get_diveders(nb):
    list_diveders=[]
    for div in range(1,nb+1):
        if nb % div == 0:
            list_diveders.append(div)
        
    return list_diveders

#print(get_diveders(28))
""" un nombre parfait un nombre dont la 
somme de ces diviseurs egal a lui meme"""
def is_perfect(n):
    if sum(get_diveders(n)[:-1]) == n:
        print("------------------------")
        return True
    else:
        return False

"""donnons la liste des nombres parfait"""
def list_perfect(inf,sup):
    l=[]
    for perfect in range(inf,sup):
        if is_perfect(perfect):
            l.append(perfect)
    return l

print(list_perfect(1,10000))
