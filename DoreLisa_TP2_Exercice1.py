import json
import csv

with open('data.json', 'r') as fichier_data:
    nb_complexes = json.load(fichier_data)

with open('sortie.csv', 'w', newline='') as sortie_file:
    sortie = csv.writer(sortie_file)
    sortie.writerow(['reel', 'imaginaire'])

    for nombre in nb_complexes:
        sortie.writerow(nombre)

print("Les données du fichier 'data.json' ont été ajoutées dans le fichier 'output.csv'.")
