from pprint import pprint

import requests

def main():
    poke_request = 'https://pokeapi.co/api/v2/pokemon-habitat/'
    pokejson = (requests.get(poke_request)).json()
    ## count = 0

    for area in pokejson['results']:  #prints each habitat
        print('############' + area['name'])
        ## count = count + 1
        ## count += 1 (this is the same as above)
        # new_req = poke_request + str(count)  #change orginal api url by cat'ing url with count++
        # print(new_req)
        area_lookup = (requests.get(area['url'])).json()

        for pokemon in area_lookup['pokemon_species']:  #todo Fix: Bug at start of this for loop
            print(pokemon['name'])
            
if __name__ == "__main__":
    main()
