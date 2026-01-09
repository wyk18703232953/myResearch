def main(n):
    from collections import Counter

    # Interpret n as number of nodes in a tree (same as original n)
    # Generate a deterministic tree: star-shaped with center 1
    num_nodes = max(2, n)  # at least 2 nodes to avoid division by zero
    s = num_nodes  # deterministic mapping for s

    d = Counter()
    # Generate edges: (1, i) for i in 2..num_nodes
    for v in range(2, num_nodes + 1):
        u = 1
        d[u] += 1
        d[v] += 1

    l = sum(v == 1 for v in d.values())
    ans = s / l * 2
    # print('%.10f' % (ans,))
    pass
if __name__ == "__main__":
    main(10)