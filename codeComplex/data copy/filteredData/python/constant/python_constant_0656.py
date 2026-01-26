def main(n):
    # Deterministically generate three points (xa, ya), (xb, yb), (xc, yc)
    # n controls the coordinate scale; ensure it's at least 3 for some spread
    if n < 3:
        n = 3
    xa, ya = 0, 0
    xb, yb = n // 2, n // 3
    xc, yc = n, n // 2

    if (xb, yb) < (xa, ya):
        xa, ya, xb, yb = xb, yb, xa, ya
    if (xc, yc) < (xa, ya):
        xa, ya, xc, yc = xc, yc, xa, ya
    if xb > xc:
        xb, yb, xc, yc = xc, yc, xb, yb
    d = 1 if ya <= yc else -1
    if ya <= yb <= yc or ya >= yb >= yc:
        # print(xc - xa + abs(yc - ya) + 1)
        pass
        for x in range(xa, xb):
            # print(x, ya)
            pass
        for y in range(ya, yc, d):
            # print(xb, y)
            pass
        for x in range(xb, xc + 1):
            # print(x, yc)
            pass
    elif yb < min(ya, yc):
        # print(xc - xa + max(ya, yc) - yb + 1)
        pass
        for x in range(xa, xc + 1):
            # print(x, min(ya, yc))
            pass
        for y in range(yb, min(ya, yc)):
            # print(xb, y)
            pass
        if ya < yc:
            for y in range(ya + 1, yc + 1):
                # print(xc, y)
                pass

        else:
            for y in range(yc + 1, ya + 1):
                # print(xa, y)
                pass

    else:
        # print(xc - xa + yb - min(ya, yc) + 1)
        pass
        for x in range(xa, xc + 1):
            # print(x, max(ya, yc))
            pass
        for y in range(max(ya, yc) + 1, yb + 1):
            # print(xb, y)
            pass
        if ya < yc:
            for y in range(ya, yc):
                # print(xa, y)
                pass

        else:
            for y in range(yc, ya):
                # print(xc, y)
                pass
if __name__ == "__main__":
    main(10)