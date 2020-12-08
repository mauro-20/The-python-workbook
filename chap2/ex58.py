# Is It a Leap Year?

year = int(input('enter a year: '))

if year % 400 == 0:
    isLeapYear = True
elif year % 100 == 0:
    isLeapYear = False
elif year % 4 == 0:
    isLeapYear = True
else:
    isLeapYear = False

if isLeapYear:
    print('leap year')
else:
    print('not leap year')
