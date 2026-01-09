from collections import namedtuple

Point = namedtuple("Point", "x y")
Square = namedtuple("Square", "left right top bottom")
Triangle = namedtuple("Triangle", "left top")


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


def generate_points_from_n(n):
    base = max(1, n)
    a_coords = [base + i for i in range(8)]
    b_coords = [base * 2 + i for i in range(8)]
    a_pts = [Point(a_coords[i], a_coords[i + 1]) for i in range(0, 8, 2)]
    b_pts = [Point(b_coords[i], b_coords[i + 1]) for i in range(0, 8, 2)]
    return a_pts, b_pts


def build_bb(b):
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
    return bb


def main(n):
    a, b = generate_points_from_n(n)
    bb = build_bb(b)
    result = solve_sqr_sqr45(a, bb)
    # print(["NO", "YES"][result])
    pass
if __name__ == "__main__":
    main(10)