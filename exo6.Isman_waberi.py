
""" Exercice 6.1

___ Pseudo code___

Ecrire "saisir un nombre" 
Lire a
Tant que la variable a < 1 ou a > 3 alors 
Lire a

___Script___

a = int(input("saisir un nombre"))
while (a < 1) | (a > 3):
    print(int(a))
    a = int(input("saisir un nombre "))
"""""



""" Exercice 6.2

___Pseudo code___

Ecrire "Saisir un nombre"
Lire a

Tant que a < 10 ou a > 20 alors 
Si a > 20 alors 
Lire "Plus petit"
    else 
    Lire " Plus grand"


___Script___

a = int(input("Saisir un nombre"))
while (a < 10) | (a > 20):
    print (int(a))
    if (a > 20):
        print("Plus petit")
    else : 
        print ("Plus grand")
    a = int(input("Saisir un nombre"))
"""



""" Exercice 6.3

nbrDepart = int(input("Saisir un nombre de depart : "))
somme = 0

for i in range(1, nbrDepart + 1):
    somme += i
print("La somme des nombres jusqu'a", nbrDepart, "est égale à", somme)
"""

""" Exercice 6.4

plusGrand = 0
position = 0

while True:
    nbr = int(input("Saisir le nombre numero {position + 1} : "))
    if nbr == 0:
        break

    if nbr > plusGrand:
        plusGrand = nbr
        position = position + 1
print("Le plus grand de ces nombres est : {plusGrand} en position {position + 1} ")
"""

""" Exercice 6.5

sommeTotal = 0

while True:
    prixAchat = int(input("Saisir le prix de l'achat"))
    if prixAchat == 0:
        break
    sommeTotal += prixAchat

sommepayer = int(input("Saisir la somme payé par le client : "))

monnaie = sommepayer - sommeTotal

while monnaie >= 5:
    coupure5 = monnaie // 5
    monnaie -= coupure5 * 5
    print(coupure5, "coupure de 5 euro")

while monnaie >= 1:
    print(monnaie, "coupure de 1 euro")
    monnaie -= monnaie
print("La totalité de la monnaie à éte rendue :")
"""

