import math as ma
import sys
from sys import exit
from decimal import Decimal as dec
from itertools import permutations

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def generate_data(n):
    # Deterministically generate arrays a and b of length n
    # Make them mostly valid but not guaranteed, just structured
    a = [i % (i + 1) for i in range(n)]
    b = [(n - i - 1) % (n - i if n - i > 0 else 1) for i in range(n)]
    return a, b

def core_logic(n, a, b):
    z = []
    for i in range(n):
        z.append((a[i] + b[i], i))
    z.sort()
    fl = True
    x = []
    cc = 0
    xp = 0
    mp = {}
    np_list = []
    for i in range(n):
        if a[i] > i:
            fl = False
        if b[i] > (n - i - 1):
            fl = False
        if (n - a[i] - b[i]) <= 0:
            fl = False

    if fl == False:
        return "NO", None

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
            return "YES", zz

        else:
            return "NO", None

def main(n):
    a, b = generate_data(n)
    res, zz = core_logic(n, a, b)
    if res == "NO":
        # print("NO")
        pass

    else:
        # print("YES")
        pass
        # print(*zz)
        pass
if __name__ == "__main__":
    # Example deterministic runs for different scales
    main(5)
    main(10)