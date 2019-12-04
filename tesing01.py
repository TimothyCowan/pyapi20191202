#!/usr/bin/env python3
# phmenu will display all options for phone utility
# Tim Cowan
# v1 -
import os
os.system('cls')

BOARDER = "*****************************************************************"
print(BOARDER, '\n'
               " Options [a|A]dd,[f|F]ind,[d|D]elete,[u|U]pdate,[v|V]iew,[q|Q]uit"
      '\n',BOARDER)
ANS = input("Enter a menu option --> ").lower()
if ANS[0] == 'a':
    print("You've selected Add")
    #     # --> phone add
    print(ANS)
elif ANS[0] == 'f':
    print("You've selected Find")
    #     # --> phone find
    print(ANS)
elif ANS[0] == 'd':
    print("You've selected Delete")
    #     # --> phone delete
    print(ANS)
elif ANS[0] == 'u':
    print("You've selected Update")
    #     # --> phone update
    print(ANS)
elif ANS[0] == 'v':
    print("You've selected View")
    #     # --> phone view  print(ANS)
elif ANS[0] == 'q':
    print("You've selected Quit")
    #     # --> phone quit
    print(ANS)