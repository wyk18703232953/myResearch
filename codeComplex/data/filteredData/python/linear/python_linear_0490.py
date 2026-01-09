def main(n):
    # Interpret n as number of nodes in a tree (n >= 1)
    if n <= 1:
        # print(0)
        pass
        return

    # Deterministically generate a tree with n nodes
    # Here: a simple chain 1-2-3-...-n
    g = dict()
    for i in range(n - 1):
        u = i
        v = i + 1
        g.setdefault(u, []).append(v)
        g.setdefault(v, []).append(u)

    st = [0]
    rank = [0] * n
    tree = [0] * n
    msk = [0] * n
    rd = dict()

    while len(st) > 0:
        top = st.pop()
        msk[top] = 1
        for c in g.get(top, []):
            if msk[c] == 0:
                st.append(c)
                tree[c] = top
                rank[c] = rank[top] + 1
                rd.setdefault(rank[c], []).append(c)

    max_rank = max(rank)
    reach = [0] * n
    build = [0] * n

    for r in range(max_rank, 2, -1):
        for node in rd.get(r, []):
            if reach[node] == 0:
                reach[node] = 1
                reach[tree[node]] = 1
                reach[tree[tree[node]]] = 1
                build[tree[node]] = 1

    # print(sum(build))
    pass
if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10)