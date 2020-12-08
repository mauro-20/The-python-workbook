# Is a License Plate Valid?

plate = input('enter a plate number: ')

plate_style = ''
if len(plate) == 6 and (plate[0] and plate[1] and plate[2]).isupper() and \
        (plate[3] and plate[4] and plate[5]).isdigit():
    plate_style = 'old style'
elif len(plate) == 7 and (plate[0] and plate[1] and plate[2] and plate[3]).isdigit() and \
        (plate[4] and plate[5] and plate[6]).isupper():
    plate_style = 'new style'
else:
    plate_style = 'invalid'

print('%s is a %s plate number' % (plate, plate_style))
