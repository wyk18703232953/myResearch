def main(n):
    # Interpret n as both grid dimension and step parameter for scalability
    # Grid: n x n, k = 2 * n (so k is even and scales with n)
    row = n
    col = n
    k = 2 * n

    # Deterministic construction of edge weights:
    # right[i][j] defined for 0 <= i < n, 0 <= j < n-1
    # down[i][j] defined for 0 <= i < n-1, 0 <= j < n
    right = [[(i + j + 1) for j in range(col - 1)] for i in range(row)]
    down = [[(i + j + 2) for j in range(col)] for i in range(row - 1)]

    if k % 2 == 1:
        for i in range(row):
            for j in range(col):
                # print("-1", end=" ")
                pass
            # print()
            pass
        return

    else:
        k = k // 2
        dp = [[[9999999 for _ in range(col)] for _ in range(row)] for _ in range(k + 1)]
        for steps in range(k + 1):
            for i in range(row):
                for j in range(col):
                    if steps == 0:
                        dp[steps][i][j] = 0
                        continue
                    ans = 99999999999
                    if i > 0:
                        ans = min(ans, dp[steps - 1][i - 1][j] + down[i - 1][j])
                    if i < row - 1:
                        ans = min(ans, dp[steps - 1][i + 1][j] + down[i][j])
                    if j < col - 1:
                        ans = min(ans, dp[steps - 1][i][j + 1] + right[i][j])
                    if j > 0:
                        ans = min(ans, dp[steps - 1][i][j - 1] + right[i][j - 1])
                    dp[steps][i][j] = ans

        for i in range(row):
            for j in range(col):
                # print(2 * dp[k][i][j], end=" ")
                pass
            # print()
            pass
if __name__ == "__main__":
    main(5)