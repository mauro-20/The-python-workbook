# Prime Factors

import math

num = int(input('enter an integer (2 or greater): '))

if num < 2:
    print('please enter an integer greater than 1')
else:
    print('the prime factors of %d are:' % num)
    factor = 2
    while factor <= num:
        if num % factor == 0:
            print(factor)
            num = math.floor(num/factor)
        else:
            factor += 1
