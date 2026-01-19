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


if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    N, M = [int(x) for x in input().split()]
    arrs = [[int(x) for x in input().split()] for i in range(N)]
    ans = solve(N, M, arrs)
    print(ans)
