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
    """
    n: problem size
    本函数内部自动生成测试数据 p, a, b，并打印原程序的输出。
    生成规则示例：
      p: 1..n 的一个排列
      a: n
      b: 2*n
    """
    # 生成测试数据
    p = list(range(1, n + 1))
    a = n
    b = 2 * n

    # 需要用到索引 0..n+1
    limit = n + 1
    makeSet(limit)

    pos = dict()
    for i in range(n):
        pos[p[i]] = i + 1

    for i in range(n):
        unionSet(i + 1, pos.get(a - p[i], n + 1))
        unionSet(i + 1, pos.get(b - p[i], 0))

    A = findSet(0)
    B = findSet(n + 1)

    if A != B:
        # print('YES')
        pass
        out = []
        for i in range(1, n + 1):
            if findSet(i) == B:
                out.append('1')

            else:
                out.append('0')
        # print(' '.join(out))
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)