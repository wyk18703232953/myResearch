import math, sys, bisect, heapq, os
from collections import defaultdict, Counter, deque
from itertools import groupby, accumulate
from functools import lru_cache

pr = lambda x: x


def list3d(a, b, c, d):
    return [[[d] * c for j in range(b)] for i in range(a)]


def Y(c):
    print(["NO", "YES"][c])


def y(c):
    print(["no", "yes"][c])


def Yy(c):
    print(["No", "Yes"][c])


def solve(n):
    # Deterministic generation of A based on n
    # Original input structure:
    # n
    # A[0..n-1]
    # Here we set A[i] = i % max(1, n//3 + 1) + i//2 to create some duplicates and variety
    if n <= 0:
        return
    base = max(1, n // 3 + 1)
    A = [(i % base) + (i // 2) for i in range(n)]

    if A.count(0) >= 2:
        print('cslnb')
    elif n == 1:
        if A[0] % 2:
            print('sjfnb')
        else:
            print('cslnb')
    else:
        g2 = 0
        flag = 1
        C = Counter(A)
        for i in C.keys():
            if C[i] >= 3:
                flag = 0
            if C[i] == 2 and C[i - 1] >= 1:
                flag = 0
            if C[i] == 2:
                g2 += 1
        if g2 >= 2:
            flag = 0
        if not flag:
            print('cslnb')
        else:
            movescount = 0
            A.sort()
            for ii, i in enumerate(A):
                movescount += i - ii
            if movescount % 2 == 0:
                print('cslnb')
            else:
                print('sjfnb')


def main(n):
    solve(n)


if __name__ == "__main__":
    main(10)