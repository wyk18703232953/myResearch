import os
import sys
from io import BytesIO, IOBase
import math
from queue import Queue
import collections
import itertools
import bisect
import heapq
import random


def binary(n):
    return bin(n).replace("0b", "")


def decimal(s):
    return int(s, 2)


def pow2(n):
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return p


def primeFactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(i)
            n = n / i
    if n > 2:
        l.append(int(n))
    return l


def primeFactorsCount(n):
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            cnt += 1
            n = n // i
    if n > 2:
        cnt += 1
    return cnt


def isPrime(n):
    if n == 1:
        return False
    root = int(n ** 0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            return False
    return True


def maxPrimeFactors(n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    if n > 2:
        maxPrime = n
    return int(maxPrime)


def countcon(s, i):
    c = 0
    ch = s[i]
    for i in range(i, len(s)):
        if s[i] == ch:
            c += 1
        else:
            break
    return c


def lis(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, dp[i])
    return maximum


def isSubSequence(str1, str2):
    m = len(str1)
    n = len(str2)
    j = 0
    i = 0
    while j < m and i < n:
        if str1[j] == str2[i]:
            j += 1
        i += 1
    return j == m


def maxfac(n):
    root = int(n ** 0.5)
    for i in range(2, root + 1):
        if n % i == 0:
            return n // i
    return n


def p2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def seive(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    i = 2
    while i * i <= n:
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
        i += 1
    pr = []
    for i in range(0, n + 1):
        if primes[i]:
            pr.append(i)
    return pr


def ncr(n, r, p):
    num = 1
    den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


def denofactinverse(n, m):
    fac = 1
    for i in range(1, n + 1):
        fac = (fac * i) % m
    return pow(fac, m - 2, m)


def numofact(n, m):
    fac = 1
    for i in range(1, n + 1):
        fac = (fac * i) % m
    return fac


def sod(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def main(n):
    # 生成规模为 n 的测试数据
    if n <= 0:
        return

    # 数组长度 n，元素取值 1..1e9
    l = [random.randint(1, 10**9) for _ in range(n)]

    # 预先计算初始逆序对个数
    inv = 0
    for i in range(1, n):
        for j in range(0, i):
            if l[j] > l[i]:
                inv += 1

    # 设查询次数 q 与 n 同规模
    q = n

    # 随机生成 q 次查询
    queries = []
    for _ in range(q):
        f = random.randint(1, n)
        r = random.randint(f, n)
        queries.append((f, r))

    # 模拟原代码的查询逻辑并输出
    for f, r in queries:
        p = (r - f + 1) // 2
        inv += p % 2
        if inv % 2:
            print("odd")
        else:
            print("even")


if __name__ == "__main__":
    # 示例：运行 main(5) 进行简单测试
    main(5)