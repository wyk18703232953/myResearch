from math import inf
import random


def main(n):
    # 这里用 n 作为网格的行数，同时令 m = n，k = 2 * n（可按需要调整）
    m = n
    k = 2 * n  # 保证为偶数，保持原题意中“往返步数”的含义

    # 生成测试数据：权重为 1~9 的随机整数
    horizontal_costs = [
        [random.randint(1, 9) for _ in range(m - 1)]
        for _ in range(n)
    ]
    vertical_costs = [
        [random.randint(1, 9) for _ in range(m)]
        for _ in range(n - 1)
    ]

    # dp[a][b][c] - 从 (a, b) 出发走 c 步的最小花费
    dp = [[[inf] * (k // 2 + 1) for _ in range(m)] for _ in range(n)]

    def find_cost(a, b, c):
        if a < 0 or a >= n or b < 0 or b >= m:
            return inf
        if c == 0:
            return 0
        if dp[a][b][c] != inf:
            return dp[a][b][c]

        # 向下
        if a < n - 1:
            dp[a][b][c] = min(
                dp[a][b][c],
                find_cost(a + 1, b, c - 1) + vertical_costs[a][b],
            )
        # 向右
        if b < m - 1:
            dp[a][b][c] = min(
                dp[a][b][c],
                find_cost(a, b + 1, c - 1) + horizontal_costs[a][b],
            )
        # 向左
        if b > 0:
            dp[a][b][c] = min(
                dp[a][b][c],
                find_cost(a, b - 1, c - 1) + horizontal_costs[a][b - 1],
            )
        # 向上
        if a > 0:
            dp[a][b][c] = min(
                dp[a][b][c],
                find_cost(a - 1, b, c - 1) + vertical_costs[a - 1][b],
            )
        return dp[a][b][c]

    ans = [[inf] * m for _ in range(n)]
    if k % 2 == 1:
        for i in range(n):
            for j in range(m):
                ans[i][j] = -1
    else:
        half = k // 2
        for i in range(n):
            for j in range(m):
                ans[i][j] = 2 * find_cost(i, j, half)

    for row in ans:
        print(*row)


if __name__ == "__main__":
    # 示例：调用 main(4) 生成 4x4 网格的测试并输出
    main(4)