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
    """
    规模参数 n：数组长度
    这里根据 n 自动生成测试数据：
      - 生成 n 个互不相同的整数
      - a, b 也按简单方式生成
    可根据需要自行调整。
    """
    # 简单测试数据生成策略：
    # lst 为 1..n
    lst = list(range(1, n + 1))
    # 令 a, b 为常量或与 n 有关，这里示例用：
    a = n + 3
    b = n + 5

    # 初始化并查集 parent 数组
    max_index = n + 2
    for i in range(max_index):
        parent[i] = i

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
        # print('NO')
        pass

    else:
        # print('YES')
        pass
        tmp = findSet(n + 1)
        ans = [0 if findSet(i) == tmp else 1 for i in range(n)]
        # print(*ans)
        pass


# 示例调用
if __name__ == '__main__':
    # 可修改 n 测试不同规模
    main(5)