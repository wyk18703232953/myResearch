import random

def main(n):
    # n 为规模，这里用来控制三种颜色数量总和或上界
    # 原代码中 n 有三个维度，这里简单设定为 n0 = n1 = n2 = n
    n0 = n1 = n2 = n

    # 生成测试数据：3 个数组，每个长度分别为 n0, n1, n2
    # 元素为 1~100 的随机整数（可根据需要调整）
    a = []
    a.append(sorted([random.randint(1, 100) for _ in range(n0)], reverse=True))
    a.append(sorted([random.randint(1, 100) for _ in range(n1)], reverse=True))
    a.append(sorted([random.randint(1, 100) for _ in range(n2)], reverse=True))

    # DP 数组
    dp = [[[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)] for _ in range(n0 + 1)]
    ans = 0

    for i in range(n0 + 1):
        for j in range(n1 + 1):
            for k in range(n2 + 1):
                if i < n0 and j < n1:
                    dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k],
                                              dp[i][j][k] + a[0][i] * a[1][j])
                if i < n0 and k < n2:
                    dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1],
                                              dp[i][j][k] + a[0][i] * a[2][k])
                if j < n1 and k < n2:
                    dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1],
                                              dp[i][j][k] + a[1][j] * a[2][k])
                ans = max(ans, dp[i][j][k])

    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)