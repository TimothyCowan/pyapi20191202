#!/usr/bin/env python3
import os
import platform
from datetime import datetime

if platform.system() == "Windows":
    os.chdir(os.environ['HOMEPATH'])
#    elif platform.system() == "Java":
#    os.chdir(os.environ['HOMEPATH'])
else:
    os.chdir(os.system('HOME'))

date_stampnow = str(datetime.today())
option_quit = "run"
while option_quit[0] != "q":
    FNAME = input("What is your first name?: ")
    LNAME = input("What is your last name?: ")
    PHNUM = input("What is your phone number?: ")
    enter_numberForLog = input("Is the entry correct?(yes or no): " + FNAME + LNAME + PHNUM).lower()
    if enter_numberForLog[0] == "y":
        FFILE = open("phlog.txt", "w")
        FFILE.write(FNAME + LNAME + PHNUM + date_stampnow)
        FFILE.close()
    else:
        continue
