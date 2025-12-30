from collections import deque
from types import GeneratorType
import math
import random

def encode(row, col, n, m):
    return row * m + col

def main(n):
    # 生成测试数据：
    # n: 行数
    # m: 列数
    # k: 步数（必须为偶数，否则答案恒为 -1）
    #
    # 这里给出一个简单的可调策略：
    # m 与 n 同规模，k 选取为 4（最小非平凡偶数）
    m = n
    k = 4

    # 权重范围
    W_MIN, W_MAX = 1, 10

    # 随机生成权重
    # 水平边权重: n 行, 每行 m-1 个
    horizontal_weights = [
        [random.randint(W_MIN, W_MAX) for _ in range(m - 1)]
        for _ in range(n)
    ]
    # 垂直边权重: n-1 行, 每行 m 个
    vertical_weights = [
        [random.randint(W_MIN, W_MAX) for _ in range(m)]
        for _ in range(n - 1)
    ]

    # 当 k 为奇数时，所有答案为 -1
    if k % 2 == 1:
        for _ in range(n):
            print(' '.join(map(str, [-1] * m)))
        return

    total_nodes = n * m
    adj = [[] for _ in range(total_nodes)]

    # 建图：水平边
    for i in range(n):
        weights = horizontal_weights[i]
        for j in range(m - 1):
            cur = encode(i, j, n, m)
            nex = encode(i, j + 1, n, m)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # 建图：垂直边
    for i in range(n - 1):
        weights = vertical_weights[i]
        for j in range(m):
            cur = encode(i, j, n, m)
            nex = encode(i + 1, j, n, m)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    half_k = k // 2
    dp = [[0] * total_nodes for _ in range(half_k + 1)]

    # remain = 0 时，dp[0][*] = 0 已初始化

    # 自底向上动态规划
    for rem in range(1, half_k + 1):
        for node in range(total_nodes):
            best = math.inf
            for nxt, w in adj[node]:
                cost = dp[rem - 1][nxt] + w
                if cost < best:
                    best = cost
            dp[rem][node] = best

    # 输出答案：每个点走恰好 k 步回到自身的最小代价
    # 是从该点出发走 half_k 步到某点，再返回 half_k 步，所以乘 2
    for i in range(n):
        row_ans = []
        for j in range(m):
            node = encode(i, j, n, m)
            val = dp[half_k][node]
            if val == math.inf:
                row_ans.append(-1)
            else:
                row_ans.append(val * 2)
        print(' '.join(map(str, row_ans)))


if __name__ == "__main__":
    # 示例：调用 main(3) 生成 3x3 网格的随机测试，并输出对应结果
    main(3)