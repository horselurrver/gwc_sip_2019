import random

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

# prints current word, returns if word has been totally guessed
def printWordArray(word, guessedLetters):
    numNotGuessed = 0
    result = ''
    word = word.upper()
    wordList = list(word)
    for character in wordList:
        if character.isalpha() and character in guessedLetters:
            result = result + character + ' '
        elif character.isalpha():
            result = result + '__' + ' '
            numNotGuessed = numNotGuessed + 1
        elif character == ' ':
            result = result + '   '
        else:
            result = result + character
    print(result)
    return numNotGuessed == 0

# get word from player 1 to be guessed by player 2
def getWord():
    word = ''
    while True:
        word = input('Player 1, please enter a word or phrase to be guessed: ')
        if hasNumbers(word):
            print('Invalid word, cannot have numbers')
        else:
            break
    word = word.upper()
    return word

def playGame(word):
    # Some useful variables
    guesses = []
    maxfails = 7
    fails = 0

    print('')
    print('Now, it\'s player 2\'s turn!')
    while fails < maxfails:
        guess = input("Guess a letter: ")
        guess = guess.upper()
    	# check if the guess is valid: Is it one letter? Have they already guessed it?
        if (not guess.isalpha()) or (len(guess) > 1):
            print('Invalid guess. Must be a single letter')
        elif guess in guesses:
            print('You\'ve already guessed the letter ' + guess)
        else:# check if the guess is correct: Is it in the word? If so, reveal the letters!
            if guess in word:
                guesses.append(guess)
                print('That is right!')
                win = printWordArray(word, guesses)
                if win:
                    print('You win!')
                    break
            else:
                fails = fails + 1
                print('Uh oh, that was wrong. You have ' + str((maxfails - fails)) + ' chances left')

print('Welcome to my game of Guess the Secret Word (aka Hangman)!')
while True:
    word = getWord()
    playGame(word)
    again = input('Play again? (y/n) ')
    if again == 'n':
        print('Thanks for playing!')
        break
