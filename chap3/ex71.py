# Approximate π

pi = 3
approximation = 0
k = 0

while approximation < 15:
    den = (2+k)*(3+k)*(4+k)
    if approximation % 2 == 0:
        pi += 4/den
    else:
        pi -= 4/den
    approximation += 1
    k += 2

print(pi)
