def main(n):
    # Deterministically generate points A(ax, ay), B(bx, by), C(cx, cy)
    # Use n to scale coordinate magnitudes
    ax = n
    ay = 2 * n
    bx = -n
    by = n // 2
    cx = n // 3
    cy = -n // 4

    if (ax - bx) * (ax - cx) > 0 and (ay - by) * (ay - cy) > 0:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)