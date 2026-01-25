def main(n):
    # 映射：给定规模 n，构造一个三元组作为原程序输入 (N, d, k)
    # 为了保证：
    # - 当 n 很小时，仍然有合法输入
    # - 当 n 变大时，原问题规模也随之增长
    #
    # 这里约定：
    #   N = max(3, n)
    #   d = min(N - 1, max(1, n // 3))
    #   k = min(N - 1, max(1, n // 4 + 1))
    #
    # 这样：
    # - N 随 n 线性增长
    # - d, k 也是 n 的确定性函数
    if n < 1:
        # 对于非正规模，直接不做任何事情
        return

    N = max(3, n)
    d = min(N - 1, max(1, n // 3))
    k = min(N - 1, max(1, n // 4 + 1))

    # 以下为原程序核心逻辑，去除所有输入依赖
    if N <= d:
        print('NO')
        return
    if k == 1 and N > 2:
        print('NO')
        return

    edgestot = []
    edges = [[] for _ in range(N)]
    tovisit = []

    for i in range(d):
        edgestot.append([i, i + 1])
        tovisit.append([i + 1, min(i + 1, d - i - 1)])
        edges[i].append(i + 1)
        edges[i + 1].append(i)

    cur = d + 1
    while cur < N and len(tovisit) > 0:
        x = tovisit.pop()
        if x[1] == 0:
            continue
        while len(edges[x[0]]) < k and cur < N:
            tovisit.append([cur, x[1] - 1])
            edgestot.append([cur, x[0]])
            edges[x[0]].append(cur)
            edges[cur].append(x[0])
            cur += 1

    if len(edgestot) == N - 1:
        print('YES')
        for i in range(N - 1):
            print(edgestot[i][0] + 1, edgestot[i][1] + 1)
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模进行一次运行
    main(10)