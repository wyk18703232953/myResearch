def main(n):
    # Deterministic generation of input:
    # Original: w, h, n from stdin, then n lines of cuts like "V x" or "H x"
    # Here: interpret n as the number of cuts; set w,h proportional to n
    w = 10 * n + 3
    h = 7 * n + 5
    cuts = []
    for i in range(n):
        # Alternate between vertical and horizontal, positions deterministic modulo dimensions
        if i % 2 == 0:
            x = (i * 3 + 5) % w
            if x == 0:
                x = 1
            cuts.append(("V", x))

        else:
            x = (i * 5 + 7) % h
            if x == 0:
                x = 1
            cuts.append(("H", x))

    # Core logic from original program, adapted to generated data
    res, vrt, hor = [], [], []
    vh = (vrt, hor)
    for i, (c, x) in enumerate(cuts):
        flag = c == 'V'
        vh[flag].append(i)
        res.append([x, flag])

    dim = []
    for tmp, m in zip(vh, (h, w)):
        tmp.sort(key=lambda e: res[e][0])
        u = [None, [0]]
        dim.append(u)
        j = z = 0
        for i in tmp:
            x = res[i][0]
            if z < x - j:
                z = x - j
            j = x
            v = [u, res[i]]
            u.append(v)
            u = v
            res[i].append(u)
        v = [u, [m], None]
        u.append(v)
        dim.append(v)
        if z < m - j:
            z = m - j
        dim.append(z)
    l, r, wmax, u, d, hmax = dim
    whmax = [wmax, hmax]
    for i in range(n - 1, -1, -1):
        x, flag, link = res[i]
        u = whmax[flag]
        res[i] = u * whmax[not flag]
        link[0][2] = link[2]
        link[2][0] = link[0]
        v = link[2][1][0] - link[0][1][0]
        if u < v:
            whmax[flag] = v
    # print('\n'.join(map(str, res)))
    pass
if __name__ == "__main__":
    # Example call for time-complexity experiments
    main(10)