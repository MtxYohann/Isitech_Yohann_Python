print ("Hello world")
import datetime

maDate = datetime.date(2004,12,15)
dateDuJour = datetime.date.today()

age_en_annee = dateDuJour.year - maDate.year
age_en_mois = age_en_annee * 12
age_en_jours = dateDuJour - maDate 
age_en_semaines = age_en_jours / 7

print(age_en_annee,"ans")
print(age_en_mois,"mois")
print(age_en_jours)
print(age_en_semaines)

#Compter les voyelles

voyelles = ["a","e","i","o","u","y"]
mot = "test"
nb_voyelles = 0
for lettre in mot:
    if lettre in voyelles :
        nb_voyelles +=1

if nb_voyelles == 0 : 
        print("Il n'y a pas de voyelles dans le mot \"" + mot + "\".\n")
else :  
    print("Le mot \"" + mot + "\" contient " + str(nb_voyelles) + " voyelles.\n")

#Compter les lettres

lettres = ["u"]
mot = "tututata"
nb_lettre = 0
for lettre in mot:
    if lettre in lettres :
        nb_lettre +=1

if nb_lettre == 0 : 
        print("Il n'y a pas la lettre U dans le mot \"" + mot + "\".\n")
else :  
    print("Le mot \"" + mot + "\" contient " + str(nb_lettre) + " fois la lettre U.\n")

#Renvoyer une liste de mot à partir d’une phrase

phrase = "Bonjour, je m'apelle Yohann"
liste_mot = []

# vérifier la présence d'une lettre

lettres = ["u"]
mot = "tututata"
verif_lettre = True
for lettre in mot:
    if lettre in lettres :
        verif_lettre = True

if verif_lettre == False : 
        print("Il n'y a pas la lettre U dans le mot \"" + mot + "\".\n")
else :  
    print("Le mot \"" + mot + "\" contient bien la lettre U.\n")

#retrouver un mot dans une liste

phrase = ["Bonjour", "voici", "une","phrase"]
mots = "Bonur"
verif_mots = True

for mot in phrase:
    if mots in mot:
        verif_mots = False

if verif_mots == True : 
        print("Il n'y a pas le mot \"" + mots + "\" dans la phrase.\n")
elif verif_mots == False :  
    print("La phrase contient bien le mot \"" + mots + "\".\n")


print("Pour sortir de la boucle suivante, il suffira d'entrer le mot \"stop.\n\n")
mot="quelconque"
liste_mot = []
while mot != "stop" :
    mot=input("Rentrez un mot (sans accent) : ")
    
    if mot == "tableau":
        print(liste_mot)
    elif mot in liste_mot:
        print("Le mot \"" + mot + "\" est déjà présent dans le tableau, il sera donc supprimé")
        liste_mot.remove(mot)
        print(liste_mot)
    else:
        liste_mot.append(mot)
        print(liste_mot)
        
    
print("\n")
input("Appuyer sur ENTER pour terminer le programme. ")