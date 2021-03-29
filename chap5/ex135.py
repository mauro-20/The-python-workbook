# The Sieve of Eratosthenes

def prime(limit):
    numbers = []
    for i in range(2, limit+1):
        numbers.append(i)
    p = 2
    while p < limit:
        for i in numbers:
            if i != p and i % p == 0:
                ind = numbers.index(i)
                numbers[ind] = 0
        p += 1
    prime_num = []
    for n in numbers:
        if n != 0:
            prime_num.append(n)
    return prime_num


print(prime(30))
