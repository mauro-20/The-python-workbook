# Name That Shape

sides = int(input("Tell me how many sides and I'll tell you the shape: "))

shape = ''
if sides == 3:
    shape = 'triangles'
elif sides == 4:
    shape = 'quadrilateral'
elif sides == 5:
    shape = 'pentagon'
elif sides == 6:
    shape = 'hexagon'
elif sides == 7:
    shape = 'heptagon'
elif sides == 8:
    shape = 'octagon'
elif sides == 9:
    shape = 'nonagon'
elif sides == 10:
    shape = 'decagon'

if shape == '':
    print('Error: number of sides out of range')
else:
    print("it's a", shape)
