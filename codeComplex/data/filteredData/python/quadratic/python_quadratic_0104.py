def rotate(li, n):
    newli = []
    for x in range(n):
        newli.append([])
        newli[x] = li[x].copy()
    for x in range(n):
        for y in range(n):
            newli[x][y] = li[n - 1 - y][x]
    return newli

def flipV(li, n):
    newli = []
    for x in range(n):
        newli.append([])
        newli[x] = li[x].copy()
    newli.reverse()
    return newli

def flipH(li, n):
    newli = []
    for x in range(n):
        newli.append([])
        newli[x] = li[x].copy()
    for x in range(n):
        newli[x].reverse()
    return newli

def main(n):
    li1, li2, li3, templi = [], [], [], []

    for x in range(n):
        li1.append([])
        li2.append([])
        li3.append([])
        templi.append([])

    for x in range(n):
        li1[x] = [chr(ord('a') + (x + y) % 26) for y in range(n)]

    for x in range(n):
        li2[x] = [chr(ord('a') + (x * 2 + y * 3) % 26) for y in range(n)]

    if li1 == li2:
        # print('Yes')
        pass
        return

    templi = flipH(li2, n)
    if li1 == templi:
        # print('Yes')
        pass
        return

    templi = flipV(li2, n)
    if li1 == templi:
        # print('Yes')
        pass
        return

    templi = rotate(li2, n)
    if li1 == templi:
        # print('Yes')
        pass
        return

    templi = rotate(templi, n)
    if li1 == templi:
        # print('Yes')
        pass
        return

    templi = rotate(templi, n)
    if li1 == templi:
        # print('Yes')
        pass
        return

    templi = flipH(li2, n)
    templi = rotate(templi, n)
    if li1 == templi:
        # print('Yes')
        pass
        return

    templi = rotate(templi, n)
    if li1 == templi:
        # print('Yes')
        pass
        return

    templi = rotate(templi, n)
    if li1 == templi:
        # print('Yes')
        pass
        return

    # print('No')
    pass
if __name__ == "__main__":
    main(5)