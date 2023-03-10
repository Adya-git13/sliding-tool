import random
import csv

branches = {'CSE', 'IT', 'ECE', 'ELE', 'MECH', 'CHEM', 'MIN', 'BTE', 'BME', 'META', 'CIV'}

field_names = ['roll', 'curr_branch', 'filled_options', 'cpi', 'crl']

data = []

crls = random.sample(range(1, 1000), k=50)

for i in range(10):
    record = {}
    record['roll'] = i
    record['curr_branch'] = random.choice(list(branches))
    new_branches = [b for b in list(branches) if b != record['curr_branch']]
    record['filled_options'] = ' '.join(random.sample(new_branches, k=random.randint(1, len(new_branches))))
    record['cpi'] = round(random.uniform(7, 10), 2)
    record['crl'] = crls[i]
    data.append(record)


with open('students.csv', 'w') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)
