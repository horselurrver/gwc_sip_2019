import datetime


responses = {}
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

def askAge():
    age = 0
    while True:
        age = input('What is your age? ')
        try:
            age = int(age)
            if age < 0 or age > 130:
                raise ValueError
        except ValueError:
            print('Invalid age')
        else:
            return int(age)

print('Hello! I have some survey questions for you')
askName()
askDOB()
askAge()
