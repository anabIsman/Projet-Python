"""
Exercice 10 : Read
"""
with open('annuaire.txt', 'r') as fichier_annuaire:
    while True:
        
        nom_recherche = input("Entrez le nom à rechercher (ou appuyez sur Entrée pour quitter) : ")
        if nom_recherche == "":
            break

        ligne_trouvee = False
        for ligne in fichier_annuaire:
            elements = ligne.strip().split(',')
            nom = elements[0].strip().split(':')[1].strip()
            numero_telephone = elements[1].strip().split(':')[1].strip()

            if nom.lower() == nom_recherche.lower():
                print(f"Le numéro de téléphone de {nom} est : {numero_telephone}")
                ligne_trouvee = True
                break
        if not ligne_trouvee:
            print(f"Aucune correspondance trouvée pour le nom {nom_recherche}")

print("Recherche terminée.")
