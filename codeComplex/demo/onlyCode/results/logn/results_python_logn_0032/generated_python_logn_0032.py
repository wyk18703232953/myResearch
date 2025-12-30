def main(n: int):
    """
    规模参数 n 用来生成测试数据 (a, b)。
    这里示例：生成两个不同的 n 位二进制数对应的整数 a, b。
    你可以根据需要调整生成方式。
    """
    if n < 2:
        # 至少保证有两位，且 a != b
        n = 2

    # 生成两个 n 位数：
    # a = 2^n - 1 (n 位全 1)
    # b = 2^(n-1)       (仅最高位为 1，其余为 0)
    a = (1 << n) - 1
    b = (1 << (n - 1))

    # 如果不希望 a == b，做一个防御性处理
    if a == b:
        b -= 1

    # ------- 以下为原逻辑 -------
    if a == b:
        print(0)
        return

    aa = ""
    bb = ""
    x, y = a, b
    while x or y:
        aa += str(x % 2)
        bb += str(y % 2)
        x //= 2
        y //= 2
    aa = aa[::-1]
    bb = bb[::-1]

    idx = 0
    while idx < len(aa) and idx < len(bb) and aa[idx] == bb[idx]:
        idx += 1

    ln = len(aa)
    r = 2 ** (ln - idx) - 1
    print(r)


if __name__ == "__main__":
    # 示例：调用 main(10)，规模 n=10
    main(10)