# Day Old Bread

bread_price = 3.49
dob_discount = 0.60

dob_purchased = int(input('how many day old bread would you like? '))

full_price = dob_purchased*bread_price
discount = full_price*dob_discount
total = full_price-discount

print('full price:   $%5.2f' % full_price)
print('discount:     $%5.2f' % discount)
print('total price:  $%5.2f' % total)
