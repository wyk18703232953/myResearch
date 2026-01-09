def main(n):
    # Interpret n as the length of each of the three arrays
    n0 = n1 = n2 = n
    n_list = [n0, n1, n2]

    # Deterministically generate a[0], a[1], a[2]
    a = []
    for idx, size in enumerate(n_list):
        if idx == 0:
            arr = [i + 1 for i in range(size)]
        elif idx == 1:
            arr = [2 * i + 1 for i in range(size)]

        else:
            arr = [3 * i + 2 for i in range(size)]
        arr.sort(reverse=True)
        a.append(arr)

    dp = [[[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)] for _ in range(n0 + 1)]
    ans = 0
    for i in range(n0 + 1):
        for j in range(n1 + 1):
            for k in range(n2 + 1):
                if i < n0 and j < n1:
                    val = dp[i][j][k] + a[0][i] * a[1][j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if i < n0 and k < n2:
                    val = dp[i][j][k] + a[0][i] * a[2][k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if j < n1 and k < n2:
                    val = dp[i][j][k] + a[1][j] * a[2][k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)