import json
import csv

with open('data.json', 'r') as data_file:
    nb_complexes = json.load(data_file)

with open('sortie.csv', 'w', newline='') as sortie_file:
    sortie = csv.writer(sortie_file)
    sortie.writerow(['reel', 'imaginaire'])

    for nombre in nb_complexes:
        sortie.writerow(nombre)

print("Les données du fichier 'data.json' ont été ajoutées dans le fichier 'output.csv'.")
