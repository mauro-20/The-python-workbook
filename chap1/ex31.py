# Units of Pressure

kp = float(input('enter the pressure in kilopascal: '))

psi = kp/6.895
mmHg = kp * 7.50062
atm = kp/101.325

print('%.2f psi' % psi)
print('%.2f mmHg' % mmHg)
print('%.2f atm' % atm)
