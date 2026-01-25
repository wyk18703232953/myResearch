def main(n):
    # Deterministic generation of three points based on n
    # n controls the scale of coordinates
    if n < 1:
        n = 1
    x1, y1 = 0, 0
    x2, y2 = n, 0
    x3, y3 = n // 2, n

    points = [(x1, y1), (x2, y2), (y3, x3)]

    def gen_points(A, B):
        return [(A[0], B[1]), (B[0], A[1])]

    points += gen_points([x1, y1], [x2, y2])
    points += gen_points([x2, y2], [x3, y3])
    points += gen_points([x1, y1], [x3, y3])

    points = list(set(points))

    ans = 1e9
    ans_l = []

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
    main(10)