import os
import sys
from math import *
from collections import *
from bisect import *
from io import BytesIO, IOBase

ALPHA = 'abcdefghijklmnopqrstuvwxyz'
M = 998244353
EPS = 1e-6

def ok(a, b, c):
    n = a[0][-1]
    ans = []
    for _ in range(a[0][0]):
        ans.append([a[1]] * n)

    l = n
    r = n - a[0][0]

    for i in range(2):
        for j in range(2):
            l1, r1 = b[0]
            l2, r2 = c[0]

            if i:
                l1, r1 = r1, l1
            if j:
                l2, r2 = r2, l2

            if l1 == l:
                if l2 != l or r1 + r2 != r:
                    continue
                for _ in range(r1):
                    ans.append([b[1]] * n)
                for _ in range(r2):
                    ans.append([c[1]] * n)
                return ans

            if l1 == r:
                if l2 != r or r1 + r2 != l:
                    continue
                for _ in range(r):
                    ans.append([b[1]] * r1 + [c[1]] * r2)
                return ans

    return False

def main(n):
    # Deterministic generation of six integers from n
    # Ensure positive sizes and some variability
    l1 = max(1, n)
    r1 = max(1, 2 * n)
    l2 = max(1, (n // 2) + 1)
    r2 = max(1, (3 * n) // 2 + 1)
    l3 = max(1, (n // 3) + 1)
    r3 = max(1, n + (n // 3) + 1)

    a = [sorted((l1, r1)), 'A']
    b = [sorted((l2, r2)), 'B']
    c = [sorted((l3, r3)), 'C']

    A = ok(a, b, c)
    B = ok(b, a, c)
    C = ok(c, a, b)

    if A:
        print(len(A))
        for row in A:
            print(*row, sep="")
    elif B:
        print(len(B))
        for row in B:
            print(*row, sep="")
    elif C:
        print(len(C))
        for row in C:
            print(*row, sep="")
    else:
        print(-1)

if __name__ == "__main__":
    main(5)