# Center a String in the TerminalWindow

# this function will center a string in a terminal window
# @param string is the string we want to center
# @param width is the width of the window
# @return a string centered in the window
def center_string(string: str, width: int):
    if len(string) >= width:
        return string
    else:
        return (width-len(string)//2) * ' ' + string


# function to test the center_string
def main():
    width = 20
    print(center_string('Hello', width))
    print(center_string('this is', width))
    print(center_string('a', width))
    print(center_string('test!', width))


if __name__ == '__main__':
    main()
