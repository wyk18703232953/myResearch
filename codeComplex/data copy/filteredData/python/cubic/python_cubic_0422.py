def solve(n, m, k, h, v):
    if k % 2:
        ans = "-1 " * m
        for _ in range(n):
            # print(ans)
            pass
        return

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    nxt = [[0] * (m + 1) for _ in range(n + 1)]

    for _ in range(2, k + 1, 2):
        for i in range(n):
            for j in range(m):
                l = 2 * h[i][j - 1] + dp[i][j - 1]
                r = 2 * h[i][j] + dp[i][j + 1]
                u = 2 * v[i - 1][j] + dp[i - 1][j]
                d = 2 * v[i][j] + dp[i + 1][j]

                hor = l if l < r else r
                ver = u if u < d else d
                nxt[i][j] = hor if hor < ver else ver

        dp, nxt = nxt, dp

    for row in dp[:-1]:
        # print(" ".join(map(str, row[:-1])))
        pass


def main(n):
    # Interpret n as base grid size; derive parameters deterministically
    # Ensure at least 1x1 grid and even k where meaningful
    if n < 1:
        n = 1

    # Grid dimensions
    rows = n
    cols = n

    # Step count k: proportional to n, ensure it's at least 2 and even
    k = (2 * n) if (2 * n) % 2 == 0 else (2 * n + 1)

    # Deterministic generation of h (n x (m+1)) and v ((n+1) x m effective)
    # h[i][j] = (i + 1) * (j + 2), last column is +inf
    h = [[(i + 1) * (j + 2) for j in range(cols)] + [float("+inf")] for i in range(rows)]

    # v[i][j] = (i + j + 3), last row is +inf
    v = [[i + j + 3 for j in range(cols)] for i in range(rows - 1)]
    v.append([float("+inf")] * cols)

    solve(rows, cols, k, h, v)


if __name__ == "__main__":
    main(5)