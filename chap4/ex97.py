# Operator Precedence

# this function will give the precedence of the operators
# @param operator the operator to be checked
# @return the precedence of the operator, if no operator found return -1
def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '**':
        return 3
    else:
        return -1


def main():
    operator = input('enter an operator: ')
    if 1 <= precedence(operator) <= 3:
        print(f'the operator precedence is {precedence(operator)}')
    else:
        print('error: input is not an operator')


if __name__ == '__main__':
    main()
