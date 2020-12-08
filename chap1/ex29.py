# Wind Chill

ta = float(input('enter the air temperature in degrees celsius: '))
v = float(input('enter the wind speed in km/h: '))

WCI = 13.12+0.6215*ta-11.37*v**0.16+0.3965*ta*v*0.16

print('the WCI is', round(WCI))
