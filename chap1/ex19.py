# Free Fall

import math

a = 9.81 # m/s2
vi = 0
ms_to_kmh = 3.6

d = float(input('enter the height in meters of the object you want to drop: '))

vf = math.sqrt(vi**2+2*a*d)
vf_kmh = vf*ms_to_kmh

print('the speed of the object touching the ground is %.2fm/s (%.1fkm/h)' % (vf, vf_kmh))
