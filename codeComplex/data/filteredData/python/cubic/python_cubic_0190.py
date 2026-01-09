def main(n):
    # Deterministically generate input array b of length n
    # Values are in [1, 2023] to match the range used in original code
    if n <= 0:
        return 0
    b = [(i % 2023) + 1 for i in range(n)]

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
    result = a[n - 1]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(1000)