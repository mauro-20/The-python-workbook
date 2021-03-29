# Does a List Contain a Sublist?

# determine if a list is a sublist of another list
# @param larger is the larger list
# @param smaller is the smaller list
# @return True if smaller is a sublist of larger, False otherwise
def is_sublist(larger, smaller):
    if smaller == []:
        return True
    elif len(smaller) > len(larger):
        return False
    elif smaller[0] in larger:
        ind = larger.index(smaller[0])
        i = 0
        while i < len(smaller):
            if smaller[i] != larger[ind+i]:
                return False
            i += 1
        return True
    else:
        return False


def main():
    list1 = [1, 2, 3, 4]
    list2 = [1, 2]
    print(is_sublist(list1, list2))


if __name__ == '__main__':
    main()
