# Maximum Integer

import random

num = random.randint(1, 100)
print(num)
max_int = num
update = 0
for i in range(99):
    num = random.randint(1, 100)
    if num > max_int:
        max_int = num
        print(max_int, ' <== update')
        update += 1
    else:
        print(num)

print('the maximum value found was {}'.format(max_int))
print('the maximum value was updated {} times'.format(update))
