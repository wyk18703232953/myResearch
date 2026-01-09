def num_sq(x, y, x2, y2):
    # 返回 (黑格数, 白格数)
    a = abs(x2 - x) + 1
    b = abs(y2 - y) + 1
    area = a * b
    if a % 2 == 0 or b % 2 == 0:
        return area // 2, area // 2
    if (x + y) % 2 == 0:
        num_b = area // 2
        return num_b, area - num_b
    num_w = area // 2
    return area - num_w, num_w


def intc(p1, p2, p3, p4):
    # 计算两个矩形的交集，矩形由左下角和右上角点给定
    x1 = max(p1[0], p3[0])
    x2 = min(p2[0], p4[0])
    y1 = max(p1[1], p3[1])
    y2 = min(p2[1], p4[1])
    if x1 <= x2 and y1 <= y2:
        return (x1, y1), (x2, y2)
    return None


def solve_case(n, m, rect1, rect2):
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2

    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    p4 = (x4, y4)

    # 整个棋盘
    all_b, all_w = num_sq(1, 1, n, m)

    # 交集
    tmp = intc(p1, p2, p3, p4)
    if tmp:
        intc_1, intc_2 = tmp
        t_b, t_w = num_sq(intc_1[0], intc_1[1], intc_2[0], intc_2[1])

    # 第一个矩形变白
    b, w = num_sq(x1, y1, x2, y2)
    if tmp:
        b -= t_b
        w -= t_w

    # 第二个矩形变黑
    b2, w2 = num_sq(x3, y3, x4, y4)
    if tmp:
        b2 -= t_b
        w2 -= t_w

    # 汇总
    w_tot, b_tot = (all_w + b - w2, all_b - b + w2)
    if tmp:
        w_tot -= t_w
        b_tot += t_w

    return w_tot, b_tot


def gen_test_case(n):
    # 简单生成一个随规模变化的测试用例：
    # 棋盘大小：n x n
    # rect1：左上部分，rect2：右下部分，有重叠
    m = n
    # 保证坐标合法：1 <= x1 <= x2 <= n, 1 <= y1 <= y2 <= m
    x1, y1 = 1, 1
    x2, y2 = max(1, n // 2), max(1, m // 2)
    x3, y3 = max(1, n // 3), max(1, m // 3)
    x4, y4 = n, m
    rect1 = (x1, y1, x2, y2)
    rect2 = (x3, y3, x4, y4)
    return n, m, rect1, rect2


def main(n):
    # 生成若干测试数据，这里生成 n 组规模递增的棋盘
    results = []
    for i in range(1, n + 1):
        N, M, r1, r2 = gen_test_case(i + 1)  # 棋盘规模随 i 增长
        w_tot, b_tot = solve_case(N, M, r1, r2)
        results.append((w_tot, b_tot))

    # 输出结果
    for w, b in results:
        # print(w, b)
        pass
if __name__ == "__main__":
    # 示例：调用 main(5)，生成 5 组测试数据并输出
    main(5)