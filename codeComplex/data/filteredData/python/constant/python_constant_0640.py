def getBW(x1, y1, x2, y2):
    if (x2 - x1) % 2 == 1 or (y2 - y1) % 2 == 1:
        return [(y2 + 1 - y1) * (x2 + 1 - x1) // 2,
                (y2 + 1 - y1) * (x2 + 1 - x1) // 2]
    else:
        if (x1 % 2 == 0 and y1 % 2 == 0) or (x1 % 2 == 1 and y1 % 2 == 1):
            return [(y2 + 1 - y1) * (x2 + 1 - x1) // 2,
                    1 + (y2 + 1 - y1) * (x2 + 1 - x1) // 2]
        else:
            return [1 + (y2 + 1 - y1) * (x2 + 1 - x1) // 2,
                    (y2 + 1 - y1) * (x2 + 1 - x1) // 2]


def main(n):
    """
    n 为规模参数，用来生成测试数据。
    这里构造一组与原题类似的数据：
      - 棋盘大小为 m = n, n = n
      - 第一块矩形覆盖左上角 n//2 的区域
      - 第二块矩形覆盖右下角 n//2 的区域
    """
    m = n

    # 生成第一块矩形 (x1, y1, x2, y2)
    x1, y1 = 1, 1
    x2, y2 = max(1, n // 2), max(1, m // 2)

    # 生成第二块矩形 (x3, y3, x4, y4)
    x3, y3 = max(1, n // 2), max(1, m // 2)
    x4, y4 = n, m

    BW = getBW(1, 1, n, m)
    BW1 = getBW(x1, y1, x2, y2)
    BW2 = getBW(x3, y3, x4, y4)

    # 求交集
    xo1 = max(x1, x3)
    xo2 = min(x2, x4)
    yo1 = max(y1, y3)
    yo2 = min(y2, y4)
    BWO = [0, 0]
    if xo2 >= xo1 and yo2 >= yo1:
        BWO = getBW(xo1, yo1, xo2, yo2)

    B = BW[0] - BW1[0] + BW2[1] + BWO[0]
    W = BW[1] + BW1[0] - BW2[1] - BWO[0]

    print(W, B)


if __name__ == "__main__":
    # 示例：使用 n = 8 作为测试规模
    main(8)