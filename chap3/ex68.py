# Compute a Grade Point Average

letter_grade = input('enter a letter grade: ')
letter_grade = letter_grade.upper()

total = 0
count = 0
while letter_grade != '':
    if letter_grade == 'A+':
        grade_points = 4.0
    elif letter_grade == 'A':
        grade_points = 4.0
    elif letter_grade == 'A-':
        grade_points = 3.7
    elif letter_grade == 'B+':
        grade_points = 3.3
    elif letter_grade == 'B':
        grade_points = 3.0
    elif letter_grade == 'B-':
        grade_points = 2.7
    elif letter_grade == 'C+':
        grade_points = 2.3
    elif letter_grade == 'C':
        grade_points = 2.0
    elif letter_grade == 'C-':
        grade_points = 1.7
    elif letter_grade == 'D+':
        grade_points = 1.3
    elif letter_grade == 'D':
        grade_points = 1.0
    elif letter_grade == 'F':
        grade_points = 0

    count += 1
    total += grade_points
    letter_grade = input('enter the next letter grade (blank to quit): ')
    letter_grade = letter_grade.upper()

average = total/count
print('your grade point average is', average)
