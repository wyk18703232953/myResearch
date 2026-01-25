def findSet(u, parent):
    if parent[u] != u:
        parent[u] = findSet(parent[u], parent)
    return parent[u]

def unionSet(u, v, parent):
    up = findSet(u, parent)
    vp = findSet(v, parent)
    parent[up] = vp

def run_algorithm(n, a, b, lst):
    parent = [i for i in range(n + 2)]
    temp = {lst[i]: i for i in range(n)}
    for i in range(n):
        if a - lst[i] in temp:
            unionSet(i, temp[a - lst[i]], parent)
        else:
            unionSet(i, n, parent)
        if b - lst[i] in temp:
            unionSet(i, temp[b - lst[i]], parent)
        else:
            unionSet(i, n + 1, parent)

    pa = findSet(n, parent)
    pb = findSet(n + 1, parent)
    if pa == pb:
        return "NO", None
    else:
        lst_res = [0 if findSet(i, parent) == pb else 1 for i in range(n)]
        return "YES", lst_res

def main(n):
    if n < 1:
        n = 1
    a = 2 * n + 3
    b = 3 * n + 5
    lst = [i * 2 + (i % 3) for i in range(n)]
    res, arr = run_algorithm(n, a, b, lst)
    print(res)
    if arr is not None:
        print(*arr)

if __name__ == "__main__":
    main(10)