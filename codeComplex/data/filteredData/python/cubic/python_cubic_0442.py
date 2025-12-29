import random


def main(n):
    # 这里的 n 作为行数，同时我们需要列数 m 和步数 k1
    # 可根据需要调整生成规则，这里简单设置为：
    m = n                 # 列数与行数相同
    k1 = 2 * min(n, m)    # 保证为偶数，且不超过网格尺度的合理范围

    # 生成测试数据：权值在 1~10 之间
    arr = [[random.randint(1, 10) for _ in range(m)] for _ in range(n)]
    brr = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    # DP 部分与原逻辑一致
    dp = [[[0 for _ in range(11)] for _ in range(m)] for _ in range(n)]

    for k in range(1, 11):
        for i in range(n):
            for j in range(m):
                dp[i][j][k] = 10 ** 9
                if i > 0:
                    dp[i][j][k] = min(
                        dp[i][j][k],
                        dp[i - 1][j][k - 1] + brr[i - 1][j] * 2,
                    )
                if i < n - 1:
                    dp[i][j][k] = min(
                        dp[i][j][k],
                        dp[i + 1][j][k - 1] + brr[i][j] * 2,
                    )
                if j > 0:
                    dp[i][j][k] = min(
                        dp[i][j][k],
                        dp[i][j - 1][k - 1] + arr[i][j - 1] * 2,
                    )
                if j < m - 1:
                    dp[i][j][k] = min(
                        dp[i][j][k],
                        dp[i][j + 1][k - 1] + arr[i][j] * 2,
                    )

    # 输出结果
    for i in range(n):
        line = []
        for j in range(m):
            if k1 % 2:
                line.append("-1")
            else:
                line.append(str(dp[i][j][k1 // 2]))
        print(" ".join(line))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)