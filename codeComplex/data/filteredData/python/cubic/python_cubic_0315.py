def main(n):
    # Interpret n as the maximum size for the three arrays.
    # To keep structure similar to original n[0], n[1], n[2],
    # we deterministically derive them from n.
    x = n // 3
    r = n % 3
    n0 = x + (1 if r > 0 else 0)
    n1 = x + (1 if r > 1 else 0)
    n2 = x

    n_list = [n0, n1, n2]

    # Deterministic construction of a[0], a[1], a[2]
    a = []
    for idx in range(3):
        length = n_list[idx]
        # Generate values depending on idx to avoid symmetry
        if idx == 0:
            arr = [i * 2 + 1 for i in range(length)]
        elif idx == 1:
            arr = [i * 3 + 2 for i in range(length)]

        else:
            arr = [i * 5 + 3 for i in range(length)]
        arr.sort(reverse=True)
        a.append(arr)

    dp = [[[0 for _ in range(n_list[2] + 1)] for _ in range(n_list[1] + 1)] for _ in range(n_list[0] + 1)]
    ans = 0
    for i in range(n_list[0] + 1):
        for j in range(n_list[1] + 1):
            for k in range(n_list[2] + 1):
                if i < n_list[0] and j < n_list[1]:
                    val = dp[i][j][k] + a[0][i] * a[1][j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if i < n_list[0] and k < n_list[2]:
                    val = dp[i][j][k] + a[0][i] * a[2][k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if j < n_list[1] and k < n_list[2]:
                    val = dp[i][j][k] + a[1][j] * a[2][k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)