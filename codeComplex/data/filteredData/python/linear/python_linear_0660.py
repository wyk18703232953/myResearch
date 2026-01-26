def main(n):
    # n: number of nodes in a tree (n >= 2 recommended)

    if n <= 1:
        # Degenerate case: no edges, no leaves
        # print(0.0)
        pass
        return

    # Deterministically construct a path tree: 1-2-3-...-n
    a = [0] * (n + 1)
    for i in range(1, n):
        u = i
        v = i + 1
        a[u] += 1
        a[v] += 1

    # Deterministically set s as a simple function of n
    s = n

    cnt_leaf = a.count(1)
    if cnt_leaf == 0:
        # print(0.0)
        pass

    else:
        # print(2.0 * s / cnt_leaf)
        pass
if __name__ == "__main__":
    # Example deterministic call
    main(10)