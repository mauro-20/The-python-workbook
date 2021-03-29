# Is a List already in Sorted Order?

# determine if a list is sorted either ascending or descending
# @param t is the list to check
# @return True if the list is sorted, False otherwise
def is_sorted(t):
    if t == sorted(t) or t == sorted(t, reverse=True):
        return True
    return False


# test is_sorted() with user inputs
def main():
    user_list = []
    num = input('enter a number (blank to quit): ')
    while num != '':
        user_list.append(num)
        num = input('enter a number (blank to quit): ')
    if is_sorted(user_list):
        print('the numbers are sorted')
    else:
        print('the numbers are not sorted')


if __name__ == '__main__':
    main()
