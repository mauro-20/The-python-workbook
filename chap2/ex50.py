# Richter Scale

magnitude = float(input('enter magnitude (from 0 to 10): '))

earthquake_description = ''
if magnitude < 2:
    earthquake_description = 'micro'
elif magnitude < 3:
    earthquake_description = 'very minor'
elif magnitude < 4:
    earthquake_description = 'minor'
elif magnitude < 5:
    earthquake_description = 'light'
elif magnitude < 6:
    earthquake_description = 'moderate'
elif magnitude < 7:
    earthquake_description = 'strong'
elif magnitude < 8:
    earthquake_description = 'major'
elif magnitude < 10:
    earthquake_description = 'great'
elif magnitude >= 10:
    earthquake_description = 'meteoric'

if earthquake_description == '':
    print('error')
else:
    print('a magnitude %.1f earthquake is considered to be a %s earthquake' % (magnitude, earthquake_description))
