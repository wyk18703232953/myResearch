import math, sys, bisect, heapq
from collections import defaultdict, Counter, deque
from itertools import groupby, accumulate
from functools import lru_cache

def list2d(a, b, c):
    return [[c] * b for _ in range(a)]

def list3d(a, b, c, d):
    return [[[d] * c for _ in range(b)] for _ in range(a)]

def Y(c):
    print(["NO", "YES"][c])

def y(c):
    print(["no", "yes"][c])

def Yy(c):
    print(["No", "Yes"][c])

def main(n):
    # Interpret n as the size of array A
    if n <= 0:
        print(0)
        return

    # Deterministic generation of parameters and array
    l = n
    r = 3 * n
    x = max(1, n // 3)

    A = [i + 1 for i in range(n)]
    A.sort()

    @lru_cache(None)
    def fun(pos=0, sm=-1, la=-1, tot=0):
        if pos == n:
            if tot >= l and tot <= r and la > 0 and (la - sm) >= x:
                return 1
            return 0
        if sm == -1:
            return fun(pos + 1, A[pos], -1, A[pos]) + fun(pos + 1, sm, la, tot)
        elif la == -1:
            return fun(pos + 1, sm, A[pos], tot + A[pos]) + fun(pos + 1, sm, la, tot)
        else:
            return fun(pos + 1, sm, A[pos], tot + A[pos]) + fun(pos + 1, sm, la, tot)

    print(fun())

if __name__ == "__main__":
    main(10)