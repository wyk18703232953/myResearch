def bitcount(m: int) -> int:
    return bin(m).count('1')


def main(n: int) -> None:
    # 这里根据 n 生成测试数据：
    # 原程序需要 n, x, y。n 是规模参数，由 main 的参数传入。
    # 我们根据 n 构造一组合理的 x, y，使得 1 <= x <= y <= n 且 x+y <= n 时有意义。
    # 示例策略：令 x = max(1, n // 4), y = max(x, n // 2)
    x = max(1, n // 4)
    y = max(x, n // 2)

    if x > y:
        x, y = y, x
    assert x <= y

    # 若 x + y > n 时，下面算法依旧可运行，只是 n // (x + y) 为 0
    mm1 = range(1, 1 << y, 2)
    vbases = [
        ((~(m1 >> (y - x)) & ~m1 & ((1 << x) - 1)) << y) | m1
        for m1 in mm1
        if m1 & (m1 >> x) == 0
    ]

    def btail(m: int) -> int:
        tail_len = n % (x + y)
        if tail_len == 0:
            return 0
        return bitcount(m & ((1 << tail_len) - 1))

    res = max(
        bitcount(m) * (n // (x + y)) + btail(m)
        for m in vbases
    )
    # print(res)
    pass
if __name__ == "__main__":
    # 示例调用，按需要修改 n
    main(20)