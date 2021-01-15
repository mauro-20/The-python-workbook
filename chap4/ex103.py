# Random Good Password

from ex100 import random_pwd
from ex102 import is_valid_password


# this function generates and print a valid password
def main():
    count = 0
    password = ''
    while not is_valid_password(password):
        password = random_pwd()
        count += 1
    print(f'This is a valid password {password} after {count} attempts')


if __name__ == '__main__':
    main()
