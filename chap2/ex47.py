# Season from Month and Day

month = input('enter a month: ')
day = int(input('enter a day: '))

season = ''
if month == 'jan' or month == 'feb' or month == 'dec' and day >= 21 or month == 'mar' and day < 20:
    season = 'winter'
elif month == 'apr' or month == 'may' or month == 'mar' and day >= 20 or month == 'jun' and day < 21:
    season = 'spring'
elif month == 'jul' or month == 'aug' or month == 'jun' and day >= 21 or month == 'sep' and day < 22:
    season = 'summer'
elif month == 'oct' or month == 'nov' or month == 'sep' and day >= 22 or month == 'dec' and day < 21:
    season = 'autumn'

if season == '':
    print('error')
else:
    print('that is', season)
