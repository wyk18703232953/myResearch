import math
import itertools
import bisect
import heapq

def binary(n):
    return (bin(n).replace("0b", ""))

def decimal(s):
    return (int(s, 2))

def pow2(n):
    p = 0
    while (n > 1):
        n //= 2
        p += 1
    return (p)

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
    return (l)

def isPrime(n):
    if (n == 1):
        return (False)

    else:
        root = int(n ** 0.5)
        root += 1
        for i in range(2, root):
            if (n % i == 0):
                return (False)
        return (True)

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
        if (s[i] == ch):
            c += 1

        else:
            break
    return (c)

def lis(arr):
    n = len(arr)
    lis_arr = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis_arr[i] < lis_arr[j] + 1:
                lis_arr[i] = lis_arr[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis_arr[i])
    return maximum

def isSubSequence(str1, str2):
    m = len(str1)
    n2 = len(str2)
    j = 0
    i = 0
    while j < m and i < n2:
        if str1[j] == str2[i]:
            j = j + 1
        i = i + 1
    return j == m

def maxfac(n):
    root = int(n ** 0.5)
    for i in range(2, root + 1):
        if (n % i == 0):
            return (n // i)
    return (n)

def p2(n):
    c = 0
    while(n % 2 == 0):
        n //= 2
        c += 1
    return c

def seive(n):
    primes = [True] * (n + 1)
    if n >= 0:
        primes[0] = False
    if n >= 1:
        primes[1] = False
    for i in range(2, n + 1):
        if(primes[i]):
            for j in range(i + i, n + 1, i):
                primes[j] = False
    p = []
    for i in range(0, n + 1):
        if(primes[i]):
            p.append(i)
    return(p)

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
    return (pow(fac, m - 2, m))

def numofact(n, m):
    fac = 1
    for i in range(1, n + 1):
        fac = (fac * i) % m
    return(fac)

def sod(n):
    s = 0
    while(n > 0):
        s += n % 10
        n //= 10
    return s

def build_test_data(n):
    if n <= 0:
        n = 1
    if n % 2 == 1:
        n += 1
    rows = n
    cols = n
    steps = 2 * n
    hor = []
    for i in range(rows):
        row = [1 + (i + j) % 7 for j in range(cols - 1)]
        hor.append(row)
    ver = []
    for i in range(rows - 1):
        row = [1 + (i * 3 + j * 2) % 9 for j in range(cols)]
        ver.append(row)
    return rows, cols, steps, hor, ver

def solve(rows, cols, steps, hor, ver):
    inF = 10 ** 20

    def getVal(x, y, sx, sy):
        if (x == -1 or y == -1 or x == rows or y == cols):
            return inF
        elif(sx == x):
            if sy < y:
                return hor[sx][sy]

            else:
                return hor[sx][y]

        else:
            if sx < x:
                return ver[sx][sy]

            else:
                return ver[x][sy]

    def rec(k, x, y, dp):
        if(x == -1 or y == -1 or x >= rows or y >= cols):
            return inF
        elif (k == 0):
            dp[k][x][y] = 0
            return dp[k][x][y]
        elif(dp[k][x][y] != -1):
            return dp[k][x][y]

        else:
            val1 = rec(k - 1, x - 1, y, dp) + getVal(x - 1, y, x, y)
            val2 = rec(k - 1, x + 1, y, dp) + getVal(x + 1, y, x, y)
            val3 = rec(k - 1, x, y + 1, dp) + getVal(x, y + 1, x, y)
            val4 = rec(k - 1, x, y - 1, dp) + getVal(x, y - 1, x, y)
            dp[k][x][y] = min(val1, val2, val3, val4)
            return dp[k][x][y]

    if(steps % 2):
        res = [[-1 for _ in range(cols)] for _ in range(rows)]
        return res

    else:
        k = steps // 2
        dp = [[[-1] * (cols + 1) for _ in range(rows + 1)] for _ in range(k + 1)]
        res = []
        for i in range(0, rows):
            row_res = []
            for j in range(0, cols):
                row_res.append(2 * rec(k, i, j, dp))
            res.append(row_res)
        return res

def main(n):
    rows, cols, steps, hor, ver = build_test_data(n)
    result = solve(rows, cols, steps, hor, ver)
    for i in range(len(result)):
        for j in range(len(result[0])):
            # print(result[i][j], end=" ")
            pass
        # print("")
        pass
if __name__ == "__main__":
    main(4)