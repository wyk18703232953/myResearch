import math

def encode(row, col, n, m):
    return row * m + col

def main(n):
    # Map n to grid and step parameters deterministically.
    # Choose n as the side length of a square grid, k as an even walk length.
    if n <= 1:
        n_local = 1
        m_local = 1

    else:
        n_local = n
        m_local = n
    # Ensure k is even and at least 2 so that the main logic runs.
    k = 2 * max(1, n // 2)

    n_rows = n_local
    n_cols = m_local

    # Deterministic edge weight generators based on indices.
    # Horizontal edges: between (i, j) and (i, j+1) for j in [0, m-2]
    horiz_weights = []
    for i in range(n_rows):
        row_weights = [(i * n_cols + j + 1) % 9 + 1 for j in range(n_cols - 1)]
        horiz_weights.append(row_weights)

    # Vertical edges: between (i, j) and (i+1, j) for i in [0, n-2]
    vert_weights = []
    for i in range(n_rows - 1):
        row_weights = [((i + 1) * n_cols + j + 3) % 9 + 1 for j in range(n_cols)]
        vert_weights.append(row_weights)

    # If k is odd, answer is all -1 (following original logic).
    if k % 2 == 1:
        res = []
        for _ in range(n_rows):
            res.append(' '.join(['-1'] * n_cols))
        # print('\n'.join(res))
        pass
        return

    total_nodes = n_rows * n_cols
    adj = [[] for _ in range(total_nodes)]

    # Build adjacency using deterministic weights.
    for i in range(n_rows):
        for j in range(n_cols - 1):
            cur = encode(i, j, n_rows, n_cols)
            nex = encode(i, j + 1, n_rows, n_cols)
            w = horiz_weights[i][j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    for i in range(n_rows - 1):
        for j in range(n_cols):
            cur = encode(i, j, n_rows, n_cols)
            nex = encode(i + 1, j, n_rows, n_cols)
            w = vert_weights[i][j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # Dynamic programming table flattened: dp[t][node] => dp[node + t*total_nodes]
    half_k = k // 2
    dp_size = total_nodes * (half_k + 1)
    dp = [-1] * dp_size

    # Base case: distance 0 is 0 for all nodes.
    for i in range(total_nodes):
        dp[i] = 0

    # Fill DP for t = 1..half_k
    for t in range(1, half_k + 1):
        base_prev = (t - 1) * total_nodes
        base_cur = t * total_nodes
        for i in range(total_nodes):
            best = None
            for v, w in adj[i]:
                val = dp[v + base_prev] + w
                if best is None or val < best:
                    best = val
            dp[i + base_cur] = best

    # Output results as in original: minimal cycle of length k from each cell.
    base_final = half_k * total_nodes
    lines = []
    for i in range(n_rows):
        row_vals = []
        for j in range(n_cols):
            node = encode(i, j, n_rows, n_cols)
            val = dp[node + base_final] * 2
            row_vals.append(str(val))
        lines.append(' '.join(row_vals))
    # print('\n'.join(lines))
    pass
if __name__ == "__main__":
    # Example deterministic call
    main(5)