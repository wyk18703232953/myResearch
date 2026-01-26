from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math
import bisect


def isPrime(x):
    for i in range(2, x):
        if i * i > x:
            break
        if x % i == 0:
            return False
    return True


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


def sieve(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime


def digits(n):
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c


def ceil(n, x):
    if n % x == 0:
        return n // x
    return n // x + 1


def main(n):
    # n is the length of the generated string
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministic periodic pattern over 3 characters
    chars = ['a', 'b', 'c']
    s = [chars[i % 3] for i in range(n)]

    l = [1]
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            l[-1] += 1

        else:
            l.append(1)

    ans = max(l)
    if len(l) > 1:
        if s[0] != s[-1]:
            ans = max(ans, l[0] + l[-1])

    # print(ans)
    pass
if __name__ == "__main__":
    # Example call; adjust n for different input scales
    main(10)