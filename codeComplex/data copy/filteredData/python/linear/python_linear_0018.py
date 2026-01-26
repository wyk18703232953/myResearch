def main(n):
    # 生成素数列表 y（与原程序相同逻辑）
    y = [2]
    for i in range(3, 1000):
        z = 0
        for x in range(2, int(i ** 0.5) + 1):
            if i % x == 0:
                z += 1
        if z == 0:
            y.append(i)

    # 生成相邻素数和列表 h
    h = []
    for i in range(0, len(y) - 1):
        x = y[i] + y[i + 1]
        h.append(x)

    # 将 n 映射为输入规模：a 和 b
    # a 控制计数区间上界，b 为需要的数量阈值
    # 为了保证可扩展和确定性，这里用简单算术构造
    if n < 1:
        a = 1
        b = 1

    else:
        # a 至少为 2，最多不超过 h 中的最大值，且随 n 增长
        max_h = max(h) + 1
        a = min(max(2, n * 10), max_h)
        # b 至少为 1，随 n 缓慢增长
        b = max(1, n // 5)

    # 原程序中对 h 的处理（每个元素加 1）
    for i in range(0, len(h)):
        h[i] = h[i] + 1

    # 在 h 中筛选素数，得到 g
    g = []
    for i in h:
        z = 0
        for x in range(2, int(i ** 0.5) + 1):
            if i % x == 0:
                z += 1
        if z == 0:
            g.append(i)

    # 统计 g 中在 [2, a] 范围内的个数 j
    j = 0
    for i in g:
        if 2 <= i <= a:
            j += 1

    # 根据 j 和 b 输出结果
    if j >= b:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 进行复杂度实验
    main(10)