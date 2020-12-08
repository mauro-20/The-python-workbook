# Making change

cents_nickel = 5
cents_dime = 10
cents_quarter = 25
cents_loonie = 100
cents_toonie = 200

change = int(input('enter the change in cents '))

toonies = change // cents_toonie
change = change % cents_toonie
loonies = change // cents_loonie
change = change % cents_loonie
quarters = change // cents_quarter
change = change % cents_quarter
dimes = change // cents_dime
change = change % cents_dime
nickels = change // cents_nickel
change = change // cents_nickel
pennies = change

print('your change is', toonies, 'toonies,', loonies, 'loonies,', quarters, \
      'quarters,', dimes, 'dimes,', nickels, 'nickels and', pennies, 'pennies')
