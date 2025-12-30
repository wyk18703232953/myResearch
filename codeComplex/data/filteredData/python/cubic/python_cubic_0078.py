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
        self.h = 0  # эвристика

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        return isinstance(other, TPoint) and self.x == other.x and self.y == other.y

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
    参数 n 作为规模，构造一个 n x n 的棋盘，并随机生成起始点。
    返回算法最终输出的 (x, y) 坐标。
    """
    # 清空全局集合，保证多次调用 main(n) 时互不影响
    global extendedPoints, startingPoints, interestPoints
    extendedPoints = set()
    startingPoints = set()
    interestPoints = []

    # 规模设成 n x n
    m = n

    # 根据规模生成测试数据：随机生成 k 个起点
    # 至少 1 个，至多 min(10, n*n)
    max_k = min(10, n * n)
    if max_k <= 0:
        return (n, m)

    random.seed()
    k = random.randint(1, max_k)

    # 随机生成 k 个不同的网格点作为 startingPoints
    used = set()
    while len(startingPoints) < k:
        x = random.randint(1, n)
        y = random.randint(1, m)
        if (x, y) in used:
            continue
        used.add((x, y))
        p = TPoint(x, y)
        startingPoints.add(p)
        extendedPoints.add(p)

    mscale = 5

    # 构建初始 interestPoints
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
        # 返回最终坐标
        return (maxPoint.x, maxPoint.y)
    else:
        return (n, m)


if __name__ == "__main__":
    # 示例：调用 main(10)，并打印返回结果
    x, y = main(10)
    print(x, y)