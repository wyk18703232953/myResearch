import math
import bisect
from collections import *


def main(n):
    # Interpret n as grid size; keep k1 fixed to preserve DP structure
    if n <= 0:
        return
    k1 = 20  # any even value in [1,20]; keeps transitions meaningful

    # Define grid dimensions based on n
    rows = n
    cols = n

    # Deterministic generation of arr (rows x (cols-1)) and brr ((rows-1) x cols)
    # Original code assumes:
    #   arr: n x m, used as horizontal edges: arr[i][j] is between (i,j) and (i,j+1)
    #   brr: (n-1) x m, used as vertical edges: brr[i][j] is between (i,j) and (i+1,j)
    # Here we keep the same roles but generate values deterministically.
    m = cols

    arr = [[(i + j + 1) for j in range(m)] for i in range(rows)]
    brr = [[(i * m + j + 1) for j in range(m)] for i in range(rows - 1)]

    # DP initialization: dp[rows][cols][21]
    dp = [[[0 for _ in range(21)] for _ in range(m)] for _ in range(rows)]

    for k in range(1, 21):
        for i in range(rows):
            for j in range(m):
                if k % 2:
                    dp[i][j][k] = -1

                else:
                    best = 10 ** 9
                    if i > 0:
                        best = min(best, dp[i - 1][j][k - 2] + brr[i - 1][j] * 2)
                    if i < rows - 1:
                        best = min(best, dp[i + 1][j][k - 2] + brr[i][j] * 2)
                    if j > 0:
                        best = min(best, dp[i][j - 1][k - 2] + arr[i][j - 1] * 2)
                    if j < m - 1:
                        best = min(best, dp[i][j + 1][k - 2] + arr[i][j] * 2)
                    dp[i][j][k] = best

    for i in range(rows):
        row_vals = []
        for j in range(m):
            row_vals.append(str(dp[i][j][k1]))
        # print(" ".join(row_vals))
        pass
if __name__ == "__main__":
    # Example: run with grid size n = 5
    main(5)