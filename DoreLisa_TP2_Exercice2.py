import csv


def lecture_poke_stats(csv_file):
    pokedex_dict = {}
    with open('pokemon.csv', 'r') as pokedex_file:
        pokedex_reader = csv.reader(pokedex_file, delimiter=',')

        for ligne in pokedex_reader:
            poke_nom = ligne[0]
            poke_stats = list(map(int, ligne[1:]))
            pokedex_dict[poke_nom] = poke_stats

    return pokedex_dict


pokedex = lecture_poke_stats('pokemon.csv')
for nom, stats in pokedex.items():
    print(f"{nom} : {stats}")

pkmn = lecture_poke_stats("pokemon.csv")
print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))

