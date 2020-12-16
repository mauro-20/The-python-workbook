# Compute the Perimeter of a Polygon
import math

perimeter = 0
x = input('enter the first x-coordinate: ')
y = input('enter the first y-coordinate: ')

first_x = x
first_y = y
prev_x = float(x)
prev_y = float(y)
while x != '':
    x_length = float(x)-prev_x
    y_length = float(y)-prev_y
    perimeter += math.sqrt(x_length**2+y_length**2)
    prev_x = float(x)
    prev_y = float(y)
    x = input('enter the next x-coordinate (blank to quit): ')
    if x == '':
        x_length = float(first_x) - prev_x
        y_length = float(first_y) - prev_y
        perimeter += math.sqrt(x_length ** 2 + y_length ** 2)
    else:
        y = input('enter the next y-coordinate: ')

print('The perimeter of that polygon is', perimeter)
