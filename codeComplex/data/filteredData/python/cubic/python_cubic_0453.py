import math
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

def sod(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

# The main grid DP logic uses these globals:
# n_rows, m_cols, k_steps, hor, ver, dp, inF
def main(n):
    """
    n: overall scale parameter.
       We set grid size and k based on n, and generate random test data.
    """

    # Choose grid size and k from n.
    # For demonstration: n_rows = n, m_cols = n, k_steps = 2*n (even).
    # You can adjust this policy as needed.
    n_rows = max(1, n)
    m_cols = max(1, n)
    k_steps = 2 * max(1, n_rows)  # ensure even

    # Generate random weights for edges:
    # hor: n_rows x (m_cols - 1) horizontal edges
    # ver: (n_rows - 1) x m_cols vertical edges
    # We'll keep weights small to avoid huge outputs.
    max_w = 10

    if m_cols > 1:
        hor = [[random.randint(1, max_w) for _ in range(m_cols - 1)] for _ in range(n_rows)]
    else:
        hor = [[] for _ in range(n_rows)]

    if n_rows > 1:
        ver = [[random.randint(1, max_w) for _ in range(m_cols)] for _ in range(n_rows - 1)]
    else:
        ver = []

    inF = 10 ** 20
    k_half = k_steps // 2

    # dp[k][x][y]: minimal cost to do k_half steps and end at (x,y)
    # dimensions: (k_half+1) x n_rows x m_cols, initialize -1
    dp = [[[-1] * m_cols for _ in range(n_rows)] for _ in range(k_half + 1)]

    # helper to get edge cost between (sx,sy) and (x,y)
    def getVal(x, y, sx, sy):
        if x < 0 or y < 0 or x >= n_rows or y >= m_cols:
            return inF
        if sx == x:
            # horizontal edge: same row, different col
            if sy == y:
                return 0
            if sy < y:
                # moving right
                return hor[sx][sy]
            else:
                # moving left
                return hor[sx][y]
        else:
            # vertical edge: same col, different row
            if sx < x:
                # moving down
                return ver[sx][sy]
            else:
                # moving up
                return ver[x][sy]

    # recursive memoized solver
    def rec(k, x, y):
        if x < 0 or y < 0 or x >= n_rows or y >= m_cols:
            return inF
        if k == 0:
            dp[k][x][y] = 0
            return 0
        if dp[k][x][y] != -1:
            return dp[k][x][y]

        val1 = rec(k - 1, x - 1, y) + getVal(x - 1, y, x, y)
        val2 = rec(k - 1, x + 1, y) + getVal(x + 1, y, x, y)
        val3 = rec(k - 1, x, y + 1) + getVal(x, y + 1, x, y)
        val4 = rec(k - 1, x, y - 1) + getVal(x, y - 1, x, y)
        ans = min(val1, val2, val3, val4)
        dp[k][x][y] = ans
        return ans

    # If k_steps is odd, answer is -1 everywhere
    if k_steps % 2 == 1:
        for i in range(n_rows):
            row = ["-1"] * m_cols
            print(" ".join(row))
        return

    # Compute and print answers for each cell
    for i in range(n_rows):
        out_row = []
        for j in range(m_cols):
            cost = rec(k_half, i, j)
            if cost >= inF:
                out_row.append("-1")
            else:
                out_row.append(str(2 * cost))
        print(" ".join(out_row))

if __name__ == "__main__":
    # Example: call main with some scale n
    main(3)