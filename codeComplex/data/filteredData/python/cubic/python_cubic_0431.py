from collections import deque
from types import GeneratorType
import math
import random

###########
# LIBRARY #
###########


def bootstrap(f, stack=[]):
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


#########
# LOGIC #
#########

def encode(row, col, n, m):
    return row * m + col


@bootstrap
def solve(node, remain, adj, dp):
    if remain == 0:
        yield 0
    key = (node, remain)
    mem = dp.get(key)
    if mem != -1:
        yield mem
    best = math.inf
    for v, w in adj[node]:
        cand = (yield solve(v, remain - 1, adj, dp)) + w
        if cand < best:
            best = cand
    dp.set(key, best)
    yield best


def main(n):
    # n: controls scale; we choose grid size and k based on n
    # Example strategy: make grid roughly sqrt(n) x sqrt(n), k even ≤ 2*min(n,m)
    if n <= 0:
        return []

    side = max(1, int(n ** 0.5))
    rows = side
    cols = side
    k = 2 * max(1, min(rows, cols) // 2)  # even and not too large

    # Generate random positive weights for edges
    total_nodes = rows * cols
    adj = [[] for _ in range(total_nodes)]

    # Horizontal edges
    horiz_weights = [
        [random.randint(1, 10) for _ in range(cols - 1)] for _ in range(rows)
    ]
    for i in range(rows):
        for j in range(cols - 1):
            cur = encode(i, j, rows, cols)
            nex = encode(i, j + 1, rows, cols)
            w = horiz_weights[i][j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # Vertical edges
    vert_weights = [
        [random.randint(1, 10) for _ in range(cols)] for _ in range(rows - 1)
    ]
    for i in range(rows - 1):
        for j in range(cols):
            cur = encode(i, j, rows, cols)
            nex = encode(i + 1, j, rows, cols)
            w = vert_weights[i][j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # If k is odd, answer is all -1
    if k % 2 == 1:
        res = [[-1] * cols for _ in range(rows)]
        for row in res:
            print(" ".join(map(str, row)))
        return res

    dp = MDArray([total_nodes, k + 2], -1)
    half = k // 2

    result_grid = []
    for i in range(rows):
        ans_row = []
        for j in range(cols):
            node = encode(i, j, rows, cols)
            val = solve(node, half, adj, dp) * 2
            ans_row.append(val)
        result_grid.append(ans_row)
        print(" ".join(map(str, ans_row)))
    return result_grid


if __name__ == "__main__":
    # Example: run with scale parameter n = 16
    main(16)