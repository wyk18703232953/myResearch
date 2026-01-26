import sys
import math
from collections import OrderedDict
from fractions import Fraction

# sys.setrecursionlimit(300000)

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

def isPrime(n):
    if n == 1:
        return False
    root = int(n ** 0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            return False
    return True

def lts(l):
    return ''.join(map(str, l))

def stl(s):
    return list(s)

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

mod = int(1e9) + 7

def p(xyz):
    # print(xyz)
    pass

def p2(a, b):
    # print(a, b)
    pass

def main(n):
    # n controls the size: create two lists of length n each
    m = n
    x = [i for i in range(n)]
    y = [i // 2 for i in range(m)]
    # original core logic: print common elements in order of x
    # deterministic and depends only on n
    for c in x:
        if c in y:
            # print(c, end=" ")
            pass
    if n > 0:
        # print()
        pass
if __name__ == "__main__":
    main(10)