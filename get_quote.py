#!/usr/bin/env python3
import os
import platform
import random

#BOARDER for formatting menu
BOARDER = "****************************************************************************"
print(BOARDER, '\n'
               " Choose quote type:  (1)Aaron (2)Inspirational (3)Dark Humor (4)Motivational"
      '\n',BOARDER)

quote_type = int(input())
list_of_quote_types = {1: "AA", 2: "HU", 3: "IN", 4: "MO"} #Dict to keep values for each quote category. AA=Aaron HU=Humor IN=Inspirational MO=Motivational
keymatch_value = list_of_quote_types[quote_type]
#print(keymatch_value)

#below checks for which OS system user is on and gets them to their home dir to open the file quotes.txt
if platform.system() == "Windows":
    os.chdir(os.environ['HOMEPATH'])
else:
    os.chdir(os.system('HOME'))

#below opens file reads it out so we can sort through it and apply the keymatch_value from our dict to pick a random quote of selected type.
quote_file = open("quotes.txt", "r")
lines = quote_file.readlines()
key_match = [s for s in lines if keymatch_value in s]

print(random.choice(key_match))




