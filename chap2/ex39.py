# Month Name to Number of Days

month = input('tell me the month and I tell you how many days: ')

days = ''
if month == 'jan' or month == 'mar' or month == 'may' or month == 'jul' \
        or month == 'aug' or month == 'oct' or month == 'dec':
    days = '31'
elif month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
    days = '30'
elif month == 'feb':
    days = '28 or 29'

if days == '':
    print('please enter a valid month')
else:
    print(month, 'has', days, 'days')
