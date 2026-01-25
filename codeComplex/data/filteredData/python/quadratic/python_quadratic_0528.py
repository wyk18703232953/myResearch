import math as ma
import sys
from sys import exit
from decimal import Decimal as dec
from itertools import permutations


def li():
    return []


def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + m0
    return x


def num():
    return 0, 0


def nu():
    return 0


def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def main(n):
    if n <= 0:
        n = 1
    # Define grid size based on n
    rows = n
    cols = n

    # Deterministically generate the original grid a of size rows x cols
    # Pattern: a[i][j] is '#' if (i+j) % 3 == 0, else '.'
    a = [[('#' if (i + j) % 3 == 0 else '.') for j in range(cols)] for i in range(rows)]

    z = [["."] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if j - 1 >= 0 and j + 1 < cols and i + 1 < rows and i - 1 >= 0:
                if (
                    a[i - 1][j] == "#" and
                    a[i + 1][j] == "#" and
                    a[i][j - 1] == "#" and
                    a[i][j + 1] == "#" and
                    a[i - 1][j - 1] == "#" and
                    a[i - 1][j + 1] == "#" and
                    a[i + 1][j - 1] == "#" and
                    a[i + 1][j + 1] == "#"
                ):
                    z[i - 1][j] = "#"
                    z[i + 1][j] = "#"
                    z[i][j - 1] = "#"
                    z[i][j + 1] = "#"
                    z[i - 1][j - 1] = "#"
                    z[i - 1][j + 1] = "#"
                    z[i + 1][j - 1] = "#"
                    z[i + 1][j + 1] = "#"

    ff = True
    for i in range(rows):
        for j in range(cols):
            if z[i][j] != a[i][j]:
                ff = False
                break
        if not ff:
            break

    if ff:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main(5)