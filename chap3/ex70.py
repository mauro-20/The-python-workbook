# Parity Bits

bits = input('enter 8 bits: ')

while bits != '':
    if bits.count('0')+bits.count('1') != 8 or len(bits) != 8:
        print('please enter a valid 8 bit')
    else:
        if bits.count('1') % 2 == 0:
            parity_bit = 0
        else:
            parity_bit = 1
        print('the even parity bit is', parity_bit)
    bits = input('enter 8 bits (blank to quit): ')
