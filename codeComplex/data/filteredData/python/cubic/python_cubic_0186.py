def main(n):
    # generate deterministic input
    b = [i % 10 + 1 for i in range(n)]
    max_v = 2024
    e = [[-1] * (n + 1) for _ in range(max_v)]

    d = [[] for _ in range(n)]
    for j, v in enumerate(b):
        if 0 <= v < max_v:
            e[v][j] = j
        d[j].append(j)

    for v in range(1, max_v - 1):
        row_v = e[v]
        row_v1 = e[v + 1]
        for i in range(n):
            j = row_v[i]
            h = row_v[j + 1] if j != -1 and j + 1 <= n else -1
            if j != -1 and h != -1:
                row_v1[i] = h
                d[i].append(h)

    a = [i for i in range(1, n + 1)]
    for s in range(n):
        for idx in d[s]:
            a[idx] = min(a[idx], a[s - 1] + 1 if s > 0 else 1)
    # print(a[n - 1])
    pass
if __name__ == "__main__":
    main(1000)