from collections import deque
from sys import stdin, stderr
lines = deque(line.strip() for line in stdin.readlines())

def nextline():
    return lines.popleft()

def types(cast, sep=None):
    return tuple(cast(x) for x in strs(sep=sep))

def ints(sep=None):
    return types(int, sep=sep)

def strs(sep=None):
    return tuple(nextline()) if sep == '' else tuple(nextline().split(sep=sep))

def signum(n):
    return 1 if n > 0 else 0 if n == 0 else -1

def range_includes(i, j):
    s = signum(j - i)
    return range(i, j + s, s)

def main():
    # lines will now contain all of the input's lines in a list
    first = ints()
    aCoords = tuple(first[i:i+2] for i in range(0, 8, 2))
    minX = min(aCoord[0] for aCoord in aCoords)
    minY = min(aCoord[1] for aCoord in aCoords)
    maxX = max(aCoord[0] for aCoord in aCoords)
    maxY = max(aCoord[1] for aCoord in aCoords)
    def inFirst(x, y):
        return x >= minX and x <= maxX and y >= minY and y <= maxY

    second = ints()
    bCoords = tuple(second[i:i+2] for i in range(0, 8, 2))
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

if __name__ == '__main__':
    print("YES" if main() else "NO")
