# Hexadecimal and Decimal Digits

# this function converts integer to hexadecimal
# @param decimal is the decimal number we want to convert
# @return hexadecimal number
def int_to_hex(decimal):
    if decimal == 0:
        return str(decimal)
    else:
        out = ''
        while decimal > 0:
            hex_digit = decimal % 16
            if hex_digit < 10:
                hex_digit = str(hex_digit)
            elif hex_digit == 10:
                hex_digit = 'A'
            elif hex_digit == 11:
                hex_digit = 'B'
            elif hex_digit == 12:
                hex_digit = 'C'
            elif hex_digit == 13:
                hex_digit = 'D'
            elif hex_digit == 14:
                hex_digit = 'E'
            elif hex_digit == 15:
                hex_digit = 'F'
            out = hex_digit + out
            decimal = decimal // 16
        return out


# this function converts hexadecimal to decimal
# @param hex is the hexadecimal number we want to convert
# @return decimal number
def hex_to_int(hex):
    for ch in hex:
        # check if the string is hexadecimal
        if (ch < 'a' or ch > 'f') and (ch < 'A' or ch > 'F') and (ch < '0' or ch > '9'):
            return 'error: invalid hexadecimal number'
        else:
            return int(hex, 16)


