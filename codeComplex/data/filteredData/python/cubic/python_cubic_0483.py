import random

def main(n):
    # 生成测试数据
    # n: 行数
    # 令 m = n，k = 2 * n（保证为偶数且与规模相关）
    m = n
    k = 2 * n

    # 生成 right 和 down 权重，取值范围 1~9
    right = [[random.randint(1, 9) for _ in range(m - 1)] for _ in range(n)]
    down = [[random.randint(1, 9) for _ in range(m)] for _ in range(n - 1)]

    # 若 k 为奇数，直接输出 -1（这里 k 被设置为偶数，一般不会触发）
    if k % 2 == 1:
        for _ in range(n):
            print(" ".join(["-1"] * m))
        return

    half_k = k // 2

    # dp[i][j][l] 表示从 (i,j) 出发走 l 步的最小代价
    dp = [[[0] * (half_k + 1) for _ in range(m)] for _ in range(n)]

    INF = float("inf")
    for l in range(half_k):
        for i in range(n):
            for j in range(m):
                best = INF
                if i > 0:
                    best = min(best, dp[i - 1][j][l] + down[i - 1][j])
                if j > 0:
                    best = min(best, dp[i][j - 1][l] + right[i][j - 1])
                if i < n - 1:
                    best = min(best, dp[i + 1][j][l] + down[i][j])
                if j < m - 1:
                    best = min(best, dp[i][j + 1][l] + right[i][j])
                dp[i][j][l + 1] = best

    for i in range(n):
        row = [str(2 * dp[i][j][half_k]) for j in range(m)]
        print(" ".join(row))


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)