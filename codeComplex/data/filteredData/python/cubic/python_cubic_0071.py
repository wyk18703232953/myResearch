from math import log
import random

spaces = (" ", "\n", "\t")
stops = ("", " ", "\n", "\t")
extendedPoints = set()
startingPoints = set()
interestPoints = []


class TPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.h = 0

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * 20000 + self.y


def sortKey(p):
    return p.h


def heuristic(p, otherPoints):
    minH = float("inf")
    for point in otherPoints:
        currentH = abs(point.x - p.x) + abs(point.y - p.y)
        if currentH < minH:
            minH = currentH
    return minH


def addPoint(p, pointList):
    if p not in extendedPoints:
        p.h = heuristic(p, startingPoints)
        extendedPoints.add(p)
        pointList.append(p)
        return True
    else:
        return False


def extend(point, n, m, poinList):
    ok = False
    if point.x > 1:
        ok = addPoint(TPoint(point.x - 1, point.y), poinList) or ok
        if point.y > 1:
            ok = addPoint(TPoint(point.x - 1, point.y - 1), poinList) or ok
        if point.y < m:
            ok = addPoint(TPoint(point.x - 1, point.y + 1), poinList) or ok
    if point.x < n:
        ok = addPoint(TPoint(point.x + 1, point.y), poinList) or ok
        if point.y > 1:
            ok = addPoint(TPoint(point.x + 1, point.y - 1), poinList) or ok
        if point.y < m:
            ok = addPoint(TPoint(point.x + 1, point.y + 1), poinList) or ok
    if point.y > 1:
        ok = addPoint(TPoint(point.x, point.y - 1), poinList) or ok
    if point.y < m:
        ok = addPoint(TPoint(point.x, point.y + 1), poinList) or ok

    return ok


def main(n):
    """
    参数 n 作为规模，用于生成一个 n x n 的网格，并随机生成起点集合。
    返回结果为字符串："x y\n"
    """
    # 清空全局状态（便于多次调用 main）
    extendedPoints.clear()
    startingPoints.clear()
    interestPoints.clear()

    # 网格大小 n x n
    m = n

    # 起点数量：与规模相关，至少 1 个，最多 n（可根据需求调整策略）
    k = max(1, min(n, n // 2))

    # 随机生成 k 个起点
    random.seed()
    for _ in range(k):
        x = random.randint(1, n)
        y = random.randint(1, m)
        p = TPoint(x, y)
        startingPoints.add(p)
        extendedPoints.add(p)

    mscale = 5

    tmpPoints = []
    tmpPoints.append(TPoint(1, 1))
    tmpPoints.append(TPoint(1, m))
    tmpPoints.append(TPoint(n, 1))
    tmpPoints.append(TPoint(n, m))
    if n > 2 and m > 2:
        tmpPoints.append(TPoint(int(n / 2), 1))
        tmpPoints.append(TPoint(1, int(m / 2)))
        tmpPoints.append(TPoint(int(n / 2), m))
        tmpPoints.append(TPoint(n, int(m / 2)))
        tmpPoints.append(TPoint(int(n / 2), int(m / 2)))

    for p in tmpPoints:
        addPoint(p, interestPoints)
    for p in startingPoints:
        extend(p, n, m, interestPoints)

    interestPoints.sort(reverse=True, key=sortKey)
    while len(interestPoints) > 3 * mscale:
        interestPoints.pop(len(interestPoints) - 1)

    random.seed()

    if len(interestPoints) > 0:
        maxPoint = interestPoints[0]
        for p in interestPoints:
            currentBeam = [p]
            canExtend = True
            while canExtend:
                addPoint(TPoint(random.randint(1, n), random.randint(1, m)), currentBeam)
                canExtend = False
                for i in range(len(currentBeam)):
                    if extend(currentBeam[i], n, m, currentBeam):
                        canExtend = True
                currentBeam.sort(reverse=True, key=sortKey)
                while len(currentBeam) > mscale:
                    currentBeam.pop(len(currentBeam) - 1)
            if currentBeam[0].h > maxPoint.h:
                maxPoint = currentBeam[0]
        result = f"{maxPoint.x} {maxPoint.y}\n"
    else:
        result = f"{n} {m}\n"

    return result