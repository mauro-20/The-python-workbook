# Cell Phone Bill

minutes_incl = 50
texts_incl = 50
plan = 15
extra_min_rate = 0.25
extra_text_rate = 0.15
charge_911 = 0.44
tax_rate = 0.05

minutes = int(input('enter minutes: '))
texts = int(input('enter texts: '))

extra_min_charge = 0
if minutes > 50:
    extra_min_charge = (minutes-minutes_incl) * extra_min_rate
extra_text_charge = 0
if texts > 50:
    extra_text_charge = (texts-texts_incl) * extra_text_rate


bill = plan + extra_min_charge + extra_text_charge + charge_911
tax = bill * tax_rate
total_bill = bill + tax

print('base charge: $%.2f' % plan)
if extra_min_charge != 0:
    print('additional minutes charge: $%.2f' % extra_min_charge)
if extra_text_charge != 0:
    print('additional texts charge: $%.2f' % extra_text_charge)
print('911 fee: $%.2f' % charge_911)
print('tax: $%.2f' % tax)
print('total bill: $%.2f' % total_bill)
