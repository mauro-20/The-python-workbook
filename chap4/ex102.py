# Check a Password

# this function determines if a password is valid
# a valid password is minimum 8 characters long and contain at least 1 uppercase, 1 lowercase and 1 digit
# @param psw is the password to be validated
# @return True if the password is valid, False otherwise
def is_valid_password(psw):
    min_length = 8
    has_lower = False
    has_upper = False
    has_number = False
    # set boolean to True if requirement is met
    for i in psw:
        if i.isupper():
            has_upper = True
        elif i.islower():
            has_lower = True
        elif i.isdigit():
            has_number = True
    # check if password has all the requirements
    if len(psw) >= min_length and has_upper and has_lower and has_number:
        return True
    return False


# test is_valid_password() from user input
def main():
    password = input('enter a password of\nminimum 8 characters\nat least one uppercase letter\n'
                     'at least one lowercase letter\nat least one number:\n ')
    if is_valid_password(password):
        print("it's a valid password")
    else:
        print("sorry your password is not valid")


if __name__ == '__main__':
    main()
