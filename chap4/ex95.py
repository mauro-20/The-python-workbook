# Capitalize It

# Capitalize the appropriate characters in a string
# @param string the string that needs capitalization
# @return a new string with the capitalization improved
def capitalize(string):
    new_string = ''
    for index in range(len(string)):
        # capitalize the first letter
        if index == 0:
            new_string += string[index].upper()
        # capitalize letters after ".!?"
        elif string[index-1] == ' ':
            if string[index-2] == '.' or string[index-2] == '!' or string[index-2] == '?':
                new_string += string[index].upper()
            # capitalize "i" if preceded by a space and followed by ".!?'"
            elif string[index] == 'i' and string[index+1] == ' ' or string[index+1] == '.' or string[index+1] == '!'\
                    or string[index + 1] == '?' or string[index+1] == "'":
                new_string += string[index].upper()
            else:
                new_string += string[index]
        else:
            new_string += string[index]
    return new_string


# testing capitalize() by the user
def main():
    string = input('enter a string to capitalize\n')
    print(capitalize(string))


if __name__ == '__main__':
    main()
