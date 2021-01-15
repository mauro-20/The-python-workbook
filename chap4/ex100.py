# Random Password

from random import randint


# this function will generate a random password
# @return a random password in a string
def random_pwd():
    min_length = 7
    max_length = 10
    min_ascii = 33
    max_ascii = 126
    # determine the length of the password
    length = randint(min_length, max_length)
    password = ""
    # generate the password
    for i in range(length):
        password += chr(randint(min_ascii, max_ascii))
    return password


# display the random password only if the module is not imported
if __name__ == '__main__':
    print(random_pwd())
