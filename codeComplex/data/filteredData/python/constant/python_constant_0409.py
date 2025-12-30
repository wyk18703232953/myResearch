import random

def onseg(p, q, r):
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0  # colinear
    return 1 if val > 0 else 2  # clock or counterclock wise

def doint(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and onseg(p1, p2, q1):
        return True
    if o2 == 0 and onseg(p1, q2, q1):
        return True
    if o3 == 0 and onseg(p2, p1, q2):
        return True
    if o4 == 0 and onseg(p2, q1, q2):
        return True

    return False

def main(n):
    # n 控制坐标范围 [-n, n]
    coords = [random.randint(-n, n) for _ in range(16)]
    x0,y0,x1,y1,x2,y2,x3,y3, x4,y4,x5,y5,x6,y6,x7,y7 = coords

    A = (x0, y0)
    B = (x1, y1)
    C = (x2, y2)
    D = (x3, y3)
    a = (x4, y4)
    b = (x5, y5)
    c = (x6, y6)
    d = (x7, y7)

    if (doint(A, B, a, b) or doint(A, C, a, b) or doint(A, D, a, b) or
        doint(B, C, a, b) or doint(B, D, a, b) or doint(C, D, a, b) or
        doint(A, B, a, c) or doint(A, C, a, c) or doint(A, D, a, c) or
        doint(B, C, a, c) or doint(B, D, a, c) or doint(C, D, a, c) or
        doint(A, B, a, d) or doint(A, C, a, d) or doint(A, D, a, d) or
        doint(B, C, a, d) or doint(B, D, a, d) or doint(C, D, a, d) or
        doint(A, B, b, c) or doint(A, C, b, c) or doint(A, D, b, c) or
        doint(B, C, b, c) or doint(B, D, b, c) or doint(C, D, b, c) or
        doint(A, B, b, d) or doint(A, C, b, d) or doint(A, D, b, d) or
        doint(B, C, b, d) or doint(B, D, b, d) or doint(C, D, b, d) or
        doint(A, B, c, d) or doint(A, C, c, d) or doint(A, D, c, d) or
        doint(B, C, c, d) or doint(B, D, c, d) or doint(C, D, c, d)):
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main(10)