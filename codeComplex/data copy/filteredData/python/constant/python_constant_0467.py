def main(n):
    # n 作为规模参数，这里仅用于构造确定性的点坐标
    # 构造三个点 A(ax, ay), B(bx, by), C(cx, cy)
    ax = n
    ay = n // 2

    bx = -n
    by = -n // 2

    cx = n * 2
    cy = n

    if ((bx < ax and cx < ax) or (bx > ax and cx > ax)) and ((by < ay and cy < ay) or (by > ay and cy > ay)):
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)