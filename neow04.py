#!/usr/bin/python3
import json
import urllib.request
import webbrowser

NEO = 'https://api.nasa.gov/neo/rest/v1/feed?api_key='

def main():
    # getting my api key from saved document
    with open(r'C:\Users\Student\Documents\nasacreds.txt', 'r') as nc:
        myapikey = nc.read()

    neo_resp = urllib.request.urlopen(NEO + myapikey)
    neo_json = neo_resp.read().decode()
    neo_py = json.loads(neo_json)

    # variables to be used
    counter = 0
    counter2 = 0
    dict_for_links = {}

    # makes menu options for user to pick astroid from
    for nasadate in neo_py["near_earth_objects"]:
        print(f'-----{nasadate}-----')  # each date displayed followed by released astroid info
        counter_endof_dict = 0  # counter saves a value to assosiate the users menu selection w/ the number of that astroid specific to its release date ex: input of '55' ---> 2019-12-10   '1'
        for astro in neo_py["near_earth_objects"][nasadate]:
            counter_endof_dict = counter_endof_dict + 1
            counter = counter + 1
            dict_for_links[counter] = nasadate + ' ' + str(
                counter_endof_dict)  # Key ---> (date of astroids release) (number of the astroid relative to other astroids in its release date group)
            print('(', counter, ')', 'Name of Astroid: ' + astro['name'])

    your_astroid = int(
        input(f"\nPlease select an astroid for more info(1-{counter}): "))  # dynamic prompt for astroid selection

    astroid_specific = int((dict_for_links[your_astroid][10:13]))  # slice end of string to use for astroid selection

    # parsing astroid data to locate users selection... this is repetitive code probably a better way to accomplish this
    for nasadate in neo_py["near_earth_objects"]:
        for astro in neo_py["near_earth_objects"][nasadate]:
            counter2 = counter2 + 1
            if counter2 == your_astroid:
                neo_py["near_earth_objects"][nasadate][astroid_specific - 1]
                print('You can find all information on astroid: ' +
                      neo_py['near_earth_objects'][nasadate][astroid_specific - 1]['name'] + ' at ' +
                      neo_py["near_earth_objects"][nasadate][astroid_specific - 1]['nasa_jpl_url'])
                webbrowser.open(neo_py["near_earth_objects"][nasadate][astroid_specific - 1]['nasa_jpl_url'])


if __name__ == "__main__":
    main()
