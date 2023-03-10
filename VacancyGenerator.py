import random
import csv

branch_vacancies = {
        'CSE' : 0,
        'IT' : 0,
        'ECE' : 0,
        'ELE' : 0,
        'MECH' : 0,
        'CHEM' : 0,
        'MIN' : 0,
        'BTE' : 0,
        'BME' : 0,
        'META' : 0,
        'CIV' : 0,
        }
    
field_names = ['Branch', 'Vacancy']


def main():
    vacancies = random.choices(range(0, 2), k=11)
    i = 0
    for branch in branch_vacancies.keys():
        branch_vacancies[branch] = vacancies[i]
        i += 1
    with open('vacancies.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for row in branch_vacancies.items():
            writer.writerow(row)

if __name__ == '__main__':
    main()
