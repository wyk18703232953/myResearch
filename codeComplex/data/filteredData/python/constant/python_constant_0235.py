def main(n):
    # n controls the scale; original program has fixed-size input:
    # two integers in first line, three integers in second line.
    # Here we deterministically generate them from n.
    a = n
    b = 2 * n
    x = 3 * n
    y = 4 * n
    z = 5 * n

    yell = 2 * x + y
    blue = y + 3 * z
    res = max(0, yell - a) + max(0, blue - b)
    return res

if __name__ == "__main__":
    # example call
    # print(main(10))
    pass