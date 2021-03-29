# 120: Formatting a List

# Format a list of items so that they are separated by commas and "and"
# @param t the list of items to format
# @return a string containing the items with the desired formatting
def format_list(t):
    res = ''
    for i in range(len(t)):
        if i < len(t)-2:
            res += t[i] + ', '
        elif i == len(t)-2:
            res += t[i] + ' and '
        elif i == len(t)-1:
            res += t[i]
    return res


# test format_list() with items entered by user
def main():
    t = []
    item = input('enter an items (blank to quit): ')
    while item != '':
        t.append(item)
        item = input('enter an items (blank to quit): ')
    print(format_list(t))


if __name__ == '__main__':
    main()
