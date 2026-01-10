class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:

    def __init__(self, start, end):
        self.x = end.x - start.x
        self.y = end.y - start.y

    def mult(self, a):
        return self.y * a.x - self.x * a.y


def onLine(points):
    n = len(points)
    if n < 3:
        return True
    a = Vector(points[0], points[1])
    for i in range(2, n):
        b = Vector(points[0], points[i])
        if a.mult(b) != 0:
            return False
    return True


def generate_points(n):
    points = []
    for i in range(n):
        x = i
        y = (i * 2 + 3) % (n + 1 if n > 0 else 1)
        points.append(Point(x, y))
    return points


def core_logic(points):
    n = len(points)

    if n <= 3:
        return 'YES'

    tmp = [points[0], points[1]]
    oth = []
    for i in range(2, n):
        tmp.append(points[i])
        if not onLine(tmp):
            oth.append(points[i])
        tmp.pop()
    if onLine(oth):
        return 'YES'

    tmp = [points[0], points[2]]
    oth = []
    for i in range(1, n):
        if i == 2:
            continue
        tmp.append(points[i])
        if not onLine(tmp):
            oth.append(points[i])
        tmp.pop()
    if onLine(oth):
        return 'YES'

    tmp = [points[1], points[2]]
    oth = []
    for i in range(0, n):
        if i == 2 or i == 1:
            continue
        tmp.append(points[i])
        if not onLine(tmp):
            oth.append(points[i])
        tmp.pop()
    if onLine(oth):
        return 'YES'

    return 'NO'


def main(n):
    points = generate_points(n)
    result = core_logic(points)
    print(result)


if __name__ == "__main__":
    main(10)