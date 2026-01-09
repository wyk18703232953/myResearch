import math as ma
import sys
from sys import exit
from decimal import Decimal as dec
from itertools import permutations

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def main(n):
    # Generate deterministic input data based on n
    # a[i] = min(i, n//3)
    # b[i] = min(n-1-i, n//3)
    a = [min(i, n // 3) for i in range(n)]
    b = [min(n - 1 - i, n // 3) for i in range(n)]

    z = []
    for i in range(n):
        z.append((a[i] + b[i], i))
    z.sort()
    fl = True
    x = []
    cc = 0
    xp = 0
    mp = {}
    np_local = []

    for i in range(n):
        if a[i] > i:
            fl = False
        if b[i] > (n - i - 1):
            fl = False
        if (n - a[i] - b[i]) <= 0:
            fl = False

    if fl == False:
        # print("NO")
        pass

    else:
        zz = [0] * n
        for i in range(n):
            zz[i] = (n - a[i] - b[i])
        for i in range(n):
            xl = 0
            xr = 0
            for j in range(i + 1, n):
                if zz[j] > zz[i]:
                    xr += 1
            for j in range(i - 1, -1, -1):
                if zz[j] > zz[i]:
                    xl += 1
            if xl != a[i] or xr != b[i]:
                fl = False
                break
        if fl == True:
            # print("YES")
            pass
            # print(*zz)
            pass

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    main(10)