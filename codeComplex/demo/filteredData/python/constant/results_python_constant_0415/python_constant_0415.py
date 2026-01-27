import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        # print(self.x, self.y)
        pass


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
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def tri_area(p1, p2, p3):
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)
    s = a + b + c
    s /= 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def inter(p, s):
    a = s.area()
    area_sum = tri_area(s.points[0], s.points[1], p) + tri_area(s.points[1], s.points[2], p)
    area_sum += tri_area(s.points[2], s.points[3], p) + tri_area(s.points[3], s.points[0], p)
    if abs(a - area_sum) < 0.000001:
        return True
    return False


def generate_square_params(k):
    base = 4 * k
    return [
        base, base,
        base + 1, base,
        base + 1, base + 1,
        base, base + 1,
    ]


def build_square_from_list(coords):
    points = []
    for i in range(0, 8, 2):
        points.append(Point(coords[i], coords[i + 1]))
    return Square(points)


def check_two_squares(s1, s2):
    yes = False
    for point in s1.points:
        if inter(point, s2):
            if not yes:
                # print("YES")
                pass
                yes = True
    for point in s2.points:
        if inter(point, s1):
            if not yes:
                # print("YES")
                pass
                yes = True
    if inter(s1.midpoint(), s2):
        if not yes:
            # print("YES")
            pass
            yes = True
    if inter(s2.midpoint(), s1):
        if not yes:
            # print("YES")
            pass
            yes = True
    if not yes:
        # print("NO")
        pass


def main(n):
    if n <= 0:
        return
    for t in range(1, n + 1):
        c1 = generate_square_params(t)
        c2 = generate_square_params(t + 1)
        s1 = build_square_from_list(c1)
        s2 = build_square_from_list(c2)
        check_two_squares(s1, s2)


if __name__ == "__main__":
    main(5)