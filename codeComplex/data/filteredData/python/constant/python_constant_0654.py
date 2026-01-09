def main(n):
    import sys

    # Deterministic data generation based on n
    # Map n to three 2D points with coordinates growing with n
    # Keep structure similar to original: p0, p1, p2 as [x, y]
    p0 = [0, 0]
    p1 = [n, n // 2]
    p2 = [n // 2, n]

    zp = [p0, p1, p2]

    def getpath(p0, p1):
        if p0[0] < p1[0]:
            sp = 1
        elif p0[0] > p1[0]:
            sp = -1

        else:
            sp = 0
        zz = [tuple(p0), tuple(p1)]
        if sp != 0:
            for x in range(p0[0], p1[0] + sp, sp):
                tp = (x, p0[1])
                zz.append(tp)
        if p0[1] < p1[1]:
            sp = 1
        elif p0[1] > p1[1]:
            sp = -1

        else:
            sp = 0
        if sp != 0:
            for y in range(p0[1], p1[1] + sp, sp):
                tp = (p1[0], y)
                zz.append(tp)
        return zz

    nr = 1000000
    zr = set()
    for i in range(3):
        for j in range(3):
            cx = zp[i][0]
            cy = zp[j][1]
            cp = (cx, cy)
            z1 = getpath(cp, zp[0])
            z2 = getpath(cp, zp[1])
            z3 = getpath(cp, zp[2])

            z0 = z1 + z2 + z3
            s1 = set(z0)
            if len(s1) < nr:
                nr = len(s1)
                zr = s1

    # Deterministic output order: sort by x, then y
    zr_list = sorted(zr)
    # print(len(zr_list))
    pass
    for x, y in zr_list:
        # print(x, y)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)