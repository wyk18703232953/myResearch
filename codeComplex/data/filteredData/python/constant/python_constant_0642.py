def wb(n, m, flip=False):
    w = b = n * m // 2
    if n % 2 == 1 and m % 2 == 1:
        w += 1
    if flip:
        return b, w
    else:
        return w, b


def main(n):
    """
    n 为规模参数，用于生成测试数据。
    本示例中：我们生成 t = n 组测试，每组棋盘大小与矩形坐标
    通过 n 派生，确保无 input()。
    """

    t = n  # 测试组数

    # 为简单起见，构造规则化的测试数据：
    # 对于第 i 组测试：
    #   棋盘尺寸：N = 10 + i, M = 10 + 2*i
    #   矩形1：从 (1,1) 到 (N//2, M//2)
    #   矩形2：从 (N//3, M//3) 到 (N, M)
    for i in range(1, t + 1):
        N = 10 + i
        M = 10 + 2 * i

        x1, y1 = 1, 1
        x2, y2 = N // 2, M // 2

        x3, y3 = N // 3, M // 3
        x4, y4 = N, M

        x5 = max(x1, x3)
        x6 = min(x2, x4)
        y5 = max(y1, y3)
        y6 = min(y2, y4)
        ov = False
        if x6 - x5 >= 0 and y6 - y5 >= 0:
            ov = True

        w, b = wb(N, M)
        wm, bm = wb(x2 - x1 + 1, y2 - y1 + 1, (x1 + y1) % 2 == 1)
        wd, bd = wb(x4 - x3 + 1, y4 - y3 + 1, (x3 + y3) % 2 == 1)
        if ov:
            wo, bo = wb(x6 - x5 + 1, y6 - y5 + 1, (x5 + y5) % 2 == 1)
        else:
            wo, bo = 0, 0

        w = w + bm - wd - bo
        b = b - bm + wd + bo
        print(w, b)


if __name__ == "__main__":
    # 示例：调用 main(3) 生成 3 组测试数据并输出结果
    main(3)