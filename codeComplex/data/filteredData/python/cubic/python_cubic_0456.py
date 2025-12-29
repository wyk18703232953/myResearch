import math
import random

def main(n):
    # 生成测试规模：n 行，m 列，k 为偶数步数
    m = n                      # 这里令 m = n，可根据需要调整
    k = 2 * (n // 2 + 1)       # 保证为偶数且与 n 同阶

    # 当 k 为奇数的情况在原代码中直接输出 -1，这里构造的 k 一定为偶数
    horz = []
    vert = []

    # 生成随机权重数据（可根据需要修改生成规则）
    # horz: n x (m-1)
    for i in range(n):
        row = [random.randint(1, 10) for _ in range(m - 1)]
        horz.append(row)
    # vert: (n-1) x m
    for i in range(n - 1):
        row = [random.randint(1, 10) for _ in range(m)]
        vert.append(row)

    # DP 数组：dp[i][j][x] 为从 (i,j) 出发走 x 步再回到 (i,j) 的最小代价
    max_k = k
    dp = [[[0 for _ in range(max_k + 1)] for _ in range(m)] for _ in range(n)]

    for x in range(2, k + 1, 2):
        for i in range(n):
            for j in range(m):
                best = math.inf
                if i > 0:
                    best = min(best, dp[i - 1][j][x - 2] + 2 * vert[i - 1][j])
                if i < n - 1:
                    best = min(best, dp[i + 1][j][x - 2] + 2 * vert[i][j])
                if j > 0:
                    best = min(best, dp[i][j - 1][x - 2] + 2 * horz[i][j - 1])
                if j < m - 1:
                    best = min(best, dp[i][j + 1][x - 2] + 2 * horz[i][j])
                dp[i][j][x] = best

    # 输出最终结果：每个格子走 k 步回到自身的最小代价
    for i in range(n):
        row = []
        for j in range(m):
            row.append(dp[i][j][k])
        print(*row)


if __name__ == "__main__":
    # 示例调用：n 可以根据需要调整
    main(4)