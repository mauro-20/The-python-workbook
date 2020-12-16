# Caesar Cipher

message = input('enter the message you want to crypt: ')
shift = int(input('enter the shift amount: '))

rot_message = ''
for letter in message:
    temp_rot_let = ord(letter) + shift
    if 'a' <= letter <= 'z':
        if temp_rot_let > ord('z'):
            temp_rot_let -= 26
        elif temp_rot_let < ord('a'):
            temp_rot_let += 26
    if 'A' <= letter <= 'Z':
        if temp_rot_let > ord('Z'):
            temp_rot_let -= 26
        elif temp_rot_let < ord('A'):
            temp_rot_let += 26
    rot_let = chr(temp_rot_let)
    rot_message += rot_let

print(rot_message)
