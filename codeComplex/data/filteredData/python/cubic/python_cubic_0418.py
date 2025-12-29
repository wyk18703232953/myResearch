from random import randint

MOD = 1000000000007
MAX = 1000000000


def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, xx, yy):
    x = find(parent, xx)
    y = find(parent, yy)
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[y] > rank[x]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1


def main(n):
    """
    n 是规模参数，用来生成测试数据：
    - N = n
    - M = n
    - K = 2 * n  (保证为偶数，避免全 -1 输出)
    - 水平边权值、垂直边权值在 [1, 9] 随机生成
    """
    N = n
    M = n
    K = 2 * n  # 令 K 为偶数，且与规模相关

    # 生成测试数据（模拟原先从输入读取的边权）
    # 对于每一行有 M-1 条水平边
    horiz = [
        [randint(1, 9) for _ in range(M - 1)]
        for _ in range(N)
    ]
    # 对于每一列有 N-1 条垂直边
    vert = [
        [randint(1, 9) for _ in range(M)]
        for _ in range(N - 1)
    ]

    # 构造权重矩阵 W[i][j][4]: L, R, U, D
    W = [[[MAX, MAX, MAX, MAX] for _ in range(M)] for _ in range(N)]

    # 水平边：左右
    for i in range(N):
        l = horiz[i]
        for j in range(M - 1):
            W[i][j][1] = l[j]       # 右
            W[i][j + 1][0] = l[j]   # 左

    # 垂直边：上下
    for i in range(N - 1):
        l = vert[i]
        for j in range(M):
            W[i][j][3] = l[j]       # 下
            W[i + 1][j][2] = l[j]   # 上

    if K % 2 == 1:
        # 不可能回到原点
        for _ in range(N):
            ans = ["-1"] * M
            print(" ".join(ans))
        return

    K //= 2
    # dp[step][i][j]: 从 (i,j) 出发走 2*step 步回到 (i,j) 的最小代价
    dp = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K + 1)]

    dl = ((0, -1), (0, 1), (-1, 0), (1, 0))  # L, R, U, D 对应 W 的索引顺序
    for step in range(1, K + 1):
        for i in range(N):
            for j in range(M):
                best = MAX
                for t, (di, dj) in enumerate(dl):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        best = min(best, dp[step - 1][ni][nj] + W[i][j][t] * 2)
                dp[step][i][j] = best

    for i in range(N):
        row = [str(dp[K][i][j]) for j in range(M)]
        print(" ".join(row))


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)