# Distance Between Two Points on Earth

import math

t1 = float(input('enter latitude of the first point: '))
g1 = float(input('enter longitude of the first point: '))
t2 = float(input('enter latitude of the second point: '))
g2 = float(input('enter longitude of the second point: '))

distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2) + math.cos(t1)*math.cos(t2)*math.cos(g1-g2))

print('the distance between this two points is %.1fkm' % distance)
