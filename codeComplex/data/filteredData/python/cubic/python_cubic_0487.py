def main(n):
    # Map n to grid dimensions and k (path length parameter)
    # Here we choose:
    #   rows = n
    #   cols = max(1, n)
    #   k = 2 * max(1, n // 2)  (ensure k is even and >= 2)
    rows = n
    cols = max(1, n)
    k = 2 * max(1, n // 2)

    kk = k
    # Initialize maps: [rows][cols][4]
    maps = [[[0 for _ in range(4)] for _ in range(cols)] for _ in range(rows)]
    # dp: [rows][cols][k//2 + 1]
    INF = 10**18
    dp = [[[INF for _ in range(k // 2 + 1)] for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            dp[i][j][0] = 0

    # Deterministic generation of horizontal edge weights
    # For each row i, for each edge (j -> j+1), assign a weight
    # weight = 1 + (i + j) % 7
    for i in range(rows):
        for j in range(cols - 1):
            w = 1 + (i + j) % 7
            maps[i][j][0] = w       # right
            maps[i][j + 1][1] = w   # left

    # Deterministic generation of vertical edge weights
    # For each column j, for each edge (i -> i+1), assign a weight
    # weight = 1 + (i * 3 + j) % 9
    for i in range(rows - 1):
        for j in range(cols):
            w = 1 + (i * 3 + j) % 9
            maps[i][j][2] = w       # down
            maps[i + 1][j][3] = w   # up

    # If k is odd, original program prints -1 grid
    if k % 2 == 1:
        for i in range(rows):
            for j in range(cols):
                # print(-1, end=" ")
                pass
            # print()
            pass
        return

    # DP transitions
    for step in range(1, kk // 2 + 1):
        for i in range(rows):
            for j in range(cols):
                cur = dp[i][j][step - 1]
                if cur == INF:
                    continue
                if j < cols - 1:
                    val = cur + maps[i][j][0]
                    if val < dp[i][j + 1][step]:
                        dp[i][j + 1][step] = val
                if i < rows - 1:
                    val = cur + maps[i][j][2]
                    if val < dp[i + 1][j][step]:
                        dp[i + 1][j][step] = val
                if i > 0:
                    val = cur + maps[i][j][3]
                    if val < dp[i - 1][j][step]:
                        dp[i - 1][j][step] = val
                if j > 0:
                    val = cur + maps[i][j][1]
                    if val < dp[i][j - 1][step]:
                        dp[i][j - 1][step] = val

    # Output
    for i in range(rows):
        for j in range(cols):
            ans = dp[i][j][kk // 2]
            if ans >= INF:
                # print(-1, end=" ")
                pass

            else:
                # print(ans * 2, end=" ")
                pass
        # print()
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)