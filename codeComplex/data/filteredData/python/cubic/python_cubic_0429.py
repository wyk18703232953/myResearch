# URDL
DR = [1, 0, -1, 0]
DC = [0, 1, 0, -1]

INF = 10 ** 9


def solve(n, m, k, w):
    if k % 2 == 1:
        return [[-1] * m for _ in range(n)]
    k //= 2
    best = [[[0] * m for _ in range(n)] for _ in range(k + 1)]
    for steps in range(1, k + 1):
        for r in range(n):
            for c in range(m):
                cur = INF
                for d in range(4):
                    r2, c2 = r + DR[d], c + DC[d]
                    if 0 <= r2 < n and 0 <= c2 < m:
                        val = 2 * w[d][r][c] + best[steps - 1][r2][c2]
                        if val < cur:
                            cur = val
                best[steps][r][c] = cur
    return best[k]


def main(n):
    # 生成规模为 n 的测试数据
    # 这里将 m 设置为 n，k 设置为 2 * n，可按需求调整
    m = n
    k = 2 * n

    # 初始化权重数组 w[4][n][m]
    w = [[[0] * m for _ in range(n)] for _ in range(4)]

    # 生成水平边权（左右），方向 1: 右，3: 左
    import random
    max_w = 10  # 最大权值，可按需调整
    for r in range(n):
        for c in range(m - 1):
            e = random.randint(1, max_w)
            w[1][r][c] = e          # 向右
            w[3][r][c + 1] = e      # 向左

    # 生成垂直边权（上下），方向 0: 下，2: 上
    for r in range(n - 1):
        for c in range(m):
            e = random.randint(1, max_w)
            w[0][r][c] = e          # 向下
            w[2][r + 1][c] = e      # 向上

    res = solve(n, m, k, w)
    for row in res:
        print(*row)


if __name__ == "__main__":
    # 示例：调用 main(4) 生成 4x4 的测试数据并求解
    main(4)