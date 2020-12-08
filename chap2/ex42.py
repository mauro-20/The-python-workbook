# Note to Frequency

note = input('enter a note: ')
letter = note[0]
octave = int(note[1])

frequency = 0
if letter == 'c':
    frequency = 261.63
elif letter == 'd':
    frequency = 293.66
elif letter == 'e':
    frequency = 329.63
elif letter == 'f':
    frequency = 349.23
elif letter == 'g':
    frequency = 392.00
elif letter == 'a':
    frequency = 440.00
elif letter == 'b':
    frequency = 493.88

frequency = frequency/(2**(4-octave))

print('the frequency is %.2f hz' % frequency)

