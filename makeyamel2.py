#!/usr/bin/python3

import yaml


def main():
    hitchhikers = [{"name": "test2", "species": "test3"},  \
                   {"name": 'test4', "species": 'test5'}]

    print(hitchhikers)

    yamlstring = yaml.dump(hitchhikers)

    print(yamlstring)

if __name__ == "__main__":
    main()
