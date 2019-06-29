
def playGame():
    # Update this text to match your story.
    start = '''
    You wake up one morning and find that you aren't in your bed; you aren't even in your room.
    You're in the middle of a giant maze.
    A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
    There is a hallway to your right and to your left.
    '''
    print(start)
    user_input = ''
    while True:
        user_input = raw_input("Type 'left' to go left or 'right' to go right. ")
        if user_input.lower() == 'left' or user_input.lower() == 'right':
            break
        else:
            print('Invalid input')
    if user_input.lower() == "left":
        print("You decide to go left and...") # Update to match your story.
        print('die a horrible horrible horrrible death')
        # Continue code to finish story.
    elif user_input.lower() == "right":
        print("You choose to go right and ...") # Update to match your story.
        print('you feel a sudden urge to use the restroom')
        # Continue code to finish story.

while True:
    playGame()
    quit = raw_input('Quit? y/n ')
    if quit == 'y':
        break
