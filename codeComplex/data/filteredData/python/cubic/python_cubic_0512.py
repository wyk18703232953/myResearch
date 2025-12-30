import random

def main(n):
    # 生成规模参数
    m = n
    # 为了避免代价为 0 的边，使用 1~10 的随机权重
    h = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    v = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]
    # k 取一个与 n 同量级的偶数，保证能走动
    k = 2 * n

    if k % 2 == 0:
        d = [[0] * m for _ in range(n)]
        for _ in range(k // 2):
            dt = [[0] * m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    x = float('inf')
                    if i - 1 >= 0:
                        x = min(x, d[i - 1][j] + v[i - 1][j] * 2)
                    if i + 1 < n:
                        x = min(x, d[i + 1][j] + v[i][j] * 2)
                    if j - 1 >= 0:
                        x = min(x, d[i][j - 1] + h[i][j - 1] * 2)
                    if j + 1 < m:
                        x = min(x, d[i][j + 1] + h[i][j] * 2)
                    dt[i][j] = x
            d = [row[:] for row in dt]
    else:
        d = [[-1] * m for _ in range(n)]

    for row in d:
        print(*row)


if __name__ == "__main__":
    # 示例：调用 main(4)
    main(4)