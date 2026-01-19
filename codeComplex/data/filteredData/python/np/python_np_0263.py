from decimal import *

def main(n):
    # generate a deterministic n x n matrix of floats in (0,1)
    # ensure n does not exceed 18 because of 1<<18 dp array size
    if n <= 0:
        return
    if n > 18:
        n = 18

    ar = [[(i + j + 1) / (n + 1) for j in range(n)] for i in range(n)]

    dp = [[0.0 for _ in range(1 << 18)] for _ in range(18)]
    ans = 0.0
    dp[0][(1 << n) - 1] = 1.0

    for i in range((1 << n) - 1, 0, -1):
        for j in range(n):
            if i & (1 << j) == 0:
                continue
            for k in range(n):
                if i & (1 << k) != 0 or j == k:
                    continue
                dp[j][i] = max(
                    dp[j][i],
                    dp[k][i ^ (1 << k)] * ar[k][j] + dp[j][i ^ (1 << k)] * ar[j][k]
                )

    for i in range(n):
        ans = max(ans, dp[i][1 << i])

    print("{:.6f}".format(ans))


if __name__ == "__main__":
    main(4)