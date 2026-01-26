def main(n):
    # Deterministically generate inputs based on n
    # yellow, blue
    yellow = n
    blue = 2 * n

    # y, g, b
    y = n // 2
    g = n // 3
    b = n // 4

    count = 0

    yt = y * 2 + g
    bt = g + b * 3

    yc = yellow - yt
    if yc < 0:
        count += -yc

    bc = blue - bt
    if bc < 0:
        count += -bc

    # print(count)
    pass
if __name__ == "__main__":
    main(10)