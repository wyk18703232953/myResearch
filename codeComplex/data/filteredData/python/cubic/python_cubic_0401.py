import random


def solve(N, M, K, right, down):
    if K % 2 == 1:
        return (("-1 " * N) + "\n") * M

    K //= 2

    inf = float("inf")
    R = N
    C = M

    for row in right:
        row.append(inf)
        row.append(inf)
        row.append(inf)
    right.append([inf] * (C + 2))
    right.append([inf] * (C + 2))
    for row in down:
        row.append(inf)
        row.append(inf)
    down.append([inf] * (C + 2))
    down.append([inf] * (C + 2))
    down.append([inf] * (C + 2))

    def right_(r, c):
        return right[r][c - 1]

    def down_(r, c):
        return down[r - 1][c]

    def left(r, c):
        return right[r][c]

    def up(r, c):
        return down[r][c]

    dist = [[inf for _ in range(C + 2)] for _ in range(R + 2)]
    for r in range(R):
        for c in range(C):
            dist[r][c] = 0
    for _ in range(K):
        nextDist = [[inf for _ in range(C + 2)] for _ in range(R + 2)]
        for r in range(R):
            for c in range(C):
                nextDist[r][c] = min(
                    dist[r][c - 1] + right_(r, c),
                    dist[r][c + 1] + left(r, c),
                    dist[r - 1][c] + down_(r, c),
                    dist[r + 1][c] + up(r, c),
                )
        dist = nextDist
    return "\n".join(" ".join(str(2 * dist[r][c]) for c in range(C)) for r in range(R))


def main(n):
    """
    n 用作规模参数，生成一个大约 n×n 的网格测试数据。
    N, M: 在 [max(1, n-1), n+1] 范围内取值
    K: 在 [0, 2n] 范围内取值（偶数）
    边权在 [1, 10^6] 随机生成
    返回 solve 的字符串结果
    """
    random.seed(0)

    # 简单设计：N、M 接近 n，保证至少为 1
    N = max(1, n)
    M = max(1, n)

    # 生成偶数 K，范围可按需求调整
    K = 2 * max(1, n // 2)

    # 生成随机权重
    right = [[random.randint(1, 10 ** 6) for _ in range(M - 1)] for _ in range(N)]
    down = [[random.randint(1, 10 ** 6) for _ in range(M)] for _ in range(N - 1)]

    return solve(N, M, K, right, down)