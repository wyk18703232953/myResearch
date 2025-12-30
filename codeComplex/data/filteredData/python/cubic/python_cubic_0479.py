import math
import random

M = 998244353
P = 1000000007
Inf = float('inf')


def solve(n, m, k, rt, do):
    """
    n, m: grid size
    k: number of steps (original k from problem)
    rt[i][j]: cost to go from (i, j) to (i, j+1), 0 <= i < n, 0 <= j < m-1
    do[i][j]: cost to go from (i, j) to (i+1, j), 0 <= i < n-1, 0 <= j < m
    """
    dp = [[0] * m for _ in range(n)]

    if k % 2 == 1:
        # print -1 grid
        for _ in range(n):
            print(*([-1] * m))
        return

    k //= 2
    for _ in range(k):
        dp_next = [[P] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans = Inf
                if i != 0:
                    ans = min(ans, dp[i - 1][j] + do[i - 1][j])
                if j != 0:
                    ans = min(ans, dp[i][j - 1] + rt[i][j - 1])
                if i != n - 1:
                    ans = min(ans, dp[i + 1][j] + do[i][j])
                if j != m - 1:
                    ans = min(ans, dp[i][j + 1] + rt[i][j])
                dp_next[i][j] = ans
        dp = dp_next

    for i in range(n):
        for j in range(m):
            print(2 * dp[i][j], end=' ')
        print()


def main(n):
    """
    n: problem scale, used here as n = m = n, and k derived from n.
    Generates random test data based on n and runs solve.
    """

    # Example generation strategy:
    #   grid size: n x n
    #   k: even number, e.g. min(2*n, 20) rounded to even
    m = n
    k = max(2, 2 * ((min(2 * n, 20) + 1) // 2))  # ensure even and not too large

    # generate rt (n x (m-1)) and do ((n-1) x m) with positive random costs
    rt = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    do = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    # run the original logic
    solve(n, m, k, rt, do)


if __name__ == "__main__":
    # example call
    main(4)