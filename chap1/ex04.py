# Area of a field

width = float(input('type the width of the field in feet\n'))
length = float(input('type the length of the field in feet\n'))
# computing the area in acres
area = width * length / 43560
print('the area of the field is %.2f acres' % area)
