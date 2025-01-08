import os
import csv
import json

dicEleves = { 
	'titi' : {'notes':{'tp1':10, 'tp2':13,'tp3':17}, 'appréciation': 'moyenne'}, 
	'toto' : {'notes':{'tp1':19, 'tp2':11,'tp3':14}, 'appréciation': 'Très Bien' }, 
	'tata' : {'notes':{'tp1':15,'tp2':8,'tp3':13}, 'appréciation': 'Bonne' },
	'tutu' : {'notes':{'tp3':15,'tp4':13}, 'appréciation': 'Bonne' },
    'tete' : {'notes':{}, 'appréciation': 'Bonne' },
}

dossier_principal = "eleves"
if not os.path.exists(dossier_principal):
    os.mkdir(dossier_principal)

for eleve, details in dicEleves.items():
    # Chemin pour chacun des élèves
    chemin_dossier = os.path.join(dossier_principal, eleve)
    os.mkdir(chemin_dossier)

    # Création du fichier txt pour l'appréciation
    chemin_txt = os.path.join(chemin_dossier, "appreciation.txt")
    appreciation= details.get("appréciation")
    with open(chemin_txt, mode="w+") as fichier_txt:
        fichier_txt.write(appreciation)

    # Création du fichier csv pour la note
    chemin_csv = os.path.join(chemin_dossier, "notes.csv")
    with open(chemin_csv, mode="w+",newline="") as fichier_csv:
        writter = csv.writer(fichier_csv)
        writter.writerow(["Travail", "Note"])
        for travail, note in details["notes"].items():
            writter.writerow([travail, note])

statistique = {}

for eleve, data in dicEleves.items():
    notes=list(data['notes'].values())
    if notes:
        moyenne = sum(notes) / len(notes)
        min_note = min(notes)
        max_note = max(notes)
    else:
        moyenne = min_note = max_note = "Pas de note"
    
    statistique[eleve] = {
        'moyenne' : moyenne,
        'min' : min_note,
        'max' : max_note
    }
with open(os.path.join('eleves','statistique.json'), 'w') as json_file:
    json.dump(statistique, json_file, indent=4)