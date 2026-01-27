def signum(n):
    return 1 if n > 0 else 0 if n == 0 else -1

def range_includes(i, j):
    s = signum(j - i)
    return range(i, j + s, s)

def main(n):
    # Deterministically generate two quadrilaterals with 4 points each
    # Scale coordinates with n to control input size magnitude
    aCoords = []
    bCoords = []
    for i in range(4):
        x = i * n
        y = (i + 1) * n
        aCoords.append((x, y))
    for i in range(4):
        x = (i + 2) * n
        y = (3 * n - i * n)
        bCoords.append((x, y))
    aCoords = tuple(aCoords)
    bCoords = tuple(bCoords)

    minX = min(aCoord[0] for aCoord in aCoords)
    minY = min(aCoord[1] for aCoord in aCoords)
    maxX = max(aCoord[0] for aCoord in aCoords)
    maxY = max(aCoord[1] for aCoord in aCoords)

    def inFirst(x, y):
        return x >= minX and x <= maxX and y >= minY and y <= maxY

    minSum = min(sum(bCoord) for bCoord in bCoords)
    maxSum = max(sum(bCoord) for bCoord in bCoords)
    minDiff = min(bCoord[0] - bCoord[1] for bCoord in bCoords)
    maxDiff = max(bCoord[0] - bCoord[1] for bCoord in bCoords)

    def inSecond(x, y):
        return x + y >= minSum and x + y <= maxSum and x - y >= minDiff and x - y <= maxDiff

    for aCoord in aCoords:
        if inSecond(*aCoord):
            return True
    for i in range(-1, 3):
        c1 = bCoords[i]
        c2 = bCoords[i + 1]
        for x, y in zip(range_includes(c1[0], c2[0]), range_includes(c1[1], c2[1])):
            if inFirst(x, y):
                return True
    return False

if __name__ == "__main__":
    # example deterministic call
    n = 10
    # print("YES" if main(n) else "NO")
    pass