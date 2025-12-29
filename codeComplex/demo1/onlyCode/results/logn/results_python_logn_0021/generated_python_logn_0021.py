def main(n: int):
    """
    使用规模参数 n 生成测试数据 (l, r)，并执行原逻辑。
    这里约定：
    - 生成 0 <= l <= r <= 2^n - 1 的一组数据。
    - 为简单起见，取 l = 0, r = 2^n - 1（可按需要修改生成规则）。
    """
    l = 0
    r = (1 << n) - 1  # 2^n - 1

    al = []
    ar = []
    rr = r
    ll = l

    while rr:
        p = rr % 2
        ar.append(p)
        rr = rr // 2
    while ll:
        p = ll % 2
        al.append(p)
        ll = ll // 2

    if len(ar) != len(al):
        ans = (2 ** len(ar)) - 1
    else:
        m = len(ar)
        k = 0
        for i in range(m - 1, -1, -1):
            if ar[i] != al[i]:
                k = i + 1
                break
        ans = (2 ** k) - 1
        if k == 0:
            ans = 0

    print(ans)


if __name__ == "__main__":
    # 示例：以 n = 5 运行
    main(5)