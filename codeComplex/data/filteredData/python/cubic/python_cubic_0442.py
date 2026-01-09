import math
import bisect
from collections import *

def main(n):
    # Map n to problem dimensions and steps
    if n < 2:
        n = 2
    rows = n
    cols = max(1, n // 2)
    k1 = min(10, n)

    m = cols

    # Deterministic generation of arr (rows x cols) and brr (rows-1 x cols)
    arr = [[(i * m + j) % 7 + 1 for j in range(m)] for i in range(rows)]
    brr = [[(i * m + j) % 5 + 1 for j in range(m)] for i in range(rows - 1)]

    dp = [[[0 for _ in range(11)] for _ in range(m)] for _ in range(rows)]

    for k in range(1, 11):
        for i in range(rows):
            for j in range(m):
                dp[i][j][k] = 10 ** 9
                if i > 0:
                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k - 1] + brr[i - 1][j] * 2)
                if i < rows - 1:
                    dp[i][j][k] = min(dp[i][j][k], dp[i + 1][j][k - 1] + brr[i][j] * 2)
                if j > 0:
                    dp[i][j][k] = min(dp[i][j][k], dp[i][j - 1][k - 1] + arr[i][j - 1] * 2)
                if j < m - 1:
                    dp[i][j][k] = min(dp[i][j][k], dp[i][j + 1][k - 1] + arr[i][j] * 2)

    for i in range(rows):
        line = []
        for j in range(m):
            if k1 % 2:
                line.append("-1")

            else:
                line.append(str(dp[i][j][k1 // 2]))
        # print(" ".join(line))
        pass
if __name__ == "__main__":
    # Example call for time-complexity experiments
    main(10)