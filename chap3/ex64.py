# Discount Table

discount = 0.6

for i in range(5, 26, 5):
    original_price = i - 0.05
    discount_amount = original_price*discount
    new_price = original_price-discount_amount
    print('original_price: $%5.2f | discount amount: $%5.2f | new price: $%5.2f' % (original_price, discount_amount, new_price))
