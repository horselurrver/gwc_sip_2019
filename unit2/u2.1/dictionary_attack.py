import difflib

def num_diff(word1, word2):
    differences = list(difflib.ndiff(word1, word2))
    diff_count = 0
    for letter in differences:
        if letter[0] == '+' or letter[0] == '-':
            diff_count += 1
    return diff_count

#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")
dictionary = []
for line in f:
    if len(line.strip()) > 0:
        dictionary.append(line.strip())

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = raw_input("Type in a trial password: ")

#Write logic to see if the password is in the dictionary file below here:

#Check if in dictionary
if test_password in dictionary:
    print("Your password is a dictionary word. Find a stronger one!")

#Check if multiple words combined
for word in dictionary:
    index = 0
    #Check for similarities between two words
    if num_diff(test_password, word) < 2 and num_diff(test_password, word) > 0:
        print("Hmm... your password looks very similar to the word " + word)
    try:
        index = test_password.index(word)
        print("Your password contains the common word " + word)
    except ValueError:
        continue
