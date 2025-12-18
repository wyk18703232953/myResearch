def resheto(a):
    numbers = list(range(0, a + 1))
    primes = set()
    for k in range(2, a + 1):
        if numbers[k] != 0:
            primes.add(k)
            for j in range(2 * k, a + 1, k):
                numbers[j] = 0
    return primes


all_primes = resheto(10**6)
n = int(input())
for i in range(2, n):
    if i not in all_primes and (n - i) not in all_primes:
        print(i, n - i)
        break