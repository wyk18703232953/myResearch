import sys
from math import floor, ceil
#sys.stdin = open('input.txt', 'r')
r = lambda: sys.stdin.readline().strip()

a = [[0] * 2 for i in range(3)]


def abs(x):
    if x < 0:
        x = -x
    return x


def calcLen(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2) + 1


def main():
    a[0][0], a[0][1] = map(int, r().split())
    a[1][0], a[1][1] = map(int, r().split())
    a[2][0], a[2][1] = map(int, r().split())
    xMax = max(a[0][0], a[1][0], a[2][0])
    xMin = min(a[0][0], a[1][0], a[2][0])
    yMax = max(a[0][1], a[1][1], a[2][1])
    yMin = min(a[0][1], a[1][1], a[2][1])

    pathLen = xMax - xMin + yMax - yMin + 1
    for i in range(3):
        for j in range(3):
            px = a[i][0]
            py = a[j][1]
            sum = 0
            for k in range(3):
                sum += (calcLen(a[k][0], a[k][1], px, py))
            sum -= 2
            if sum == pathLen:
                break
        if sum == pathLen:
            break
    sq = [[0]*(yMax+1) for i in range(xMax+1)]
    for i in range(3):
        if px == a[i][0]:
            c = -1
            if py > a[i][1]:
                c = 1
            for j in range(a[i][1], py, c):
                sq[px][j]=1
        elif py== a[i][1]:
            c = -1
            if px > a[i][0]:
                c= 1
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
                c= 1
            for j in range(a[i][0], px, c):
                sq[j][py] = 1
    sq[px][py] = 1
    ans = []
    for i in range(xMax + 1):
        for j in range(yMax + 1):
            if sq[i][j] == 1:
                ans.append((i, j))
    print(len(ans))
    for i in ans:
        print(i[0], i[1])

main()
