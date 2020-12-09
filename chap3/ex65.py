# Temperature Conversion Table

print('Celsius | Fahrenheit')
print('--------|-----------')
for i in range(0, 101, 10):
    celsius = i
    fahrenheit = (i*9/5)+32
    print(' %3d°C  | %3d°F' % (celsius, fahrenheit))
