import random

def main(n: int):
    # 生成规模为 n 的测试数据：n x n 的概率矩阵，满足对角线为 0
    prob = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                prob[i][j] = random.random()

    # 原逻辑
    dp = [[0.0] * (1 << n) for _ in range(n)]
    dp[0][1] = 1.0

    for mask in range(3, 1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue
            for j in range(n):
                if i != j and (mask & (1 << j)):
                    dp[i][mask] = max(
                        dp[i][mask],
                        dp[i][mask - (1 << j)] * prob[i][j]
                        + dp[j][mask - (1 << i)] * prob[j][i]
                    )

    ans = max(dp[i][(1 << n) - 1] for i in range(n))
    print(ans)


if __name__ == "__main__":
    # 示例调用：n 可根据需要调整
    main(5)