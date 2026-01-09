def main(n):
    # Deterministically generate A, C based on n
    A = n + 1
    C = 2 * n + 3

    def Ro(x, y):
        return A * x - y + C

    # Generate n triples (z, x, y) deterministically
    # Pattern: spread values so that there are repeated Ro(x+z, z*A+y) and x
    triples = []
    for i in range(n):
        z = i % (max(1, n // 3))
        x = (i // 2) % (max(1, n // 4) + 1)
        y = (i * 3 + 1) % (max(1, n // 5) + 2)
        triples.append((z, x, y))

    huh = []
    for z, x, y in triples:
        huh.append((Ro(x + z, z * A + y), x))

    huh = sorted(huh)
    anss = 0
    c1 = 0
    c2 = 0
    prev = (-9999999999999, -999999999999999)
    g = []

    huh.append((-9999999999999, -999999999999999))
    for huhh in huh:
        if huhh[0] != prev[0]:
            g.append(c1)
            for j in g:
                anss += (c2 - j) * j
            g = []
            c1 = 1
            c2 = 1
            prev = (huhh[0], huhh[1])
            continue
        c2 += 1
        if huhh[1] != prev[1]:
            g.append(c1)
            c1 = 0
            prev = (huhh[0], huhh[1])
        c1 += 1

    # print(anss)
    pass
if __name__ == "__main__":
    main(1000)