def main(n):
    # n controls the magnitude of coordinates; ensure at least 3 for diversity
    if n < 3:
        n = 3

    # Deterministically generate three coordinate pairs based on n
    # Structure inferred: 3 lines, each "a b"
    a1, b1 = 0, 0
    a2, b2 = n // 2, n
    a3, b3 = n, n // 2

    l = []
    l.append((a1, b1))
    l.append((a2, b2))
    l.append((a3, b3))

    l.sort()
    path = []
    path.append(l[0])
    x = l[0][0]
    while x < l[1][0]:
        path.append((x, l[0][1]))
        x = x + 1
    up = False
    if l[0][1] < l[1][1]:
        up = True
    if up:
        y = l[0][1]
        while y <= l[1][1]:
            path.append((l[1][0], y))
            y = y + 1

    else:
        y = l[0][1]
        while y >= l[1][1]:
            path.append((l[1][0], y))
            y = y - 1
    up = False
    if l[1][1] < l[2][1]:
        up = True
    if up:
        y = l[1][1]
        while y <= l[2][1]:
            path.append((l[1][0], y))
            y = y + 1

    else:
        y = l[1][1]
        while y >= l[2][1]:
            path.append((l[1][0], y))
            y = y - 1
    x = l[1][0]
    while x < l[2][0]:
        path.append((x, l[2][1]))
        x = x + 1
    path.append(l[2])
    path = list(set(path))
    # print(len(path))
    pass
    for i in range(len(path)):
        # print(str(path[i][0]) + " " + str(path[i][1]))
        pass
if __name__ == "__main__":
    main(10)