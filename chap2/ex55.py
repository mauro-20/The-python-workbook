# Wavelengths of Visible Light

wavelength = float(input('enter a wavelength(nm): '))

color = ''
if 380 <= wavelength < 450:
    color = 'violet'
elif 450 <= wavelength < 495:
    color = 'blue'
elif 495 <= wavelength < 570:
    color = 'green'
elif 570 <= wavelength < 590:
    color = 'yellow'
elif 590 <= wavelength < 620:
    color = 'orange'
elif 620 <= wavelength < 750:
    color = 'red'

if color == '':
    print('the wavelength is outside the visible spectrum')
else:
    print('%dnm correspond to %s color' % (wavelength, color))
