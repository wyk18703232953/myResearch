def main(n):
    # n controls the size of each color array; original code expects three integers
    # Here we set n[0] = n[1] = n[2] = n
    n_list = [n, n, n]

    # Deterministically generate three arrays u[0], u[1], u[2] of lengths n_list[0..2]
    u = []
    u.append([i for i in range(1, n_list[0] + 1)])
    u.append([2 * i for i in range(1, n_list[1] + 1)])
    u.append([3 * i for i in range(1, n_list[2] + 1)])

    u[0].sort(reverse=True)
    u[1].sort(reverse=True)
    u[2].sort(reverse=True)

    res = 0
    dp = [[[0] * (n_list[2] + 1) for _ in range(n_list[1] + 1)] for _ in range(n_list[0] + 1)]
    for i in range(n_list[0] + 1):
        for j in range(n_list[1] + 1):
            for k in range(n_list[2] + 1):
                x0 = (dp[i - 1][j - 1][k] + u[0][i - 1] * u[1][j - 1]) if i and j else 0
                x1 = (dp[i][j - 1][k - 1] + u[1][j - 1] * u[2][k - 1]) if j and k else 0
                x2 = (dp[i - 1][j][k - 1] + u[0][i - 1] * u[2][k - 1]) if i and k else 0
                dp[i][j][k] = max(x0, x1, x2)
                res = max(res, dp[i][j][k])
    # print(res)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to change input scale
    main(3)