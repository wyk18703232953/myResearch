parent = [i for i in range(int(1e5 + 10))]

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
    max_size = int(1e5 + 10)
    if n + 2 > max_size:
        parent = [i for i in range(n + 3)]
    else:
        parent = [i for i in range(max_size)]
    a = 2 * n
    b = 3 * n + 1
    lst = [(i * 2 + 1) % (2 * n + 3) for i in range(n)]
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
    if findSet(n) == findSet(n + 1):
        print('NO')
    else:
        print('YES')
        tmp = findSet(n + 1)
        lst_out = [0 if findSet(i) == tmp else 1 for i in range(n)]
        print(*lst_out)

if __name__ == "__main__":
    main(10)