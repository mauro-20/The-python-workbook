# Chinese Zodiac

year = int(input('enter your year of birth: '))

calc_year = (2000-year) % 12

sign = ''
if calc_year == 0:
    sign = 'dragon'
elif calc_year == 11:
    sign = 'snake'
elif calc_year == 10:
    sign = 'horse'
elif calc_year == 9:
    sign = 'sheep'
elif calc_year == 8:
    sign = 'monkey'
elif calc_year == 7:
    sign = 'rooster'
elif calc_year == 6:
    sign = 'dog'
elif calc_year == 5:
    sign = 'pig'
elif calc_year == 4:
    sign = 'rat'
elif calc_year == 3:
    sign = 'ox'
elif calc_year == 2:
    sign = 'tiger'
elif calc_year == 1:
    sign = 'hare'

if sign == '':
    print('error')
else:
    print('your chinese zodiac sign is', sign)
