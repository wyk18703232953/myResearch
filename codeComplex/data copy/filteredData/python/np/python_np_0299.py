import sys
from math import gcd, ceil

def prod(a, mod=10**9+7):
    ans = 1
    for each in a:
        ans = (ans * each) % mod
    return ans

def lcm(a, b):
    return a * b // gcd(a, b)

def binary(x, length=16):
    y = bin(x)[2:]
    return y if len(y) >= length else "0" * (length - len(y)) + y

def main(n):
    if n <= 0:
        print(0)
        return
    MAX_A = 10**5
    size = min(max(1, n), MAX_A)
    # deterministic construction of a[0..size-1] within [1, MAX_A]
    a = [i % MAX_A + 1 for i in range(size)]

    mod = 10**9 + 7
    twosz = MAX_A + 69
    twopow = [1] * twosz
    for i in range(1, twosz):
        twopow[i] = (twopow[i - 1] * 2) % mod
    count = [0] * (MAX_A + 69)
    for v in a:
        if 1 <= v <= MAX_A:
            count[v] += 1
    multiples = [0] * (MAX_A + 69)
    for i in range(1, MAX_A + 1):
        s = 0
        for j in range(i, MAX_A + 1, i):
            s += count[j]
        multiples[i] = s
    gcd_of = [0] * (MAX_A + 69)
    for i in range(MAX_A, 0, -1):
        val = (twopow[multiples[i]] - 1) % mod
        j = 2 * i
        while j <= MAX_A:
            val -= gcd_of[j]
            j += i
        gcd_of[i] = val
    print(gcd_of[1] % mod)

if __name__ == "__main__":
    main(10000)