# Greatest Common Divisor

m = float(input('enter the first number: '))
n = float(input('enter the second number: '))

# initialize d as the smaller number
divisor = min(m, n)

# find the greatest common divisor
while m % divisor or n % divisor:
    divisor -= 1

print('the greatest common divisor is', divisor)
