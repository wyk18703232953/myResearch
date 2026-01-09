def main(n):
    # Interpret n as the length of arrays a and b, with m equal to n for scale
    # Deterministically generate a and b
    # a: strictly increasing integers
    # b: pattern with 1 every 3rd position (ensures some 1s)
    if n <= 0:
        return
    m = n
    a = [i * 2 for i in range(n)]
    b = [(1 if i % 3 == 0 else 0) for i in range(n)]

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

    output = []
    for i in range(len(a)):
        if b[i] == 1:
            output.append(str(c[i]))
    # print(" ".join(output))
    pass
if __name__ == "__main__":
    main(10)