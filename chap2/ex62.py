# Roulette Payouts

import random

number = random.randint(-1, 37)

if number > 0:
    if number == 1 or number == 3 or number == 5 or number == 7 or number == 9 or number == 12 or number == 14 or \
            number == 16 or number == 18 or number == 19 or number == 21 or number == 23 or number == 25 or \
            number == 27 or number == 30 or number == 32 or number == 36:
        colour = 'red'
    else:
        colour = 'black'
    if number % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'
    if number <= 18:
        one_to_18_or_19_to_36 = '1 to 18'
    else:
        one_to_18_or_19_to_36 = '19 to 36'

if number == -1:
    number = '00'

print('The spin resulted in', number, '...')
if number != 0 and number != '00':
    print('pay', number)
    print('pay', colour)
    print('pay', one_to_18_or_19_to_36)
