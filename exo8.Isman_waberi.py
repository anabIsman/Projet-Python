"""
Exercice 8.1

tableau = [0] * 9
print(len(tableau))
for i in range(0,len(tableau)):
    print("saisir un nombre pour la case n° ", i)
    tableau[i] = input()

print("\n")

somme = 0
for j in range(0, len(tableau)) :
    somme = somme + int(tableau[j])

print("la somme est égale à ", somme)

"""

"""
Exercice 8.2


tab1 = [4, 8, 7, 9, 1, 5, 4, 6]
tab2 = [7, 6, 5, 2, 1, 3, 7, 4]

tab3 = [0] * len(tab1)

for i in range (0, len(tab1)):
    tab3[i] = tab1[i] + tab2[i]

for j in range (0, len(tab3)):
    print(tab3[j])

"""

"""
Exercice 8.3

noms = [] 
notes = []

while True:
    print("saisir un nom d'élève ")
    noms.append(input())
    print("saisir sa note ")
    notes.append(input())

    print("voulez vous quitter? tape (q) ")
    if(input() == 'q'):
        break
somme = 0
for i in range (0, len(notes)):
    somme = somme + int(notes[i])

moyenne = somme / len(notes)

print("la moyenne de la classe est : ", moyenne)

print("voici les élèves qui ont une note supérieur à la moyenne de la classe")

for i in range (0, len(notes)) :
    if(int(notes[i]) > moyenne ) :
        print("nom de l'élève : ", noms[i], "et sa note : ", notes[i])
"""
