import datetime
from os import chdir, environ, path
from platform import system
from socket import gethostname
# v1 - By Tim Cowan

your_name = gethostname()
your_time = datetime.datetime.now()
your_file = input("Please enter a name for the file to create/append -->")  #include extension if desired

#test for windows or other and sets cwd to users home
if system() == "Windows":
    chdir(environ['HOMEPATH'])
else:
    chdir(environ['HOME'])

#previously named file is created or appened
if path.isfile(your_file):
    print('This file already exist')
    print(f'appending hostname:>{your_name}< and local time to file: >{your_file}<')
    open(your_file, 'a').write(f"\nOpened by:>{your_name}< at {your_time}")
else:
    print('This file does not currently exist')
    print(f'writing hostname:>{your_name}< and local time to file:>{your_file}<')
    open(your_file, 'w').write(f"Created by:>{your_name}< at {your_time}")