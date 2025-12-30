import random

def main(n: int):
    # 生成规模
    # 为保持原逻辑的一般性，这里令 m = n，k = 2*n（保证为偶数且随规模增长）
    m = n
    k = 2 * n

    # 生成测试数据：YOKO 为 n 行 m-1 列，TATE 为 n-1 行 m 列的非负权重
    # 可根据需要调整生成范围
    MAX_W = 10
    YOKO = [[random.randint(1, MAX_W) for _ in range(m - 1)] for _ in range(n)]
    TATE = [[random.randint(1, MAX_W) for _ in range(m)] for _ in range(n - 1)]

    # 以下为原逻辑
    if k % 2 == 1:
        for _ in range(n):
            print(*([-1] * m))
        return

    DP = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            MIN = 1 << 30

            if j - 1 >= 0:
                MIN = min(MIN, YOKO[i][j - 1] * 2)
            if j < m - 1:
                MIN = min(MIN, YOKO[i][j] * 2)

            if i - 1 >= 0:
                MIN = min(MIN, TATE[i - 1][j] * 2)
            if i < n - 1:
                MIN = min(MIN, TATE[i][j] * 2)

            DP[i][j] = MIN

    DP0 = [row[:] for row in DP]

    for _ in range(k // 2 - 1):
        NDP = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                MIN = DP[i][j] + DP0[i][j]

                if 0 <= i + 1 < n:
                    MIN = min(MIN, TATE[i][j] * 2 + DP[i + 1][j])

                if 0 <= i - 1 < n:
                    MIN = min(MIN, TATE[i - 1][j] * 2 + DP[i - 1][j])

                if 0 <= j + 1 < m:
                    MIN = min(MIN, YOKO[i][j] * 2 + DP[i][j + 1])

                if 0 <= j - 1 < m:
                    MIN = min(MIN, YOKO[i][j - 1] * 2 + DP[i][j - 1])

                NDP[i][j] = MIN
        DP = NDP

    for dp in DP:
        print(*dp)


if __name__ == "__main__":
    # 示例调用：可以在此调整规模 n
    main(4)