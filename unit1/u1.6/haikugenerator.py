#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
firstLine = ['An old silent pond...', 'Autumn moonlight-', 'In the twilight rain', 'A summer river being crossed', 'Light of the moon', 'Trusting the Buddha, good and bad,']
secondLine = ['A frog jumps into the pond,', 'a worm digs silently', 'these brilliant-hued hibiscus -', 'how pleasing', 'Moves west, flowers\' shadows', 'The color and scent of the wisteria']
thirdLine = ['splash! Silence again.', 'into the chestnut.', 'A lovely sunset.', 'with sandals in my hands!', 'Creep eastward.', 'Seems far away.']
#Generates a random integer.
print('Haiku time!')
print('')
while True:
    index1 = randint(0, len(firstLine) - 1)
    index2 = randint(0, len(secondLine) - 1)
    index3 = randint(0, len(thirdLine) - 1)
    print(firstLine[index1])
    print(secondLine[index2])
    print(thirdLine[index3])
    print('')
    answer = input('Quit? (y/n) ')
    if answer == 'y':
        print('Bye!')
        break
