def main(n):
    # generate deterministic input of size n
    b = [(i % 10) + 1 for i in range(n)]
    e = [[-1] * (n + 1) for _ in range(2002)]

    d = [[] for _ in range(n)]
    for i, v in enumerate(b):
        e[v][i] = i
        d[i].append(i)

    for v in range(1, 2002):
        for i in range(n):
            j = e[v][i]
            h = e[v][j + 1] if j != -1 and j + 1 <= n else -1
            if j != -1 and h != -1:
                e[v + 1][i] = h
                d[i].append(h)

    a = [x for x in range(1, n + 1)]
    for s in range(n):
        for e_idx in d[s]:
            a[e_idx] = min(a[e_idx], a[s - 1] + 1 if s > 0 else 1)
    # print(a[n - 1])
    pass
if __name__ == "__main__":
    main(1000)