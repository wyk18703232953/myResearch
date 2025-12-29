from math import floor, ceil
import random

# 全局数组保持与原代码结构一致
a = [[0] * 2 for _ in range(3)]


def my_abs(x):
    if x < 0:
        x = -x
    return x


def calcLen(x1, y1, x2, y2):
    return my_abs(x1 - x2) + my_abs(y1 - y2) + 1


def solve(points):
    # points: [(x0,y0), (x1,y1), (x2,y2)]
    for i in range(3):
        a[i][0], a[i][1] = points[i]

    xMax = max(a[0][0], a[1][0], a[2][0])
    xMin = min(a[0][0], a[1][0], a[2][0])
    yMax = max(a[0][1], a[1][1], a[2][1])
    yMin = min(a[0][1], a[1][1], a[2][1])

    pathLen = xMax - xMin + yMax - yMin + 1

    # 找到中转点 (px, py)
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

    # 画从三点到 (px, py) 的路径
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

    return ans


def main(n):
    """
    n 作为规模参数用于控制生成的坐标范围：
    - 坐标在 [0, n] 区间内随机生成三点
    """
    if n < 1:
        n = 1
    # 生成测试数据：三组点 (x, y)
    points = [(random.randint(0, n), random.randint(0, n)) for _ in range(3)]

    ans = solve(points)

    # 输出结果，与原逻辑保持一致
    print(len(ans))
    for x, y in ans:
        print(x, y)


# 示例调用（评测时会由外部调用 main(n)）
# main(10)