#!/usr/bin/python3

import json
import random

# open poems database
with open('poems.json') as poemj:
    pythonpoems = json.load(poemj)  # loaded json file and imported to work w/ python
# randomly select poem
x = random.choice(list(pythonpoems.values())).replace(".", ".\n")
print(x)



