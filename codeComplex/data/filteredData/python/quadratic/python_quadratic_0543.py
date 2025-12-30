import random


def gen_points(A, B):
    """
    +--.
    |
    |
    .
    """
    return [(A[0], B[1]), (B[0], A[1])]


def mark_points(A, B):
    A = list(A)
    B = list(B)
    d = set()
    x_s = 1 if A[0] < B[0] else -1
    y_s = 1 if A[1] < B[1] else -1
    d.add((A[0], A[1]))
    while A[0] != B[0]:
        A[0] += x_s
        d.add((A[0], A[1]))
    while A[1] != B[1]:
        A[1] += y_s
        d.add((A[0], A[1]))
    return d


def main(n):
    # 使用 n 控制点坐标的随机范围：[-n, n]
    x1, y1 = random.randint(-n, n), random.randint(-n, n)
    x2, y2 = random.randint(-n, n), random.randint(-n, n)
    x3, y3 = random.randint(-n, n), random.randint(-n, n)

    points = [(x1, y1), (x2, y2), (x3, y3)]

    points += gen_points([x1, y1], [x2, y2])
    points += gen_points([x2, y2], [x3, y3])
    points += gen_points([x1, y1], [x3, y3])

    points = list(set(points))

    ans = 1e9
    ans_l = []

    for el in points:
        d = mark_points([x1, y1], el).union(mark_points([x2, y2], el))
        d = d.union(mark_points([x3, y3], el))
        if len(d) < ans:
            ans = len(d)
            ans_l = d

    print(ans)
    for el in ans_l:
        print(*el)


if __name__ == "__main__":
    # 示例调用：规模设为 10
    main(10)