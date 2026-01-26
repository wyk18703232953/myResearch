from sys import stdout

mp = 29

# 预计算 2 的幂
powers = [1]
for i in range(32):
    powers.append(powers[-1] * 2)


def main(n: int):
    """
    n 用作规模参数，这里用于控制 mp 和幂次数上限。
    原逻辑中 mp = 29、幂次到 2^32；为了体现规模参数，
    将 mp 和幂次数限制在 n 以内（不超过原来的上限）。
    """

    # 限制 mp 和幂次数规模
    mp_local = min(mp, max(0, n - 1))  # 至少 0，最多 29
    max_power_idx = min(32, max(0, n))  # 至少 0，最多 32

    # 为本次运行构造 a, b：用 n 生成一组确定的测试数据
    # 原程序中 a,b 实际是隐藏值，此处用 n 决定它们
    if n <= 0:
        a_hidden, b_hidden = 3, 1

    else:
        a_hidden = (3 + n * 7) & 0x3FFFFFFF
        b_hidden = (1 + n * 5) & 0x3FFFFFFF

    # 重新生成 powers，根据 max_power_idx 限制
    local_powers = [1]
    for _ in range(max_power_idx):
        local_powers.append(local_powers[-1] * 2)

    # 交互接口：不再 input，而是直接用隐藏的 a,b 计算
    def get_ans(c, d):
        # 返回值与原交互协议一致: -sign((a^c) - (b^d))
        ac = a_hidden ^ c
        bd = b_hidden ^ d
        if ac > bd:
            return -1
        elif ac < bd:
            return 1

        else:
            return 0

    # 以下是对原逻辑的直接改写，只是使用本地 get_ans 与 local_powers
    a, b = 0, 0
    c, d = 0, 0

    q = get_ans(0, 0)

    for i in range(mp_local + 1):
        cp = mp_local - i
        c += local_powers[cp]
        d += local_powers[cp]

        if q == 0:
            continue

        t = get_ans(c, d)

        if t != q:
            if t == 1:
                a += local_powers[cp]
                c -= local_powers[cp]
            elif t == -1:
                b += local_powers[cp]
                d -= local_powers[cp]
            q = get_ans(c, d)

    for i in range(mp_local + 1):
        cp = mp_local - i
        if (c & local_powers[cp]) > 0 and (d & local_powers[cp]) > 0:
            c -= local_powers[cp]
            t = get_ans(c, d)

            if t < 0:
                a += local_powers[cp]
                b += local_powers[cp]

            c += local_powers[cp]

    # 输出最后推断出来的 a, b
    # print('!', a, b)
    pass


# 简单示例：需要时可调用 main(n)
if __name__ == "__main__":
    # 示例规模，可按需修改或从外部调用 main(n)
    main(30)