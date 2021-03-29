# Generate All Sublists of a List

def sublists_generator(t):
    sublists = [[]]
    for length in range(1, len(t) + 1):
        for i in range(0, len(t) - length + 1):
            sublists.append(t[i: i + length])
    print(sublists)


list1 = [1, 2, 3, 4, 5]
list2 = []
sublists_generator(list1)
