import math

class MDArray(object):
    def __init__(self, dimensions, initial_value=0):
        dim_total = 1
        for i in dimensions:
            dim_total *= i
        self.dimensions = dimensions
        self.arr = [initial_value] * dim_total

    def _index(self, indexes):
        assert len(indexes) == len(self.dimensions)
        idx_multi = 1
        idx = 0
        for i in range(len(indexes)):
            assert 0 <= indexes[i] < self.dimensions[i]
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
    # 通过 n 构造网格规模和步数
    # n >= 1
    rows = max(1, n // 3)
    cols = max(1, n // 3)
    k = 2 * max(1, n // 5)  # 保证为偶数

    n_rows = rows
    n_cols = cols

    total_nodes = n_rows * n_cols
    adj = [[] for _ in range(total_nodes)]

    # 构造水平方向边权：完全确定性
    # weight(i,j -> i,j+1) = (i + 1) + (j + 1)
    for i in range(n_rows):
        for j in range(n_cols - 1):
            w = (i + 1) + (j + 1)
            cur = encode(i, j, n_rows, n_cols)
            nex = encode(i, j + 1, n_rows, n_cols)
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # 构造垂直方向边权：完全确定性
    # weight(i,j -> i+1,j) = (i + 1) * (j + 1)
    for i in range(n_rows - 1):
        for j in range(n_cols):
            w = (i + 1) * (j + 1)
            cur = encode(i, j, n_rows, n_cols)
            nex = encode(i + 1, j, n_rows, n_cols)
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # 如果 k 为奇数，按原逻辑全部输出 -1
    if k % 2 == 1:
        res = [[-1] * n_cols for _ in range(n_rows)]
        for row in res:
            # print(" ".join(map(str, row)))
            pass
        return

    # 动态规划
    dp = MDArray([total_nodes, k + 2], -1)

    for i in range(total_nodes):
        dp.set((i, 0), 0)

    half = k // 2
    for t in range(1, half + 1):
        for i in range(total_nodes):
            best = math.inf
            for v, w in adj[i]:
                cand = dp.get((v, t - 1)) + w
                if cand < best:
                    best = cand
            dp.set((i, t), best)

    for i in range(n_rows):
        ans_row = []
        for j in range(n_cols):
            node = encode(i, j, n_rows, n_cols)
            val = dp.get((node, half)) * 2
            ans_row.append(val)
        # print(" ".join(map(str, ans_row)))
        pass
if __name__ == "__main__":
    main(10)