# Area of a Triangle (Again)

import math

s1 = float(input('enter the length of side 1: '))
s2 = float(input('enter the length of side 2: '))
s3 = float(input('enter the length of side 3: '))

s = (s1+s2+s3)/2
area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

print('the area of the triangle is', area)
