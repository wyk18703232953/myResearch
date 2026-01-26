def main(n):
    if n <= 0:
        return 0

    # Deterministically generate b of length n with values in [1, 3023]
    b = [(i % 3023) + 1 for i in range(n)]

    e = [[-1] * (n + 1) for _ in range(3024)]
    d = [[] for _ in range(n)]
    for i, v in enumerate(b):
        e[v][i] = i
        d[i].append(i)
    for v in range(1, 3024):
        for i in range(n):
            j = e[v][i]
            h = e[v][j + 1] if j != -1 and j + 1 <= n else -1
            if j != -1 and h != -1:
                e[v + 1][i] = h
                d[i].append(h)

    a = [i for i in range(1, n + 1)]
    for s in range(n):
        for ee in d[s]:
            a[ee] = min(a[ee], a[s - 1] + 1 if s > 0 else 1)
    return a[n - 1]


if __name__ == "__main__":
    # Example deterministic calls for experimentation
    for size in [1, 5, 10, 50, 100]:
        # print(size, main(size))
        pass