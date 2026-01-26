def main(n):
    # Deterministic generation of input array b of length n
    # Values in b are in [1, 2023] to match the original algorithm's value range
    if n <= 0:
        # print(0)
        pass
        return

    b = [(i % 2023) + 1 for i in range(n)]

    e = [[-1] * (n + 1) for _ in range(2024)]

    d = [[] for _ in range(n)]
    for i, v in enumerate(b):
        e[v][i] = i
        d[i].append(i)

    for v in range(1, 2024):
        row_v = e[v]
        row_v1 = e[v + 1]
        for i in range(n):
            j = row_v[i]
            if j != -1:
                h = row_v[j + 1]
                if h != -1:
                    row_v1[i] = h
                    d[i].append(h)

    a = [i for i in range(1, n + 1)]
    for s in range(n):
        prev_val = a[s - 1] + 1 if s > 0 else 1
        for pos in d[s]:
            if prev_val < a[pos]:
                a[pos] = prev_val

    # print(a[n - 1])
    pass
if __name__ == "__main__":
    main(1000)