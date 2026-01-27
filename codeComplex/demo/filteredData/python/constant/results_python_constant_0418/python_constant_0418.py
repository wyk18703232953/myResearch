def main(n):
    # Deterministically generate 8 coordinates for first set and 8 for second set from n
    # Scale coordinates so that ranges grow with n
    # First quadrilateral-like set
    x1 = 0
    y1 = 0
    x2 = n
    y2 = 0
    x3 = n
    y3 = n
    x4 = 0
    y4 = n

    # Second "diamond" or rotated square-like set, shifted and scaled from n
    x11 = n // 2
    y11 = n // 2
    x22 = n + n // 2
    y22 = n // 2
    x33 = n + n // 2
    y33 = n + n // 2
    x44 = n // 2
    y44 = n + n // 2

    min_x1 = min(x1, x2, x3, x4)
    min_y1 = min(y1, y2, y3, y4)
    max_x1 = max(x1, x2, x3, x4)
    max_y1 = max(y1, y2, y3, y4)

    min_x11 = min(x11, x22, x33, x44)
    min_y11 = min(y11, y22, y33, y44)
    max_x11 = max(x11, x22, x33, x44)
    max_y11 = max(y11, y22, y33, y44)

    a = (max_x11 + min_x11) / 2
    b = (max_y11 + min_y11) / 2
    d2 = (max_x11 - min_x11) / 2

    found = False
    for x in range(min_x1, max_x1 + 1):
        for y in range(min_y1, max_y1 + 1):
            if abs(x - a) + abs(y - b) <= d2:
                found = True
                break
        if found:
            break

    if found:
        # print("yes")
        pass

    else:
        # print("no")
        pass
if __name__ == "__main__":
    main(1000)