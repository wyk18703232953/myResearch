import random

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
    # 生成测试数据
    # n: 数组大小
    # 生成 ps 中的元素为 1..2n 的不重复随机数
    ps = random.sample(range(1, 2 * n + 1), n)
    # 根据 ps 中的最大值来生成 a, b，保证一定的可配对性
    max_ps = max(ps)
    a = random.randint(max_ps + 1, max_ps + 2 * n)
    b = random.randint(max_ps + 1, max_ps + 2 * n)

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
    # 示例调用，规模可自行修改
    main(5)