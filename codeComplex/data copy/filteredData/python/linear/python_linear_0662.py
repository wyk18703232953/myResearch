def main(n):
    # n: number of nodes in a path-like tree
    # s: choose deterministically as n for scaling
    if n < 2:
        # For n < 2 the original logic (edges = n-1) does not make sense
        # Define output as 0 to avoid division / meaningless case
        # print(0)
        pass
        return

    s = n
    v = [[]]
    for _ in range(n):
        v.append([])

    # Deterministically build a simple path tree: 1-2-3-...-n
    for i in range(1, n):
        a, b = i, i + 1
        v[a].append(b)
        v[b].append(a)

    ans = 0
    for i in range(1, n + 1):
        if len(v[i]) == 1:
            ans += 1

    # print(2 * s / ans)
    pass
if __name__ == "__main__":
    main(10)