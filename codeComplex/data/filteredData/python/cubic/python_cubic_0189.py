def main(n):
    # Deterministically generate input array b of length n
    # Values are in [0, 2047] to fit the original e table indexing
    b = [(i * 37) % 2048 for i in range(n)]

    e = [[-1] * (n + 1) for _ in range(2048)]
    d = [[] for _ in range(n)]

    for i, v in enumerate(b):
        if 0 <= v < 2048:
            e[v][i] = i
        d[i].append(i)

    for v in range(1, 2047):  # v+1 must be < 2048
        for i in range(n):
            j = e[v][i]
            if j != -1:
                if j + 1 <= n:
                    h = e[v][j + 1]

                else:
                    h = -1

            else:
                h = -1
            if j != -1 and h != -1:
                e[v + 1][i] = h
                d[i].append(h)

    a = [i for i in range(1, n + 1)]
    for s in range(n):
        for idx in d[s]:
            if s > 0:
                temp = a[s - 1] + 1

            else:
                temp = 1
            a[idx] = min(a[idx], temp)

    # print(a[n - 1])
    pass
if __name__ == "__main__":
    main(1000)