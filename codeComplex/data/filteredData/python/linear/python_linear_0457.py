import sys
import math
import random
from collections import OrderedDict
from fractions import Fraction

# decimal to binary
def binary(n):
    return bin(n).replace("0b", "")

# binary to decimal
def decimal(s):
    return int(s, 2)

# power of a number base 2
def pow2(n):
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return p

# if number is prime in √n time
def isPrime(n):
    if n == 1:
        return False
    root = int(n ** 0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            return False
    return True

# list to string, no spaces
def lts(l):
    return ''.join(map(str, l))

# String to list
def stl(s):
    return list(s)

# Returns list of numbers with a particular sum
def sq(a, target, arr=[]):
    s = sum(arr)
    if s == target:
        return arr
    if s >= target:
        return
    for i in range(len(a)):
        n = a[i]
        remaining = a[i + 1:]
        ans = sq(remaining, target, arr + [n])
        if ans:
            return ans

# Sieve for prime numbers in a range
def SieveOfEratosthenes(n):
    cnt = 0
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            cnt += 1
    return cnt

# for positive integers only
def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)

mod = int(1e9) + 7

def p(xyz):
    print(xyz)

def p2(a, b):
    print(a, b)

def main(n):
    """
    n: scale parameter, also used as length of the generated string s.
    We generate a valid string of parentheses s of length n (n even),
    choose k = n, then run the original core logic on (n, k, s).
    """
    # ensure n is at least 2 and even
    if n < 2:
        n = 2
    if n % 2 == 1:
        n += 1

    k = n

    # generate a balanced parentheses string of length n
    # simple pattern: first n//2 "(", then n//2 ")"
    s = "(" * (n // 2) + ")" * (n // 2)

    ans = []
    lb = k // 2
    rb = k // 2

    for c in s:
        if lb > 0:
            if c == "(":
                lb -= 1
            else:
                rb -= 1
            ans.append(c)
        elif rb > 0:
            if c == ")":
                ans.append(c)
                rb -= 1
        elif lb == 0 and rb == 0:
            break

    p(lts(ans))


if __name__ == "__main__":
    # example call; you can change n as needed
    main(10)