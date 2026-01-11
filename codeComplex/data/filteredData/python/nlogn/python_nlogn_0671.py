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

def generate_graph(n):
    if n <= 1:
        return 1, [[]], [[]], [[]]
    m = n * n
    path = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    num = [[] for _ in range(n)]
    edge_id = 1
    for u in range(n):
        for v in range(n):
            c = (u * n + v) + 1
            path[u].append(v)
            cost[u].append(c)
            num[u].append(edge_id)
            edge_id += 1
    return m, path, cost, num

def main(n):
    if n < 1:
        return
    m, path, cost, num = generate_graph(n)
    hi, lo = 10 ** 9, 0
    ans = hi
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
    # print(ans, len(an))
    pass

    if an:
        # print(*an)
        pass
if __name__ == "__main__":
    main(5)