# Assessing Employees

emp_raise = 2400.00
rating = float(input('enter an employee rate: '))

meaning = ''
if rating == 0.0:
    meaning = 'unacceptable performance'
elif rating == 0.4:
    meaning = 'acceptable performance'
elif rating >= 0.6:
    meaning = 'meritorious performance'

emp_raise = emp_raise*rating

if meaning == '':
    print('please enter a valid rate')
else:
    print('this year you had %s and your raise is $%.2f' % (meaning, emp_raise))
