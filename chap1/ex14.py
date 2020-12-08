# Height Units

# One foot is 12 inches. One inch is 2.54 centimeters

inches_conv = 2.54 #cm
foot_conv = 12*inches_conv

foot_in = float(input('enter yor height in foot: '))
inches_in = float(input('enter you height in inches: '))

height_cm = foot_in*foot_conv + inches_in*inches_conv

print('your height in cm is', height_cm)
