# Decimal to Binary

decimal = int(input('enter a decimal (base 10) number: '))

binary = ''
while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal = decimal // 2

print('the equivalent binary number is', binary)
