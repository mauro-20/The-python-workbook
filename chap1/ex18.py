# Volume of a Cylinder

import math

radius = float(input('enter the radius of the cylinder: '))
height = float(input('enter the height of the cylinder: '))

volume = math.pi * radius**2 *height

print('the volume of the cylinder is %.1f cubic cm' % volume)
