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
        y >>= 1
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


def solve(final, n):
    fifi = [[final[j][i] for j in range(n)] for i in range(n)]

    k = []
    for i in range(n):
        k.append(sum(final[i]))
    a = max(k) - min(k)

    a = a * a
    k = []
    for i in range(n):
        k.append(sum(fifi[i]))
    b = max(k) - min(k)

    b = b * b

    return a + b


def inte(a, b, c, d):
    a = max(a, c)
    b = min(b, d)
    return [a, b]


def main(n):
    # 生成测试数据：n 个区间 [l_i, r_i]
    # 保证 l_i <= r_i，范围在 [0, 1e6]
    MAXV = 10**6
    l = []
    for _ in range(n):
        x = random.randint(0, MAXV)
        y = random.randint(0, MAXV)
        if x > y:
            x, y = y, x
        l.append([x, y])

    f = []
    ff = []
    a = 0
    b = 10_000_000_000_000
    f.append([a, b])

    for i in range(n):
        x = inte(a, b, l[i][0], l[i][1])
        a = x[0]
        b = x[1]
        f.append([a, b])

    a = 0
    b = 10_000_000_000_000
    ff = [[] for _ in range(n)]
    for i in reversed(range(n)):
        x = inte(a, b, l[i][0], l[i][1])
        a = x[0]
        b = x[1]
        ff[i] = [a, b]

    ff.append([0, 100_000_000_000_000])

    ans = 0
    for i in range(n):
        a = f[i]
        b = ff[i + 1]
        y = inte(a[0], a[1], b[0], b[1])
        if y[1] >= y[0]:
            ans = max(ans, y[1] - y[0])

    print(ans)


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)