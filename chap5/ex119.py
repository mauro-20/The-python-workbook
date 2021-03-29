# Below and Above Average

# enter numbers by user and display
# the average number
# a list of the below average numbers
# a list of the average numbers (if any)
# a list of the above average numbers
def below_above_average():
    numbers = []
    average = []
    below = []
    above = []
    number = input('enter a number (blank to quit): ')
    while number != '':
        numbers.append(float(number))
        number = input('enter a number (blank to quit): ')

    av_number = sum(numbers)/len(numbers)

    for num in numbers:
        if num < av_number:
            below.append(num)
        elif num > av_number:
            above.append(num)
        else:
            average.append(num)

    print('the average is {}'.format(av_number))
    print('the below average numbers are {}'.format(below))
    if average:
        print('the average numbers are {}'.format(average))
    print('the above average numbers are {}'.format(above))


below_above_average()
