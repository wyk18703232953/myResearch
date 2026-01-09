def solve(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    ba = bin(a)[2:]
    bb = bin(b)[2:]
    r = ''
    if len(ba) != len(bb):
        int('1' * len(bb), 2)

    else:
        for ca, cb in zip(ba, bb):
            if ca == cb:
                r += '0'

            else:
                r += '1'
                break
    r += '1' * (len(bb) - len(r))
    return int(r, 2)


def main(n: int):
    # 规模含义：n 为整数的比特长度（至少为 1）
    if n < 1:
        n = 1

    # 确定性构造两个 n 比特以内的非负整数 a, b
    # a 的二进制形态：从 1 到 n 的奇偶模式
    # b 的二进制形态：从 1 到 n 的 3 的余数模式
    a = 0
    b = 0
    for i in range(n):
        bit_pos = i
        # a: 第 i 位为 (i % 2)
        if i % 2 == 1:
            a |= (1 << bit_pos)
        # b: 第 i 位为 (i % 3 == 0)
        if i % 3 == 0:
            b |= (1 << bit_pos)

    res = solve(a, b)
    # print(res)
    pass
if __name__ == "__main__":
    main(20)