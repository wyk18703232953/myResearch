import random

import math
gcd = math.gcd
ceil = math.ceil
mod1 = (10 ** 9) + 7
mod2 = 998244353


def strinp(testcases):
    k = 5
    if testcases == -1 or testcases == 1:
        k = 1
    # 保留函数签名和行为，但不再使用 input()
    f = ""
    f = f[2:len(f) - k]
    return f


def alp(a):
    return ord(a) - ord("a")


def main(n):
    """
    n: 控制网格规模，生成 n x n 的随机权重网格和 k 步数（偶数）。
    这里令:
      - 行数 = n
      - 列数 = n
      - k = 2 * n  (保证为偶数且随规模增长)
    """
    # 生成参数
    rows = n
    cols = n
    k = 2 * n  # 必须为偶数，否则答案全为 -1

    # 生成测试数据：
    # lrw: 行内左右边权 (rows x (cols-1))
    # udw: 行间上下边权 ((rows-1) x cols)
    # 为避免权值过大，使用 1~9 的小整数
    lrw = [[random.randint(1, 9) for _ in range(cols - 1)] for _ in range(rows)]
    udw = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows - 1)]

    # 以下为原逻辑（稍作变量名对齐）
    n_rows = rows
    m_cols = cols
    n = n_rows
    m = m_cols

    if k % 2 == 1:
        a = [-1] * m
        for _ in range(n):
            print(*a)
        return

    dp1 = [[0 for _ in range(m)] for _ in range(n)]
    dp2 = [[0 for _ in range(m)] for _ in range(n)]
    inf = 10 ** 10
    dis = k // 2

    for _ in range(dis):
        for i in range(n):
            for j in range(m):
                a = inf
                b = inf
                c = inf
                d = inf
                if j > 0:
                    a = lrw[i][j - 1] + dp2[i][j - 1]
                if j < m - 1:
                    b = lrw[i][j] + dp2[i][j + 1]
                if i > 0:
                    c = udw[i - 1][j] + dp2[i - 1][j]
                if i < n - 1:
                    d = udw[i][j] + dp2[i + 1][j]
                dp1[i][j] = min(a, b, c, d)
        dp2 = dp1
        dp1 = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            dp2[i][j] *= 2

    for i in range(n):
        print(*dp2[i])


if __name__ == '__main__':
    # 示例调用：规模 n = 4
    main(4)