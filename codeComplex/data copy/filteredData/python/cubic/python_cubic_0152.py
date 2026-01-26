import io
import os
from functools import lru_cache
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 5)


def solve(N, A):
    valToLeftRight = defaultdict(lambda: defaultdict(set))
    valToRightLeft = defaultdict(lambda: defaultdict(set))

    for i, x in enumerate(A):
        valToLeftRight[x][i].add(i)
        valToRightLeft[x][i].add(i)

    maxVal = 1000 + 10
    for val in range(maxVal):
        for l, rights in valToLeftRight[val - 1].items():
            for r in rights:
                l2 = r + 1
                if l2 in valToLeftRight[val - 1]:
                    for r2 in valToLeftRight[val - 1][l2]:
                        assert l <= r
                        assert r + 1 == l2
                        assert l2 <= r2
                        valToLeftRight[val][l].add(r2)
                        valToRightLeft[val][r2].add(l)
                r2 = l - 1
                if r2 in valToRightLeft[val - 1]:
                    for l2 in valToRightLeft[val - 1][r2]:
                        assert l2 <= r2
                        assert r2 == l - 1
                        assert l <= r
                        valToLeftRight[val][l2].add(r)
                        valToRightLeft[val][r].add(l2)

    intervals = defaultdict(list)
    for val in range(maxVal):
        for l, rights in valToLeftRight[val].items():
            for r in rights:
                intervals[l].append(r)

    @lru_cache(maxsize=None)
    def getBest(left):
        if left == N:
            return 0
        best = float("inf")
        for right in intervals[left]:
            best = min(best, 1 + getBest(right + 1))
        return best

    return getBest(0)


def main(n):
    N = n
    A = [(i * 7) % 1001 for i in range(N)]
    ans = solve(N, A)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)