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
    """
    n: 问题规模（元素数量）
    本函数内部自动生成测试数据 a, b, lst。
    """

    # 生成测试数据（示例策略，可按需要修改）：
    # a, b 为和目标；lst 为长度为 n 的整数数组
    a = 10
    b = 20
    # 简单生成 lst: 1, 2, ..., n
    lst = list(range(1, n + 1))

    # 重新初始化 parent 数组，保证规模足够
    global parent
    max_index = max(n + 2, int(1e5 + 2))
    parent = [i for i in range(max_index)]

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
        # print('NO')
        pass

    else:
        # print('YES')
        pass
        ans = [0 if findSet(i) == pb else 1 for i in range(n)]
        # print(*ans)
        pass
if __name__ == "__main__":
    # 示例调用
    main(5)