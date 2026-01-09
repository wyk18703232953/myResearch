def main(n):
    from collections import defaultdict

    # Deterministically construct parameters and data based on n
    # Interpret n as number of points
    # Make a and b simple deterministic functions of n
    a = n % 5  # a can be zero or non-zero depending on n
    b = (n // 5) % 7  # not used in logic but kept for structural parity

    XV = []
    # Generate n triples (x, vx, vy) deterministically
    for i in range(n):
        x = i
        vx = (i * 2 + 1) % (max(1, n))
        vy = (i * 3 + 2) % (max(1, n))
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
        # print(ans * 2)
        pass

    else:
        ans = 0
        d = defaultdict(lambda: defaultdict(lambda: 0))
        ds = defaultdict(lambda: 0)
        for x, vx, vy in XV:
            ans += max(0, ds[vy] - d[vy][vx])
            d[vy][vx] += 1
            ds[vy] += 1
        # print(ans * 2)
        pass
if __name__ == "__main__":
    main(10)