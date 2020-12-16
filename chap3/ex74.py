# Square Root

x = float(input('enter a number: '))

guess = x/2
while abs(guess**2-x) > 10e-12:
    guess = (guess+x/guess)/2

print('the square root is', guess)
