def main(n):
    # 根据规模 n 生成测试数据：
    # 令 m = n，构造 3 组测试：
    # 1. 两个矩形无交集
    # 2. 两个矩形部分重叠
    # 3. 一个矩形完全包含另一个
    tests = []

    m = n

    # 测试1：无交集
    # 第一个矩形在左上，第二个在右下
    a1, b1, c1, d1 = 1, 1, max(1, n // 2), max(1, n // 2)
    e1, f1, g1, h1 = max(1, n // 2) + 1, max(1, n // 2) + 1, n, n
    tests.append((n, m, a1, b1, c1, d1, e1, f1, g1, h1))

    # 测试2：部分重叠
    # 让第二个矩形从第一个矩形内部开始并向右下扩展
    a2, b2, c2, d2 = 1, 1, n, max(1, n // 2)
    e2, f2 = max(1, n // 3), max(1, n // 3)
    g2, h2 = n, n
    tests.append((n, m, a2, b2, c2, d2, e2, f2, g2, h2))

    # 测试3：包含关系
    # 第二个矩形完全包含第一个矩形
    a3, b3 = max(1, n // 4), max(1, n // 4)
    c3, d3 = max(a3, n // 2), max(b3, n // 2)
    e3, f3 = 1, 1
    g3, h3 = n, n
    tests.append((n, m, a3, b3, c3, d3, e3, f3, g3, h3))

    def calc(x1, y1, x2, y2):
        if x1 > x2 or y1 > y2:
            return 0
        area = (x2 - x1 + 1) * (y2 - y1 + 1)
        if area % 2 == 0:
            return area // 2
        if (x1 + y1) % 2 == 1:
            return area // 2 + 1
        return area // 2

    for case in tests:
        n, m, a, b, c, d, e, f, g, h = case
        j, k, l, q = max(a, e), max(b, f), min(c, g), min(d, h)
        black = (
            calc(1, 1, n, m)
            - calc(a, b, c, d)
            - calc(e, f, g, h)
            + (h - f + 1) * (g - e + 1)
            + calc(j, k, l, q)
        )
        # print(n * m - black, black)
        pass
if __name__ == "__main__":
    # 示例调用：规模 n = 8
    main(8)