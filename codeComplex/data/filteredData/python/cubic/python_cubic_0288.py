import random

def main(n: int):
    # 生成规模：三种颜色数量之和约为 n
    # 这里简单地按比例分成 3 份（尽量均匀）
    R = n // 3
    G = (n - R) // 2
    B = n - R - G

    # 生成测试数据：1 到 1000 的随机整数
    r = [random.randint(1, 1000) for _ in range(R)]
    g = [random.randint(1, 1000) for _ in range(G)]
    b = [random.randint(1, 1000) for _ in range(B)]

    r.sort()
    g.sort()
    b.sort()

    # 初始化三维 DP 数组
    dp = []
    for i in range(R + 1):
        d = []
        for j in range(G + 1):
            d.append([0] * (B + 1))
        dp.append(d)

    # 状态转移
    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i + j + k < 2:
                    continue
                if i > 0 and j > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1])
                if i > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1])
                if j > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1])

    # 输出结果（与原程序行为一致）
    print(dp[R][G][B])


if __name__ == "__main__":
    # 示例：n = 9 时，R,G,B 大致各为 3
    main(9)