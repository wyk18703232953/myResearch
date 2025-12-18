n, m = map(int, input().split())

a = []


def is_center(a, y, x):
    count1 = count2 = count3 = count4 = 0
    # up
    y1 = y
    x1 = x
    while True:
        y2 = y1 - 1
        if y2 < 0:
            break
        c = a[y2][x]
        if c == "W":
            break
        count1 += 1
        y1 = y2

    # down
    y1 = y
    x1 = x
    while True:
        y2 = y1 + 1
        if y2 == n:
            break
        c = a[y2][x]
        if c == "W":
            break
        count2 += 1
        y1 = y2

    # left
    y1 = y
    x1 = x
    while True:
        x2 = x1 - 1
        if x2 < 0:
            break
        c = a[y1][x2]
        if c == "W":
            break
        count3 += 1
        x1 = x2

    # right
    y1 = y
    x1 = x
    while True:
        x2 = x1 + 1
        if x2 == m:
            break
        c = a[y1][x2]
        if c == "W":
            break
        count4 += 1
        x1 = x2

    return count1 == count2 == count3 == count4 and a[y][x] == "B"


for k in range(n):
    s = input()
    a.append(s)


for y in range(n):
    c = False
    for x in range(m):
        if is_center(a, y, x):
            print(y+1, x+1)
            c = True
            break
    if c:
        break


