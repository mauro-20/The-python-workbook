# Sorted Order
# Display a list of integers entered by the user in ascending order.

# initialize the list
my_list = []

# Read values and add them to the list until the user enters 0
num = int(input('enter an integer (0 to quit): '))
while num != 0:
    my_list.append(num)
    num = int(input('enter an integer (0 to quit): '))

# sort the elements of the list
my_list.sort()

# print each elements on a separate line
for el in my_list:
    print(el)
