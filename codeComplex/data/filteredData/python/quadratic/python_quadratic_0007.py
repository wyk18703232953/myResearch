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
        if primes[p]:
            prime.append(p)
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    if n >= 1:
        primes[1] = False
    if n >= 0:
        primes[0] = False
    return primes

def primefactors(n):
    fac = []
    while n % 2 == 0:
        fac.append(2)
        n = n // 2
    i = 3
    limit = int(__import__('math').sqrt(n)) + 2
    while i <= limit:
        while n % i == 0:
            fac.append(i)
            n = n // i
        i += 2
        limit = int(__import__('math').sqrt(n)) + 2
    if n > 1:
        fac.append(n)
    return fac

def factors(n):
    import math
    fac = set()
    fac.add(1)
    fac.add(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            fac.add(i)
            fac.add(n // i)
    return list(fac)

def NcR(n, r):
    import math
    p = 1
    k = 1
    if n - r < r:
        r = n - r
    if r != 0:
        while r:
            p *= n
            k *= r
            m = math.gcd(p, k)
            p //= m
            k //= m
            n -= 1
            r -= 1

    else:
        p = 1
    return p

def Log2(x):
    import math
    if x == 0:
        return False
    return math.log10(x) / math.log10(2)

def isPowerOfTwo(n):
    import math
    return math.ceil(Log2(n)) == math.floor(Log2(n))

def core_algorithm(n, r, x):
    c = []
    result = []
    for i in range(n):
        k = r
        for x1, j in c:
            d = abs(x[i] - x1)
            if d <= 2 * r:
                k = max(k, j + (4 * r ** 2 - d * d) ** 0.5)
        c.append([x[i], k])
        result.append(k)
    return result

def main(n):
    # n is the input size: length of the list x
    # Deterministically construct r and x based on n
    # Ensure r >= 1
    r = max(1, n // 3)
    # Construct x as a deterministic sequence with varying gaps
    # to exercise the inner loop: e.g., arithmetic progression with wrap mod (4*r)
    x = [(i * 3) % (4 * r + 1) for i in range(n)]
    res = core_algorithm(n, r, x)
    for v in res:
        # print(v)
        pass
if __name__ == "__main__":
    # example fixed-scale call for experimentation
    main(10)