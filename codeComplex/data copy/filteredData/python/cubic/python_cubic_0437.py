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
    best = math.inf
    for v, w in adj[node]:
        val = solve(v, remain - 1, adj, dp, n, m) + w
        if val < best:
            best = val
    dp[key] = best
    return best

def main(n):
    # Interpret n as grid size parameter:
    # n: base parameter
    # rows = n
    # cols = n
    # k   = 2 * n  (even, proportional to n)
    r = n
    c = n
    k = 2 * n

    if k % 2 == 1:
        # This branch will never trigger with k = 2 * n, keep for logic completeness
        res = [[-1] * c for _ in range(r)]
        for row in res:
            # print(" ".join(map(str, row)))
            pass
        return

    total_nodes = r * c
    adj = [[] for _ in range(total_nodes)]

    # Deterministic horizontal edge weights
    # weight formula: (i + 1) * (j + 2)
    for i in range(r):
        weights = [(i + 1) * (j + 2) for j in range(c - 1)]
        for j in range(c - 1):
            cur = encode(i, j, r, c)
            nex = encode(i, j + 1, r, c)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # Deterministic vertical edge weights
    # weight formula: (i + 2) * (j + 1)
    for i in range(r - 1):
        weights = [(i + 2) * (j + 1) for j in range(c)]
        for j in range(c):
            cur = encode(i, j, r, c)
            nex = encode(i + 1, j, r, c)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    half_k = k // 2
    dp_size = r * c * (half_k + 1)
    dp = [-1] * dp_size

    for i in range(r):
        ans_row = []
        for j in range(c):
            node = encode(i, j, r, c)
            val = solve(node, half_k, adj, dp, r, c) * 2
            ans_row.append(val)
        # print(" ".join(map(str, ans_row)))
        pass
if __name__ == "__main__":
    main(3)