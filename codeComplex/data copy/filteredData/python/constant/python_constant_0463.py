def main(n):
    # n 作为平面规模参数，生成三个点坐标
    size = n
    x1, y1 = 1, 1
    x2, y2 = size // 2 + 1, size // 3 + 1
    x3, y3 = size, size

    if (y2 - y1) * (y3 - y1) > 0 and (x2 - x1) * (x3 - x1) > 0 and x1 + y1 != x3 + y3:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)