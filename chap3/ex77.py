# Multiplication Table

print('%4s' % '', end='')
for i in range(1, 11):
    print('%4d' % i, end='')
print()

for i in range(1, 11):
    print('%4d' % (1*i), end='')
    for j in range(1, 11):
        print('%4d' % (i*j), end='')
    print()

