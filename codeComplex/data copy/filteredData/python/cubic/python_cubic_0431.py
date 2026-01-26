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


def solve(node, remain, adj, dp):
    if remain == 0:
        return 0
    key = (node, remain)
    mem = dp.get(key)
    if mem != -1:
        return mem
    best = math.inf
    for to, w in adj[node]:
        val = solve(to, remain - 1, adj, dp) + w
        if val < best:
            best = val
    dp.set(key, best)
    return best


def main(n):
    # Interpret n as grid size n x n, and choose k as an even number derived from n
    # Ensure k >= 2 for nontrivial behavior
    grid_n = max(1, n)
    grid_m = max(1, n)
    # k is even, proportional to n but capped to keep recursion reasonable
    k = max(2, 2 * min(n, 20))

    n_rows = grid_n
    m_cols = grid_m

    if k % 2 == 1:
        # This branch will not occur because we enforce even k, but we keep logic consistent
        result = []
        for _ in range(n_rows):
            result.append(' '.join(map(str, [-1] * m_cols)))
        # print('\n'.join(result))
        pass
        return

    total_nodes = n_rows * m_cols
    adj = [[] for _ in range(total_nodes)]

    # Deterministic horizontal edge weights
    # Original input: n lines, each with m-1 weights
    # We generate weight(i,j) = (i + j + 1) for edge between (i,j) and (i,j+1)
    for i in range(n_rows):
        weights = [(i + j + 1) for j in range(m_cols - 1)]
        for j in range(m_cols - 1):
            cur = encode(i, j, n_rows, m_cols)
            nex = encode(i, j + 1, n_rows, m_cols)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # Deterministic vertical edge weights
    # Original input: n-1 lines, each with m weights
    # We generate weight(i,j) = (i + j + 2) for edge between (i,j) and (i+1,j)
    for i in range(n_rows - 1):
        weights = [(i + j + 2) for j in range(m_cols)]
        for j in range(m_cols):
            cur = encode(i, j, n_rows, m_cols)
            nex = encode(i + 1, j, n_rows, m_cols)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    dp = MDArray([total_nodes, k + 2], -1)

    half_k = k // 2
    output_lines = []
    for i in range(n_rows):
        ans_row = []
        for j in range(m_cols):
            node = encode(i, j, n_rows, m_cols)
            val = solve(node, half_k, adj, dp) * 2
            ans_row.append(val)
        output_lines.append(' '.join(map(str, ans_row)))
    # print('\n'.join(output_lines))
    pass
if __name__ == "__main__":
    main(5)