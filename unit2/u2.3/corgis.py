import school_scores

def getNumTestTakers(element):
    total = 0
    GPA = element['GPA']
    for grade in GPA:
        total += GPA[grade]['Test-takers']
    return total

list_of_record = school_scores.get_all()
# print out the first element
print(list_of_record[0])
# print out the state name and year for each row in the data set.
for elem in list_of_record:
    #sum = getNumTestTakers(elem)
    #state = elem.State
    #year = elem.Year
    stateName = elem['State']['Name']
    year = elem['Year']
    total = getNumTestTakers(elem)
    print(f'State: {stateName}, Year: {year}, Total test-takers: {total}')
    print('')
# print out the total number of test-takers for each state per year.
