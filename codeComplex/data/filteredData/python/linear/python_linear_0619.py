def main(n):
    # Interpret n as both the number of positions and the number of stations
    m = n

    # Deterministic generation of xs and ts based on n
    # xs: 0, 1, 2, ..., n-1
    xs = list(range(n))
    # ts: alternate between 0 and 1 -> deterministic pattern
    ts = [i % 2 for i in range(n)]

    # Core logic from original program
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