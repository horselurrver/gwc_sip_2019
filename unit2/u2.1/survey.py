import datetime
import json

# list of dictionaries
responses = []

# load data into responses
def loadJSON(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    print('Loaded: ' + str(data))
    return data

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

# calculate person's age using dob
def calcAge(dob):
    bday = datetime.datetime.strptime(dob, '%m/%d/%Y')
    diff = datetime.datetime.now().year - bday.year
    return diff

# daily hours spent on phone
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

# main program to run
def conductSurvey():
    print('Hello! I have some survey questions for you')
    name = askName()
    dob = askDOB()
    age = calcAge(dob)
    hours = askHours()
    responses.append({
        'name': name,
        'dob': dob,
        'age': age,
        'hours': hours
    })

# calculate average age of participants
def calcAverageAge():
    sum = 0
    numResponses = len(responses)
    for person in responses:
        sum = sum + person['age']
    average = sum/numResponses
    print('Average age of participants: ' + str(average) + ' years')

# analyze collected data
def analyzeData():
    calcAverageAge()

# dump data in json file
def saveToJSON(filename):
    with open(filename, 'w') as outfile:
        json.dump(responses, outfile)

if __name__ == '__main__':
    filename = 'survey.json'
    responses = loadJSON(filename)
    while True:
        conductSurvey()
        cont = input('Continue collecting responses? (y/n) ')
        if cont == 'n':
            print('Saving to ' + filename + ': ' + str(responses))
            break
    saveToJSON(filename)
    analyzeData()
