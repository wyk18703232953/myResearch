import sys, math, bisect
from collections import deque, defaultdict, Counter
import heapq, string

inf = float('inf')
mod = 998244353

def lcm(a, b):
    return int((a / math.gcd(a, b)) * b)

def gcd(a, b):
    return int(math.gcd(a, b))

def tobinary(n):
    return bin(n)[2:]

def binarySearch(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i

    else:
        return -1

def lowerBound(a, x):
    i = bisect.bisect_left(a, x)
    if i:
        return (i - 1)

    else:
        return -1

def upperBound(a, x):
    i = bisect.bisect_right(a, x)
    if i != len(a) + 1 and a[i - 1] == x:
        return (i - 1)

    else:
        return -1

def primesInRange(n):
    ans = []
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] is True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            ans.append(p)
    return ans

def primeFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors

def isPrime(n, k=5):
    if n < 2:
        return True
    # deterministic replacement for randint-based logic
    # use fixed bases modulo n (wrapped) for reproducibility
    for i in range(k):
        a = (i + 1) % (n - 1) + 1
        if pow(a, n - 1, n) != 1:
            return False
    return True

def main(n):
    # Deterministic generation of input:
    # Original program:
    # n = int(input())
    # s = input() (string of digits length n)
    # Here: length of s is n, digits pattern is (i % 10)
    length = n
    s_str = ''.join(str(i % 10) for i in range(length))

    s = [int(i) for i in s_str]
    for i in range(0, (9 * length) + 1):
        count = 0
        curr_sum = 0
        for j in s:
            curr_sum += j
            if curr_sum == i:
                count += 1
                curr_sum = 0
        if count > 1 and curr_sum == 0:
            # print('YES')
            pass
            return
    # print('NO')
    pass
if __name__ == "__main__":
    main(10)