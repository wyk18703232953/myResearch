def main(n):
    import random

    # 根据规模 n 生成测试数据 a
    # 这里生成 1 到 3 的随机整数，可根据需要调整生成规则
    a = [random.randint(1, 3) for _ in range(n)]

    # 原始逻辑开始
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
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    print(dp[0][n])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)