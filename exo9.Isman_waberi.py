""" Exercice 9.1

def fact(n):
    if n == 0:
        return 1
    else: 
        return n * fact(n-1)
    
#le nombre des chevaux partants et les nombres jouées 

nbrchevauxPartants = int(input("Saisir les nombres des chevaux partants"))
nbrchevauxjouees = int(input("Saisir les nombres des chevaux jouées"))

# Je calcul les chances de gagner dans l'ordre 

chanceOrdre = fact(nbrchevauxPartants) / fact(nbrchevauxPartants - nbrchevauxjouees)

# Je calcul les chances de gagner en desordre 

chancedesordre = fact(nbrchevauxPartants) / (fact(nbrchevauxjouees) * fact(nbrchevauxPartants - nbrchevauxjouees))

# J'affiche les résultats 
print("dans l'ordre : une chance sur", int(chanceOrdre), "de gagne" )
print("dans le desordre : une chance sur", int(chancedesordre), "de gagne")
"""

""" Exercice 9.2

def compteVoyelle (chaine):
    voyelle = "aioeouAEOUI"
    nbrVoyelle = 0

    for caracter in chaine:
        if caracter in voyelle:
            nbrVoyelle += 1

    return nbrVoyelle

chaine = "Je m'amuse beaucoup en algo"
res = compteVoyelle(chaine)
print("le nombre de voyelle dans la chaine est:", res)
"""

