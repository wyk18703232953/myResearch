def find(u, par):
    if u != par[u]:
        par[u] = find(par[u], par)
    return par[u]

def union(u, v, par):
    u = find(u, par)
    v = find(v, par)
    par[u] = v

def core_logic(n, a, b, p):
    mp = dict()
    for i in range(n):
        mp[p[i]] = i + 1
    par = [i for i in range(n + 2)]

    for i in range(n):
        union(i + 1, mp.get(a - p[i], n + 1), par)
        union(i + 1, mp.get(b - p[i], 0), par)

    A = find(0, par)
    B = find(n + 1, par)

    if A != B:
        res = ['1' if find(i, par) == B else '0' for i in range(1, n + 1)]
        return "YES\n" + " ".join(res)

    else:
        return "NO"

def main(n):
    a = 2 * n + 3
    b = 3 * n + 5
    p = [(i * 2 + 1) % (4 * n + 7) for i in range(n)]
    result = core_logic(n, a, b, p)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)