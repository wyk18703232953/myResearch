from collections import deque
from types import GeneratorType
import math
import random

###########
# LIBRARY #
###########


def bootstrap(f, stack=[]):
    # Deep Recursion helper.
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


class MDArray(object):
    def __init__(self, dimensions, initial_value=0):
        self.dimensions = dimensions
        dim_total = 1
        for i in dimensions:
            dim_total *= i
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


#########
# LOGIC #
#########

def encode(row, col, n, m):
    return row * m + col


def main(n):
    """
    n: 控制规模的参数
    这里将 n 作为网格的行数与列数的基准，示例中设置:
      rows = n
      cols = n
      k    = 2*n (保证为偶数且不太大)
    若需要，可根据实际需求调整生成规则。
    """
    # 生成测试数据
    rows = max(1, n)
    cols = max(1, n)
    # 保证 k 为偶数且 >= 2
    k = max(2, 2 * ((n + 1) // 2))

    # 每条边的权重 1..9 随机生成
    random.seed(0)

    total_nodes = rows * cols
    adj = [[] for _ in range(total_nodes)]

    # 水平边权重: rows 行, 每行 (cols-1) 条边
    horiz_weights = []
    for _ in range(rows):
        row_w = [random.randint(1, 9) for _ in range(max(0, cols - 1))]
        horiz_weights.append(row_w)

    # 垂直边权重: (rows-1) 行, 每行 cols 条边
    vert_weights = []
    for _ in range(max(0, rows - 1)):
        row_w = [random.randint(1, 9) for _ in range(cols)]
        vert_weights.append(row_w)

    # 构造邻接表
    for i in range(rows):
        weights = horiz_weights[i]
        for j in range(cols - 1):
            cur = encode(i, j, rows, cols)
            nex = encode(i, j + 1, rows, cols)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    for i in range(rows - 1):
        weights = vert_weights[i]
        for j in range(cols):
            cur = encode(i, j, rows, cols)
            nex = encode(i + 1, j, rows, cols)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # 若 k 为奇数, 输出 -1; 本生成保证 k 为偶数, 保留逻辑以保持原意
    if k % 2 == 1:
        for _ in range(rows):
            print(' '.join(map(str, [-1] * cols)))
        return

    half = k // 2
    dp = [-1] * (rows * cols * (half + 1))

    @bootstrap
    def solve(node, remain):
        if remain == 0:
            yield 0

        key = node + remain * rows * cols
        mem = dp[key]
        if mem != -1:
            yield mem

        best = math.inf
        for to, w in adj[node]:
            cand = (yield solve(to, remain - 1)) + w
            if cand < best:
                best = cand
        dp[key] = best
        yield best

    for i in range(rows):
        ans_row = []
        for j in range(cols):
            node = encode(i, j, rows, cols)
            val = solve(node, half)
            ans_row.append(val * 2)
        print(' '.join(map(str, ans_row)))


if __name__ == "__main__":
    # 示例调用: 规模参数 n = 5
    main(5)