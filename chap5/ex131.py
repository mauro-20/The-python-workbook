# Infix to Postfix

from ex129 import tokenizing
from ex130 import unary


def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == 'U+' or operator == 'U-':
        return 3
    elif operator == '^':
        return 4
    else:
        return -1


def postfix(infix):
    oper = ['+', '-', '*', '/', '^', 'U-', 'U+']
    operators = []
    postfix = []

    for token in infix:
        if token.isdigit():
            postfix.append(token)
        if token in oper:
            while operators != [] and operators[-1] != '(' and precedence(token) <= precedence(operators[-1]):
                postfix.append(operators.pop())
            operators.append(token)
        if token == '(':
            operators.append(token)
        if token == ')':
            while operators[-1] != '(':
                postfix.append(operators.pop())
            operators.remove('(')
    while operators != []:
        postfix.append(operators.pop())

    return postfix


def main():
    expression = input('enter a mathematical expression:\n')
    tokens = tokenizing(expression)
    unary(tokens)
    post = ' '.join(postfix(tokens))
    print('the equivalent postfix expression is {}'.format(post))


if __name__ == '__main__':
    main()
