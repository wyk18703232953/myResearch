import sys, os, io
from math import log, gcd, ceil
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import math


alphabets = list('abcdefghijklmnopqrstuvwxyz')


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


def SieveOfEratosthenes(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime


def countdig(n):
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c


def prefix_sum(arr):
    r = [0] * (len(arr) + 1)
    for i, el in enumerate(arr):
        r[i + 1] = r[i] + el
    return r


def divideCeil(n, x):
    if n % x == 0:
        return n // x
    return n // x + 1


def ws(s):
    sys.stdout.write(s + '\n')


def wi(n):
    sys.stdout.write(str(n) + '\n')


def wia(a):
    sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def power_set(L):
    cardinality = len(L)
    n = 2 ** cardinality
    powerset = []

    for i in range(n):
        a = bin(i)[2:]
        subset = []
        for j in range(len(a)):
            if a[-j - 1] == '1':
                subset.append(L[j])
        powerset.append(subset)
    powerset_orderred = []
    for k in range(cardinality + 1):
        for w in powerset:
            if len(w) == k:
                powerset_orderred.append(w)

    return powerset_orderred


def fastPlrintNextLines(a):
    # print('\n'.join(map(str, a)))
    pass


def sortByFirstAndSecond(A):
    A = sorted(A, key=lambda x: x[0])
    A = sorted(A, key=lambda x: x[1])
    return list(A)


def solve(n, k, p):
    groups = [-1] * 256
    newar = [-1] * n
    for i in range(n):
        color = p[i]
        j = color
        if groups[color] != -1:
            newar[i] = groups[color]
            continue

        while j > 0:
            if groups[j] != -1:
                break
            if color - j + 1 == k:
                break
            j -= 1

        if groups[j] == -1:
            for h in range(j, color + 1):
                groups[h] = j
            newar[i] = groups[color]
            continue
        if color - j < k:
            alreadySize = j - groups[j] + 1
            if alreadySize + color - j <= k:
                for h in range(j + 1, color + 1):
                    groups[h] = groups[h - 1]
                newar[i] = groups[color]
                continue

            else:
                for h in range(j + 1, color + 1):
                    groups[h] = j + 1
                newar[i] = groups[color]
                continue

        else:
            for h in range(j + 1, color + 1):
                groups[h] = j + 1
            newar[i] = groups[color]
            continue
    return newar


def generate_input(n):
    if n < 1:
        n = 1
    max_n = 200000
    if n > max_n:
        n = max_n
    k = (n // 3) + 1
    max_color = 255
    p = [(i * 37 + 13) % (max_color + 1) for i in range(n)]
    return n, k, p


def main(n):
    n_gen, k, p = generate_input(n)
    res = solve(n_gen, k, p)
    # print(*res)
    pass
if __name__ == "__main__":
    main(10)