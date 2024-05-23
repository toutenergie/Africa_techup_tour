""" un spy numbre c'est un nombre dont la somme de ces chiffre est
egale au produit de ces chiffre"""
def spynumbres(nb):
    somme =0 #sum(map(int,list(str(nb))))
    prodr=1
    for i in str(nb):
        prodr *=int(i)
        somme +=int(i)
    return somme == prodr
    
def Spy_numbres_int(inf,sup):
    list_spy =[]
    for i in range(inf,sup):
        if spynumbres(i):
            list_spy.append(i)
    return list_spy

print(Spy_numbres_int(1,1000))
#print(spynumbres(22))


