def main(n):
    # n: number of points
    # Deterministically generate a, b based on n
    a = n % 10 + 1
    b = (n // 10) % 10 + 1

    dc = {}
    # Deterministically generate n triples (x, vx, vy)
    for i in range(n):
        x = i
        vx = (i * 2) % (n + 1 if n > 0 else 1)
        vy = (i * 3 + 1) % (n + 2 if n > 0 else 1)

        nx = x + vx
        ny = a * x + b + vy
        dd = a * nx - ny + b

        if dd not in dc:
            dc[dd] = {}
        if (vx, vy) not in dc[dd]:
            dc[dd][(vx, vy)] = 0
        dc[dd][(vx, vy)] += 1

    tot = 0
    for _, k in dc.items():
        tt = 0
        pp = 0
        for _, cc in k.items():
            tt -= cc * (cc + 1) // 2
            pp += cc
        tt += pp * (pp + 1) // 2
        tot += tt * 2

    # print(tot)
    pass
if __name__ == "__main__":
    main(10)