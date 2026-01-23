from math import floor, gcd, fabs, factorial, fmod, sqrt, inf, log
from collections import defaultdict as dd, deque
from heapq import merge, heapify, heappop, heappush, nsmallest
from bisect import bisect_left as bl, bisect_right as br, bisect

mod = pow(10, 9) + 7
mod2 = 998244353


def core(a, b):
    c = 0
    x = 0
    while not (c >= b and c - b + x == a):
        x += 1
        c += x
    return a - x


def main(n):
    # 将 n 映射为一组 (a, b)，规模由 n 控制
    # 这里令 b = n，a = n*(n+1)//2 的一半偏移，以保证有解且随 n 增长
    if n <= 0:
        a, b = 0, 0
    else:
        b = n
        s = n * (n + 1) // 2
        a = (s // 2) + (n // 3)
    result = core(a, b)
    print(result)


if __name__ == "__main__":
    main(1000)