from collections import deque
from types import GeneratorType
import math
import heapq
import random


def encode(row, col, n, m):
    return row * m + col


def main(n):
    """
    n 为规模参数，这里用来生成一个 n x n 的网格图，
    k 设为一个与 n 相关的偶数步长（例如 k = 2 * n）。
    返回值为一个 n x n 的二维列表，对应每个格子的答案。
    """
    # 规模设置
    rows = n
    cols = n
    # k 必须是偶数，这里设为 2*n（可根据需要自行修改策略）
    k = 2 * n
    if k % 2 == 1:
        # 不可能情况，保持与原逻辑一致
        return [[-1] * cols for _ in range(rows)]

    # 生成测试数据：网格边权为 1~10 的随机整数
    # 水平边：rows 行，每行有 (cols - 1) 条边
    horizontal_weights = [
        [random.randint(1, 10) for _ in range(cols - 1)]
        for _ in range(rows)
    ]
    # 垂直边： (rows - 1) 行，每行有 cols 条边
    vertical_weights = [
        [random.randint(1, 10) for _ in range(cols)]
        for _ in range(rows - 1)
    ]

    total_nodes = rows * cols
    adj = [[] for _ in range(total_nodes)]

    # 构建水平边
    for i in range(rows):
        weights = horizontal_weights[i]
        for j in range(cols - 1):
            cur = encode(i, j, rows, cols)
            nex = encode(i, j + 1, rows, cols)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # 构建垂直边
    for i in range(rows - 1):
        weights = vertical_weights[i]
        for j in range(cols):
            cur = encode(i, j, rows, cols)
            nex = encode(i + 1, j, rows, cols)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # DP 数组：dp[t][v] 表示从节点 v 走 t 步的最小花费
    half_k = k // 2
    # 使用一维数组，布局为: dp[t * total_nodes + v]
    dp = [0] * (total_nodes * (half_k + 1))

    # 初始化 t = 0 时的花费为 0，已在创建时完成
    # 对每一个步数 t，计算 dp
    for t in range(1, half_k + 1):
        base_prev = (t - 1) * total_nodes
        base_cur = t * total_nodes
        for v in range(total_nodes):
            best = math.inf
            for to, w in adj[v]:
                cand = dp[base_prev + to] + w
                if cand < best:
                    best = cand
            dp[base_cur + v] = best

    # 结果：从每个点出发走 k 步回到起点（往返）的最小花费
    # 等于走半程的最小花费乘以 2
    result = []
    base_final = half_k * total_nodes
    for i in range(rows):
        row_ans = []
        for j in range(cols):
            node = encode(i, j, rows, cols)
            val = dp[base_final + node]
            row_ans.append(val * 2)
        result.append(row_ans)

    return result


# 示例：运行 main(3) 并打印结果
if __name__ == "__main__":
    ans = main(3)
    for row in ans:
        print(" ".join(map(str, row)))