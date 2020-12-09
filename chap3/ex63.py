# Average

number = float(input('enter a number: '))
n = 0
total = 0

if number == 0:
    print('please enter a number that is not 0')
else:
    while number != 0:
        total += number
        n += 1
        number = float(input('enter an other number / 0 to quit: '))
    average = total / n
    print('average is', average)
