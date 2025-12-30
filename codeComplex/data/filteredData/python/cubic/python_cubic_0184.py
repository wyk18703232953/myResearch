import random

def main(n: int):
    # 生成测试数据：长度为 n 的数组 a，数值范围可自行调整
    # 这里生成 1 到 3 之间的随机整数
    a = [random.randint(1, 3) for _ in range(n)]

    m = n
    dp = [[505] * m for _ in range(m)]
    Max = [[0] * m for _ in range(m)]

    for i in range(m):
        dp[i][i] = 1
        Max[i][i] = a[i]

    for length in range(1, m + 1):
        for i in range(m - length + 1):
            j = i + length - 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                if dp[i][k] == 1 and dp[k + 1][j] == 1 and Max[i][k] == Max[k + 1][j]:
                    dp[i][j] = 1
                    Max[i][j] = Max[i][k] + 1

    print(dp[0][m - 1])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)