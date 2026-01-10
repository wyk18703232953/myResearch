import re
from bisect import bisect_left as bsl, bisect_right as bsr
from collections import Counter, defaultdict as ddict, deque
from functools import lru_cache
from heapq import *
from itertools import *
from math import inf
from pprint import pprint as pp

cache = lru_cache(None)
enum = enumerate
cat = ''.join
catn = '\n'.join
mod = 1000000007
d4 = [(0, -1), (1, 0), (0, 1), (-1, 0)]
d8 = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def main(n):
    # Scale: n = number of segments; t = n as well (deterministic mapping)
    if n <= 0:
        print(0)
        return

    t = n
    a = []

    # Deterministic generation of (x, m)
    # Example pattern: x = i, m = (i % 5) + 1
    for i in range(n):
        x = i
        m = (i % 5) + 1
        a.append((x - m / 2, m))

    a.sort()
    ans = 2
    for i in range(n - 1):
        x_val = a[i][0] + a[i][1] + t
        y_val = a[i + 1][0]
        ans += (x_val <= y_val) + (x_val < y_val)
    print(ans)


if __name__ == "__main__":
    main(10)