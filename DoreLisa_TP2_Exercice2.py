import csv

with open('pokemon.csv', 'r') as pokedex_file:
    pokedex = csv.reader(pokedex_file)