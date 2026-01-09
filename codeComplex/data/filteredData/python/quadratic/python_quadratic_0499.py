def main(n):
    if n <= 0:
        return
    vis = [0] * n
    st = [0] * n
    if n == 1:
        # print(1)
        pass
        return

    def dfs(g, e):
        if vis[e] == 1:
            return
        vis[e] = 1
        for i in g[e]:
            dfs(g, i)
        if len(g[e]) == 1 and e != 0:
            st[e] += 1
        for i in g[e]:
            st[e] += st[i]

    # Deterministic generation of array a of length n-1 with values in [0, n-1]
    # Original code uses 1-based then subtracts 1, so we keep 0-based here.
    # Pattern: parent of node i+1 is (i * 2) % (i+1), then clipped to [0, n-1].
    a = [((i * 2) % (i + 1)) for i in range(n - 1)]
    a = [min(x, n - 1) for x in a]

    g = [[] for _ in range(n)]
    for i in range(n - 1):
        g[i + 1].append(a[i])
        g[a[i]].append(i + 1)

    dfs(g, 0)
    st.sort()
    # print(*st)
    pass
if __name__ == "__main__":
    main(10)