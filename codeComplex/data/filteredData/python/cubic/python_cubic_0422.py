import random
import math


def solve(n, m, k, h, v):
    if k % 2:
        ans = "-1 " * m
        for _ in range(n):
            print(ans)
        return

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    nxt = [[0] * (m + 1) for _ in range(n + 1)]

    for _ in range(2, k + 1, 2):
        for i in range(n):
            for j in range(m):
                l = 2 * h[i][j - 1] + dp[i][j - 1]
                r = 2 * h[i][j] + dp[i][j + 1]
                u = 2 * v[i - 1][j] + dp[i - 1][j]
                d = 2 * v[i][j] + dp[i + 1][j]

                hor = min(l, r)
                ver = min(u, d)

                nxt[i][j] = min(hor, ver)

        dp, nxt = nxt, dp

    for row in dp[:-1]:
        print(" ".join(map(str, row[:-1])))


def main(n):
    # 规模 n 控制网格大小，这里设置 m = n，k 与 n 相关
    m = n
    # 令 k 为偶数步数，避免直接输出 -1；保证至少 2 步
    k = 2 * max(1, n // 2)

    # 生成测试数据：h 为 n x m，v 为 n-1 x m
    # 使用较小的权重范围，便于调试和查看
    max_w = 10

    # h[i][j]: 水平方向边权 (i, j) <-> (i, j+1)
    h = [
        [random.randint(1, max_w) for _ in range(m)] + [math.inf]
        for _ in range(n)
    ]

    # v[i][j]: 垂直方向边权 (i, j) <-> (i+1, j)
    v = [
        [random.randint(1, max_w) for _ in range(m)]
        for _ in range(n - 1)
    ]
    v.append([math.inf] * m)

    solve(n, m, k, h, v)


if __name__ == "__main__":
    # 示例：调用 main(5) 生成 5x5 网格的测试
    main(5)