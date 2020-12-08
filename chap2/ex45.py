# Date to Holiday Name

month = input('enter a month: ')
day = input('enter a day: ')

holiday = ''
if month == 'jan' and day == '1':
    holiday = "New year's day"
elif month == 'jul' and day == '1':
    holiday = 'Canada day'
elif month == 'dec' and day == '25':
    holiday = 'Christmas day'

if holiday == '':
    print('sorry no national holiday on that day')
else:
    print('that is', holiday)
