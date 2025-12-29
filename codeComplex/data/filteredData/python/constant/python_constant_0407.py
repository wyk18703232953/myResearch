import random


def main(n: int):
    # 生成测试数据：
    # 使用 n 控制坐标范围大小，例如坐标在 [-n, n] 内随机生成
    coords = [random.randint(-n, n) for _ in range(16)]
    (
        x1, y1, x2, y2,
        x3, y3, x4, y4,
        X1, Y1, X2, Y2,
        X3, Y3, X4, Y4
    ) = coords

    x = [x1, x2, x3, x4]
    y = [y1, y2, y3, y4]
    x = sorted(set(x))
    y = sorted(set(y))
    xl, xr = x
    yl, yr = y

    if xl <= X1 <= xr and yl <= Y1 <= yr:
        print('YES')
        return
    if xl <= X2 <= xr and yl <= Y2 <= yr:
        print('YES')
        return
    if xl <= X3 <= xr and yl <= Y3 <= yr:
        print('YES')
        return
    if xl <= X4 <= xr and yl <= Y4 <= yr:
        print('YES')
        return

    CX, CY = (X1 + X2 + X3 + X4) // 4, (Y1 + Y2 + Y3 + Y4) // 4
    X1, X2, X3, X4 = X1 - CX, X2 - CX, X3 - CX, X4 - CX
    Y1, Y2, Y3, Y4 = Y1 - CY, Y2 - CY, Y3 - CY, Y4 - CY

    if xl <= CX <= xr and yl <= CY <= yr:
        print('YES')
        return

    A = 0
    for X in (X1, X2, X3, X4):
        A = max(A, abs(X))

    if abs(x1 - CX) + abs(y1 - CY) <= A:
        print('YES')
        return
    if abs(x2 - CX) + abs(y2 - CY) <= A:
        print('YES')
        return
    if abs(x3 - CX) + abs(y3 - CY) <= A:
        print('YES')
        return
    if abs(x4 - CX) + abs(y4 - CY) <= A:
        print('YES')
        return

    print('NO')


if __name__ == "__main__":
    # 示例：n = 10
    main(10)