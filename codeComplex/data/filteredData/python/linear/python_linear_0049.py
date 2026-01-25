parent = [i for i in range(int(1e5 + 2))]

def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[up] = vp

def main(n):
    global parent
    parent = [i for i in range(int(1e5 + 2))]
    if n <= 0:
        return
    a = 2 * n
    b = 3 * n
    lst = [i + 1 for i in range(n)]
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
        res = [0 if findSet(i) == pb else 1 for i in range(n)]
        print(*res)

if __name__ == "__main__":
    main(10)