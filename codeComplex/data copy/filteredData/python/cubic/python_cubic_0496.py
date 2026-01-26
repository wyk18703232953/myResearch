inf = 10000000000

def main(n):
    # 映射 n -> (行数, 列数, 步数)
    rows = max(1, n)
    cols = max(1, n)
    steps = 2 * max(1, n % 10 + 1)  # 保证为偶数且随 n 可变

    # 生成确定性的 h 和 z
    h = [[(i * cols + j) % 7 + 1 for j in range(cols)] for i in range(rows)]
    if rows > 1:
        z = [[(i * cols + j) % 5 + 1 for j in range(cols)] for i in range(rows - 1)]

    else:
        z = []

    dh = lambda x, y: h[x][y] if 0 <= x < len(h) and 0 <= y < len(h[0]) else inf
    dz = lambda x, y: z[x][y] if 0 <= x < len(z) and 0 <= y < len(z[0]) else inf

    dp = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(2)]
    ddp = lambda x, y, zidx: dp[x][y][zidx] if 0 <= y < rows and 0 <= zidx < cols else inf

    k = steps
    if k % 2 != 0:
        for i in dp[0]:
            for j in i:
                # print(-1, end=' ')
                pass
            # print()
            pass

    else:
        for _ in range(k // 2):
            for i in range(rows):
                for j in range(cols):
                    dp[1][i][j] = min(
                        ddp(0, i - 1, j) + dz(i - 1, j),
                        ddp(0, i + 1, j) + dz(i, j),
                        ddp(0, i, j - 1) + dh(i, j - 1),
                        ddp(0, i, j + 1) + dh(i, j),
                    )
            dp.reverse()
        for i in dp[0]:
            for j in i:
                # print(2 * j, end=' ')
                pass
            # print()
            pass
if __name__ == "__main__":
    main(5)