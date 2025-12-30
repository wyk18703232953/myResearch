from collections import defaultdict
import random


class MDArray(object):
    def __init__(self, dimensions, initial_value=0):
        dim_total = 1
        self.dimensions = list(dimensions)
        for d in self.dimensions:
            dim_total *= d
        self.arr = [initial_value] * dim_total

    def _index(self, indexes):
        idx_multi = 1
        idx = 0
        for i in range(len(indexes)):
            idx += indexes[i] * idx_multi
            idx_multi *= self.dimensions[i]
        return idx

    def get(self, indexes):
        return self.arr[self._index(indexes)]

    def set(self, indexes, value):
        self.arr[self._index(indexes)] = value
        return value


def encode(row, col, n, m):
    return row * m + col


def main(n):
    # 参数含义：
    # n: 网格行数，也作为规模参数
    # 自动生成：
    #   m: 列数，这里取 m = n
    #   k: 步数，这里取一个偶数，例如 k = 2 * n（至少为 2）
    #
    # 可以根据需要修改生成规则。

    # ------------------------
    # 1. 根据 n 生成测试数据
    # ------------------------
    if n <= 0:
        return

    m = n
    k = max(2, 2 * n)  # 保证为偶数且至少为 2

    total_nodes = n * m

    # 为了可重复性，固定随机种子
    random.seed(1)

    # 生成水平边权重：n 行，每行 m-1 个
    horizontal_weights = [
        [random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)
    ]

    # 生成垂直边权重：n-1 行，每行 m 个
    vertical_weights = [
        [random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)
    ]

    # ------------------------
    # 2. 构建图
    # ------------------------
    adj = [[] for _ in range(total_nodes)]

    # 水平边
    for i in range(n):
        weights = horizontal_weights[i]
        for j in range(m - 1):
            cur = encode(i, j, n, m)
            nex = encode(i, j + 1, n, m)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # 垂直边
    for i in range(n - 1):
        weights = vertical_weights[i]
        for j in range(m):
            cur = encode(i, j, n, m)
            nex = encode(i + 1, j, n, m)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # ------------------------
    # 3. 动态规划计算答案
    # ------------------------
    if k % 2 == 1:
        # 不可能从同一格走奇数步回到自身
        for _ in range(n):
            print(' '.join(['-1'] * m))
        return

    dp = MDArray([total_nodes, k + 2], -1)

    for i in range(total_nodes):
        dp.set((i, 0), 0)

    half = k // 2
    for t in range(1, half + 1):
        for i in range(total_nodes):
            best = None
            for v, w in adj[i]:
                val = dp.get((v, t - 1)) + w
                if best is None or val < best:
                    best = val
            dp.set((i, t), best)

    # ------------------------
    # 4. 输出结果
    # ------------------------
    for i in range(n):
        row_ans = []
        for j in range(m):
            node = encode(i, j, n, m)
            row_ans.append(dp.get((node, half)) * 2)
        print(' '.join(map(str, row_ans)))


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)