# The Collatz Conjecture

import math

num = int(input('enter an integer (negative or zero to quit): '))

while num > 0:
    while num != 1:
        if num % 2 == 0:
            num = math.floor(num/2)
        else:
            num = num * 3 + 1
        print(num)
    num = int(input('enter an integer (negative or zero to quit): '))
