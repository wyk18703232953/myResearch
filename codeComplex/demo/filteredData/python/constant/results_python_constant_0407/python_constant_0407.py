def main(n):
    # n controls coordinate scale; ensure at least 1
    if n < 1:
        n = 1

    # Deterministically generate first quadrilateral points (x1..x4, y1..y4)
    # Use simple arithmetic patterns based on n
    x1 = 0
    y1 = 0
    x2 = n
    y2 = 0
    x3 = 0
    y3 = n
    x4 = n
    y4 = n

    # Deterministically generate second quadrilateral points (X1..X4, Y1..Y4)
    # Slightly shift and scale with modular patterns to vary position
    shift = n // 2
    span = max(1, n // 3)

    X1 = shift
    Y1 = shift
    X2 = shift + span
    Y2 = shift
    X3 = shift
    Y3 = shift + span
    X4 = shift + span
    Y4 = shift + span

    x = [x1, x2, x3, x4]
    y = [y1, y2, y3, y4]
    x = list(set(x))
    y = list(set(y))
    x.sort()
    y.sort()
    xl, xr = x
    yl, yr = y

    if xl <= X1 <= xr and yl <= Y1 <= yr:
        # print('YES')
        pass
        return
    if xl <= X2 <= xr and yl <= Y2 <= yr:
        # print('YES')
        pass
        return
    if xl <= X3 <= xr and yl <= Y3 <= yr:
        # print('YES')
        pass
        return
    if xl <= X4 <= xr and yl <= Y4 <= yr:
        # print('YES')
        pass
        return

    CX, CY = (X1 + X2 + X3 + X4) // 4, (Y1 + Y2 + Y3 + Y4) // 4
    X1, X2, X3, X4 = X1 - CX, X2 - CX, X3 - CX, X4 - CX
    Y1, Y2, Y3, Y4 = Y1 - CY, Y2 - CY, Y3 - CY, Y4 - CY

    if xl <= CX <= xr and yl <= CY <= yr:
        # print('YES')
        pass
        return

    A = 0
    for X in (X1, X2, X3, X4):
        A = max(A, abs(X))
    if abs(x1 - CX) + abs(y1 - CY) <= A:
        # print('YES')
        pass
        return
    if abs(x2 - CX) + abs(y2 - CY) <= A:
        # print('YES')
        pass
        return
    if abs(x3 - CX) + abs(y3 - CY) <= A:
        # print('YES')
        pass
        return
    if abs(x4 - CX) + abs(y4 - CY) <= A:
        # print('YES')
        pass
        return
    # print('NO')
    pass
if __name__ == "__main__":
    main(10)