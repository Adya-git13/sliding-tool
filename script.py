import csv
from functools import cmp_to_key

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

class Student:

    def __init__(self, roll, curr_branch, filled_options, cpi, crl):
        self.roll = roll
        self.curr_branch = curr_branch
        self.alloted_branch = None
        self.filled_options = filled_options
        self.cpi = float(cpi)
        self.crl = float(crl)
    
    def __str__(self):
        return str(self.roll) + ":" + str(self.curr_branch) + "->" + str(self.alloted_branch)

    def __repr__(self):
        return str(self)


def initVacancies():
    with open('vacancies.csv', mode='r') as csvFile:
        vacancy_data = csv.reader(csvFile)
        for lines in vacancy_data:
            branch_vacancies[lines[0]] = int(lines[1])


def initStudents():
    students = []
    with open('students.csv', mode='r') as csvFile:
        student_data = csv.DictReader(csvFile)
        for lines in student_data:
            students.append(Student(lines['roll'], lines['curr_branch'], lines['filled_options'].split(), lines['cpi'], lines['crl']))
    return students

def studentCompare(s1, s2):
    if s1.cpi == s2.cpi:
        return s1.crl - s2.crl
    else:
        return s2.cpi - s1.cpi

def main():
    initVacancies()
    students = initStudents()
    students.sort(key=cmp_to_key(studentCompare))
    i = 0
    reset = False
    while i < len(students):
        reset = False
        for option in students[i].filled_options:
            if students[i].alloted_branch == option:
                break
            if branch_vacancies[option] > 0:
                students[i].alloted_branch = option
                branch_vacancies[option] -= 1
                branch_vacancies[students[i].curr_branch] += 1
                i = 0
                reset = True
                break
        if not reset: 
            i += 1
    
    slid_students = [student for student in students if student.alloted_branch != None]
    print(slid_students)

if __name__ == '__main__':
    main()
