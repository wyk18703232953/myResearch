import random

def main(n):
    # 1. 生成测试数据：n x n 概率矩阵 probs
    # 这里生成的是随机行归一化矩阵，即每一行之和为 1
    probs = []
    for _ in range(n):
        row = [random.random() for _ in range(n)]
        s = sum(row)
        if s == 0:
            # 避免全 0 行
            row[0] = 1.0
            s = 1.0
        row = [x / s for x in row]
        probs.append(row)

    # 2. 原逻辑：DP 计算
    dp = [[0.0 for _ in range(1 << n)] for _ in range(n)]
    dp[0][(1 << n) - 1] = 1.0

    ak = [[] for _ in range(n + 1)]
    for mask in range(1 << n):
        ak[bin(mask).count("1")].append(mask)

    for k in range(1, n):
        # 剩余人数为 n-k+1，对应的 mask 中 1 的个数
        for ele in ak[n - k + 1]:
            for j in range(n):
                if ele & (1 << j):
                    for w in range(n):
                        if (ele & (1 << w)) and j != w:
                            dp[k][ele - (1 << j)] += (
                                dp[k - 1][ele]
                                * probs[w][j]
                                / (((n - k + 1) * (n - k)) / 2)
                            )

    # 3. 输出最终结果
    for i in range(n):
        print(dp[n - 1][1 << i], end=" ")
    print()


if __name__ == "__main__":
    # 示例：运行规模 n=3
    main(3)