#!/usr/bin/env python

def main(n):
    """
    生成规模为 n 的测试数据并执行原逻辑。

    这里假设：
    - 网格为 n x n
    - 步数参数 k = 2 * n  （保证为偶数）
    - 水平边权 H[i][j]、垂直边权 V[i][j] 都用简单的可重复生成规则：
        H[i][j] = (i + j) % 9 + 1
        V[i][j] = (i * 2 + j * 3) % 9 + 1
    """

    max_int = 10 ** 9

    # 生成参数 n, m, k
    m = n
    k = 2 * n  # 任意偶数函数，只要是偶数即可

    # 生成水平边权 H：n 行，每行 m-1 条边
    # 原代码中 H[i] 长度为 m-1，随后会 append(max_int) 作为哨兵
    H = []
    for i in range(n):
        row = []
        for j in range(m - 1):
            row.append((i + j) % 9 + 1)
        row.append(max_int)  # 保持与原逻辑一致，多一列哨兵
        H.append(row)

    # 生成垂直边权 V：n-1 行，每行 m 条边
    V = []
    for i in range(n - 1):
        row = []
        for j in range(m):
            row.append((i * 2 + j * 3) % 9 + 1)
        V.append(row)
    V.append([max_int] * m)  # 多一行哨兵

    # 原逻辑开始
    if k % 2:
        for _ in range(n):
            # print(' '.join(['-1'] * m))
            pass
        return

    k //= 2

    DP0 = [[0] * (m + 1) for _ in range(n + 1)]
    DP1 = [[0] * (m + 1) for _ in range(n + 1)]

    for _ in range(k):
        for i in range(n):
            for j in range(m):
                l = DP0[i][j - 1] + H[i][j - 1]
                r = DP0[i][j + 1] + H[i][j]
                u = DP0[i - 1][j] + V[i - 1][j]
                d = DP0[i + 1][j] + V[i][j]
                DP1[i][j] = min(l, r, u, d)
        DP0, DP1 = DP1, DP0

    O = []
    for row in DP0[:-1]:
        O.append(' '.join(str(val * 2) for val in row[:-1]))

    # print('\n'.join(O))
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)