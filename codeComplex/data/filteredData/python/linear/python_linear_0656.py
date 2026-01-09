def main(n):
    from collections import Counter

    # Map n to the number of nodes; ensure at least 2 nodes for a tree
    N = max(2, n)
    # Deterministic s based on N
    s = N

    # Build a deterministic tree: a simple path 1-2-3-...-N
    d = Counter()
    for i in range(1, N):
        u, v = i, i + 1
        d[u] += 1
        d[v] += 1

    l = sum(val == 1 for val in d.values())
    ans = s / l * 2
    # print('%.10f' % ans)
    pass
if __name__ == "__main__":
    main(10)