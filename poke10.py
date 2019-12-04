from pprint import pprint

import requests

POKE = 'https://pokeapi.co/api/v2/pokemon-habitat/'


def main():
    pokereq = requests.get(POKE)
    for i in
    pokereq2 = requests.get(POKE+'1')
    pokejson = pokereq.json()
    pokejson2 = pokereq2.json()

    # pprint(pokejson)
    # print('###################')

    for abl in pokejson['results']:
        print('>'+abl['name'])
        for indx in pokejson2['pokemon_species']:
            print(indx['name'])



if __name__ == "__main__":
    main()
