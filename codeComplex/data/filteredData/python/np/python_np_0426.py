def main(n):
    # Interpret n as number of rows; keep m fixed at 8 (since powls has length 10 and bitmask uses first m)
    m = 8
    n = max(1, n)

    # Deterministic data generation for arrmv: n x m matrix
    # Example pattern: arrmv[i][j] = (i * 7 + j * 11) % 1000
    arrmv = [[(i * 7 + j * 11) % 1000 for j in range(m)] for i in range(n)]

    x = 0
    y = int(1e9 + 1)
    sucls = [0, 0]

    powls = [int(pow(2, i)) for i in range(10)]
    twodarray = [0 for _ in range(1 << m)]

    while x + 1 < y:
        mid = x + (y - x) // 2
        for idx in range(len(twodarray)):
            twodarray[idx] = 0

        tols = []
        for topidx, eletop in enumerate(arrmv):
            tmp = 0
            for idx, ele in enumerate(eletop):
                if ele >= mid:
                    tmp += powls[idx]

            if not twodarray[tmp]:
                twodarray[tmp] = 1
                tols.append((tmp, topidx))

        sz = len(tols)
        suc = 0
        no = int(pow(2, m))
        for i in range(sz):
            for j in range(i, sz):
                if (tols[i][0] | tols[j][0]) == no - 1:
                    sucls[0], sucls[1] = tols[i][1], tols[j][1]
                    suc = 1
                    break
            if suc:
                break

        if suc:
            x = mid
        else:
            y = mid

    print(sucls[0] + 1, sucls[1] + 1)


if __name__ == "__main__":
    main(1000)