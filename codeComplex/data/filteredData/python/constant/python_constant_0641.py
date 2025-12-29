from random import randint


def solve(n, m, x1, y1, x2, y2,
          x3, y3, x4, y4):

    def inside(x, y):
        return 1 <= x <= m and 1 <= y <= n

    def col(a, b):
        assert inside(a, b)
        return 'WB'[(a + b) % 2]

    def cols(x1, y1, x2, y2):
        assert inside(x1, y1) and inside(x2, y2)
        assert x1 <= x2 and y1 <= y2
        w, h = x2 + 1 - x1, y2 + 1 - y1
        if w % 2 == 0 or h % 2 == 0:
            return w * h // 2, w * h // 2
        else:
            wh, bl = w * h // 2, w * h // 2
            if col(x1, y1) == 'W':
                wh += 1
            else:
                bl += 1
            return wh, bl

    def overlap():
        X1 = max(x1, x3)
        X2 = min(x2, x4)
        Y1 = max(y1, y3)
        Y2 = min(y2, y4)
        if X1 > X2 or Y1 > Y2:
            return None
        return X1, Y1, X2, Y2

    tot_wh, tot_bl = cols(1, 1, m, n)

    A_wh, A_bl = cols(x1, y1, x2, y2)
    ovrlp = overlap()
    if ovrlp is not None:
        O_wh, O_bl = cols(*ovrlp)
        assert A_wh >= O_wh and A_bl >= O_bl
        A_wh -= O_wh
        A_bl -= O_bl

    B_wh, B_bl = cols(x3, y3, x4, y4)

    # Paint A white:
    tot_wh += A_bl
    tot_bl -= A_bl

    # Paint B black:
    tot_wh -= B_wh
    tot_bl += B_wh
    return tot_wh, tot_bl


def main(n):
    """
    n: 测试数据规模（测试组数）
    生成 n 组随机测试数据并输出每组结果：
    - 第一行输出使用的参数 n（测试组数）
    - 后续 n 行，每行输出一组 solve(...) 的结果：white_count black_count
    """
    t = n
    print(t)
    for _ in range(t):
        # 随机生成棋盘大小
        rows = randint(1, 50)
        cols = randint(1, 50)

        # 随机生成两个矩形的顶点
        x1, x2, x3, x4 = [randint(1, rows) for _ in range(4)]
        y1, y2, y3, y4 = [randint(1, cols) for _ in range(4)]
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        x3, x4 = min(x3, x4), max(x3, x4)
        y3, y4 = min(y3, y4), max(y3, y4)

        wh, bl = solve(rows, cols, x1, y1, x2, y2, x3, y3, x4, y4)
        print(wh, bl)


if __name__ == "__main__":
    # 示例：生成 5 组随机测试
    main(5)