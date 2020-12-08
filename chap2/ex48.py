# BirthDate to Astrological Sign

day = int(input('enter your day of birthday: '))
month = input('enter your month of birthday: ')

sign = ''
if month == 'dec' and day >= 22 or month == 'jan' and day <= 19:
    sign = 'capricorn'
elif month == 'jan' and day >= 20 or month == 'feb' and day <= 18:
    sign = 'aquarius'
elif month == 'feb' and day >= 19 or month == 'mar' and day <= 20:
    sign = 'pisces'
elif month == 'mar' and day >= 21 or month == 'apr' and day <= 19:
    sign = 'aries'
elif month == 'apr' and day >= 20 or month == 'may' and day <= 20:
    sign = 'taurus'
elif month == 'may' and day >= 21 or month == 'jun' and day <= 20:
    sign = 'gemini'
elif month == 'jun' and day >= 21 or month == 'jul' and day <= 22:
    sign = 'cancer'
elif month == 'jul' and day >= 23 or month == 'aug' and day <= 22:
    sign = 'leo'
elif month == 'aug' and day >= 23 or month == 'sep' and day <= 22:
    sign = 'virgo'
elif month == 'sep' and day >= 23 or month == 'oct' and day <= 22:
    sign = 'libra'
elif month == 'oct' and day >= 23 or month == 'nov' and day <= 21:
    sign = 'scorpio'
elif month == 'nov' and day >= 22 or month == 'dec' and day <= 21:
    sign = 'sagittarius'

if sign == '':
    print('error')
else:
    print('your zodiac sign is', sign)
