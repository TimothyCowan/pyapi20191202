#!/usr/bin/python3

ASTROS = {"people": [{"name": "Christina Koch", "craft": "ISS"}, {"name": "Alexander Skvortsov", "craft": "ISS"},
                     {"name": "Luca Parmitano", "craft": "ISS"}, {"name": "Andrew Morgan", "craft": "ISS"},
                     {"name": "Oleg Skripochka", "craft": "ISS"}, {"name": "Jessica Meir", "craft": "ISS"}],
          "number": 6, "message": "success"}


def main():
    for person_craft in ASTROS["people"]:
        print(person_craft['name'], "on the", person_craft['craft'])
        print(f'{person_craft["name"]}')


if __name__ == "__main__":
    main()
