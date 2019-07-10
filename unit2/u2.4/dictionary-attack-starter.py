"""
Useful url: https://stackoverflow.com/questions/10018679/python-find-closest-string-from-a-list-to-another-string
"""
import difflib

NUM_MATCHES = 10
# returns new word with non alphabetic letters removed
def removeNonAlpha(word):
    result = ''
    for char in word:
        if char.isalpha():
            result = result + char
    return result
# returns whether or not word is in dictionary
def wordInDict(word, dict):
    return word in dict

# returns whether word is a close match to a dictionary word
def findCloseMatches(word, dict):
    closeMatches = difflib.get_close_matches(word, dict, NUM_MATCHES)
    # removes the word itself from the close matches
    if word in closeMatches:
        closeMatches.remove(word)

    return closeMatches

# returns whether or not the word contains dictionary words
def containsDictWords(word, dict):
    wordsContained = []
    for dictWord in dict:
        if dictWord in word:
            wordsContained.append(dictWord)
    return wordsContained
print("Can your password survive a dictionary attack?")

# opens file and reads dictionary into list
with open("dictionary.txt","r") as f:
    dictionary = f.readlines()

dictionary = [x.strip() for x in dictionary if len(x.strip()) > 1]
# print(str(dictionary))

# ask user for password input
test_password = input("Type in a trial password: ")
test_password = test_password.lower()

# check if password is dictionary word or contains dictionary words
if wordInDict(test_password, dictionary):
    print(f'Wow... your password is a straight up dictionary word: {test_password}')
else:
    wordsContained = containsDictWords(test_password, dictionary)
    if len(wordsContained) == 0:
        print('Wow! Your password contains 0 dictionary words!')
    else:
        words = ', '.join(wordsContained)
        # create variable for password without non alphabetic characters
        onlyAlphabet = removeNonAlpha(test_password)
        print(f'Sad face... your password contains the following words: {words}')
        closeMatches = findCloseMatches(onlyAlphabet, dictionary)
        print(f'Top {NUM_MATCHES} close matches: ' + ', '.join(closeMatches)) if len(closeMatches) > 0 else print('No close matches found')
