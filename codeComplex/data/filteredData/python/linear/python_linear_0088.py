import random

maxN = 10**6 + 5

def main(n):
    # n: number of beacons to generate

    dp = [0] * maxN
    b = [0] * maxN

    # 生成测试数据：随机产生 n 个不同的位置，每个位置一个随机范围
    # 位置范围在 [0, maxN - 1]，范围值在 [0, 1000]（可按需调整）
    positions = random.sample(range(maxN), n)
    for pos in positions:
        b[pos] = random.randint(0, 1000)

    if b[0] > 0:
        dp[0] = 1

    for i in range(1, maxN):
        if b[i] == 0:
            dp[i] = dp[i - 1]
        else:
            if b[i] >= i:
                dp[i] = 1
            else:
                dp[i] = dp[i - b[i] - 1] + 1

    print(n - max(dp))


if __name__ == "__main__":
    # 示例：调用 main(1000) 生成规模为 1000 的测试数据并运行
    main(1000)