import math
import collections
import heapq
import decimal

def main(n):
    # 映射 n 到网格尺寸和步数
    # 为了可规模化，这里设定：
    # n >= 2 时：行列数从 1 开始增长，k 从 2 开始增长
    # n = 1 时：最小可运行规模
    if n <= 1:
        rows = 1
        cols = 1
        k = 2

    else:
        rows = n
        cols = n
        k = 2 * n  # 偶数，保证进入主要逻辑

    # 生成确定性的权重矩阵 a (水平边) 和 b (垂直边)
    # a 的形状: rows x cols
    # b 的形状: (rows-1) x cols
    a = [[(i * cols + j) % 7 + 1 for j in range(cols)] for i in range(rows)]
    if rows > 1:
        b = [[((i * cols + j) * 2) % 9 + 1 for j in range(cols)] for i in range(rows - 1)]

    else:
        b = []

    n_rows = rows
    m_cols = cols

    # 原算法逻辑
    if k % 2 == 1:
        for i in range(n_rows):
            for j in range(m_cols):
                # print(-1, end=" ")
                pass
            # print()
            pass

    else:
        k //= 2
        pre = [[0 for _ in range(m_cols)] for _ in range(n_rows)]
        for _ in range(k):
            curr = [[float("inf") for _ in range(m_cols)] for _ in range(n_rows)]
            for i in range(n_rows):
                for j in range(m_cols):
                    if j > 0:
                        curr[i][j] = min(curr[i][j], pre[i][j - 1] + a[i][j - 1])
                    if i < n_rows - 1:
                        curr[i][j] = min(curr[i][j], pre[i + 1][j] + b[i][j])
                    if j < m_cols - 1:
                        curr[i][j] = min(curr[i][j], pre[i][j + 1] + a[i][j])
                    if i > 0:
                        curr[i][j] = min(curr[i][j], pre[i - 1][j] + b[i - 1][j])
            pre = [row[:] for row in curr]
        for i in range(n_rows):
            for j in range(m_cols):
                # print(2 * pre[i][j], end=" ")
                pass
            # print()
            pass
if __name__ == "__main__":
    main(5)