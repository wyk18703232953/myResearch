def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def SieveOfEratosthenes(n):
    prime = []
    primes = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p] is True:
            prime.append(p)
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return prime


def factors(n):
    fac = []
    while n % 2 == 0:
        fac.append(2)
        n = n // 2
    i = 3
    while i <= int(n**0.5) + 1:
        while n % i == 0:
            fac.append(i)
            n = n // i
        i += 2
    if n > 1:
        fac.append(n)
    return fac


def main(n):
    a = ''.join(str((i % 3) + 1) for i in range(n))
    b = a.count('1')
    a = a.replace('1', '')
    c = a.find('2')
    if c == -1:
        a = a + '1' * b

    else:
        a = a[:c] + '1' * b + a[c:]
    # print(a)
    pass
if __name__ == "__main__":
    main(10)