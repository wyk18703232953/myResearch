from math import log

spaces = (" ", "\n", "\t")
stops = ("", " ", "\n", "\t")
extendedPoints = set()
startingPoints = set()
interestPoints = []


class TPoint:
    x = 0
    y = 0
    h = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

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


def det_rand_int(seed, n, m):
    val = seed * 1103515245 + 12345
    if val < 0:
        val = -val
    # map to [1, n] or [1, m] deterministically
    x = (val % n) + 1
    y = (val // 7 % m) + 1
    return x, y


def main(n):
    global extendedPoints, startingPoints, interestPoints

    extendedPoints = set()
    startingPoints = set()
    interestPoints = []

    # map n to grid size and number of starting points
    if n < 2:
        g = 2

    else:
        g = n
    rows = g
    cols = g
    k = max(1, g // 2)

    mscale = 5

    for i in range(1, k + 1):
        x = (i * 37) % rows + 1
        y = (i * 53) % cols + 1
        p = TPoint(x, y)
        startingPoints.add(p)
        extendedPoints.add(p)

    tmpPoints = []
    tmpPoints.append(TPoint(1, 1))
    tmpPoints.append(TPoint(1, cols))
    tmpPoints.append(TPoint(rows, 1))
    tmpPoints.append(TPoint(rows, cols))
    if rows > 2 and cols > 2:
        tmpPoints.append(TPoint(rows // 2, 1))
        tmpPoints.append(TPoint(1, cols // 2))
        tmpPoints.append(TPoint(rows // 2, cols))
        tmpPoints.append(TPoint(rows, cols // 2))
        tmpPoints.append(TPoint(rows // 2, cols // 2))

    for p in tmpPoints:
        addPoint(p, interestPoints)
    for p in startingPoints:
        extend(p, rows, cols, interestPoints)

    interestPoints.sort(reverse=True, key=sortKey)
    while len(interestPoints) > 3 * mscale:
        interestPoints.pop(len(interestPoints) - 1)

    if len(interestPoints) > 0:
        maxPoint = interestPoints[0]
        for idx, p in enumerate(interestPoints):
            currentBeam = [p]
            canExtend = True
            local_seed = (rows * 1000003 + cols * 10007 + idx * 97)
            step = 0
            while canExtend:
                xr, yr = det_rand_int(local_seed + step, rows, cols)
                step += 1
                addPoint(TPoint(xr, yr), currentBeam)
                canExtend = False
                for i in range(len(currentBeam)):
                    if extend(currentBeam[i], rows, cols, currentBeam):
                        canExtend = True
                currentBeam.sort(reverse=True, key=sortKey)
                while len(currentBeam) > mscale:
                    currentBeam.pop(len(currentBeam) - 1)
            if currentBeam[0].h > maxPoint.h:
                maxPoint = currentBeam[0]
        # print(str(maxPoint.x) + " " + str(maxPoint.y))
        pass

    else:
        # print(str(rows) + " " + str(cols))
        pass
if __name__ == "__main__":
    main(10)