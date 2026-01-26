def main(n):
    from collections import Counter

    # Deterministic generation of (n, s) and edges
    # n: number of nodes in a tree
    # s: some total value; choose a simple deterministic function of n
    if n < 2:
        n = 2
    s = n * (n + 1) // 2

    # Build a simple path tree: 1-2-3-...-n
    d = Counter()
    for i in range(1, n):
        u, v = i, i + 1
        d[u] += 1
        d[v] += 1

    l = sum(v == 1 for v in d.values())
    ans = s / l * 2
    # print('%.10f' % (ans,))
    pass
if __name__ == "__main__":
    main(10)