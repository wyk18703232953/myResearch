def getcol(x1, y1, x2, y2):
    dx = max((x2 - x1 + 1), 0)
    dy = max((y2 - y1 + 1), 0)
    b = w = dx * dy // 2
    if dx % 2 and dy % 2:
        if (x1 + y1) % 2:
            b = b + 1
        else:
            w = w + 1
    return w, b


def main(n):
    """
    n 作为规模参数，用来生成测试数据。
    这里约定：
      - 棋盘大小为 n x n
      - 生成一个测试用例
      - 矩形1 和 矩形2 都为棋盘内的一小块区域
    """
    # 棋盘大小
    board_n = n
    board_m = n

    # 为了简单，构造两个固定形式的矩形：
    # 第一个矩形：左上角 (1, 1)，右下角 (n//2, n//2)
    x1, y1 = 1, 1
    x2, y2 = max(1, n // 2), max(1, n // 2)

    # 第二个矩形：右下角附近的一块
    x3, y3 = max(1, n // 2), max(1, n // 2)
    x4, y4 = board_n, board_m

    # 棋盘整体的白黑格数量
    w, b = getcol(1, 1, board_n, board_m)

    # 两个矩形各自的白黑格数量
    w1, b1 = getcol(x1, y1, x2, y2)
    w2, b2 = getcol(x3, y3, x4, y4)

    # 两个矩形交集的白黑格数量
    w3, b3 = getcol(max(x1, x3), max(y1, y3), min(x2, x4), min(y2, y4))

    # 去掉两个区域后剩余棋盘的白黑格数量
    woff = w - w1 - w2 + w3
    boff = b - b1 - b2 + b3

    # 根据原逻辑计算最终白格、黑格
    final_w = woff + w1 - w3 + b1 - b3
    final_b = boff + w3 + b3 + b2 - b3 + w2 - w3

    print(final_w, final_b)


if __name__ == "__main__":
    # 示例：使用 n=8 运行
    main(8)