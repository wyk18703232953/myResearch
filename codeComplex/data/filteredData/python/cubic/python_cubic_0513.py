import sys
from math import inf
import random


def explorer(n, m, k, R, C):
    if k % 2:
        return None

    G = [[0] * m for _ in range(n)]
    G_ = [[0] * m for _ in range(n)]
    for _ in range(k // 2):
        for i in range(n):
            for j in range(m):
                x = inf
                if i > 0:
                    x = min(x, G[i - 1][j] + 2 * C[i - 1][j])
                if i + 1 < n:
                    x = min(x, G[i + 1][j] + 2 * C[i][j])
                if j > 0:
                    x = min(x, G[i][j - 1] + 2 * R[i][j - 1])
                if j + 1 < m:
                    x = min(x, G[i][j + 1] + 2 * R[i][j])
                G_[i][j] = x
        G, G_ = G_, G
    return G


def lstr(l):
    return ' '.join(map(str, l))


def llstr(ll):
    return '\n'.join(map(lstr, ll))


def main(n):
    """
    n: 规模参数，用于生成测试数据。
       这里设定：
       - 网格大小为 n x n
       - 步数 k 为 2*n（偶数）
       - R, C 的权值为 1..10 的随机整数
    """
    m = n
    k = 2 * n  # 保证为偶数

    # 生成测试数据：R 为 n x (m-1)，C 为 (n-1) x m
    if m > 1:
        R = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    else:
        R = [[0] * 0 for _ in range(n)]

    if n > 1:
        C = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]
    else:
        C = [[0] * m for _ in range(0)]

    G = explorer(n, m, k, R, C)
    if G:
        print(llstr(G))
    else:
        s = ' '.join('-1' for _ in range(m))
        print('\n'.join(s for _ in range(n)))


if __name__ == '__main__':
    # 示例：可以改成任意正整数规模
    main(4)