import sys
import math
from collections import Counter

alphabets = list('abcdefghijklmnopqrstuvwxyz')

def bootstrap(f, stack=[]):
    from types import GeneratorType
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)

        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)

                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p

def primeFactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(int(i))
            n = n / i
    if n > 2:
        l.append(n)
    c = dict(Counter(l))
    return list(set(l))

def power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def sieveForSmallestPrimeFactor():
    MAXN = 100001
    spf = [0 for _ in range(MAXN)]
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i
    for i in range(4, MAXN, 2):
        spf[i] = 2
    for i in range(3, math.ceil(math.sqrt(MAXN))):
        if spf[i] == i:
            for j in range(i * i, MAXN, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def getPrimeFactorizationLOGN(x):
    spf = sieveForSmallestPrimeFactor()
    ret = []
    while x != 1:
        ret.append(spf[x])
        x = x // spf[x]
    return ret

def SieveOfEratosthenes(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime

def divideCeil(n, x):
    if n % x == 0:
        return n // x
    return n // x + 1

def solve_from_data(n, a, b, c, t, ti):
    if b > c:
        return n * a
    ans = 0
    ti_sorted = sorted(ti)
    for i in ti_sorted:
        ans += (t - i) * (c - b) + a
    return ans

def generate_test_data(n):
    # Map n to:
    # n: number of elements in ti
    # a, b, c, t: deterministic functions of n
    if n <= 0:
        n = 1
    a = 1 + (n % 5)
    b = 2 + (n % 7)
    c = 3 + (n % 11)
    t = n + 5
    ti = [i % (t + 1) for i in range(1, n + 1)]
    return n, a, b, c, t, ti

def main(n):
    n_val, a, b, c, t, ti = generate_test_data(n)
    result = solve_from_data(n_val, a, b, c, t, ti)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)