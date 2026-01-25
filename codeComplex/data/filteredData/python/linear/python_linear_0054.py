MAX = 100001
parent = []

def makeSet(limit):
    global parent
    parent = [i for i in range(limit + 1)]

def findSet(u):
    global parent
    if u != parent[u]:
        parent[u] = findSet(parent[u])
    return parent[u]

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[up] = vp

def main(n):
    if n <= 0:
        return

    # 映射：n 为数组长度
    # 构造确定性的 a, b, p
    a = 2 * n + 3
    b = 3 * n + 5
    p = [(i * 7 + 3) % (2 * n + 11) for i in range(1, n + 1)]

    limit = max(n + 1, 2 * n + 11)
    makeSet(limit)

    pos = {}
    for i in range(n):
        pos[p[i]] = i + 1

    for i in range(n):
        unionSet(i + 1, pos.get(a - p[i], n + 1))
        unionSet(i + 1, pos.get(b - p[i], 0))

    A = findSet(0)
    B = findSet(n + 1)

    if A != B:
        print('YES')
        for i in range(1, n + 1):
            if findSet(i) == B:
                print('1', end=" ")
            else:
                print('0', end=" ")
    else:
        print('NO')

if __name__ == "__main__":
    main(10)