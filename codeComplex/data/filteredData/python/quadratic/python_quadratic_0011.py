def main(n):
    # 生成测试数据：n 个点的 x 坐标，以及半径 r
    # 这里示例为：r 固定为 1，x 为等差序列 0, 2, 4, ...，保证相邻圆恰好能接触
    r = 1
    x = [2 * i for i in range(n)]

    y = []
    for xi in x:
        yi = r
        for tx, ty in zip(x, y):
            if xi - 2 * r <= tx <= xi + 2 * r:
                dy = (4.0 * r ** 2 - (tx - xi) ** 2) ** 0.5
                yi = max(yi, ty + dy)
        y.append(yi)

    print(*y)


if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)