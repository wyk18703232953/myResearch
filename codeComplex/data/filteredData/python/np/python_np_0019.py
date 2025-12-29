import random


def main(n: int):
    # 生成测试数据：n x n 的概率矩阵，prob[i][j] 为 i 打败 j 的概率
    # 这里生成概率满足 prob[i][j] + prob[j][i] = 1，且 prob[i][i] = 0
    prob = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            p = random.random()
            prob[i][j] = p
            prob[j][i] = 1.0 - p

    full_bit = (1 << n) - 1
    dp = [0.0] * full_bit + [1.0]

    for bit in range(full_bit, 0, -1):
        popcount = 0
        for i in range(n):
            if (1 << i) & bit:
                popcount += 1
        if popcount == 1 or dp[bit] == 0.0:
            continue
        div = 1 / ((popcount * (popcount - 1)) >> 1)

        for i in range(n):
            if ((1 << i) & bit) == 0:
                continue
            for j in range(i + 1, n):
                if ((1 << j) & bit) == 0:
                    continue
                dp[bit - (1 << j)] += dp[bit] * prob[i][j] * div
                dp[bit - (1 << i)] += dp[bit] * prob[j][i] * div

    # 输出结果
    print(*(dp[1 << i] for i in range(n)))


if __name__ == "__main__":
    # 示例：调用 main(4)
    main(4)