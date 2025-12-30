import random

def main(n: int):
    # 生成 n x n 概率矩阵，diag 为 0，其余为 [0,1) 随机浮点数
    prob = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                prob[i][j] = random.random()

    dp = [[0.0] * n for _ in range(1 << n)]
    dp[1][0] = 1.0

    for mask in range(3, 1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue
            for j in range(n):
                if i != j and (mask & (1 << j)):
                    dp[mask][i] = max(
                        dp[mask][i],
                        dp[mask ^ (1 << j)][i] * prob[i][j] +
                        dp[mask ^ (1 << i)][j] * prob[j][i]
                    )

    # 输出最终结果
    print(max(dp[(1 << n) - 1]))


if __name__ == "__main__":
    # 示例：调用 main(4)，可根据需要修改规模
    main(4)