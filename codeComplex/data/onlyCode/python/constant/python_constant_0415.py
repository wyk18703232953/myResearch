import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print(self.x, self.y)


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def on(self, p):
        return distance(self.p1, p) + distance(self.p2, p) == distance(self.p1, self.p2)

    def print(self):
        self.p1.print()
        self.p2.print()


class Square:
    def __init__(self, points):
        self.points = points

    def area(self):
        return distance(self.points[0], self.points[1]) ** 2

    def lines(self):
        l = []
        for i in range(3):
            l.append(Line(self.points[i], self.points[i + 1]))
        l.append(Line(self.points[3], self.points[0]))
        return l

    def midpoint(self):
        return Point(self.points[0].x / 2 + self.points[2].x / 2, self.points[0].y / 2 + self.points[2].y / 2)

    def print(self):
        for point in self.points:
            point.print()


def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** .5


def tri_area(p1, p2, p3):
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)
    s = a + b + c
    s /= 2
    return (s * (s - a) * (s - b) * (s - c)) ** .5


def inter(p, s):
    a = s.area()
    area_sum = tri_area(s.points[0], s.points[1], p) + tri_area(s.points[1], s.points[2], p)
    area_sum += tri_area(s.points[2], s.points[3], p) + tri_area(s.points[3], s.points[0], p)
    if abs(a - area_sum) < 0.000001:
        return True
    return False


c1 = input().split(" ")
c2 = input().split(" ")
for i in range(8):
    c1[i] = int(c1[i])
    c2[i] = int(c2[i])
c1p = []
c2p = []
for i in range(0, 8, 2):
    c1p.append(Point(c1[i], c1[i + 1]))
    c2p.append(Point(c2[i], c2[i + 1]))
s1 = Square(c1p)
s2 = Square(c2p)
yes = False
for point in s1.points:
    if inter(point, s2):
        if not yes:
            print("YES")
            yes = True
for point in s2.points:
    if inter(point, s1):
        if not yes:
            print("YES")
            yes = True
if inter(s1.midpoint(), s2):
    if not yes:
        print("YES")
        yes = True
if inter(s2.midpoint(), s1):
    if not yes:
        print("YES")
if not yes:
    print("NO")