import os
from math import inf

def main(n):
    a = [0] + [i % 5 for i in range(1, n + 1)]
    dp = [[[-1, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i][0], dp[i][i][1] = a[i], 1
    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n + 1):
            for k in range(j - i):
                left, right = dp[i][i + k], dp[i + k + 1][j]
                if left[1] and right[1] and left[0] == right[0]:
                    dp[i][j][0], dp[i][j][1] = left[0] + 1, 1
                    break
    val = [0, 0] + [inf] * n
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][j][1]:
                val[j + 1] = min(val[j + 1], val[i] + 1)
    result = val[-1]
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)