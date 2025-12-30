import random

def main(n):
    # 1. 生成测试数据：长度为 n 的随机数组 a，取值范围 1..3（可按需调整）
    # 下标从 1 开始，与原程序保持一致
    a = [0] + [random.randint(1, 3) for _ in range(n)]

    # 2. 原逻辑：区间 DP
    dp = [[[-1, -1, -1] for _ in range(n + 1)] for _ in range(n + 1)]
    # dp[i][j] = [left_value, right_value, length]

    for i in range(1, n + 1):
        dp[i][i] = [a[i], a[i], 1]

    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n + 1):
            mini = 10 ** 10
            for k in range(j - i):
                x = dp[i][i + k][2] + dp[i + k + 1][j][2]
                if dp[i][i + k][1] == dp[i + k + 1][j][0]:
                    if mini > x - 1:
                        mini = x - 1
                        dp[i][j][0] = dp[i][i + k][0] + (dp[i][i + k][2] == 1)
                        dp[i][j][1] = dp[i + k + 1][j][1] + (dp[i + k + 1][j][2] == 1)
                        dp[i][j][2] = x - 1
                else:
                    if mini > x:
                        mini = x
                        dp[i][j][0] = dp[i][i + k][0]
                        dp[i][j][1] = dp[i + k + 1][j][1]
                        dp[i][j][2] = x

    # 输出结果（原程序是 print(dp[1][n][2])）
    print(dp[1][n][2])


if __name__ == "__main__":
    # 示例：运行 main，规模可自行修改
    main(5)