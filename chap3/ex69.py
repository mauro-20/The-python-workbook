# Admission Price

guest_age = input('enter the age of the first guest: ')

total_price = 0
while guest_age != '':
    guest_age = int(guest_age)
    if guest_age <= 2:
        price = 0
    elif 3 <= guest_age <= 12:
        price = 14
    elif guest_age >= 65:
        price = 18
    else:
        price = 23
    total_price += price
    guest_age = input('enter the age of the next guest (blank to quit): ')

print('the total price for the group is $%.2f' % total_price)
