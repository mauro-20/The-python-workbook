# No More Pennies

item_price = input('enter the item price: ')
total = 0.0

while item_price != '':
    total += float(item_price)
    item_price = input('enter the item price (blank to quit): ')

total_cents = total*100
cents_remainder = total_cents % 5
if cents_remainder < 2.5:
    total_cash = total-cents_remainder/100
else:
    total_cash = total+(5-cents_remainder)/100

print('total price is $%.2f' % total)
print('total to pay by cash is $%.2f' % total_cash)
