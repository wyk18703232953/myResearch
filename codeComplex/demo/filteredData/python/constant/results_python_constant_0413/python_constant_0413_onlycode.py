from collections import namedtuple

Point = namedtuple("Point", "x y")
Square = namedtuple("Square", "left right top bottom")
Triangle = namedtuple("Triangle", "left top")

a = [int(v) for v in input().split()]
b = [int(v) for v in input().split()]

a = [Point(a[i], a[i + 1]) for i in range(0, 8, 2)]
b = [Point(b[i], b[i + 1]) for i in range(0, 8, 2)]

bc = Point(sum(p.x for p in b) // 4, sum(p.y for p in b) // 4)
bb = [None] * 4
for p in b:
    if p.x < bc.x:
        bb[0] = p
    elif p.y > bc.y:
        bb[1] = p
    elif p.x > bc.x:
        bb[2] = p
    elif p.y < bc.y:
        bb[3] = p
    else:
        assert False

def in_sqr(sqr, pt):
    return sqr.left <= pt.x <= sqr.right and sqr.bottom <= pt.y <= sqr.top

def in_tri(tri, pt):
    return (
        tri.left.x <= pt.x <= tri.top.x and
        tri.left.y <= pt.y <= tri.top.y and
        pt.y - tri.left.y <= pt.x - tri.left.x
    )

def solve_sqr_tri(sqr, tri):
    return (
        in_sqr(sqr, tri.left) or
        in_sqr(sqr, tri.top) or
        in_sqr(sqr, Point(tri.top.x, tri.left.y)) or
        in_tri(tri, Point(sqr.left, sqr.top)) or
        in_tri(tri, Point(sqr.right, sqr.top)) or
        in_tri(tri, Point(sqr.right, sqr.bottom)) or
        in_tri(tri, Point(sqr.left, sqr.bottom))
    )

def rotate90(pt):
    return Point(-pt.y, pt.x)

def iterate_rot(pt, times):
    for _ in range(times):
        pt = rotate90(pt)
    return pt

def solve_sqr_sqr45(sqr_pts, sqr45):
    for i in range(4):
        tri_pts = sqr45[i], sqr45[(i + 1) % 4]
        left, top = [iterate_rot(pt, i) for pt in tri_pts]

        assert left.x < top.x
        assert left.y < top.y

        tri = Triangle(left=left, top=top)

        sqr = Square(
            left=min(p.x for p in sqr_pts),
            right=max(p.x for p in sqr_pts),
            top=max(p.y for p in sqr_pts),
            bottom=min(p.y for p in sqr_pts),
        )

        if solve_sqr_tri(sqr, tri):
            return True

        sqr_pts = [rotate90(pt) for pt in sqr_pts]

    return False


print(["NO", "YES"][solve_sqr_sqr45(a, bb)])
