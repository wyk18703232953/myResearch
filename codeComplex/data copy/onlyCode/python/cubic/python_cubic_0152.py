import io
import os

import sys
from functools import lru_cache
from collections import defaultdict

sys.setrecursionlimit(10 ** 5)


def solve(N, A):
    # Compute all intervals that merge down to a single value
    # val -> leftEndpoint -> rightEndpoints
    valToLeftRight = defaultdict(lambda: defaultdict(set))
    # val -> rightEndpoint -> leftEndpoints
    valToRightLeft = defaultdict(lambda: defaultdict(set))

    # Initialize with intervals of length 1 (left and right endpoints inclusive)
    for i, x in enumerate(A):
        valToLeftRight[x][i].add(i)
        valToRightLeft[x][i].add(i)

    # Go from smallest to largest values
    # Note: max val is created with 1000 repeated 500 times which should be around 1000 + lg(500)
    maxVal = 1000 + 10
    for val in range(maxVal):
        for l, rights in valToLeftRight[val - 1].items():
            for r in rights:
                # Merge all (l, r) with all (l2, r2) with value (val - 1)
                l2 = r + 1
                if l2 in valToLeftRight[val - 1]:
                    for r2 in valToLeftRight[val - 1][l2]:
                        assert l <= r
                        assert r + 1 == l2
                        assert l2 <= r2
                        valToLeftRight[val][l].add(r2)
                        valToRightLeft[val][r2].add(l)
                # Merge all (l2, r2) with all (l, r) with value (val - 1)
                r2 = l - 1
                if r2 in valToRightLeft[val - 1]:
                    for l2 in valToRightLeft[val - 1][r2]:
                        assert l2 <= r2
                        assert r2 == l - 1
                        assert l <= r
                        valToLeftRight[val][l2].add(r)
                        valToRightLeft[val][r].add(l2)

    # Get all intervals regardless of the value it forms
    intervals = defaultdict(list)
    for val in range(maxVal):
        for l, rights in valToLeftRight[val].items():
            for r in rights:
                # print(A[l : r + 1], l, r, val)
                intervals[l].append(r)

    @lru_cache(maxsize=None)
    def getBest(left):
        # Returns number of nonoverlapping intervals completely covering A[left:]
        if left == N:
            return 0
        best = float("inf")
        for right in intervals[left]:
            # A[left:right+1] is covered by 1 interval, get best of A[right + 1:]
            best = min(best, 1 + getBest(right + 1))
        return best

    return getBest(0)


if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    N, = list(map(int, input().split()))
    A = list(map(int, input().split()))
    ans = solve(N, A)
    print(ans)
