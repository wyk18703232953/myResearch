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


def deterministic_randint(i, lower, upper):
    span = upper - lower + 1
    return lower + (i * 1103515245 + 12345) % span


def main(n):
    global extendedPoints, startingPoints, interestPoints
    extendedPoints = set()
    startingPoints = set()
    interestPoints = []

    if n < 1:
        n = 1

    # map n to grid and number of starting points
    grid_size = max(2, n)
    max_start = grid_size * grid_size
    num_start = max(1, min(n // 2, max_start))

    N = grid_size
    M = grid_size
    K = num_start
    mscale = 5

    # deterministic starting points
    for i in range(K):
        x = (i % N) + 1
        y = (i // N) % M + 1
        p = TPoint(x, y)
        startingPoints.add(p)
        extendedPoints.add(p)

    tmpPoints = []
    tmpPoints.append(TPoint(1, 1))
    tmpPoints.append(TPoint(1, M))
    tmpPoints.append(TPoint(N, 1))
    tmpPoints.append(TPoint(N, M))
    if N > 2 and M > 2:
        tmpPoints.append(TPoint(int(N / 2), 1))
        tmpPoints.append(TPoint(1, int(M / 2)))
        tmpPoints.append(TPoint(int(N / 2), M))
        tmpPoints.append(TPoint(N, int(M / 2)))
        tmpPoints.append(TPoint(int(N / 2), int(M / 2)))

    for p in tmpPoints:
        addPoint(p, interestPoints)
    for p in list(startingPoints):
        extend(p, N, M, interestPoints)

    interestPoints.sort(reverse=True, key=sortKey)
    while len(interestPoints) > 3 * mscale:
        interestPoints.pop(len(interestPoints) - 1)

    if len(interestPoints) > 0:
        maxPoint = interestPoints[0]
        for idx, p in enumerate(interestPoints):
            currentBeam = [p]
            canExtend = True
            step = 0
            while canExtend:
                rx = deterministic_randint(idx * 100000 + step, 1, N)
                ry = deterministic_randint(idx * 200000 + step, 1, M)
                addPoint(TPoint(rx, ry), currentBeam)
                canExtend = False
                for i in range(len(currentBeam)):
                    if extend(currentBeam[i], N, M, currentBeam):
                        canExtend = True
                currentBeam.sort(reverse=True, key=sortKey)
                while len(currentBeam) > mscale:
                    currentBeam.pop(len(currentBeam) - 1)
                step += 1
            if currentBeam[0].h > maxPoint.h:
                maxPoint = currentBeam[0]
        # print(str(maxPoint.x) + " " + str(maxPoint.y))
        pass
        return maxPoint.x, maxPoint.y

    else:
        # print(str(N) + " " + str(M))
        pass
        return N, M


if __name__ == "__main__":
    main(10)