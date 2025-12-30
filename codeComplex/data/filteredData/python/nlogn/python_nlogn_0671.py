import random

def check(n, mid, path, cost, num):
    ans, poi, visi = [], [0] * n, [0] * n
    for i in range(n):
        if visi[i]:
            continue
        visi[i], st, st1 = 2, [i], []
        while len(st):
            x, y = st[-1], path[st[-1]]
            if poi[x] == len(y):
                visi[x] = 1
                st1.append(st.pop())
            else:
                i2, j = y[poi[x]], cost[st[-1]][poi[x]]
                poi[x] += 1
                if j <= mid:
                    continue
                if visi[i2] == 2:
                    return -1
                if not visi[i2]:
                    st.append(i2)
                    visi[i2] = 2
        ans += st1
    start = [0] * n
    for ind, i in enumerate(reversed(ans)):
        start[i] = ind
    poi, visi, fin = [0] * n, [0] * n, []
    for i in range(n):
        if visi[i]:
            continue
        visi[i], st = 1, [i]
        while len(st):
            x, y = st[-1], path[st[-1]]
            if poi[x] == len(y):
                st.pop()
            else:
                i2, j, k = y[poi[x]], cost[st[-1]][poi[x]], num[st[-1]][poi[x]]
                poi[x] += 1
                visi[i2] = 1
                st.append(i2)
                if start[i2] < start[x] and j <= mid:
                    fin.append(k)
    return fin

def main(n):
    # 根据规模 n 生成测试数据
    # 生成一个有向图，节点数为 n，边数 m 约为 n*(n-1)//2 的一部分
    max_edges = n * (n - 1) // 2
    m = min(max_edges, max(1, n * 2))  # 控制边数，至少 1 条边
    edges = set()
    while len(edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u == v:
            continue
        if (u, v) in edges:
            continue
        edges.add((u, v))

    path = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    num = [[] for _ in range(n)]

    edge_list = list(edges)
    for idx, (u, v) in enumerate(edge_list, start=1):
        c = random.randint(1, 10**9)
        path[u].append(v)
        cost[u].append(c)
        num[u].append(idx)

    hi, lo = 10**9, 0
    ans = 0
    an = []
    while hi >= lo:
        mid = (hi + lo) // 2
        z = check(n, mid, path, cost, num)
        if z == -1:
            lo = mid + 1
        else:
            hi = mid - 1
            ans = mid
            an = z

    print(ans, len(an))
    if an:
        print(*an)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)