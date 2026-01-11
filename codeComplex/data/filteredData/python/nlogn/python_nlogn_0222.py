import math, bisect
from collections import defaultdict, Counter, deque
from itertools import groupby, accumulate

def list2d(a, b, c):
    return [[c] * b for _ in range(a)]

def list3d(a, b, c, d):
    return [[[d] * c for _ in range(b)] for _ in range(a)]

def Y(c):
    # print(["NO", "YES"][c])
    pass

def y(c):
    # print(["no", "yes"][c])
    pass

def Yy(c):
    # print(["No", "Yes"][c])
    pass

def core_algorithm(n, U, A):
    Ans = -1
    for i in range(n - 2):
        x = A[i]
        y = x + U
        z = bisect.bisect_left(A, y, lo=i + 2, hi=n)
        if z == n:
            z -= 1
        if A[z] <= x + U:
            a = A[z]
        elif A[z - 1] <= x + U and z - 1 != i + 1:
            a = A[z - 1]

        else:
            continue
        if a != A[i]:  # avoid division by zero
            b = (a - A[i + 1]) / (a - A[i])
            Ans = max(Ans, b)
    return Ans

def main(n):
    if n < 3:
        # print(-1)
        pass
        return

    U = n // 2 + 1
    A = [i for i in range(1, n + 1)]
    result = core_algorithm(n, U, A)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)