import random

def main(n):
    # 这里的 n 用作网格的行数，列数 m、步数 k 由规则生成
    # 你也可以自行修改下面的 m 和 k 的生成方式
    m = max(1, n)          # 简单设为与 n 相同规模
    k = 2 * max(1, n // 2) # 确保为偶数（算法要求 k 为偶数才有解）

    # 生成测试数据：网格边权重
    # l1: 水平边权，大小 n x (m-1)
    # l2: 垂直边权，大小 (n-1) x m
    # 使用 1..10 的随机权值
    random.seed(0)
    l1 = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    l2 = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    inf = 10 ** 18

    def check(x, y):
        return 0 <= x < n and 0 <= y < m

    # dp[i][j][t]: 从 (i, j) 出发，走恰好 t 步到某个格子并回到原点的最小半程代价
    # 原题中 t 最大为 k//2，且 k <= 40 通常，原代码直接开到 21
    max_half = min(20, k // 2)
    dp = [[[inf] * (max_half + 1) for _ in range(m)] for _ in range(n)]

    # 初始化 t = 1
    for i in range(n):
        for j in range(m):
            if check(i, j + 1):
                dp[i][j][1] = min(l1[i][j], dp[i][j][1])
            if check(i, j - 1):
                dp[i][j][1] = min(l1[i][j - 1], dp[i][j][1])
            if check(i + 1, j):
                dp[i][j][1] = min(l2[i][j], dp[i][j][1])
            if check(i - 1, j):
                dp[i][j][1] = min(l2[i - 1][j], dp[i][j][1])

    # 递推 t = 2..k//2
    for x in range(2, max_half + 1):
        for i in range(n):
            for j in range(m):
                if check(i, j + 1):
                    dp[i][j][x] = min(dp[i][j][x], l1[i][j] + dp[i][j + 1][x - 1])
                if check(i, j - 1):
                    dp[i][j][x] = min(dp[i][j][x], l1[i][j - 1] + dp[i][j - 1][x - 1])
                if check(i + 1, j):
                    dp[i][j][x] = min(dp[i][j][x], l2[i][j] + dp[i + 1][j][x - 1])
                if check(i - 1, j):
                    dp[i][j][x] = min(dp[i][j][x], l2[i - 1][j] + dp[i - 1][j][x - 1])

    ans = [[-1] * m for _ in range(n)]
    if k % 2 == 0:
        half = min(max_half, k // 2)
        for i in range(n):
            for j in range(m):
                if dp[i][j][half] < inf:
                    ans[i][j] = 2 * dp[i][j][half]

    for row in ans:
        print(*row)


if __name__ == "__main__":
    # 示例调用：规模 n = 4
    main(4)