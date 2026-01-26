def push(d, u, v):
    if u not in d:
        d[u] = []
    if v not in d:
        d[v] = []
    d[u].append(v)
    d[v].append(u)

def push_v(d, u, val):
    if u not in d:
        d[u] = 0
    d[u] += val

def main(n):
    # Deterministic generation of n, k, and the tree
    if n < 3:
        n_eff = 3

    else:
        n_eff = n

    # Define k as a deterministic function of n
    # Example: height for a complete 3-ary tree-like structure
    k = max(1, n_eff // 3)

    g = {}

    # Generate a deterministic tree:
    # We'll build a star-like tree where node 1 is the center
    # and all other nodes are leaves. This is deterministic and
    # simple, and respects the tree constraints.
    for v in range(2, n_eff + 1):
        u = 1
        push(g, u, v)

    deg1 = []
    used = [0] * (n_eff + 1)

    for u in g:
        if len(g[u]) == 1:
            used[u] = 1
            deg1.append(u)

    flg = True
    kk = k  # local copy so original k isn't modified outside logic

    while kk > 0:
        if kk >= 1 and len(deg1) < 3:
            flg = False
            break

        cnt = {}
        for u in deg1:
            for v in g[u]:
                if used[v] == 0:
                    push_v(cnt, v, 1)

        for v in deg1:
            used[v] = 1

        deg1 = []

        for v, val in cnt.items():
            if val < 3:
                flg = False
                break
            deg1.append(v)

        if flg is False:
            break
        kk -= 1

    if flg is True and len(deg1) > 1:
        flg = False

    if flg is False:
        # print('NO')
        pass

    else:
        # print('YES')
        pass
if __name__ == "__main__":
    main(10)