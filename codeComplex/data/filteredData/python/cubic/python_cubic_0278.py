import random

def main(n):
    # 依据规模 n 生成测试数据：
    # 让 x, y, z 的总和与 n 同阶，这里简单设 x = y = z = n
    x = y = z = n

    # 生成长度分别为 x, y, z 的正整数数组（颜色强度）
    # 数值范围可按需调整
    R = [random.randint(1, 10**9) for _ in range(x)]
    G = [random.randint(1, 10**9) for _ in range(y)]
    B = [random.randint(1, 10**9) for _ in range(z)]

    # 按原程序逻辑排序（降序）
    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)

    # 三维 DP：dp[i][j][k] = 用前 i 个 R，前 j 个 G，前 k 个 B 能得到的最大值
    dp = [[[0] * (z + 1) for _ in range(y + 1)] for _ in range(x + 1)]

    total = x + y + z
    for t in range(0, total + 1, 2):
        for i in range(x + 1):
            for j in range(y + 1):
                k = t - i - j
                if 0 <= k <= z:
                    cur = dp[i][j][k]
                    if i + 1 <= x and j + 1 <= y:
                        dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k],
                                                  cur + R[i] * G[j])
                    if i + 1 <= x and k + 1 <= z:
                        dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1],
                                                  cur + R[i] * B[k])
                    if j + 1 <= y and k + 1 <= z:
                        dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1],
                                                  cur + G[j] * B[k])

    ans = 0
    for i in range(x + 1):
        ans = max(ans, dp[i][y][z])
    for j in range(y + 1):
        ans = max(ans, dp[x][j][z])
    for k in range(z + 1):
        ans = max(ans, dp[x][y][k])

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(50) 运行一次
    main(50)