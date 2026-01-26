from math import ceil, floor, gcd, log, log2, factorial
from collections import *

maxx = float('inf')


def compute_result(n, k, s):
    fl = 0
    l = None
    for i in range(1, n):
        x = s[i:n]
        for j in range(n):
            if x == s[:j + 1]:
                l = j + 1
                fl = 1
                break
        if fl:
            break
    if fl:
        ans = s + s[l:n] * (k - 1)
        return ans

    else:
        return s * k


def main(n):
    if n <= 0:
        return ""
    k = max(1, n // 3)
    base = "abca"
    s = (base * ((n + len(base) - 1) // len(base)))[:n]
    result = compute_result(n, k, s)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)