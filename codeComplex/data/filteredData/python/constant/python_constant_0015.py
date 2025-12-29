def func(u, v, a, l):
    if (v ** 2 - u ** 2) >= 2 * a * l:
        return ((u ** 2 + 2 * a * l) ** 0.5 - u) / a
    else:
        t1 = (v - u) / a
        t2 = (l - (u * t1 + a * t1 * t1 / 2)) / v
        return t1 + t2


def efficient(v, a, w, d):
    if 2 * v * v - w * w <= 2 * a * d:
        t1 = v / a
        t2 = (v - w) / a
        t3 = (d - 0.5 * a * t1 * t1 - v * t2 + 0.5 * a * t2 * t2) / v
        return t1 + t2 + t3
    else:
        bound = ((2 * a * d + w * w) / 2) ** 0.5
        t1 = bound / a
        t2 = (bound - w) / a
        t3 = func(0, w, a, d)
        # 原代码这里有一个永远不会执行到的 return t1+t2
        return min(t1 + t2, t3)


def main(n):
    """
    n 为规模参数，这里用来生成测试数据：
    a, v, l, d, w 都与 n 成线性关系，仅作为示例。
    可以根据需要调整生成规则。
    """
    # 生成一组随 n 变化的测试数据（保证为正数）
    a = max(1, n)
    v = max(1, 2 * n)
    l = max(1, 3 * n)
    d = max(1, 2 * n)
    w = max(1, n)

    if 2 * a * d <= w ** 2 or v <= w:
        t1 = func(0, v, a, l)
        result = t1
    else:
        t1 = efficient(v, a, w, d)
        t2 = func(w, v, a, l - d)
        result = t1 + t2

    # 按原程序格式输出
    print(f"{result:.8f}")


if __name__ == "__main__":
    # 示例：用 n = 10 运行
    main(10)