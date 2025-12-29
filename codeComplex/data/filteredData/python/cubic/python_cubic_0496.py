import random

def main(n):
    # 参数化尺寸：原程序中有 n, m, k
    # 这里约定：m = n，k 为随机偶数（2 到 2*n 之间）
    m = n
    if m <= 0:
        return
    k = random.randint(1, n) * 2  # 保证为偶数

    inf = 10_000_000_000

    # 生成测试数据：
    # h 为 n x m 的非负权值
    # z 为 (n-1) x m 的非负权值
    max_weight = 10
    h = [[random.randint(0, max_weight) for _ in range(m)] for _ in range(n)]
    if n > 1:
        z = [[random.randint(0, max_weight) for _ in range(m)] for _ in range(n - 1)]
    else:
        z = []

    dh = lambda x, y: h[x][y] if 0 <= x < len(h) and 0 <= y < len(h[0]) else inf
    dz = lambda x, y: z[x][y] if 0 <= x < len(z) and 0 <= y < len(z[0]) else inf

    dp = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
    ddp = (
        lambda x, y, z_idx: dp[x][y][z_idx]
        if 0 <= y < n and 0 <= z_idx < m
        else inf
    )

    if k % 2 != 0:
        for i in dp[0]:
            print(" ".join("-1" for _ in i))
    else:
        half_k = k // 2
        for _ in range(half_k):
            for i in range(n):
                for j in range(m):
                    dp[1][i][j] = min(
                        ddp(0, i - 1, j) + dz(i - 1, j),
                        ddp(0, i + 1, j) + dz(i, j),
                        ddp(0, i, j - 1) + dh(i, j - 1),
                        ddp(0, i, j + 1) + dh(i, j),
                    )
            dp.reverse()
        for row in dp[0]:
            print(" ".join(str(2 * v) for v in row))


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(5)