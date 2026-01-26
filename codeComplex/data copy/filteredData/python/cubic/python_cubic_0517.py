def main(n):
    # Map n to grid size and step count
    # Use n as base to define a square grid and even K
    if n < 2:
        n = 2
    m = n
    K = 2 * n  # even, scales with n

    # Deterministic generation of edgesh and edgesv based on indices
    edgesh = [[(i + j + 1) for j in range(m - 1)] for i in range(n)]
    edgesv = [[(i + j + 2) for j in range(m)] for i in range(n - 1)]

    INF = 10**10
    dp = [[[INF for _ in range(K + 1)] for _ in range(m)] for _ in range(n)]

    for k in range(0, K + 1, 2):
        for i in range(n):
            for j in range(m):
                if k == 0:
                    dp[i][j][k] = 0
                elif i == 0 and j == 0:
                    dp[i][j][k] = min(
                        2 * edgesh[i][j] + dp[i][j + 1][k - 2],
                        2 * edgesv[i][j] + dp[i + 1][j][k - 2],
                    )
                elif i == 0 and j == m - 1:
                    dp[i][j][k] = min(
                        2 * edgesh[i][j - 1] + dp[i][j - 1][k - 2],
                        2 * edgesv[i][j] + dp[i + 1][j][k - 2],
                    )
                elif i == 0:
                    dp[i][j][k] = min(
                        2 * edgesh[i][j] + dp[i][j + 1][k - 2],
                        2 * edgesv[i][j] + dp[i + 1][j][k - 2],
                        2 * edgesh[i][j - 1] + dp[i][j - 1][k - 2],
                    )
                elif j == 0 and i == n - 1:
                    dp[i][j][k] = min(
                        2 * edgesh[i][j] + dp[i][j + 1][k - 2],
                        2 * edgesv[i - 1][j] + dp[i - 1][j][k - 2],
                    )
                elif j == 0:
                    dp[i][j][k] = min(
                        2 * edgesh[i][j] + dp[i][j + 1][k - 2],
                        2 * edgesv[i - 1][j] + dp[i - 1][j][k - 2],
                        2 * edgesv[i][j] + dp[i + 1][j][k - 2],
                    )
                elif i == n - 1 and j == m - 1:
                    dp[i][j][k] = min(
                        2 * edgesh[i][j - 1] + dp[i][j - 1][k - 2],
                        2 * edgesv[i - 1][j] + dp[i - 1][j][k - 2],
                    )
                elif i == n - 1:
                    dp[i][j][k] = min(
                        2 * edgesh[i][j] + dp[i][j + 1][k - 2],
                        2 * edgesv[i - 1][j] + dp[i - 1][j][k - 2],
                        2 * edgesh[i][j - 1] + dp[i][j - 1][k - 2],
                    )
                elif j == m - 1:
                    dp[i][j][k] = min(
                        2 * edgesh[i][j - 1] + dp[i][j - 1][k - 2],
                        2 * edgesv[i - 1][j] + dp[i - 1][j][k - 2],
                        2 * edgesv[i][j] + dp[i + 1][j][k - 2],
                    )

                else:
                    dp[i][j][k] = min(
                        2 * edgesh[i][j] + dp[i][j + 1][k - 2],
                        2 * edgesv[i - 1][j] + dp[i - 1][j][k - 2],
                        2 * edgesv[i][j] + dp[i + 1][j][k - 2],
                        2 * edgesh[i][j - 1] + dp[i][j - 1][k - 2],
                    )

    for i in range(n):
        row = []
        for j in range(m):
            if dp[i][j][K] >= INF:
                row.append("-1")

            else:
                row.append(str(dp[i][j][K]))
        # print(" ".join(row))
        pass
if __name__ == "__main__":
    main(5)