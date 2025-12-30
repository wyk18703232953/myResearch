def bs(c, t):
    l, r = 0, t - 1
    while l <= r:
        mid = (l + r) >> 1
        if ((2 * t - mid - 1) * mid) // 2 + 1 < c:
            l = mid + 1
        else:
            r = mid - 1
    return r + 1


def main(n: int):
    """
    n 作为规模参数，这里用来生成测试数据：
    - casas 在 1 到 n*n 之间
    - tubos 在 max(1, n//2) 到 n 之间
    根据需要可以调整生成规则。
    """
    # 生成测试数据
    tubos = max(1, n // 2)
    casas = min(n * n, (tubos * (tubos + 1)) // 2)  # 保证在可搜索范围内

    res = bs(casas, tubos)
    print(-1 if res == tubos else res)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)