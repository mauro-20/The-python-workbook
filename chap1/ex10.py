# Arithmetic

import math

a = int(input('enter number a '))
b = int(input('enter number b '))

som = a+b
dif = a-b
prod = a*b
quot = a/b
rem = a%b
log = math.log10(a)
exp = a**b

print('The sum of a and b is', som)
print('The difference when b is subtracted from a is', dif)
print('The product of a and b is', prod)
print('The quotient when a is divided by b is', quot)
print('The remainder when a is divided by b is', rem)
print('The result of log10a is', log)
print('The result of a ex b is', exp)

