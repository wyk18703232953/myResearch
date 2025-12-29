import math
import random
from itertools import accumulate
from decimal import Decimal

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
    return prime


def primefactors(n):
    fac = []
    while n % 2 == 0:
        fac.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 2):
        while n % i == 0:
            fac.append(i)
            n //= i
    if n > 1:
        fac.append(n)
    return sorted(fac)


def factors(n):
    fac = set()
    fac.add(1)
    fac.add(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            fac.add(i)
            fac.add(n // i)
    return list(fac)


def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x += m0
    return x


def main(n):
    # 生成测试数据：
    # n: 数组长度
    # k: 随机选择一个整数（避免 0）
    if n <= 0:
        print(0)
        return

    k = random.randint(1, 10)
    # 生成 n 个正整数，范围 1..10^6
    a = [random.randint(1, 10**6) for _ in range(n)]

    # 原逻辑
    a = list(sorted(a, reverse=True))
    s = set()
    for i in range(len(a)):
        if a[i] * k not in s:
            s.add(a[i])

    print(len(s))


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(10)