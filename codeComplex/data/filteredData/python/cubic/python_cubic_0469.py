import math
from collections import defaultdict as dd

mod = 1000000007

def main(n):
    # Interpret n as grid size: n x n, and k = 2 * n (even and scales with n)
    if n <= 0:
        return
    m = n
    k = 2 * n

    # Generate deterministic horizontal and vertical edge weights
    # h: n rows, m-1 columns
    h = []
    for i in range(n):
        row = [(i * m + j) % 9 + 1 for j in range(m - 1)]
        h.append(row)
    # v: n-1 rows, m columns
    v = []
    for i in range(n - 1):
        row = [((i + 1) * m + j * 2) % 9 + 1 for j in range(m)]
        v.append(row)

    # Initialize dp array: dp[i][j][l] = minimal cost from (i,j) in exactly l steps
    max_l = k // 2
    dp = [[[0 for _ in range(max_l + 1)] for _ in range(m)] for _ in range(n)]

    for l in range(1, max_l + 1):
        for i in range(n):
            for j in range(m):
                best = float("inf")
                if j - 1 >= 0:
                    cost = dp[i][j - 1][l - 1] + h[i][j - 1]
                    if cost < best:
                        best = cost
                if i - 1 >= 0:
                    cost = dp[i - 1][j][l - 1] + v[i - 1][j]
                    if cost < best:
                        best = cost
                if j + 1 < m:
                    cost = dp[i][j + 1][l - 1] + h[i][j]
                    if cost < best:
                        best = cost
                if i + 1 < n:
                    cost = dp[i + 1][j][l - 1] + v[i][j]
                    if cost < best:
                        best = cost
                dp[i][j][l] = best

    # Print result matrix: minimal cost to return in exactly k steps = 2 * dp[i][j][k//2]
    for i in range(n):
        row_vals = []
        for j in range(m):
            row_vals.append(str(2 * dp[i][j][max_l]))
        # print(" ".join(row_vals))
        pass
if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(5)