# Correction TD exercices e
# Ecrire un scrype qui determine dans une chaine caractere s'il est present ou non la letrtre "e"
nom_chaine= 'RDZEEeese'
for i in nom_chaine:
    if i=='e':
        break
        print("e est de dans")
    else:
        print("pas de e de dans")
        break

# CORRECTION EXERCICE 2

# COMPTER LES E
l=0
for j in nom_chaine:
    if j == 'e':
        l=l+1
print(l)
# CORRECTION EXERCICE SUIVANTE
nom="gaston"
for no in nom:
    print(no,"*")
    continue
 