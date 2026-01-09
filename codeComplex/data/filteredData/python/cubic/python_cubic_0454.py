def main(n):
    # Map n to grid size and k (even)
    # Ensure at least 1x1 grid and k >= 2
    if n < 2:
        m = 1
        rows = 1
        k = 2

    else:
        rows = n
        m = n
        # choose an even k proportional to n, at least 2
        k = 2 * ((n // 2) or 1)

    # Deterministic generation of edge weights
    horizontal_edges = []
    for i in range(rows):
        row = []
        for j in range(m - 1):
            # simple deterministic weight depending on position
            row.append((i + 1) + (j + 1))
        horizontal_edges.append(row)

    vertical_edges = []
    for i in range(rows - 1):
        row = []
        for j in range(m):
            row.append((i + 1) * (j + 1))
        vertical_edges.append(row)

    # Handle odd k (though we always generate even k, keep logic)
    if k % 2 == 1:
        for i in range(rows):
            for j in range(m):
                # print(-1, end=' ')
                pass
            # print()
            pass
        return

    INF = 10 ** 9
    dp = [[[INF for _ in range(k + 1)] for _ in range(m)] for _ in range(rows)]

    for i in range(rows):
        for j in range(m):
            dp[i][j][0] = 0

    for z in range(2, k + 1, 2):
        for i in range(rows):
            for j in range(m):
                # vertical moves
                if i > 0:
                    if i < rows - 1:
                        dp[i][j][z] = min(
                            dp[i - 1][j][z - 2] + 2 * vertical_edges[i - 1][j],
                            dp[i + 1][j][z - 2] + 2 * vertical_edges[i][j],
                        )

                    else:
                        dp[i][j][z] = dp[i - 1][j][z - 2] + 2 * vertical_edges[i - 1][j]

                else:
                    if rows > 1:
                        dp[i][j][z] = dp[i + 1][j][z - 2] + 2 * vertical_edges[i][j]

                # horizontal moves
                if j > 0:
                    if j < m - 1:
                        dp[i][j][z] = min(
                            dp[i][j][z],
                            dp[i][j - 1][z - 2] + 2 * horizontal_edges[i][j - 1],
                            dp[i][j + 1][z - 2] + 2 * horizontal_edges[i][j],
                        )

                    else:
                        dp[i][j][z] = min(
                            dp[i][j][z],
                            dp[i][j - 1][z - 2] + 2 * horizontal_edges[i][j - 1],
                        )

                else:
                    if m > 1:
                        dp[i][j][z] = min(
                            dp[i][j][z],
                            dp[i][j + 1][z - 2] + 2 * horizontal_edges[i][j],
                        )

    for i in range(rows):
        for j in range(m):
            # print(dp[i][j][k], end=' ')
            pass
        # print()
        pass
if __name__ == "__main__":
    # Example deterministic call
    main(5)