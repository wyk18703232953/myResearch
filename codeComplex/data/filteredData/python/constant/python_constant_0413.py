from collections import namedtuple
import random

Point = namedtuple("Point", "x y")
Square = namedtuple("Square", "left right top bottom")
Triangle = namedtuple("Triangle", "left top")


def in_sqr(sqr, pt):
    return sqr.left <= pt.x <= sqr.right and sqr.bottom <= pt.y <= sqr.top


def in_tri(tri, pt):
    return (
        tri.left.x <= pt.x <= tri.top.x
        and tri.left.y <= pt.y <= tri.top.y
        and pt.y - tri.left.y <= pt.x - tri.left.x
    )


def solve_sqr_tri(sqr, tri):
    return (
        in_sqr(sqr, tri.left)
        or in_sqr(sqr, tri.top)
        or in_sqr(sqr, Point(tri.top.x, tri.left.y))
        or in_tri(tri, Point(sqr.left, sqr.top))
        or in_tri(tri, Point(sqr.right, sqr.top))
        or in_tri(tri, Point(sqr.right, sqr.bottom))
        or in_tri(tri, Point(sqr.left, sqr.bottom))
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


def gen_axis_aligned_square(center_x, center_y, half_side):
    return [
        Point(center_x - half_side, center_y - half_side),
        Point(center_x + half_side, center_y - half_side),
        Point(center_x + half_side, center_y + half_side),
        Point(center_x - half_side, center_y + half_side),
    ]


def gen_rotated_square(center_x, center_y, half_diag):
    # square rotated 45 degrees: 4 points on diagonals
    pts = [
        Point(center_x - half_diag, center_y),
        Point(center_x, center_y + half_diag),
        Point(center_x + half_diag, center_y),
        Point(center_x, center_y - half_diag),
    ]
    # shuffle order a bit to avoid any accidental assumptions
    random.shuffle(pts)
    return pts


def main(n):
    random.seed(n)

    # use n as a scale; ensure positive sizes
    base = max(1, n)
    cx = base * 2
    cy = base * 3

    # axis-aligned square (a)
    half_side = max(1, base // 2)
    a = gen_axis_aligned_square(cx, cy, half_side)

    # rotated square (b), around nearby center
    cx2 = cx + base // 3
    cy2 = cy + base // 4
    half_diag = max(1, base // 2)
    b = gen_rotated_square(cx2, cy2, half_diag)

    # original post-processing on b to form bb
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
            raise AssertionError("Unexpected point location")

    res = solve_sqr_sqr45(a, bb)
    print(["NO", "YES"][res])


if __name__ == "__main__":
    # example run with n = 10
    main(10)