import os
from collections import defaultdict
import unidecode
import re

# Chemin vers le fichier candide.txt
file_path = os.path.join(os.path.dirname(__file__), 'candide.txt')

# Lire le fichier et afficher son contenu
file = open(file_path, 'r', encoding='utf-8') 
texte = unidecode.unidecode(file.read())

# Regrouper les caractères
groupes_alpha = defaultdict(str)  
groupes_punct = defaultdict(str) 

for caractere in texte:
    if caractere.isalnum():
        groupes_alpha[caractere.lower()] += caractere
    elif caractere in ".,!?-':;":
        groupes_punct[caractere] += caractere


# Trier les groupes 
caracteres_groupes_alpha = sorted(groupes_alpha.items())

caracteres_groupes_punct = sorted(groupes_punct.items())

# Chemin vers candide_Gen.txt
output_file_path = os.path.join(os.path.dirname(__file__), 'candide_Gen.txt')

# Écrire les caractères regroupés dans le fichier de sortie
with open(output_file_path, 'w', encoding='utf-8') as f:
    # Écrire d'abord les lettres et chiffres
    for _, caracteres in caracteres_groupes_alpha:
        f.write(caracteres + '\n')
    # Ensuite, écrire les caractères de ponctuation
    for _, caracteres in caracteres_groupes_punct:
        f.write(caracteres + '\n')


# partie statistiques

# Compter les mots
mots = re.findall(r'\b\w+\b', texte)
nombre_de_mots = len(mots)

# Compter les phrases
phrases = re.split(r'[.!?]', texte)
nombre_de_phrases = len([phrase for phrase in phrases if phrase.strip() != ""])

# Compter les voyelles
voyelles = 'aeiouyAEIOUY'
nombre_de_voyelles = sum(texte.count(v) for v in voyelles)

print("Statistiques du texte :")
print(f"Nombre de mots : {nombre_de_mots}")
print(f"Nombre de phrases : {nombre_de_phrases}")
print(f"Nombre de voyelles : {nombre_de_voyelles}")

# Partie Statistiques plus précises
print("Statistiques plus précises :")
# mots les plus utilisés

mots = re.findall(r'\b\w+\b', texte)
mots = [mot.lower() for mot in mots]
mots_count = defaultdict(int)
for mot in mots:
    if len(mot) > 1:
        mots_count[mot] += 1
mots_count = sorted(mots_count.items(), key=lambda x: x[1], reverse=True)
mots_count = [(mot, count) for mot, count in mots_count if count > 1]
mots_count = mots_count[:5]
print("Mots 5 mots les plus utilisés :")
for mot, count in mots_count:
    print(f"{mot} : {count}")

# les mots avec plus de 7 lettres
mots = re.findall(r'\b\w+\b', texte)
mots = [mot.lower() for mot in mots]
mots_count = defaultdict(int)
for mot in mots:
    if len(mot) > 7:
        mots_count[mot] += 1
        print(mot)
mots_count = sorted(mots_count.items(), key=lambda x: x[1], reverse=True)
mots_count = [(mot, count) for mot, count in mots_count if count > 1]
mots_count = mots_count[:5]
print("Mots avec plus de 7 lettres :")
for mot, count in mots_count:
    print(f"{mot} : {count}")