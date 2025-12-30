import random

def main(n: int):
    # 生成测试数据：r,g,b 都在 [0, n] 内
    r = random.randint(0, n)
    g = random.randint(0, n)
    b = random.randint(0, n)

    # 为三个数组生成随机值，范围可自行调整
    ra = [random.randint(1, 1000) for _ in range(r)]
    ga = [random.randint(1, 1000) for _ in range(g)]
    ba = [random.randint(1, 1000) for _ in range(b)]

    ra.sort()
    ga.sort()
    ba.sort()

    # dp 只需要到 r,g,b 的大小即可
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i > 0 and j > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j - 1][k] + ra[i - 1] * ga[j - 1])
                if i > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j][k - 1] + ra[i - 1] * ba[k - 1])
                if j > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i][j - 1][k - 1] + ga[j - 1] * ba[k - 1])

    print(dp[r][g][b])


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)