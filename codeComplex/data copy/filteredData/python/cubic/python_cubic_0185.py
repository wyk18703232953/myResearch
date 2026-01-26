def main(n):
    # Generate deterministic input
    # Original input: n, then list b of length n with integer values used as indices up to 2023
    # We map n to list length, and values in [1, 2023]
    if n <= 0:
        return
    b = [(i % 2023) + 1 for i in range(n)]

    e = [[-1] * (n + 1) for _ in range(2024)]
    d = [[] for _ in range(n)]

    for i, v in enumerate(b):
        e[v][i] = i
        d[i].append(i)

    for v in range(1, 2024):
        row_v = e[v]
        row_v1 = e[v + 1] if v + 1 < 2024 else None
        for i in range(n):
            j = row_v[i]
            h = row_v[j + 1] if j != -1 and j + 1 <= n else -1
            if j != -1 and h != -1:
                row_v1[i] = h
                d[i].append(h)

    a = [i for i in range(1, n + 1)]
    for s in range(n):
        for pos in d[s]:
            a[pos] = min(a[pos], a[s - 1] + 1 if s > 0 else 1)

    # print(a[n - 1])
    pass
if __name__ == "__main__":
    main(10)