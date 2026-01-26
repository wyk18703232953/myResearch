import sys
from math import floor, ceil

a = [[0] * 2 for _ in range(3)]


def abs_val(x):
    if x < 0:
        x = -x
    return x


def calcLen(x1, y1, x2, y2):
    return abs_val(x1 - x2) + abs_val(y1 - y2) + 1


def core():
    xMax = max(a[0][0], a[1][0], a[2][0])
    xMin = min(a[0][0], a[1][0], a[2][0])
    yMax = max(a[0][1], a[1][1], a[2][1])
    yMin = min(a[0][1], a[1][1], a[2][1])

    pathLen = xMax - xMin + yMax - yMin + 1
    for i in range(3):
        for j in range(3):
            px = a[i][0]
            py = a[j][1]
            s = 0
            for k in range(3):
                s += calcLen(a[k][0], a[k][1], px, py)
            s -= 2
            if s == pathLen:
                break
        if s == pathLen:
            break
    sq = [[0] * (yMax + 1) for _ in range(xMax + 1)]
    for i in range(3):
        if px == a[i][0]:
            c = -1
            if py > a[i][1]:
                c = 1
            for j in range(a[i][1], py, c):
                sq[px][j] = 1
        elif py == a[i][1]:
            c = -1
            if px > a[i][0]:
                c = 1
            for j in range(a[i][0], px, c):
                sq[j][py] = 1

        else:
            c = -1
            if py > a[i][1]:
                c = 1
            for j in range(a[i][1], py + c, c):
                sq[a[i][0]][j] = 1

            c = -1
            if px > a[i][0]:
                c = 1
            for j in range(a[i][0], px, c):
                sq[j][py] = 1
    sq[px][py] = 1
    ans = []
    for i in range(xMax + 1):
        for j in range(yMax + 1):
            if sq[i][j] == 1:
                ans.append((i, j))
    # print(len(ans))
    pass
    for i in ans:
        # print(i[0], i[1])
        pass


def main(n):
    # Deterministically generate 3 points based on n
    # Coordinate range grows with n to make the scale meaningful
    # Example mapping (all non-negative to avoid negative indices):
    # a[0] = (n, 2n)
    # a[1] = (2n, 3n)
    # a[2] = (3n, n)
    # Ensure n >= 1 for meaningful behavior
    if n < 1:
        n = 1
    a[0][0], a[0][1] = n, 2 * n
    a[1][0], a[1][1] = 2 * n, 3 * n
    a[2][0], a[2][1] = 3 * n, n
    core()


if __name__ == "__main__":
    main(10)