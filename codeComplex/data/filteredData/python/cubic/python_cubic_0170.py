def main(n):
    if n <= 0:
        return 0

    # Deterministically generate input list b of length n
    b = [(i * 2 + 1) % 7 + 1 for i in range(n)]

    d = [[b[i] if i == j else -1 for i in range(n)] for j in range(n)]

    def f(i, j):
        if d[i][j] != -1:
            return d[i][j]
        d[i][j] = 0
        for m in range(i, j):
            l = f(i, m)
            if f(m + 1, j) == l and l:
                d[i][j] = l + 1
                break
        return d[i][j]

    a = [x for x in range(1, n + 1)]
    for e in range(1, n):
        for s in range(e + 1):
            if f(s, e):
                a[e] = min(a[e], (a[s - 1] + 1) if s > 0 else a[s])
    return a[-1]


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    result = main(10)
    # print(result)
    pass