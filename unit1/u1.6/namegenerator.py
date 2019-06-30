#imports the ability to get a random number (we will learn more about this later!)
from random import *
# https://pypi.org/project/names/
import names

print('Welcome! Let\'s generate some names!')
while True:
    response = input('Female, male, or quit? (m, f, q)? ')
    if response == 'f':
        print(names.get_first_name(gender='female'))
    elif response == 'm':
        print(names.get_first_name(gender='male'))
    elif response == 'q':
        print('Okay, bye!')
        break
    else:
        print('Lol, invalid input')
