import io
import os
from collections import Counter, defaultdict, deque

DEBUG = False


def bisect_f(f, lo, hi):
    if DEBUG:
        assert f(lo) and not f(hi)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if f(mid):
            lo = mid
        else:
            hi = mid
        if DEBUG:
            assert f(lo) and not f(hi)
    if DEBUG:
        assert hi - lo == 1
        assert f(lo) and not f(hi)
    return lo


def solve(N, M, arrs):
    def isPossible(target):
        possible = set()
        for arr in arrs:
            mask = 0
            for pos, x in enumerate(arr):
                if x >= target:
                    mask += 1 << pos
            possible.add(mask)
        allMask = (1 << M) - 1
        for mask1 in possible:
            for mask2 in possible:
                if mask1 | mask2 == allMask:
                    return (mask1 << 8) + mask2
        return 0

    lo = min(arrs[0])
    hi = 10 ** 9 + 1
    index = bisect_f(isPossible, lo, hi)

    mask1, mask2 = divmod(isPossible(index), 1 << 8)
    ans = [-1, -1]
    for i, arr in enumerate(arrs):
        mask = 0
        for pos, x in enumerate(arr):
            if x >= index:
                mask += 1 << pos
        if mask == mask1:
            ans[0] = str(i + 1)
        if mask == mask2:
            ans[1] = str(i + 1)
    return " ".join(ans)


def generate_data(n):
    # Map n to N (number of rows) and M (number of columns)
    if n < 2:
        N = 2
    else:
        N = n
    M = 8
    arrs = []
    for i in range(N):
        base = i + 1
        row = []
        for j in range(M):
            val = (base * (j + 1)) % 1000 + (j // 2)
            row.append(val)
        arrs.append(row)
    return N, M, arrs


def main(n):
    N, M, arrs = generate_data(n)
    ans = solve(N, M, arrs)
    print(ans)


if __name__ == "__main__":
    main(10)