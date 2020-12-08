# Sort 3 Integers

a = int(input('enter the first integer: '))
b = int(input('enter the second integer: '))
c = int(input('enter the third integer: '))

minimum = min(a, b, c)
maximum = max(a, b, c)
middle = (a+b+c) - (minimum+maximum)

print('the numbers are sorted from minimum to maximum value: %d, %d, %d' % (minimum, middle, maximum))
