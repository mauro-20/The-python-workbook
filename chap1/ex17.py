# Heat Capacity

water_heat_capacity = 4.186 # j/(g*°C)
j_kwh_conv = 0.0000002778
kwh_cost = 8.9 # cents

m = float(input('enter the amount of water in gr: '))
t = float(input('enter the temperature change: '))

c = water_heat_capacity
q = m*c*t
cost = q * j_kwh_conv * kwh_cost

print('the energy you need to change temperature is %dj' % q)
print('and it costs you %.1f cents' % cost)

