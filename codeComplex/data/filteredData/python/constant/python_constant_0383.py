from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math
import bisect
import random


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
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(int(i))
            n = n // i
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
    """
    n: 规模参数。这里复用为原题中的 n，
       并基于 n 随机生成 a, b, c：
       0 <= c <= min(a, b) <= n
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    # 生成测试数据
    a = random.randint(0, n)
    b = random.randint(0, n)
    c = random.randint(0, min(a, b))  # 保证 c <= a 且 c <= b

    d = a + b - c

    if d > n - 1 or c > a or c > b:
        print(-1)
    else:
        print(n - d)


if __name__ == "__main__":
    # 示例：可以在此处调用 main，传入某个规模 n
    main(10)