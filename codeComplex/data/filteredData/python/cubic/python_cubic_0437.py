from collections import defaultdict
import random
import math

def encode(row, col, n, m):
    return row * m + col

def solve(node, remain, adj, dp, n, m):
    if remain == 0:
        return 0

    key = node + remain * n * m
    mem = dp[key]
    if mem != -1:
        return mem

    ans = min(solve(to, remain - 1, adj, dp, n, m) + w for to, w in adj[node])
    dp[key] = ans
    return ans

def main(n):
    # 生成规模参数
    # 这里设定：
    #   行数 = n
    #   列数 = n
    #   步数 k = 2 * n（保证为偶数且与规模相关）
    rows = n
    cols = n
    k = 2 * n

    # 若 k 为奇数，无解，输出 -1
    if k % 2 == 1:
        for _ in range(rows):
            print(' '.join(str(-1) for _ in range(cols)))
        return

    total_nodes = rows * cols
    adj = [[] for _ in range(total_nodes)]

    # 生成横向边权（随机正整数）
    # 对应原输入的 n 行、每行 m-1 个数
    horizontal_weights = [
        [random.randint(1, 10) for _ in range(cols - 1)]
        for _ in range(rows)
    ]
    for i in range(rows):
        weights = horizontal_weights[i]
        for j in range(cols - 1):
            cur = encode(i, j, rows, cols)
            nex = encode(i, j + 1, rows, cols)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # 生成纵向边权（随机正整数）
    # 对应原输入的 n-1 行、每行 m 个数
    vertical_weights = [
        [random.randint(1, 10) for _ in range(cols)]
        for _ in range(rows - 1)
    ]
    for i in range(rows - 1):
        weights = vertical_weights[i]
        for j in range(cols):
            cur = encode(i, j, rows, cols)
            nex = encode(i + 1, j, rows, cols)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    half_k = k // 2
    dp_size = rows * cols * (half_k + 1)
    dp = [-1] * dp_size

    for i in range(rows):
        ans_row = []
        for j in range(cols):
            node = encode(i, j, rows, cols)
            val = solve(node, half_k, adj, dp, rows, cols) * 2
            ans_row.append(val)
        print(' '.join(map(str, ans_row)))


if __name__ == "__main__":
    # 示例调用：规模 n = 4
    main(4)