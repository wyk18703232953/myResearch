def main(n):
    # Interpret n as grid size parameter:
    # n = 2 => rows = 2, cols = 2, k = 2
    # In general, rows = max(1, n), cols = max(1, n), k = 2 * max(1, n//2)
    rows = max(1, n)
    cols = max(1, n)
    k = 2 * max(1, n // 2)

    # Core logic from original main, with deterministic data generation

    if k % 2 == 1:
        ans = [[-1] * cols for _ in range(rows)]
        for li in ans:
            # print(*li)
            pass
        return

    dp = [[float('inf')] * cols for _ in range(rows)]
    crr = []
    rrr = []

    # Generate horizontal edge costs: rows lists, each of length cols-1
    # Deterministic pattern: cost[i][j] = (i + 1) * (j + 2)
    for i in range(rows):
        arr = [(i + 1) * (j + 2) for j in range(cols - 1)] if cols > 1 else []
        for j in range(cols - 1):
            dp[i][j] = min(dp[i][j], arr[j])
            dp[i][j + 1] = min(dp[i][j + 1], arr[j])
        crr.append(arr)

    # Generate vertical edge costs: (rows-1) lists, each of length cols
    # Deterministic pattern: cost[i][j] = (i + 2) * (j + 1)
    for i in range(rows - 1):
        arr = [(i + 2) * (j + 1) for j in range(cols)]
        for j in range(cols):
            dp[i][j] = min(dp[i][j], arr[j])
            dp[i + 1][j] = min(dp[i + 1][j], arr[j])
        rrr.append(arr)

    # Dynamic programming iterations
    for _ in range(1, k // 2):
        ndp = [[float('inf')] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                x, y = i, j
                if x > 0:
                    ndp[i][j] = min(ndp[i][j], dp[x - 1][y] + rrr[x - 1][y])
                if x < rows - 1:
                    ndp[i][j] = min(ndp[i][j], dp[x + 1][y] + rrr[x][y])
                if y > 0:
                    ndp[i][j] = min(ndp[i][j], dp[x][y - 1] + crr[x][y - 1])
                if y < cols - 1:
                    ndp[i][j] = min(ndp[i][j], dp[x][y + 1] + crr[x][y])
        dp = ndp

    for li in dp:
        li = [2 * x for x in li]
        # print(*li)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(5)