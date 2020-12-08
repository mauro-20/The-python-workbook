# Frequency to Note

c4 = 261.63
d4 = 293.66
e4 = 329.63
f4 = 349.23
g4 = 392.00
a4 = 440.00
b4 = 493.88
limit = 1

frequency = float(input('enter a frequency (hz): '))

note = ''
if c4 - limit < frequency < c4 + limit:
    note = 'C4'
elif d4 - limit < frequency < d4 + limit:
    note = 'D4'
elif e4 - limit < frequency < e4 + limit:
    note = 'E4'
elif f4 - limit < frequency < f4 + limit:
    note = 'F4'
elif g4 - limit < frequency < g4 + limit:
    note = 'G4'
elif a4 - limit < frequency < a4 + limit:
    note = 'A4'
elif b4 - limit < frequency < b4 + limit:
    note = 'B4'

print(frequency,'hz correspond to', note)
