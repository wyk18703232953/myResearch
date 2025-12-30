def main(n: int):
    # 根据 n 生成一组测试数据 (a, v, l, d, w)
    # 这里简单用 n 构造，确保数值为正且有一定变化
    a = max(1, n % 10 + 1)          # 加速度
    v = max(1, (n * 2) % 20 + 1)    # 最大速度
    l = max(1, (n * 3) % 100 + 10)  # 总路程
    d = max(1, (n * 5) % l)         # 前段长度（小于 l）
    w = max(1, (n * 7) % v)         # 限速

    # 原逻辑
    if v <= w or w * w > 2 * a * d:
        if v * v > 2 * a * l:
            ans = (2 * l / a) ** 0.5
        else:
            ans = l / v + v / 2 / a
    else:
        u = (w * w / 2 + a * d) ** 0.5
        if u > v:
            m = (
                v / a
                + (v - w) / a
                + (d - (v * v / 2 / a) - (v * v - w * w) / 2 / a) / v
            )
        else:
            m = (2 * u - w) / a

        if v * v > 2 * a * (l - d + w * w / 2 / a):
            ans = m - w / a + (2 * (l - d + (w * w / 2 / a)) / a) ** 0.5
        else:
            ans = m - w / a + (l - d + w * w / 2 / a) / v + v / 2 / a

    print(ans)


if __name__ == "__main__":
    # 示例：用 n=10 调用
    main(10)