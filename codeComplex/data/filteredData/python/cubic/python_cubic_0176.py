def main(n):
    # 确定性生成长度为 n 的数组 a
    # 模式：a[i] = (i % 3) + 1，保证有重复结构便于算法运行
    a = [(i % 3) + 1 for i in range(n)]

    dp = [[1000] * (n + 1) for _ in range(n + 1)]
    val = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        dp[i][i + 1] = 1
        val[i][i + 1] = a[i]

    for p in range(2, n + 1):
        for i in range(n - p + 1):
            j = i + p
            for k in range(i + 1, j):
                if dp[i][k] == 1 and dp[k][j] == 1 and val[i][k] == val[k][j]:
                    dp[i][j] = 1
                    val[i][j] = val[i][k] + 1

                else:
                    cand = dp[i][k] + dp[k][j]
                    if cand < dp[i][j]:
                        dp[i][j] = cand

    # print(dp[0][n])
    pass
if __name__ == "__main__":
    # 示例：使用 n=10 作为输入规模
    main(10)