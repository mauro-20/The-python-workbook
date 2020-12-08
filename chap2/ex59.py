# Next Day

year = int(input('enter a year: '))
month = int(input('enter a month: '))
day = int(input('enter a day: '))

if year % 400 == 0:
    isLeapYear = True
elif year % 100 == 0:
    isLeapYear = False
elif year % 4 == 0:
    isLeapYear = True
else:
    isLeapYear = False

if isLeapYear:
    feb_days = 29
else:
    feb_days = 28

next_day = day+1
if (month == 2 and next_day > feb_days) or \
        ((month == 4 or month == 6 or month == 9 or month == 11) and next_day > 30) or \
        ((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and next_day > 31):
    next_day = 1
    next_month = month+1
    next_year = year
elif month == 12 and next_day > 31:
    next_day = 1
    next_month = 1
    next_year = year + 1
else:
    next_month = month
    next_year = year

print('the next day is %04d-%02d-%02d' % (next_year, next_month, next_day))
