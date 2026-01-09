def main(n):
    # Deterministic construction of input array b of length n
    if n <= 0:
        return
    b = [i % 10 + 1 for i in range(n)]

    e = [[-1] * (n + 1) for _ in range(2024)]
    d = [[] for _ in range(n)]

    for i, v in enumerate(b):
        e[v][i] = i
        d[i].append(i)

    for v in range(1, 2024):
        for i in range(n):
            j = e[v][i]
            h = e[v][j + 1] if j != -1 and j + 1 <= n else -1
            if j != -1 and h != -1:
                e[v + 1][i] = h
                d[i].append(h)

    a = [x for x in range(1, n + 1)]
    for s in range(n):
        for pos in d[s]:
            a[pos] = min(a[pos], a[s - 1] + 1 if s > 0 else 1)
    # print(a[n - 1])
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)