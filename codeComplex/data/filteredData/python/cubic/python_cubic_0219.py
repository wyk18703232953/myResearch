import random

def main(n: int):
    # n 作为规模参数，这里用来控制每种颜色数组的长度
    # 可按需调整 r, g, b 的生成方式，这里设为与 n 同级别
    r = n
    g = n
    b = n

    # 生成测试数据：1 到 1000 的随机整数
    red = [random.randint(1, 1000) for _ in range(r)]
    green = [random.randint(1, 1000) for _ in range(g)]
    blue = [random.randint(1, 1000) for _ in range(b)]

    red.sort(reverse=True)
    green.sort(reverse=True)
    blue.sort(reverse=True)

    # 三维 DP：dp[i][j][k] 表示使用前 i 个 red, j 个 green, k 个 blue 的最大值
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    answer = 0
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
                if dp[i][j][k] > answer:
                    answer = dp[i][j][k]

    print(answer)

# 示例：运行 main(3) 作为简单测试
if __name__ == "__main__":
    main(3)