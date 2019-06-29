#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)
def playGame():
    numTries = 3;
    guessed = False
    while numTries > 0:
        guess = raw_input('Guess a number between 1 and 20 (inclusive): ')
        if not guess.isdigit(): # checks if a string is only digits 0 to 9
            print('That\'s not a positive whole number, try again!')
        else:
            numTries = numTries - 1
            intGuess = int(guess) # converts a string to an integer
            if intGuess == aRandomNumber:
                print('You guessed the correct number in ' + numTries + ' tries!')
                guessed = True
            else:
                print('WRONG')
    if not guessed:
        print('The correct answer was ' + str(aRandomNumber))

while True:
    playGame()
    playAgain = raw_input('Play again again? y/n ')
    if playAgain == 'n':
        break
