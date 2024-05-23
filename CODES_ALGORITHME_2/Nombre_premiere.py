"""definir uyne fonction qui determine si un nombre premiere ou non"""
def nb_premiere(nb):
    if nb <2:
        return False
    for i in range(2,nb):
        if nb  % i == 0:
            return False
    return True
    
    


""" 
definition d'une fonction qui determine si un nombre
est de sophie germin ou non
definition:
    un nombre premiere est de sophie germin (G) si:
    2*G + 1 est un nombre premiere 
"""
def is_SG_prime(nb):
    if nb_premiere(nb) and nb_premiere(2*nb+1):
        return True
    else:
        return False
    
""" 
fonction de recuperation de la liste des nombres de sophies germin
"""
def list_sg_prime(inf, sup):
    list_SG =[]
    for SG in range(inf,sup+1):
        if is_SG_prime(SG):
            list_SG.append(SG)
    return list_SG
    
print(list_sg_prime(1,100)) 
            
        
