# Area of a Regular Polygon

import math

n = int(input('enter the number of sides of the regular polygon: '))
s = float(input('enter the length of the side of the regular polygon: '))

a = (n*s**2)/(4*math.tan(math.pi/n))

print('the area of the regular polygon is %.2f' % a)
