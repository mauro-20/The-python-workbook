# Ideal Gas Law

r = 8.314 # J/(mol*K)

pressure = float(input('enter the pressure in Pascals: '))
volume = float(input('enter the volume in liters: '))
temperature = float(input('enter the temperature in degrees Celsius: '))

t = temperature + 273.15
n_mole = (pressure*volume)/(r*t)

print('the number of mole is %.4f' % n_mole)
