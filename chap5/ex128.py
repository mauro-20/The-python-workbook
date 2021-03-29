# Count the Elements


# Determine how many elements in data are greater than or equal to mn and less than mx
# @param data the list of values to examine
# @param mn the minimum acceptable value
# @param mx the exclusive upper bound on acceptability
# @return the number of elements, e, such that mn <= e < mx
def count_range(t, mn, mx):
    res = 0
    for num in t:
        if mn <= num <= mx:
            res += 1
    return res


# test count_range()
def main():
    list1 = [1, 2, 3.2, 3, 4, 6, 5.1, 5, 5, 7, 6, 6, 6, ]
    print(count_range(list1, 2, 5))
    print(count_range(list1, 3, 8))


main()
