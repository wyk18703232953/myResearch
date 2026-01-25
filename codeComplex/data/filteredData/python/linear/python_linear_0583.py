import sys
from math import *

MOD = 1000000007

def add(a, b):
    return (a + b) % MOD

def mul(a, b):
    return (a * b) % MOD

def sub(a, b):
    return (a - b + MOD) % MOD

def qpow(a, b):
    r = 1
    k = a
    for i in range(17):
        if b & (1 << i):
            r = mul(r, k)
        k = mul(k, k)
    return r

def main(n):
    # Interpret n as string length; let number of queries q = n
    length = n
    q = n

    # Deterministic generation of binary string a of length n
    # a[i] is '1' if i index has odd number of bits, else '0'
    a = ['1' if bin(i).count('1') % 2 == 1 else '0' for i in range(1, length + 1)]

    # Prefix sums of ones
    c = [0] * (length + 1)
    for i in range(length):
        c[i + 1] = c[i] + int(a[i])

    # Deterministic generation of queries
    # For i-th query, let l = (i % n) + 1, r = n - (i % n)
    # Ensure l <= r by swapping if needed
    queries = []
    for i in range(q):
        l = (i % length) + 1
        r = length - (i % length)
        if l > r:
            l, r = r, l
        queries.append((l, r))

    # Process queries with the original algorithm
    for l, r in queries:
        k = (r - l + 1)
        o = c[r] - c[l - 1]
        z = sub(qpow(2, o), 1)
        print(mul(z, qpow(2, k - o)))

if __name__ == "__main__":
    main(10)