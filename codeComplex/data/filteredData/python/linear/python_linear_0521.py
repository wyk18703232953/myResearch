from collections import defaultdict

def main(n):
    if n < 2:
        n = 2

    # Deterministically build a tree on vertices 1..n as a simple chain: 1-2-3-...-n
    t = defaultdict(list)
    for u in range(1, n):
        v = u + 1
        t[u].append(v)
        t[v].append(u)

    # Deterministically build permutation a of 1..n
    # Example: reverse order
    a = list(range(n, 1, -1)) + [1]

    o = {a_: i for i, a_ in enumerate(a)}

    i = 0
    q = [1]
    lv = {1: 0}
    par = {1: 1}
    while i < len(q):
        u = q[i]
        i += 1
        for v in t[u]:
            if v not in lv:
                lv[v] = lv[u] + 1
                q.append(v)
                par[v] = u

    depths = defaultdict(list)
    for x in a:
        depths[lv[x]].append(o[par[x]])

    ans = a[0] == 1
    if ans:
        for d in depths.values():
            if not all(d[i] <= d[i + 1] for i in range(len(d) - 1)):
                ans = False
                break

    if ans:
        l = [lv[x] for x in a]
        ans = all(l[i] <= l[i + 1] for i in range(len(l) - 1))

    print(('No', 'Yes')[ans])


if __name__ == "__main__":
    main(10)