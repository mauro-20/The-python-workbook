# Negatives,Zeros and Positives

# initialize the lists
negatives = []
zeros = []
positives = []

# Read all of the integers from the user, storing each integer in the correct list
num = input('enter an integer (blank to quit): ')
while num != '':
    num = int(num)
    if num < 0:
        negatives.append(num)
    elif num == 0:
        zeros.append(num)
    else:
        positives.append(num)
    num = input('enter an integer (blank to quit): ')

# Display all of the negative values, then all of the zeros, then all of the positive values
for n in negatives:
    print(n)
for n in zeros:
    print(n)
for n in positives:
    print(n)
