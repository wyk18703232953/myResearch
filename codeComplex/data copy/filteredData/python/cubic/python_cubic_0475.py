def main(n):
    # Interpret n as grid size: use n x n grid and k = 2 * n (even, proportional to size)
    rows = n
    cols = n
    k = 2 * n

    # Deterministic generation of lr (horizontal edge costs) and ud (vertical edge costs)
    # lr: rows x (cols-1)
    lr = [[(i + j + 1) % 7 + 1 for j in range(cols - 1)] for i in range(rows)]
    # ud: (rows-1) x cols
    ud = [[(i * cols + j + 3) % 9 + 1 for j in range(cols)] for i in range(rows - 1)]

    if k % 2:
        arr = [-1] * cols
        for _ in range(rows):
            # print(*arr)
            pass
        return

    kk = k // 2
    INF = 10 ** 10

    dp = [[[INF] * (kk + 1) for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            dp[i][j][0] = 0

    for z in range(1, kk + 1):
        for i in range(rows):
            for j in range(cols):
                cur = dp[i][j][z]
                if i > 0:
                    v = dp[i - 1][j][z - 1] + ud[i - 1][j]
                    if v < cur:
                        cur = v
                if i < rows - 1:
                    v = dp[i + 1][j][z - 1] + ud[i][j]
                    if v < cur:
                        cur = v
                if j > 0:
                    v = dp[i][j - 1][z - 1] + lr[i][j - 1]
                    if v < cur:
                        cur = v
                if j < cols - 1:
                    v = dp[i][j + 1][z - 1] + lr[i][j]
                    if v < cur:
                        cur = v
                dp[i][j][z] = cur

    ans = [[dp[i][j][kk] * 2 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        # print(*ans[i])
        pass
if __name__ == "__main__":
    main(5)