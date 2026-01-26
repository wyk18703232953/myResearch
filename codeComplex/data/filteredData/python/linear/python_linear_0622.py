def main(n):
    # Interpret n as the length of arrays a and b; also set m = n for compatibility
    if n <= 0:
        return

    m = n

    # Deterministic construction of a and b based on n
    # a: strictly increasing sequence
    a = [i for i in range(1, n + 1)]

    # b: pattern of 0/1 with at least one 1 when possible
    b = [(i % 3 == 0) for i in range(n)]
    if all(x == 0 for x in b):
        b[0] = 1

    l = [None] * (n + m)
    r = [None] * (n + m)
    c = [0] * (n + m)

    x = None
    for i in range(len(a)):
        l[i] = x
        if b[i] == 1:
            x = i

    x = None
    for i in range(len(a) - 1, -1, -1):
        r[i] = x
        if b[i] == 1:
            x = i

    for i in range(len(a)):
        if b[i] == 0:
            aa = a[i]
            ll = l[i]
            rr = r[i]
            if ll is None:
                if rr is not None:
                    c[rr] += 1
            elif rr is None:
                c[ll] += 1

            else:
                if aa - a[ll] <= a[rr] - aa:
                    c[ll] += 1

                else:
                    c[rr] += 1

    out = []
    for i in range(len(a)):
        if b[i] == 1:
            out.append(str(c[i]))
    if out:
        # print(" ".join(out))
        pass
if __name__ == "__main__":
    main(10)