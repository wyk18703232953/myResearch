def findSet(u, parents):
    if parents[u] != u:
        parents[u] = findSet(parents[u], parents)
    return parents[u]


def unionSet(u, v, parents, ranks):
    up = findSet(u, parents)
    vp = findSet(v, parents)
    if up == vp:
        return

    if ranks[up] > ranks[vp]:
        parents[vp] = up
    elif ranks[up] < ranks[vp]:
        parents[up] = vp
    else:
        parents[up] = vp
        ranks[vp] += 1


def main(n):
    # 映射：n 为 ps 的长度；a,b 为确定性构造
    if n <= 0:
        return

    a = 2 * n + 1
    b = 2 * n + 3
    ps = list(range(1, n + 1))

    mapping = set(ps)

    parents = {x: x for x in ps}
    parents['A'] = 'A'
    parents['B'] = 'B'
    ranks = {x: 0 for x in ps}
    ranks['A'] = 0
    ranks['B'] = 0

    for x in ps:
        if a - x in mapping:
            unionSet(x, a - x, parents, ranks)
        else:
            unionSet(x, 'B', parents, ranks)

        if b - x in mapping:
            unionSet(x, b - x, parents, ranks)
        else:
            unionSet(x, 'A', parents, ranks)

    if findSet('A', parents) == findSet('B', parents):
        print("NO")
    else:
        print("YES")
        for i in ps:
            if findSet(i, parents) == findSet('A', parents):
                print("0", end=' ')
            else:
                print("1", end=' ')
        print()


if __name__ == "__main__":
    main(10)