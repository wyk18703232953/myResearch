def main(n):
    # Interpret n as two input integers: a = n, d = 2*n
    a = n
    d = 2 * n

    # Generate deterministic second line: y, g, b
    y = n // 2
    g = n // 3
    b = n // 4 + 1

    m = y * 2 + g
    nn = b * 3 + g
    c = 0
    if m > a:
        c += m - a
    if nn > d:
        c += nn - d
    # print(c)
    pass
if __name__ == "__main__":
    main(10)