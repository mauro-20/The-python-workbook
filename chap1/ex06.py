# Tax and tip

tax_perc = 1 / 100 * 21
tip_perc = 1 / 100 * 18
meal_price = float(input('enter the cost of the meal without tax\n'))

tax = meal_price * tax_perc
tip = meal_price * tip_perc
grand_total = meal_price + tax + tip

print('the tax of the meal is %.2f$' % tax)
print('the tip of the meal is %.2f$' % tip)
print('the Grand total of the meal is %.2f$' % grand_total)
