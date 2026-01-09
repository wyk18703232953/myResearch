import sys
from functools import lru_cache
from collections import defaultdict

sys.setrecursionlimit(10 ** 5)


def solve_quadratic(N, A):
    # O(N^2) solution

    # val -> leftEndpoint -> rightEndpoints
    valToLeftRight = defaultdict(lambda: defaultdict(set))
    # val -> rightEndpoint -> leftEndpoints
    valToRightLeft = defaultdict(lambda: defaultdict(set))

    # Initialize with intervals of length 1 (left and right endpoints inclusive)
    for i, x in enumerate(A):
        valToLeftRight[x][i].add(i)
        valToRightLeft[x][i].add(i)

    # Go from smallest to largest values
    maxVal = 1000 + 10
    for val in range(maxVal):
        for l, rights in valToLeftRight[val - 1].items():
            for r in rights:
                # Merge all (l, r) with all (l2, r2) with value (val - 1)
                l2 = r + 1
                if l2 in valToLeftRight[val - 1]:
                    for r2 in valToLeftRight[val - 1][l2]:
                        valToLeftRight[val][l].add(r2)
                        valToRightLeft[val][r2].add(l)
                # Merge all (l2, r2) with all (l, r) with value (val - 1)
                r2 = l - 1
                if r2 in valToRightLeft[val - 1]:
                    for l2 in valToRightLeft[val - 1][r2]:
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


def tup(l, r):
    return l * 16384 + r


def untup(t):
    return divmod(t, 16384)


def solve_cubic(N, A):
    # Alternative solution O(N^3) DP
    cache = {}

    def f(lr):
        if lr not in cache:
            l, r = untup(lr)
            # l inclusive, r exclusive
            if r - l == 1:
                return tup(1, A[l])
            best = tup(float("inf"), float("inf"))
            for i in range(l + 1, r):
                lSplit = f(tup(l, i))
                rSplit = f(tup(i, r))
                lLen, lVal = untup(lSplit)
                rLen, rVal = untup(rSplit)
                if lLen != 1 or rLen != 1:
                    best = min(best, tup(lLen + rLen, 9999))

                else:
                    if lVal == rVal:
                        best = min(best, tup(1, lVal + 1))

                    else:
                        best = min(best, tup(2, 9999))
            cache[lr] = best

        return cache[lr]

    ans = untup(f(tup(0, N)))[0]
    return ans


def generate_input(n):
    # n is the array length N
    N = max(1, n)
    # Deterministic construction: values between 0 and 9, with some repetition pattern
    A = [(i ^ (i // 2)) % 10 for i in range(N)]
    return N, A


def main(n):
    N, A = generate_input(n)
    # You can choose which algorithm to time/compare here.
    # For example, run both and return one result to keep behaviour deterministic.
    ans1 = solve_quadratic(N, A)
    ans2 = solve_cubic(N, A)
    # Return one of them; they should match if algorithms are equivalent.
    return ans2


if __name__ == "__main__":
    # Example deterministic call for timing/experiments
    result = main(100)
    # print(result)
    pass