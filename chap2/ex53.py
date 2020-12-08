# Grade Points to Letter Grade

grade_point = float(input('enter a grade point: '))

grade_letter = ''
if grade_point > 4.0:
    grade_letter = 'A+'
elif 3.9 <= grade_point <= 4.0:
    grade_letter = 'A'
elif 3.5 <= grade_point < 3.9:
    grade_letter = 'A-'
elif 3.2 <= grade_point < 3.5:
    grade_letter = 'B+'
elif 2.9 <= grade_point < 3.2:
    grade_letter = 'B'
elif 2.5 <= grade_point < 2.9:
    grade_letter = 'B-'
elif 2.2 <= grade_point < 2.5:
    grade_letter = 'C+'
elif 1.9 <= grade_point < 2.2:
    grade_letter = 'C'
elif 1.5 <= grade_point < 1.9:
    grade_letter = 'C-'
elif 1.2 <= grade_point < 1.5:
    grade_letter = 'D+'
elif 0.5 <= grade_point < 1.2:
    grade_letter = 'D'
elif grade_point < 0.5:
    grade_letter = 'F'

if grade_letter == '':
    print('please enter a valid grade point')
else:
    print(grade_point, 'is equals to', grade_letter)
