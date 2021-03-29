# Remove Outliers

# Remove the outliers from a list of values
# @param data the list of values to process
# @param n the number of smallest and largest values to remove
# @return a new copy of data where the smallest and largest values have been removed
def remove_outliers(data, n):
    res = data[:]
    for i in range(n):
        res.remove(max(res))
    for i in range(n):
        res.remove(min(res))
    return res


# Read data from the user, and remove the two largest and two smallest values
def main():
    data = []
    num = int(input('enter an integer (0 to quit): '))
    while num != 0:
        data.append(num)
        num = int(input('enter an integer (0 to quit): '))
    if len(data) < 4:
        print('please enter more than 4 integers')
    else:
        print('this is the list with 2 outliers removed: {}'.format(remove_outliers(data, 2)))
        print('this is the original list {}'.format(data))


if __name__ == '__main__':
    main()
