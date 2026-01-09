def main(n):
    # Map n to problem dimensions and k
    # n controls both grid size and k to keep scaling simple and cubic-ish:
    # let rows = n, cols = n, k = 2 * n (ensuring k is even and grows with n)
    rows = n
    cols = n
    k = 2 * n

    # Deterministic construction of edge weights
    # ej: horizontal edges, size rows x cols, last column unused by algorithm
    # ei: vertical edges, size (rows-1) x cols
    ej = [[(i + j + 1) for j in range(cols)] for i in range(rows)]
    if rows > 1:
        ei = [[(i + j + 2) for j in range(cols)] for i in range(rows - 1)]

    else:
        ei = []

    if k % 2:
        for _ in range(rows):
            # print(*([-1] * cols))
            pass
        return

    inf = -1
    total_cells = rows * cols
    half_k = k // 2
    dp = [[inf] * total_cells for _ in range(half_k + 1)]
    for t in range(total_cells):
        dp[0][t] = 0

    for c in range(half_k):
        for i in range(rows):
            for j in range(cols):
                t = i * cols + j

                # move down
                tt = (i + 1) * cols + j
                if i + 1 < rows:
                    cost = dp[c][t] + ei[i][j]
                    if dp[c + 1][tt] == -1 or dp[c + 1][tt] > cost:
                        dp[c + 1][tt] = cost

                # move right
                tt = i * cols + j + 1
                if j + 1 < cols:
                    cost = dp[c][t] + ej[i][j]
                    if dp[c + 1][tt] == -1 or dp[c + 1][tt] > cost:
                        dp[c + 1][tt] = cost

                # move up
                tt = (i - 1) * cols + j
                if i - 1 >= 0:
                    cost = dp[c][t] + ei[i - 1][j]
                    if dp[c + 1][tt] == -1 or dp[c + 1][tt] > cost:
                        dp[c + 1][tt] = cost

                # move left
                tt = i * cols + j - 1
                if j - 1 >= 0:
                    cost = dp[c][t] + ej[i][j - 1]
                    if dp[c + 1][tt] == -1 or dp[c + 1][tt] > cost:
                        dp[c + 1][tt] = cost

    res = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            res[i][j] = dp[-1][i * cols + j] * 2
        # print(*res[i])
        pass
if __name__ == "__main__":
    main(5)