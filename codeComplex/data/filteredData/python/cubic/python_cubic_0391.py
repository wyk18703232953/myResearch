import random

def main(n):
    # 生成测试数据：n 行，m 列，步数 k
    # 这里约定 m = n，k = 2 * n（可按需调整）
    m = n
    k = 2 * n

    # 生成 reb1: n 行 m-1 列，边权为 1~10 的随机整数
    reb1 = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    # 生成 reb2: n-1 行 m 列
    reb2 = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    if k % 2:
        for _ in range(n):
            print(" ".join(["-1"] * m))
        return

    minsum = [[0] * m for _ in range(n)]
    nminsum = [[0] * m for _ in range(n)]

    for _ in range(k // 2):
        for i in range(n):
            for j in range(m):
                cmin = 1000000000010
                if i != 0:
                    cmin = min(cmin, minsum[i - 1][j] + reb2[i - 1][j])
                if i != n - 1:
                    cmin = min(cmin, minsum[i + 1][j] + reb2[i][j])
                if j != 0:
                    cmin = min(cmin, minsum[i][j - 1] + reb1[i][j - 1])
                if j != m - 1:
                    cmin = min(cmin, minsum[i][j + 1] + reb1[i][j])
                nminsum[i][j] = cmin
        for i in range(n):
            for j in range(m):
                minsum[i][j] = nminsum[i][j]

    for row in minsum:
        print(" ".join(str(v * 2) for v in row))


if __name__ == "__main__":
    # 示例：规模 n=4
    main(4)