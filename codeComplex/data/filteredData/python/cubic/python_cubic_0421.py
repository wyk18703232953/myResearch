import math
from collections import defaultdict
import random


def main(n):
    """
    n: 规模参数，这里用于决定网格大小、k值等。
    示例策略：
      - 令网格为 n x n
      - 令 k 为不超过 2n 的偶数（若 n<1 时做保护）
    可根据需要自行调整生成规则。
    """
    if n <= 0:
        return

    # 根据 n 生成测试数据（可根据需要修改策略）
    rows = n
    cols = n
    # 保证 k 为偶数且 >= 2
    k = max(2, 2 * (n // 2))

    # 随机生成边权，范围 1..9
    # d1: 行内相邻点之间的横边权 (rows x (cols-1))
    d1 = [[random.randint(1, 9) for _ in range(cols - 1)] for _ in range(rows)]
    # d2: 列内相邻点之间的纵边权 ((rows-1) x cols)
    d2 = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows - 1)]

    # 算法逻辑与原程序等价（去掉 IO 与 FastIO 包装）
    n_rows, m_cols = rows, cols

    if k % 2 != 0:
        ans = [[-1 for _ in range(m_cols)] for _ in range(n_rows)]
    else:
        # 使用(n_rows+1)x(m_cols+1)的扩展数组，与原代码一致
        INF = float('inf')
        ans = [[INF for _ in range(m_cols + 1)] for _ in range(n_rows + 1)]

        # 初始化：从每个格子走 2 步的最小花费
        for i in range(n_rows):
            for j in range(m_cols):
                # 对应原代码的调用方式，需要防止越界
                best = INF
                # 右
                if j < m_cols - 1:
                    best = min(best, 2 * d1[i][j])
                # 左
                if j - 1 >= 0:
                    best = min(best, 2 * d1[i][j - 1])
                # 下
                if i < n_rows - 1:
                    best = min(best, 2 * d2[i][j])
                # 上
                if i - 1 >= 0:
                    best = min(best, 2 * d2[i - 1][j])

                ans[i][j] = best

        curr = 2
        while curr != k:
            new = [[INF for _ in range(m_cols + 1)] for _ in range(n_rows + 1)]
            for i in range(n_rows):
                for j in range(m_cols):
                    best = INF
                    # 左
                    if j - 1 >= 0:
                        best = min(best, ans[i][j - 1] + 2 * d1[i][j - 1])
                    # 右
                    if j < m_cols - 1:
                        best = min(best, ans[i][j + 1] + 2 * d1[i][j])
                    # 上
                    if i - 1 >= 0:
                        best = min(best, ans[i - 1][j] + 2 * d2[i - 1][j])
                    # 下
                    if i < n_rows - 1:
                        best = min(best, ans[i + 1][j] + 2 * d2[i][j])

                    new[i][j] = best

            ans = new
            curr += 2

    # 输出结果，与原代码格式一致
    for i in range(n_rows):
        print(*ans[i][:m_cols])


# 允许直接运行文件进行简单测试
if __name__ == "__main__":
    # 示例：n = 5
    main(5)