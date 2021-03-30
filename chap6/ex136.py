# Reverse Lookup

# Conduct a reverse lookup on a dictionary
# @param d the dictionary on which the reverse lookup is performed
# @param v the value to search for in the dictionary
# @return a list (possibly empty) of keys from data that map to value
def reverse_lookup(d, v):
    keys_list = []
    for k in d:
        if d[k] == v:
            keys_list.append(k)
    return keys_list


# testing reverse_lookup() function
def main():
    d4 = {'k1': 2, 'k2': 2, 'k3': 2, 'k4': 4}
    # multiple keys
    print(reverse_lookup(d4, 2))
    # single key
    print(reverse_lookup(d4, 4))
    # no keys
    print(reverse_lookup(d4, 3))


if __name__ == '__main__':
    main()
