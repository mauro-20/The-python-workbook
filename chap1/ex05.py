# Bottle deposit

small_bottle = 0.10
big_bottle = 0.25

small = int(input('how many less then 1 liter bottles do you want to return?\n'))
big = int(input('how many more then 1 liter bottles do you want to return?\n'))

refund = small * small_bottle + big * big_bottle

print('your bottle refund is %.2f$' % refund)

