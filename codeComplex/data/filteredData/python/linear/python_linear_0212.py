def main(n):
    from collections import defaultdict

    # Deterministic parameter generation
    # Interpret n as number of points
    # a and b are fixed deterministically as functions of n
    # To exercise both branches, choose a != 0 for odd n, a == 0 for even n
    if n <= 0:
        return

    if n % 2 == 1:
        a = 1
        b = 2

    else:
        a = 0
        b = 3

    XV = []
    # Deterministic construction of (x, vx, vy)
    for i in range(n):
        x = i
        vx = (i * 2 + 1) % (n + 3)
        vy = (i * 3 + 2) % (n + 5)
        XV.append((x, vx, vy))

    if a != 0:
        ans = 0
        d = defaultdict(int)
        dvx = defaultdict(int)
        dvy = defaultdict(int)
        dvxy = defaultdict(int)
        for x, vx, vy in XV:
            k = -a * vx + vy
            ans += max(
                0,
                d[k] - (dvx[(k, vx)] + dvy[(k, vy)] - dvxy[(k, vx, vy)]),
            )
            d[k] += 1
            dvx[(k, vx)] += 1
            dvy[(k, vy)] += 1
            dvxy[(k, vx, vy)] += 1
        # print(ans * 2)
        pass

    else:
        ans = 0
        d = defaultdict(lambda: defaultdict(int))
        ds = defaultdict(int)
        for x, vx, vy in XV:
            ans += max(0, ds[vy] - d[vy][vx])
            d[vy][vx] += 1
            ds[vy] += 1
        # print(ans * 2)
        pass
if __name__ == "__main__":
    main(10)