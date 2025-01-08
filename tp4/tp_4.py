import json
import os
import pathlib
import csv

myFolderpath= pathlib.Path(__file__).parent.resolve()	
os.chdir(myFolderpath)

dicBoisson = { 
	'Café noir' : {'prix':20}, 
	'Café au lait' : {'prix':25}, 
	'Thé' : {'prix':15},
	'Chocolat au lait' : {'prix':35},
    'Cappuccino' : {'prix':40},
    'Annuler' : {'prix':0}
}

dicPiece = {
    '5': {'quantité': 10},
    '10': {'quantité': 10},
    '20': {'quantité': 10},
    '50': {'quantité': 10}
}
dicVentes = {boisson: 0 for boisson in dicBoisson if boisson != 'Annuler'}

# Création du fichier JSON pour les boissons

with open('liste_boisson.json', 'w') as file:
    json.dump(dicBoisson, file, indent=4)

# Création du fichier csv pour les pièces
with open('liste_piece.csv', mode="w+") as fichier_csv:
    writter = csv.writer(fichier_csv)
    writter.writerow(["Pièce", "Quantité"])
    for piece, details in dicPiece.items():
        writter.writerow([piece, details['quantité']])

def ajouter_piece(piece):
    if piece in dicPiece:
        dicPiece[piece]['quantité'] += 1
    else:
        dicPiece[piece] = {'quantité': 1}

def retirer_piece(piece):
    if piece in dicPiece and dicPiece[piece]['quantité'] > 0:
        dicPiece[piece]['quantité'] -= 1
        return True
    return False

def afficher_stock():
    print("Stock de pièces :")
    for piece in dicPiece:
        print(f"{piece}€ : {dicPiece[piece]['quantité']}")

def afficher_ventes():
    print("\nVentes de boissons :")
    for boisson, quantite in dicVentes.items():
        print(f"{boisson} : {quantite} vendue(s)")


# Création du distributeur de boisson

choix = ""
while choix != "Annuler":
    print("\n\n--------Voici la liste des choix--------")
    print("Boissons")
    print("Autre")
    print("Annuler")
    print("--------------------------------------------")
    choix = input("Que voulez vous faire ?")
    if choix == "Autre":
        print("\n\n--------Voici la liste des boissons et leur prix--------")
        print("-1 pour afficher le stock")
        print("-2 pour afficher les boissons vendues")
        print("--------------------------------------------------------")

        choix = input("Que voulez vous faire ?")
        if choix == "-1":
            afficher_stock()
        elif choix == "-2":
            afficher_ventes()
    elif choix == "Boissons":
        print("\n\n--------Voici la liste des boissons et leur prix--------")

        for boisson in dicBoisson:
            if boisson == "Annuler":
                print(boisson)
            else:
                print(boisson, dicBoisson[boisson]['prix'],"C")

        print("--------------------------------------------------------")
        choix = input("Que voulez vous faire ?")
        if choix == "Annuler":
            print("Vous avez annulé votre choix.")
        elif choix in dicBoisson:
            print(f"Vous avez choisi {choix}. Le prix est de {dicBoisson[choix]['prix']}C.")
            montant_insere = 0
            while montant_insere < dicBoisson[choix]['prix']:
                pièce = input("Insérez une pièce (5, 10, 20, 50 C): ")
                if pièce in dicPiece:
                    ajouter_piece(pièce)
                    montant_insere += int(pièce)
                    print(f"Montant inséré : {montant_insere} C")
                else:
                    print("Pièce non valide.")
            monnaie_a_rendre = montant_insere - dicBoisson[choix]['prix']
            print(f"Voici votre {choix}.")
            print(f"Monnaie à rendre : {monnaie_a_rendre}€")
            for piece in sorted(dicPiece.keys(), key=float, reverse=True):
                while monnaie_a_rendre >= float(piece) and dicPiece[piece]['quantité'] > 0:
                    monnaie_a_rendre -= float(piece)
                    retirer_piece(piece)
                    print(f"Rendu : {piece}€")

            if monnaie_a_rendre > 0:
                print(f"Il reste {monnaie_a_rendre}€ non rendu. Veuillez contacter le support.")
            print("Merci pour votre achats, à bientôt.")
            dicVentes[choix] += 1 
        else:
            print("Le choix n'est pas valide.")
    elif choix == "Annuler":
        print("Vous avez annulé votre choix.")
        
    else:
        print("Le choix n'est pas valide.")
    
    
 

