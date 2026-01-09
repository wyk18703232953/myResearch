parent = []


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
    根据规模 n 生成测试数据并执行原逻辑。
    这里构造：
        a = 2 * n
        b = 2 * n + 1
        lst = [1, 2, ..., n]
    你可以按需修改数据生成方式。
    """
    global parent
    # 预留到 n+1（原代码中最大用到 n+1 的下标）
    size = max(100002, n + 2)
    parent = [i for i in range(size)]

    a = 2 * n
    b = 2 * n + 1
    lst = [i + 1 for i in range(n)]  # 一个简单的递增序列作为测试数据

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
    # 示例：调用 main(5)
    main(5)