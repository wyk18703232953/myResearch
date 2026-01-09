import math as M
import itertools as ITR
from collections import defaultdict as D
from collections import Counter as C
from collections import deque as Q
import threading
from functools import lru_cache, reduce
from functools import cmp_to_key as CMP
from bisect import bisect_left as BL
from bisect import bisect_right as BR

enum = enumerate

MOD = 1_00_00_00_007
MA = float("inf")
MI = float("-inf")

di8 = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))
di4 = ((1, 0), (0, 1), (-1, 0), (0, -1))


def increase_stack():
    import sys

    sys.setrecursionlimit(2 ** 32 // 2 - 1)
    threading.stack_size(1 << 27)


def binary(n):
    return bin(n)[2:]


def decimal(s):
    return int(s, 2)


def pow2(n):
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return p


def maxfactor(n):
    q = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            q.append(i)
    if q:
        return q[-1]


def factors(n):
    q = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            q.append(i)
            q.append(n // i)
    return list(sorted(list(set(q))))


def primeFactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n / 2
    for i in range(3, int(M.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(i)
            n = n / i
    if n > 2:
        l.append(int(n))
    l.sort()
    return l


def isPrime(n):
    if n == 1:
        return False

    else:
        root = int(n ** 0.5)
        root += 1
        for i in range(2, root):
            if n % i == 0:
                return False
        return True


def seive(n):
    a = []
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] is True:
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p = p + 1
    for p in range(2, n + 1):
        if prime[p]:
            a.append(p)
    prime[0] = prime[1] = False
    return a, prime


def maxPrimeFactors(n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1
    for i in range(3, int(M.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    if n > 2:
        maxPrime = n
    return int(maxPrime)


def countchar(s, i):
    c = 0
    ch = s[i]
    for i in range(i, len(s)):
        if s[i] == ch:
            c += 1

        else:
            break
    return c


def str_counter(a):
    q = [0] * 26
    for i in range(len(a)):
        q[ord(a[i]) - 97] = q[ord(a[i]) - 97] + 1
    return q


def lis(arr):
    n = len(arr)
    lis_arr = [1] * n
    maximum = 0

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis_arr[i] < lis_arr[j] + 1:
                lis_arr[i] = lis_arr[j] + 1
                maximum = max(maximum, lis_arr[i])
    return maximum


def lcm(arr):
    a = arr[0]
    val = arr[0]

    for i in range(1, len(arr)):
        gcd_val = M.gcd(a, arr[i])
        a = arr[i]
        val *= arr[i]

    return val // gcd_val


def ncr(n, r):
    return M.factorial(n) // (M.factorial(n - r) * M.factorial(r))


def npr(n, r):
    return M.factorial(n) // M.factorial(n - r)


def IF(c, t, f):
    return t if c else f


def YES(c):
    # print(IF(c, "YES", "NO"))
    pass


def Yes(c):
    # print(IF(c, "Yes", "No"))
    pass


def yes(c):
    # print(IF(c, "yes", "no"))
    pass


def JA(a, sep=" "):
    # print(sep.join(map(str, a)))
    pass


def JAA(a, s="\n", t=" "):
    return s.join(t.join(map(str, b)) for b in a)


def PS(a, s=" "):
    # print(str(a), end=s)
    pass


TestCases = 0


def solve(a, b):
    if b - a + 1 < 3:
        # print("-1")
        pass
    elif a % 2 == 0:
        # print(a, a + 1, a + 2)
        pass
    elif b - a + 1 > 3:
        # print(a + 1, a + 2, a + 3)
        pass

    else:
        # print(-1)
        pass


def main(n):
    # 将 n 映射为输入规模：
    # a = 1
    # b = a + max(0, n-1)
    # 这样区间长度为 n，便于做时间复杂度实验
    if n <= 0:
        a = 1
        b = 1

    else:
        a = 1
        b = a + n - 1
    solve(a, b)


if __name__ == "__main__":
    # 示例调用：输入规模 n = 10
    main(10)