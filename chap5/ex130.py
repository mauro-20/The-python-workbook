# Unary and Binary Operators

from ex129 import tokenizing


def unary(tokens):
    operators = ['*', '/', '-', '+', '(']
    for i in range(len(tokens)):
        if (tokens[i] == '-' or tokens[i] == '+') and i == 0:
            tokens[i] = 'U' + tokens[i]
        elif (tokens[i] == '-' or tokens[i] == '+') and tokens[i-1] in operators:
            tokens[i] = 'U' + tokens[i]


def main():
    expression = input('enter a mathematical expression: ')
    tokens = tokenizing(expression)
    print(tokens)
    unary(tokens)
    print(tokens)


if __name__ == '__main__':
    main()
