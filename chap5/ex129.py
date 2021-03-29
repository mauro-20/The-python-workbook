# Tokenizing a String


# Convert a mathematical expression into a list of tokens
# @param string the string to tokenize
# @return a list of the tokens
def tokenizing(string):
    operators = ['*', '/', '^', '-', '+', '(', ')']
    tokens = []
    # remove the spaces
    s = string.replace(' ', '')
    i = 0
    while i < len(s):
        # handle the operators as token
        if s[i] in operators:
            tokens.append(s[i])
            i += 1
        # handle numbers as single token
        elif s[i].isdigit():
            num = ''
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            tokens.append(num)
    return tokens


# test with user input
def main():
    expression = input('enter an expression:\n')
    print(tokenizing(expression))


if __name__ == '__main__':
    main()
