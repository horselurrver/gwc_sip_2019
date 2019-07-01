
import random
# --- Define your functions below! ---
def printOptions():
    print('')
    print('Enter one of the following numbers....')
    print('1. Rock paper scissors')
    print('2. Knock knock')
    print('3. Quit')

def getUserInput():
    answer = input("(What will you say?) ")
    return answer

def greet():
    print('Chatbot initializing...')
    input = getUserInput()
    if input.lower() == 'hi':
        print('Hi! I will be your chatbot today!')
    else:
        print('What, so you\'re not going to say hi to me?')

def knockknock():
    secondLines = ['Cow says', 'A little old lady', 'Europe', 'Etch', 'Robin', 'Cash']
    punchLines = ['No, cow says moo!', 'All this time, I had no idea you could yodel.', "No I'm not!", 'Bless you, friend.', 'Robin you, now hand over the cash', 'No thanks, I’ll have some peanuts.']

    while True:
        print('Knock knock!')
        index = random.randint(0, len(secondLines) - 1)
        while True:
            user = input()
            if user.lower() == "who's there?":
                break
            else:
                print("Dude, you're supposed to say, 'Who's there?'")
        firstResponse = secondLines[index]
        print(firstResponse)
        while True:
            user = input()
            if user.lower() == (firstResponse + ' who?').lower():
                break
            else:
                print("Dude, you're supposed to say, '" + firstResponse + " who?'")
        secondResponse = punchLines[index]
        print(secondResponse)
        print('Keep playing? (y/n)')
        response = input()
        if response == 'n':
            break


def rockpaperscissors():
    responses = ['rock', 'paper', 'scissors', 'quit']
    user = ''
    play = True
    while play:
        index = random.randint(0, 2)
        computer = responses[index]
        while True:
            user = input('Rock, paper, scissors, or quit? ')
            if user.lower() in responses:
                break
            else:
                print('Invalid response')
        if user == 'quit':
            print('Thanks for playing!')
            play = False

        if computer == user:
            print('Tie! Both you and the computer chose ' + user)
        elif computer == 'rock':
            if user == 'paper':
                print('User wins! Computer chose ' + computer)
            else: # user chose scissors
                print('Computer wins! Computer chose ' + computer)
        elif computer == 'paper':
            if user == 'rock':
                print('Computer wins! Computer chose ' + computer)
            else: # user chose scissors
                print('User wins! Computer chose ' + computer)
        else: # computer chose scissors
            if user == 'rock':
                print('User wins! Computer chose ' + computer)
            else: # user chose paper
                print('Computer wins! Computer chose ' + computer)

# --- Put your main program below! ---
def main():
    greet()
    while True:
        printOptions()
        input = getUserInput()
        if input == '1':
            rockpaperscissors()
        elif input == '2':
            knockknock()
        elif input == '3':
            print('Okay, bye I guess')
            break
        else:
            print('Invalid response')

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
