# Roots of a Quadratic Function
import math

a = float(input('enter a: '))
b = float(input('enter b: '))
c = float(input('enter c: '))

discriminant = b**2-4*a*c

num_root = -1
if discriminant < 0:
    num_root = 0
    print('there is 0 real root')
elif discriminant == 0:
    num_root = 1
    root1 = -b/2*a
    print('there is 1 real root, root:%.2f' % root1)
elif discriminant > 0:
    num_root = 2
    root1 = (-b-math.sqrt(discriminant))/2*a
    root2 = (-b+math.sqrt(discriminant))/2*a
    print('there are 2 real roots, root1=%.2f root2=%.2f' % (root1, root2))
