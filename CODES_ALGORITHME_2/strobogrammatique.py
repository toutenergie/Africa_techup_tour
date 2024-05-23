""" 
les nombres strobogrammatique
definition:
    C'est un nombre qui s'ecrive de la meme facon quant on pivote de 180C
"""
def is_strobogrammatique(n):
    strobo ={"0":"0","1":"1","2":"2","8":"8","6":"9","9":"6"}
    if type(n) is int:
        n = str(n)
    left = 0
    reghit = len(n)-1
    while reghit - left >= 0:
        if not n[left] in strobo.keys() or not n[reghit] in strobo.keys() or n[left] != strobo[n[reghit]]:
            return False
        reghit -= 1
        left += 1
    return True

for i in range(1,100):
    if is_strobogrammatique(i):
        print("{} : {}".format(i,is_strobogrammatique(i)))