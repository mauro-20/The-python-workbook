# Compound Interest

year_interest = 4/100
initial_deposit = float(input('how much would you like to deposit? '))

interest_year1 = initial_deposit*year_interest
balance_year1 = initial_deposit+interest_year1
interest_year2 = balance_year1*year_interest
balance_year2 = balance_year1+interest_year2
interest_year3 = balance_year2*year_interest
balance_year3 = balance_year2+interest_year3

print('the interests earned after 1 year is %.2f$ making the balance %.2f' %(interest_year1,balance_year1))
print('the interests earned after 2 year is %.2f$ making the balance %.2f' %(interest_year2,balance_year2))
print('the interests earned after 3 year is %.2f$ making the balance %.2f' %(interest_year3,balance_year3))