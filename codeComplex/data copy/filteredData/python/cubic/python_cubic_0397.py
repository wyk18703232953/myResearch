def main(n):
    # Interpret n as grid size; keep grid roughly square and k proportional to size
    if n <= 0:
        return
    rows = max(1, n // 2)
    cols = max(1, n - rows)
    k = max(1, n)  # ensure k >= 1

    # Generate deterministic edge weights
    lr = [[1 + (i * cols + j) % 9 for j in range(cols - 1)] for i in range(rows)]
    ud = [[1 + (i * cols + j * 2) % 9 for j in range(cols)] for i in range(rows - 1)]

    m = cols

    if k % 2:
        arr = [-1] * m
        for _ in range(rows):
            # print(*arr)
            pass
        return

    kk = k // 2
    INF = 10 ** 10
    dp = [[[INF] * (kk + 1) for _ in range(m)] for _ in range(rows)]
    for i in range(rows):
        for j in range(m):
            dp[i][j][0] = 0

    for z in range(1, kk + 1):
        for i in range(rows):
            for j in range(m):
                val = dp[i][j][z]
                if i > 0:
                    cost = dp[i - 1][j][z - 1] + ud[i - 1][j]
                    if cost < val:
                        val = cost
                if i < rows - 1:
                    cost = dp[i + 1][j][z - 1] + ud[i][j]
                    if cost < val:
                        val = cost
                if j > 0:
                    cost = dp[i][j - 1][z - 1] + lr[i][j - 1]
                    if cost < val:
                        val = cost
                if j < m - 1:
                    cost = dp[i][j + 1][z - 1] + lr[i][j]
                    if cost < val:
                        val = cost
                dp[i][j][z] = val

    ans = [[dp[i][j][kk] * 2 for j in range(m)] for i in range(rows)]
    for i in range(rows):
        # print(*ans[i])
        pass
if __name__ == "__main__":
    # example call for experimental runs
    main(10)