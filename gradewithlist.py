students = []

while True:
    name = input('Name: ').strip()
    grade1 = float(input('Grade 1: '))
    grade2 = float(input('Grade 2: '))
    average = (grade1 + grade2) / 2
    
    students.append([name, [grade1, grade2], average])
    
    resp = input('Do you want to continue? [Y/N] ').strip().upper()
    if resp in 'N':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NAME":<15}{"AVERAGE":>8}')
print('-' * 35)

for i, student in enumerate(students, start=1):
    print(f'{i:<4}{student[0]:<15}{student[2]:>8.1f}')

while True:
    print('-' * 35)
    option = int(input('Show grades of which student? (999 to exit) '))
    if option == 999:
        print('FINISHING...')
        break
    
    if 0 <= option < len(students):
        print(f'Grades of {students[option][0]} are {students[option][1]}')
    else:
        print('Invalid student number!')