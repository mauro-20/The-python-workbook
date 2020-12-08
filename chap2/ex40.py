# Sound Levels

# Jackhammer 130 dB
# Gas Lawnmower 106 dB
# Alarm Clock 70 dB
# Quiet Room 40 dB

noise = int(input('enter the sound level in DB: '))

noise_type = ''
if noise == 40:
    noise_type = 'quiet room'
elif noise == 70:
    noise_type = 'alarm clock'
elif noise == 106:
    noise_type = 'Gas Lawnmower'
elif noise == 130:
    noise_type = 'Jackhammer'
elif noise < 40:
    noise_type = 'less than a quiet room'
elif noise < 70:
    noise_type = 'between a quiet room and alarm clock'
elif noise < 106:
    noise_type = 'between an alarm clock and Gas Lawnmower'
elif noise < 130:
    noise_type = 'between a Gas Lawnmower and Gas Jackhammer'
elif noise > 130:
    noise_type = 'more than Jackhammer'

print('the noise is', noise_type)
