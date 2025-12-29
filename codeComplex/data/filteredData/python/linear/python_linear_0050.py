def findSet(u, parent):
    if parent[u] != u:
        parent[u] = findSet(parent[u], parent)
    return parent[u]


def unionSet(u, v, parent):
    up = findSet(u, parent)
    vp = findSet(v, parent)
    parent[up] = vp


def main(n):
    # 生成测试数据：简单构造一个可行的例子
    # 这里设置：
    #   lst = [0, 1, 2, ..., n-1]
    #   a = n - 1
    #   b = 2 * (n - 1)
    a = n - 1
    b = 2 * (n - 1)
    lst = list(range(n))

    parent = [i for i in range(n + 2)]
    temp = {lst[i]: i for i in range(n)}

    for i in range(n):
        # 处理 a
        if a - lst[i] in temp:
            unionSet(i, temp[a - lst[i]], parent)
        else:
            unionSet(i, n, parent)
        # 处理 b
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
        ans = [0 if findSet(i, parent) == pb else 1 for i in range(n)]
        print(*ans)


if __name__ == '__main__':
    # 示例：调用 main，规模 n 可按需修改
    main(5)