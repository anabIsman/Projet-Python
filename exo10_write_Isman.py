"""
Exercice 10 : Write
"""

with open('annuaire.txt', 'a') as fichier_annuaire:
    while True:
        nom = input("Entrez un nom (ou appuyez sur Entrée pour quitter) : ")
        if nom == "":
            break

        numero_telephone = input("Entrez un numéro de téléphone : ")
    
        fichier_annuaire.write(f"Nom : {nom}, Telephone : {numero_telephone}\n")
        
print("Données sauvegardées dans l'annuaire.")
