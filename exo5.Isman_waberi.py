
""" Exercice 5.1

a = input("Saisir un nombre ")
if int(a) > 0 :
    print ("nombre est positif")
else :
    print("nombre est negatif")
"""

""" Exercice 5.2

a = input("Saisir un nombre ")
b = input("Saisir un deuxieme nombre ")
c = int(a) * int(b) 

if c > 0 :
    print("produit de ", int(a), " et ", int(b), " est positif")
else:
    print("produit de ", int(a), " et ", int(b), " est négatif")
"""

""" Exercice 5.3

a = input("Saisir un premier nom ")
b = input("Saisir un deuxieme nom ")
c = input("Saisir un troisieme nom ")

if(a[0] < b[0]) :
    if(a[0] < c[0]):
        print("Ils sont dans l'ordre alphabétique")
    else:
        print("Ils ne sont pas dans l'ordre alphabétique")
else:
    print("Ils ne sont pas dans l'ordre alphabétique")

    """

""" Exercice 5.4

age = input("saisir votre age ")
abonnement = input("Avez vous un abonnement ? Si Oui (O) sinon (N) ")

if (abonnement == "N"):
    if  int(age) > 25 : 
        print("vous allez payer 10€")
    else:
        print("vous allez payer 7.5€")
else:
    print("vous allez payer 8€")
"""

""" Exercice 5.5

annee = input("saisir une année ")
if (int(annee) % 4 == 0 and int(annee) % 100 != 0) :
     print("annee  bisextille")
elif (int(annee) % 400 == 0):
     print("annee  bisextille")
else:
    print("annee non bisextille")
"""

"""
    Exercice 5.6

heure = input("saisir l'heure ")
minute = input("saisir les minutes ")

if(int(heure) == 23):
    if(int(minute) == 59 ):
        print("Dans une minute, il sera 0 heure 00")
    else:
        print("Dans une minute, il sera", int(heure), " heure ", int(minute) + 1)
else:
    if(int(heure) < 23 ):
        if(int(minute) == 59):
            print("Dans une minute, il sera", int(heure) + 1, " heure ", 00)
        else:
            print("Dans une minute, il sera", int(heure), " heure ", int(minute) + 1)
        """

""" Exercice 5.7


nbrPhotocopie = int(input("Saisir les nombres de photocopie "))
nbrTotal = 0
if nbrPhotocopie <= 10:
    nbrTotal = nbrPhotocopie * 0.1
elif nbrPhotocopie <= 30:
    nbrTotal = 10 * 0.1 + (nbrPhotocopie - 10) * 0.09
else:
    nbrTotal = 10 * 0.1 + 20 * 0.09 + (nbrPhotocopie - 30) * 0.8
print("La facture pour", nbrPhotocopie, "Photocopie est de", nbrTotal, "€")
"""

""" Exercice 5.8

age = int(input("Entrez l'age de l'habitat"))
sexe = int(input("Entrez votre sexe si c'est un Homme (H) sinon (F)" ))
revenuImpossable = int(input("Entrez votre revenu"))
montantImpot = 0
if sexe == "H" & age >= 20:
    revenuImpossable = float(input("Saisir votre revenu impossable : "))
    if age <= 40:
        montantImpot = revenuImpossable * 0.1
    else: 
        montantImpot = revenuImpossable * 0.15
elif sexe == "F" & 18 <= age <= 35:
    revenuImpossable = float(input("saisir votre revenu impossable : "))
    montantImpot = revenuImpossable * 0.1

if montantImpot > 0:
    print("L'habitant est impossable. le mantant de l'impot est", "mantantImpot", "€")
else:
    print("L'habitant n'est pas impossable ")
"""

""" Exercice 5.9

age = int(input("Entrez l'age du conducteur "))
anneePermis = int(input("Saisir le nombre d'année en possession du permis"))
nbrAccidents = int(input("Saisir le nombre d'année que le conducteur a fais un accident "))
nbrAnneeFidelité = int(input("Saisir le nombre d'année de fidelité" ))

tarifBleu = "refusé"
tarifVert = "tarif vert"
tarifOrange = "tarif orange"
tarifRouge = "tarif rouge"

if age < 25 & anneePermis < 2:
    if nbrAccidents == 0:
        tarif = tarifRouge
    else:
        tarif = "refusé"

elif age >= 25 & anneePermis >= 2:
    if nbrAccidents == 0:
        tarif = tarifOrange
    else:
        tarif = tarifRouge
elif age >= 25 & anneePermis >= 2:
    if nbrAccidents == 0:
        tarif = tarifVert
    elif nbrAccidents == 1:
        tarif = tarifOrange
    else: 
        tarfi = tarifRouge
# Je vérifie la fidelité du client et beneficie un contrat avantageux 
if nbrAnneeFidelité > 1:
    if tarif == tarifRouge:
        tarif = tarifOrange
    elif  tarif == tarifOrange:
        tarif = tarifVert

print("Tarif applicable est :", tarif)

"""




    

