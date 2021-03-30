# Write out Numbers in English

def written_numbers(num):
    unit = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
            '9': 'nine'}
    decimal = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy',
               '8': 'eighty', '9': 'ninety'}
    teens = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
             '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}

    result = ''
    num = list(str(num))
    while len(num) == 3:
        for k in unit:
            if num[0] == k:
                result += unit[k] + ' hundred '
                num.pop(0)
            break

    while len(num) == 2:
        print(num, '22')
        if num[0] == '0':
            num.pop(0)
            break
        elif num[0] == '1':
            for k in teens:
                if ''.join(num) == k:
                    result += teens[k] + ' '
                    num.clear()
                    break
        else:
            for ke in decimal:
                if num[0] == ke:
                    result += decimal[ke] + ' '
                    num.pop(0)
                    break

    while len(num) == 1:
        if num[0] != '0':
            for k in unit:
                if num[0] == k:
                    result += unit[k]
                    num.pop(0)
                    break
        else:
            num.pop(0)

    return result


written_numbers(102)
