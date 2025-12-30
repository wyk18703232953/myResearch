import random
from collections import defaultdict


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
    # Note: max val formable is with A = [1000] * 500 which should be around 1000 + lg(500)
    maxVal = 1000 + 100
    for val in range(maxVal):
        for l, rights in valToLeftRight[val - 1].items():
            for r in rights:
                # Merge (l, r) with (l2, r2) with value (val - 1)
                l2 = r + 1
                if l2 in valToLeftRight[val - 1]:
                    for r2 in valToLeftRight[val - 1][l2]:
                        assert l <= r
                        assert r + 1 == l2
                        assert l2 <= r2
                        valToLeftRight[val][l].add(r2)
                        valToRightLeft[val][r2].add(l)
                # Merge (l2, r2) with (l, r) with value (val - 1)
                r2 = l - 1
                if r2 in valToRightLeft[val - 1]:
                    for l2 in valToRightLeft[val - 1][r2]:
                        assert l2 <= r2
                        assert r2 == l - 1
                        assert l <= r
                        valToLeftRight[val][l2].add(r)
                        valToRightLeft[val][r].add(l2)

    # Merge all left to right endpoints regardless of value formed
    intervals = defaultdict(list)
    for val in range(maxVal):
        for l, rights in valToLeftRight[val].items():
            for r in rights:
                intervals[l].append(r)

    # DP[i] returns most area you can cover in A[i:]
    dp = {}
    dp[N] = 0
    for left in range(N - 1, -1, -1):
        best = float("inf")
        for right in intervals[left]:
            # left to right inclusive is combined down to one character
            best = min(best, 1 + dp[right + 1])
        dp[left] = best

    return dp[0]


def main(n):
    # 生成规模为 n 的测试数据
    # A 中的元素范围与原题假设一致：1..1000
    random.seed(0)
    N = n
    A = [random.randint(1, 1000) for _ in range(N)]

    ans = solve(N, A)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)