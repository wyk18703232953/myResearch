def main(n):
    """
    n 用来控制测试数据规模，这里简单生成一组依赖 n 的参数：
    a, v, l, d, w 都为正数，且随 n 线性变化。
    你可以根据实际需要自行修改生成规则。
    """
    # 生成测试数据（示例规则）
    a = 1 + n          # 加速度
    v = 2 + n          # 最大速度
    l = 10 * n         # 总路程
    d = max(1, n // 2) # 前段限制距离
    w = max(1, n // 3) # 前段限速

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
    # 示例调用：可以修改这里的 n 或在外部导入 main 后自行调用
    main(10)