import random

def main(n):
    # 根据规模 n 生成测试数据
    # 这里将三种颜色数量都设为 n，可按需要调整比例
    c1 = c2 = c3 = n

    # 生成随机数据，范围可根据需求修改
    r = sorted(random.randint(1, 1000) for _ in range(c1))
    g = sorted(random.randint(1, 1000) for _ in range(c2))
    b = sorted(random.randint(1, 1000) for _ in range(c3))

    dp = [[[0 for _ in range(c3 + 1)] for _ in range(c2 + 1)] for _ in range(c1 + 1)]

    for i in range(c1 + 1):
        for j in range(c2 + 1):
            for k in range(c3 + 1):
                if i > 0 and j > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1])
                if i > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1])
                if j > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1])

    print(dp[c1][c2][c3])

if __name__ == "__main__":
    # 示例：规模为 3
    main(3)