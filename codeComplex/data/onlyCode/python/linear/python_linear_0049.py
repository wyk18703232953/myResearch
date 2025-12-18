parent = [i for i in range(int(1e5 + 2))]
def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[up] = vp

if __name__ == '__main__':
    n, a, b = map(int, input().split())
    lst = list(map(int, input().split()))
    temp = {lst[i]: i for i in range(n)}
    for i in range(n):
        if a - lst[i] in temp:
            unionSet(i, temp[a - lst[i]])
        else:
            unionSet(i, n)
        if b - lst[i] in temp:
            unionSet(i, temp[b - lst[i]])
        else:
            unionSet(i, n + 1)

    pa = findSet(n)
    pb = findSet(n + 1)
    if pa == pb:
        print('NO')
    else:
        print('YES')
        lst = [0 if findSet(i) == pb else 1 for i in range(n)]
        print(*lst)