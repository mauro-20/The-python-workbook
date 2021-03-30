# Postal Codes

def cn_post_code():

    code = input('Enter a Canadian postal code: ').upper()

    postal_codes = {'Newfoundland': 'A', 'Nova Scotia': 'B', 'Prince Edward Island': 'C', 'New Brunswick': 'E',
                    'Quebec': ['G', 'H', 'J'], 'Ontario': ['K', 'L', 'M', 'N', 'P'], 'Manitoba': 'R',
                    'Saskatchewan': 'S', 'Alberta': 'T', 'British Columbia': 'V',
                    'Nunavut or Northwest Territories': 'X', 'Yukon': 'Y'}

    state = ''
    for k in postal_codes:
        if code[0] in postal_codes[k]:
            state = k

    if state == '':
        print('First character is invalid')
        return

    if code[1].isdigit():
        if int(code[1]) == 0:
            area_type = ' rural'
        elif int(code[1]) >= 1:
            area_type = 'n urban'
    else:
        print('Second character must be a digit')
        return

    print('The postal code is for a{} address in {}'.format(area_type, state))


if __name__ == '__main__':
    cn_post_code()
