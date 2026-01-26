def check(map1, map2, n):
    f = True
    for i in range(n):
        for j in range(n):
            if map1[i][j] != map2[i][j]:
                f = False
                break
        if not f:
            break
    if f:
        return True

    f = True
    for i in range(n):
        for j in range(n):
            if map1[i][j] != map2[n - 1 - i][j]:
                f = False
                break
        if not f:
            break
    if f:
        return True

    f = True
    for i in range(n):
        for j in range(n):
            if map1[i][j] != map2[i][n - 1 - j]:
                f = False
                break
        if not f:
            break
    if f:
        return True

    return False


def rotate(map1, n):
    wk1 = []
    for i in range(n):
        wk1.append([])
        for j in range(n):
            wk1[i].append(map1[i][j])

    for i in range(n):
        for j in range(n):
            map1[i][j] = wk1[j][n - 1 - i]


def generate_maps(n):
    # generate two n x n character matrices deterministically
    map1 = []
    map2 = []
    for i in range(n):
        row1 = []
        row2 = []
        for j in range(n):
            row1.append('#' if (i + j) % 2 == 0 else '.')
            row2.append('#' if (i * n + j) % 3 == 0 else '.')
        map1.append(row1)
        map2.append(row2)
    return map1, map2


def main(n):
    if n <= 0:
        return
    map1, map2 = generate_maps(n)
    f = False
    for _ in range(4):
        if check(map1, map2, n):
            f = True
            break
        rotate(map1, n)
    if f:
        # print("Yes")
        pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    main(5)