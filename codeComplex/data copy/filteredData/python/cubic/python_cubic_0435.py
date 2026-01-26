def main(n):
    # Interpret n as grid size: n x n, with fixed even k
    if n <= 1:
        return
    m = n
    k = 10  # fixed even number of steps for experiment, can be adjusted

    # Deterministic construction of y_axis and x_axis
    # y_axis: n rows, m-1 edges per row (horizontal edges)
    # x_axis: n-1 rows, m edges per row (vertical edges)
    y_axis = [[(i + j) % 7 + 1 for j in range(m - 1)] for i in range(n)]
    x_axis = [[(i * 2 + j * 3) % 9 + 1 for j in range(m)] for i in range(n - 1)]

    if k % 2 == 1:
        for _ in range(n):
            # print(" ".join(["-1"] * m))
            pass
        return
    inf = 10 ** 9
    dp = [[[inf for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]

    # Initialize for z = 2
    for i in range(n):
        for j in range(m):
            # vertical moves
            if i > 0:
                if i < n - 1:
                    v1 = 2 * x_axis[i][j] if i < n - 1 else inf
                    v2 = 2 * x_axis[i - 1][j]
                    dp[i][j][2] = min(dp[i][j][2], v1, v2)

                else:
                    dp[i][j][2] = min(dp[i][j][2], 2 * x_axis[i - 1][j])

            else:
                if n > 1:
                    dp[i][j][2] = min(dp[i][j][2], 2 * x_axis[i][j])
            # horizontal moves
            if j > 0:
                if j < m - 1:
                    h1 = 2 * y_axis[i][j] if j < m - 1 else inf
                    h2 = 2 * y_axis[i][j - 1]
                    dp[i][j][2] = min(dp[i][j][2], h1, h2)

                else:
                    dp[i][j][2] = min(dp[i][j][2], 2 * y_axis[i][j - 1])

            else:
                if m > 1:
                    dp[i][j][2] = min(dp[i][j][2], 2 * y_axis[i][j])

    # DP transitions for larger even z
    for z in range(4, k + 1, 2):
        for i in range(n):
            for j in range(m):
                # vertical transitions
                if i > 0:
                    if i < n - 1:
                        up_cost = dp[i - 1][j][z - 2] + 2 * x_axis[i - 1][j]
                        down_cost = dp[i + 1][j][z - 2] + 2 * x_axis[i][j]
                        dp[i][j][z] = min(dp[i][j][z], up_cost, down_cost)

                    else:
                        up_cost = dp[i - 1][j][z - 2] + 2 * x_axis[i - 1][j]
                        dp[i][j][z] = min(dp[i][j][z], up_cost)

                else:
                    if n > 1:
                        down_cost = dp[i + 1][j][z - 2] + 2 * x_axis[i][j]
                        dp[i][j][z] = min(dp[i][j][z], down_cost)
                # horizontal transitions
                if j > 0:
                    if j < m - 1:
                        left_cost = dp[i][j - 1][z - 2] + 2 * y_axis[i][j - 1]
                        right_cost = dp[i][j + 1][z - 2] + 2 * y_axis[i][j]
                        dp[i][j][z] = min(dp[i][j][z], left_cost, right_cost)

                    else:
                        left_cost = dp[i][j - 1][z - 2] + 2 * y_axis[i][j - 1]
                        dp[i][j][z] = min(dp[i][j][z], left_cost)

                else:
                    if m > 1:
                        right_cost = dp[i][j + 1][z - 2] + 2 * y_axis[i][j]
                        dp[i][j][z] = min(dp[i][j][z], right_cost)

    # Output result for full k
    for i in range(n):
        row = []
        for j in range(m):
            if dp[i][j][k] == inf:
                row.append("-1")

            else:
                row.append(str(dp[i][j][k]))
        # print(" ".join(row))
        pass
if __name__ == "__main__":
    main(5)