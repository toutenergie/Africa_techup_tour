""" definition d'un numbre pair"""
def pair(nb):
    if nb % 2 == 0:
        return True
    else:
        return False
    
print(pair(3))