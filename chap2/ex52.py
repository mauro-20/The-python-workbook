# Letter Grade to Grade Points

letter_grade = input('enter a letter grade: ')
letter_grade = letter_grade.upper()

grade_points = -1
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

if grade_points == -1:
    print('please enter a valid letter grade')
else:
    print(letter_grade, 'is equals to', grade_points)
