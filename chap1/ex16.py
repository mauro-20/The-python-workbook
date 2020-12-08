# Area and Volume
import math

r = float(input('enter the radius in cm: '))

circle_area = math.pi*r**2
sphere_volume = 4/3*math.pi*r**3

print('the area of the circle is %.2f squared cm' % circle_area)
print('the volume of the sphere is %.2f cubic cm' % sphere_volume)
