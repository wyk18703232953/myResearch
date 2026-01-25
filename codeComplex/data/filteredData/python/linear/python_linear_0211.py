def main(n):
    from collections import defaultdict

    # Deterministic parameter generation
    # Map n to:
    # - number of points: n
    # - a, b: simple deterministic functions of n
    a = n % 5  # a can be zero or non-zero depending on n
    b = (n * 3 + 1) % 7

    XV = []
    for i in range(n):
        x = i
        vx = (i * 2 + 1) % (n + 1 if n > 0 else 1)
        vy = (i * 3 + 2) % (n + 2 if n > 0 else 1)
        XV.append((x, vx, vy))

    if a != 0:
        ans = 0
        d = defaultdict(lambda: 0)
        dvx = defaultdict(lambda: 0)
        for x, vx, vy in XV:
            k = -a * vx + vy
            ans += max(0, d[k] - dvx[(k, vx)])
            d[k] += 1
            dvx[(k, vx)] += 1
        print(ans * 2)
    else:
        ans = 0
        d = defaultdict(lambda: defaultdict(lambda: 0))
        ds = defaultdict(lambda: 0)
        for x, vx, vy in XV:
            ans += max(0, ds[vy] - d[vy][vx])
            d[vy][vx] += 1
            ds[vy] += 1
        print(ans * 2)


if __name__ == "__main__":
    main(1000)