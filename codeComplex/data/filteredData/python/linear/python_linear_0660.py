def main(n):
    # Interpret n as number of nodes in a tree; need at least 2 nodes and s>0
    if n < 2:
        n = 2
    s = n  # deterministic choice of s proportional to n

    a = [0] * (n + 1)

    # Deterministically generate a tree with n nodes
    # Use a simple path: 1-2-3-...-n
    for i in range(1, n):
        u = i
        v = i + 1
        a[u] += 1
        a[v] += 1

    leaf_count = a.count(1)
    if leaf_count == 0:
        result = 0.0

    else:
        result = 2.0 * s / leaf_count
    # print(result)
    pass
if __name__ == "__main__":
    main(10)