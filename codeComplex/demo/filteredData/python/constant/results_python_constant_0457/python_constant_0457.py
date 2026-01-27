def main(n):
    # Deterministically generate three points based on n
    # Point A
    ax = n
    ay = n * 2
    # Point B
    bx = n + 1
    by = n * 2 + 1
    # Point C
    cx = n + 2
    cy = n * 2 + 2

    x = [ax, bx, cx]
    y = [ay, by, cy]

    x.sort()
    y.sort()

    if (x[1] != ax) and (y[1] != ay):
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)