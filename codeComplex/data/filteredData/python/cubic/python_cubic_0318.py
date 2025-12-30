import random

def main(n):
    # 生成测试数据：r,g,b 都设为 n
    r = g = b = n

    # 为了避免数值过大，随机值控制在 [-10^3, 10^3] 范围内
    red = [random.randint(-1000, 1000) for _ in range(r)]
    green = [random.randint(-1000, 1000) for _ in range(g)]
    blue = [random.randint(-1000, 1000) for _ in range(b)]

    red.sort()
    green.sort()
    blue.sort()

    dp = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i > 0 and j > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j - 1][k] + red[i - 1] * green[j - 1])
                if i > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j][k - 1] + red[i - 1] * blue[k - 1])
                if j > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i][j - 1][k - 1] + green[j - 1] * blue[k - 1])

    print(dp[-1][-1][-1])


if __name__ == "__main__":
    # 示例：规模 n = 3
    main(3)