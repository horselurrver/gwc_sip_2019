with open('countries.txt') as f:
    lines = f.read().lower().splitlines()

lines = [line for line in lines if line.isalpha()]
print(lines)
