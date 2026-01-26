def findSet(u, parent):
    if parent[u] != u:
        parent[u] = findSet(parent[u], parent)
    return parent[u]

def unionSet(u, v, parent):
    up = findSet(u, parent)
    vp = findSet(v, parent)
    parent[up] = vp

if __name__ == '__main__':
    n, a, b = map(int, input().split())
    lst = list(map(int, input().split()))
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
        print('NO')
    else:
        print('YES')
        lst = [0 if findSet(i, parent) == pb else 1 for i in range(n)]
        print(*lst)