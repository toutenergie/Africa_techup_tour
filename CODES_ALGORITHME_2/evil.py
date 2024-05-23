"""
Les evil numbers:

Cest un nombre dont sa conversion bin convient un nombre pair de 1
3 <-- 11 c'est un evil number
4 <-- 100 n'est pas un evil number
"""
def is_evil(nb):
    n_list = 0
    while nb != 0:
        if nb % 2 == 1:
            n_list += 1
        nb = nb // 2
    return n_list % 2 == 0

""" 
definissons une fonction qui nous donne tous les evil numbers dans une 
intervalle donner
"""
def list_evil_numbers(inf,sup):
    list_evil = []
    for i in range(inf,sup):
        if is_evil(i):
            list_evil.append(i)
    return list_evil

print(list_evil_numbers(1,10))