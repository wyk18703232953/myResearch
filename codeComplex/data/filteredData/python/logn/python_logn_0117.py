import math
import string
from functools import reduce

def solve(L, R):
    if L == R:
        return 0
    l = len(bin(L)[2:])
    r = len(bin(R)[2:])
    while l == r:
        L -= pow(2, r - 1)
        R -= pow(2, r - 1)
        l = len(bin(L)[2:])
        r = len(bin(R)[2:])
    return pow(2, r) - 1

def main(n):
    if n < 2:
        n = 2
    # Deterministically generate L and R based on n
    # Ensure 0 <= L <= R and R grows with n
    L = n // 3
    R = n
    if L > R:
        L, R = R, L
    ans = solve(L, R)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)