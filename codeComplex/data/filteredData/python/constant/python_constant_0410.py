def main(n):
    # Deterministic data generation based on n
    # Map n to 16 integers: a, b, c, d, e, f, g, h, i, j, k, l, m, o, p
    # Stay in a small range to keep numbers reasonable
    vals = [((i * 37 + n * 13) % 101) - 50 for i in range(16)]
    a, b, c, d, e, f, g, h, i, j, k, l, m, nn, o, p = vals

    s1 = [[a, b], [c, d], [e, f], [g, h]]
    s1.sort()
    bleft = s1[0]
    tr = s1[3]
    u, v, w, x = bleft[0], bleft[1], tr[0], tr[1]

    def check(xd, dx, u, v, w, x):
        return (u <= xd and xd <= w and v <= dx and dx <= x)

    god = [(i + k + m + o) / 4, (j + l + nn + p) / 4]
    nani = 0
    for moo in [[i, j], [k, l], [m, nn], [o, p]]:
        if check(moo[0], moo[1], u, v, w, x):
            return "Yes"

    if check(god[0], god[1], u, v, w, x):
        nani += 1

    i, j = i + j, i - j
    k, l = k + l, k - l
    m, nn = m + nn, m - nn
    o, p = o + p, o - p

    a, b = a + b, a - b
    c, d = c + d, c - d
    e, f = e + f, e - f
    g, h = g + h, g - h

    a, b, c, d, e, f, g, h, i, j, k, l, m, nn, o, p = (
        i,
        j,
        k,
        l,
        m,
        nn,
        o,
        p,
        a,
        b,
        c,
        d,
        e,
        f,
        g,
        h,
    )

    s1 = [[a, b], [c, d], [e, f], [g, h]]
    s1.sort()
    bleft = s1[0]
    tr = s1[3]
    u, v, w, x = bleft[0], bleft[1], tr[0], tr[1]

    def check2(xd, dx, u, v, w, x):
        return (u <= xd and xd <= w and v <= dx and dx <= x)

    god = [(i + k + m + o) / 4, (j + l + nn + p) / 4]

    for moo in [[i, j], [k, l], [m, nn], [o, p]]:
        if check2(moo[0], moo[1], u, v, w, x):
            return "Yes"

    if check2(god[0], god[1], u, v, w, x):
        nani += 1
    if nani == 2:
        return "Yes"

    return "No"


if __name__ == "__main__":
    # Example: run main with a chosen scale n and print result
    result = main(1000)
    # print(result)
    pass