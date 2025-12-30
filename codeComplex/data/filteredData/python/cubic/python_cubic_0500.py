import math
import random


class Node:
    def __init__(self, u=math.inf, d=math.inf, l=math.inf, r=math.inf):
        self.up = u
        self.dn = d
        self.lt = l
        self.rt = r

    def __str__(self):
        return 'U:{},D:{},L:{},R:{}'.format(self.up, self.dn, self.lt, self.rt)


def main(n):
    """
    n: 规模参数，用来生成测试数据规模:
       - 行数 rows = n
       - 列数 cols = n
       - 步数 k = 2*n（保证为偶数，且随规模线性增长）
    """

    # 根据 n 生成测试数据
    rows = n
    cols = n
    k = 2 * n  # 必须为偶数才有解

    # 生成边权，随机正整数或你可以改成固定值以便调试
    # 水平边: rows 行，每行 (cols-1) 条边
    horizontal_weights = [
        [random.randint(1, 10) for _ in range(cols - 1)]
        for _ in range(rows)
    ]
    # 垂直边: (rows-1) 行，每行 cols 条边
    vertical_weights = [
        [random.randint(1, 10) for _ in range(cols)]
        for _ in range(rows - 1)
    ]

    # 构建图结构
    graph = [[Node() for _ in range(cols)] for _ in range(rows)]

    # 设置左右边权
    for i in range(rows):
        wts = horizontal_weights[i]
        for j in range(cols - 1):
            graph[i][j].rt = wts[j]
            graph[i][j + 1].lt = wts[j]

    # 设置上下边权
    for i in range(rows - 1):
        wts = vertical_weights[i]
        for j in range(cols):
            graph[i][j].dn = wts[j]
            graph[i + 1][j].up = wts[j]

    ans = [[math.inf for _ in range(cols)] for _ in range(rows)]

    if k % 2:  # 如果 k 为奇数，与原题一致：全为 -1
        for s in ans:
            print(' '.join('-1' for _ in s))
        return

    # k 为偶数的情况
    dp = [[[math.inf for _ in range(k + 1)] for _ in range(cols)] for _ in range(rows)]

    def bfs(prsnt, stps):
        if stps == 0:
            return 0
        if dp[prsnt[0]][prsnt[1]][stps] == math.inf:
            min_cost = math.inf
            r, c = prsnt
            # (dx, dy, cost)
            moves = [
                (0, 1, graph[r][c].dn),   # 下
                (1, 0, graph[r][c].rt),   # 右
                (0, -1, graph[r][c].up),  # 上
                (-1, 0, graph[r][c].lt)   # 左
            ]
            for dx, dy, cost in moves:
                nr, nc = r + dy, c + dx
                if 0 <= nr < rows and 0 <= nc < cols:
                    min_cost = min(min_cost, bfs((nr, nc), stps - 1) + cost)
            dp[r][c][stps] = min_cost
        return dp[prsnt[0]][prsnt[1]][stps]

    half_k = k // 2
    for i in range(rows):
        for j in range(cols):
            res = bfs((i, j), half_k)
            ans[i][j] = res * 2 if res != math.inf else math.inf

    # 输出答案，保持原始格式
    for s in ans:
        print(' '.join(str(-1) if x == math.inf else str(x) for x in s))


if __name__ == "__main__":
    # 示例：调用 main(5) 生成 5x5 的测试数据并求解
    main(5)