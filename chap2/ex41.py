# Classifying Triangles

side1 = float(input('enter the length of the first triangle side: '))
side2 = float(input('enter the length of the second triangle side: '))
side3 = float(input('enter the length of the third triangle side: '))

triangle_type = ''
if side1 == side2 and side1 == side3:
    triangle_type = 'equilateral'
elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle_type = 'isosceles'
else:
    triangle_type = 'scalene'

print('the triangle is', triangle_type)
