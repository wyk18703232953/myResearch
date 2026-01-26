import math
from queue import Queue
import itertools
import bisect
import heapq

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
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i + i, n + 1, i):
                primes[j] = False
    p = []
    for i in range(0, n + 1):
        if primes[i]:
            p.append(i)
    return p

def ncr(n, r, p):
    num = den = 1
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

def build_grids(n_rows, n_cols):
    hor = []
    ver = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols - 1):
            val = (i + 1) * (j + 2)
            row.append(val)
        hor.append(row)
    for i in range(n_rows - 1):
        row = []
        for j in range(n_cols):
            val = (i + 2) * (j + 1)
            row.append(val)
        ver.append(row)
    return hor, ver

def solve_core(n_rows, n_cols, k_steps, hor, ver):
    inF = 10 ** 20
    k = k_steps // 2
    dp = [[[-1] * (n_cols + 1) for _ in range(n_rows + 1)] for _ in range(k + 1)]

    def getVal(x, y, sx, sy):
        if x == -1 or y == -1 or x == n_rows or y == n_cols:
            return inF
        elif sx == x:
            a = sy
            b = y
            if a > b:
                a, b = b, a
            if b - 1 < 0:
                return inF
            return hor[sx][a]

        else:
            a = sx
            b = x
            if a > b:
                a, b = b, a
            if b - 1 < 0:
                return inF
            return ver[a][sy]

    def rec(k_cur, x, y):
        if x == -1 or y == -1 or x >= n_rows or y >= n_cols:
            return inF
        if k_cur == 0:
            dp[k_cur][x][y] = 0
            return dp[k_cur][x][y]
        if dp[k_cur][x][y] != -1:
            return dp[k_cur][x][y]
        val1 = rec(k_cur - 1, x - 1, y) + getVal(x - 1, y, x, y)
        val2 = rec(k_cur - 1, x + 1, y) + getVal(x + 1, y, x, y)
        val3 = rec(k_cur - 1, x, y + 1) + getVal(x, y + 1, x, y)
        val4 = rec(k_cur - 1, x, y - 1) + getVal(x, y - 1, x, y)
        dp[k_cur][x][y] = min(val1, val2, val3, val4)
        return dp[k_cur][x][y]

    res = []
    if k_steps % 2 == 1:
        for i in range(n_rows):
            res.append([-1] * n_cols)

    else:
        for i in range(n_rows):
            row = []
            for j in range(n_cols):
                val = 2 * rec(k, i, j)
                row.append(val)
            res.append(row)
    return res

def main(n):
    if n < 1:
        n = 1
    n_rows = n
    n_cols = n
    k_steps = 2 * n
    hor, ver = build_grids(n_rows, n_cols)
    result = solve_core(n_rows, n_cols, k_steps, hor, ver)
    for i in range(n_rows):
        # print(" ".join(str(x) for x in result[i]))
        pass
if __name__ == "__main__":
    main(5)