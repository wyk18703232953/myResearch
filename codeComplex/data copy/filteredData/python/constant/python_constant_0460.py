import math


def main(n):
    # Deterministic data generation based on n
    # n is not used in original logic; we map it to coordinates deterministically
    x = n
    y = 2 * n
    bx = n // 2
    by = n // 3
    cx = n // 4
    cy = n // 5

    x1, y1 = x - bx, y - by
    x2, y2 = x - cx, y - cy

    if abs(x2) == abs(y2):
        # print('NO')
        pass
        return
    if math.copysign(x2, x1) != x2:
        # print('NO')
        pass
        return
    if math.copysign(y2, y1) != y2:
        # print('NO')
        pass
        return
    # print('YES')
    pass
if __name__ == "__main__":
    main(10)