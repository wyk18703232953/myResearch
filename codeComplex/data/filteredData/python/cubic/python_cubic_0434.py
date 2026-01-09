import math
import heapq


def encode(row, col, n, m):
    return row * m + col


def main(n):
    # Interpret n as both grid size and path length scale
    if n <= 0:
        return

    # Define grid and k (must be even to do any work)
    rows = n
    cols = n
    k = 2 * n  # even

    # Core logic starts here (no I/O objects)
    if k % 2 == 1:
        res = []
        for _ in range(rows):
            res.append([-1] * cols)
        for row in res:
            # print(" ".join(map(str, row)))
            pass
        return

    total_nodes = rows * cols
    adj = [[] for _ in range(total_nodes)]

    # Deterministic horizontal edge weights
    # weight formula: (i + j + 1) % 9 + 1
    for i in range(rows):
        weights = [(i + j + 1) % 9 + 1 for j in range(cols - 1)]
        for j in range(cols - 1):
            cur = encode(i, j, rows, cols)
            nex = encode(i, j + 1, rows, cols)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # Deterministic vertical edge weights
    # weight formula: (i * cols + j + 3) % 9 + 1
    for i in range(rows - 1):
        weights = [((i * cols + j + 3) % 9) + 1 for j in range(cols)]
        for j in range(cols):
            cur = encode(i, j, rows, cols)
            nex = encode(i + 1, j, rows, cols)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # Convert k/2 to integer because original code used k/2
    half_k = k // 2

    # DP table: dp[remain][node]
    # Using list of lists for determinism and clarity
    dp = [[-1] * total_nodes for _ in range(half_k + 1)]

    def solve(node, remain):
        if remain == 0:
            return 0
        mem = dp[remain][node]
        if mem != -1:
            return mem
        best = math.inf
        for nxt, w in adj[node]:
            cost = solve(nxt, remain - 1) + w
            if cost < best:
                best = cost
        dp[remain][node] = best
        return best

    # Compute and print results
    for i in range(rows):
        ans_row = []
        for j in range(cols):
            node = encode(i, j, rows, cols)
            val = solve(node, half_k)
            ans_row.append(val * 2)
        # print(" ".join(map(str, ans_row)))
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(3)