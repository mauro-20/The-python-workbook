# Does a String Represent an Integer?


# Determine if a string contains a valid representation of an integer
# @param s the string to check
# @return True if s represents an integer. False otherwise.
def is_integer(string):
    # remove + - and white spaces from the beginning and the end of the string
    stripped = string.strip('+- ')
    # chek if the string is an integer
    if stripped.isdigit():
        return True
    else:
        return False


# check is_integer()
def main():
    string = input('enter a string: ')
    if is_integer(string):
        print("it's an integer")
    else:
        print("it's not an integer")


if __name__ == '__main__':
    main()
