import datetime
import json
# list of dictionaries
responses = []
def askName():
    name = ''
    while True:
        name = input('What is your name? ')
        if not name.isalpha():
            print('Invalid name')
        else:
            return name

# https://docs.python.org/2/library/datetime.html
def askDOB():
    dob = ''
    while True:
        dob = input('What is your date of birth? (MM/DD/YYYY) ')
        try:
            datetime.datetime.strptime(dob, '%m/%d/%Y')
            return dob
        except ValueError:
            print('Invalid date')

def calcAge(dob):
    bday = datetime.datetime.strptime(dob, '%m/%d/%Y')
    diff = datetime.datetime.now().year - bday.year
    return diff

def askHours():
    hours = 0
    while True:
        hours = input('How many hours do you spend on your phone daily? ')
        try:
            hours = int(hours)
            if hours < 0 or hours > 130:
                raise ValueError
        except ValueError:
            print('Invalid age')
        else:
            return int(hours)

def conductSurvey():
    print('Hello! I have some survey questions for you')
    name = askName()
    dob = askDOB()
    calcAge(dob)
    hours = askHours()
    responses.append({
        'name': name,
        'dob': dob,
        'hours': hours
    })

def saveToJSON(filename):
    with open(filename, 'w') as outfile:
        json.dump(responses, outfile)

if __name__ == '__main__':
    filename = 'survey.json'
    while True:
        conductSurvey()
        cont = input('Continue collecting responses? (y/n) ')
        if cont == 'n':
            print('Saving to ' + filename + ': ' + str(responses))
            break
    saveToJSON(filename)
