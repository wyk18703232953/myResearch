def main(n):
    # Interpret n as the length of xs, ts and the value of m
    if n <= 0:
        return
    m = n

    # Deterministically generate xs and ts based on n
    xs = [i for i in range(n)]
    ts = [i % 2 for i in range(n)]

    ps = [x for x, t in zip(xs, ts) if t == 0]
    ds = [x for x, t in zip(xs, ts) if t == 1]
    ans = [0] * m

    di = 0
    for pi, p in enumerate(ps):
        while di < m - 1 and abs(ds[di] - p) > abs(ds[di + 1] - p):
            di += 1

        if di >= m:
            ans[m - 1] += n - pi
            break

        ans[di] += 1

    # print(' '.join(map(str, ans)))
    pass
if __name__ == "__main__":
    main(10)