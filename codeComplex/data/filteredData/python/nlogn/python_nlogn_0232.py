import random


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def point3(x1, y1, x2, y2, x3, y3):
    dy12 = x2 - x1
    dx12 = -(y2 - y1)
    dx13 = x3 - x1
    dy13 = y3 - y1
    return (dx12 * dx13 + dy12 * dy13) == 0


def main(n):
    # 生成测试数据：n 个整数点 (x, y)，坐标在 [-10, 10] 内
    # 对应原程序：第一行是 n，后续 n 行是两个整数
    points = [(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(n)]

    lstline = []

    if n <= 4:
        # 原程序在 n <= 4 时只读掉点并输出 YES
        print('YES')
        return

    # n >= 5 的情况
    lst5 = []
    for j in range(5):
        lst5.append([points[j][0], points[j][1]])

    ok = True
    # 在前 5 个点中找 3 点共线（point3 返回 True 表示第三点在由前两点定义的直线上）
    for i in range(3):
        for j in range(i + 1, 4):
            for k in range(j + 1, 5):
                if ok and point3(
                    lst5[i][0], lst5[i][1],
                    lst5[j][0], lst5[j][1],
                    lst5[k][0], lst5[k][1]
                ):
                    l1x1 = lst5[i][0]
                    l1y1 = lst5[i][1]
                    l1x2 = lst5[j][0]
                    l1y2 = lst5[j][1]
                    ok = False

    if not ok:
        lstline = []
        for j in range(5):
            if not point3(l1x1, l1y1, l1x2, l1y2, lst5[j][0], lst5[j][1]):
                lstline.append([lst5[j][0], lst5[j][1]])

    if ok:
        # 未找到第一条公共线，原程序直接将剩余点读完并输出 NO
        print('NO')
        return

    res = 'YES'
    ok1 = True

    # 从第 6 个点开始处理（原代码中 n - 5 次 input()）
    for idx in range(5, n):
        mas = [points[idx][0], points[idx][1]]
        okey1 = point3(l1x1, l1y1, l1x2, l1y2, mas[0], mas[1])

        if ok1:
            if len(lstline) == 2:
                l2x1 = lstline[0][0]
                l2y1 = lstline[0][1]
                l2x2 = lstline[1][0]
                l2y2 = lstline[1][1]
                ok1 = False
                okey2 = point3(l2x1, l2y1, l2x2, l2y2, mas[0], mas[1])
                if (not okey1) and (not okey2):
                    res = 'NO'
            elif not okey1:
                lstline.append([mas[0], mas[1]])
        else:
            if not okey1:
                okey2 = point3(l2x1, l2y1, l2x2, l2y2, mas[0], mas[1])
                if not okey2:
                    res = 'NO'

    print(res)


if __name__ == "__main__":
    # 示例：运行 main，规模 n 可在此处修改
    main(10)