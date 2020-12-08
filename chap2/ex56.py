# Frequency to Name

frequency = float(input('enter a frequency(hz): '))

name = ''
if frequency < 3e9:
    name = 'radio waves'
elif 3e9 <= frequency < 3e12:
    name = 'microwaves'
elif 3e12 <= frequency < 4.3e14:
    name = 'infrared light'
elif 4.3e14 <= frequency < 7.5e14:
    name = 'visible light'
elif 7.5e14 <= frequency < 3e17:
    name = 'ultraviolet light'
elif 3e17 <= frequency < 3e19:
    name = 'x-rays'
elif 3e19 <= frequency:
    name = 'gamma rays'

if name == '':
    print('please enter a valid frequency')
else:
    print('this frequency is', name)

