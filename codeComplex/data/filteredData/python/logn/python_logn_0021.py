def main(n: int):
    """
    n 为规模参数，用来生成一对 (l, r) 作为测试数据：
    这里约定生成：
        l = 2**(n-1)
        r = 2**n - 1
    保证 0 <= l <= r，且二进制长度约为 n 位。
    """
    if n <= 0:
        # 若 n 不合法，给一个默认值
        l, r = 0, 0
    else:
        l = 1 << (n - 1)      # 2**(n-1)
        r = (1 << n) - 1      # 2**n - 1

    # 以下为原逻辑，仅移除 input() 并封装
    al = []
    ar = []
    rr = r
    ll = l

    while rr:
        p = rr % 2
        ar.append(p)
        rr //= 2

    while ll:
        p = ll % 2
        al.append(p)
        ll //= 2

    if len(ar) != len(al):
        ans = (2 ** len(ar)) - 1
    else:
        n_bits = len(ar)
        k = 0
        for i in range(n_bits - 1, -1, -1):
            if ar[i] != al[i]:
                k = i + 1
                break
        ans = (2 ** k) - 1
        if k == 0:
            ans = 0

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)