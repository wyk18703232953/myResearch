import random

def iscollinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    cross = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    ans = bool(cross)
    return not ans

def checkfortwolines(a, b, points, n):
    set1 = set(points)
    for i in range(n):  # erase all points collinear with a, b
        if iscollinear(a, b, points[i]):
            set1.remove(points[i])

    if len(set1) <= 2:
        return True
    else:
        pts1 = list(set1)
        for i in range(len(pts1)):  # check if remaining points are all collinear
            if not iscollinear(pts1[0], pts1[1], pts1[i]):
                return False
        return True

def generate_points(n, coord_limit=10**6):
    points = []
    for _ in range(n):
        x = random.randint(-coord_limit, coord_limit)
        y = random.randint(-coord_limit, coord_limit)
        points.append((x, y))
    return points

def main(n):
    if n <= 0:
        return "NO"

    if n <= 4:
        return "YES"

    points = generate_points(n)

    a = points[0]
    b = points[1]
    c = points[2]

    if (checkfortwolines(a, b, points, n) or
        checkfortwolines(b, c, points, n) or
        checkfortwolines(c, a, points, n)):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    # 示例调用：规模为 10 的测试
    print(main(10))