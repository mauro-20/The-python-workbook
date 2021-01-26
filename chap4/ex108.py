# Reduce Measures


# Reduce an imperial measurement to the largest possible units of measure
# @param num the number of units that need to be reduced
# @param unit the unit of measure ('cup', 'tablespoon' or 'teaspoon')
# @return a string representing the measurement in reduced form
def reduce(num, unit):

    ts_per_tblsp = 3
    ts_per_cup = 48

    # convert the unit in teaspoons for an easier calculation
    if unit == 'teaspoon':
        teaspoon = num
    elif unit == 'tablespoon':
        teaspoon = num * ts_per_tblsp
    elif unit == 'cup':
        teaspoon = num * ts_per_cup

    # compute the reduce
    cup = teaspoon//ts_per_cup
    teaspoon = teaspoon - cup * ts_per_cup
    tablespoon = teaspoon//ts_per_tblsp
    teaspoon = teaspoon - tablespoon * ts_per_tblsp

    # build the string to return
    result = ''
    if cup > 0:
        result = '{} cup'.format(cup)
        if cup > 1:
            result += 's'
    if tablespoon > 0:
        result += ', {} tablespoon'.format(tablespoon)
        if tablespoon > 1:
            result += 's'
    if teaspoon > 0:
        result += ', {} teaspoon'.format(teaspoon)
        if teaspoon > 1:
            result += 's'

    return result


# test
if __name__ == '__main__':
    print(reduce(59, 'teaspoon'))
