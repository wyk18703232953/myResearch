from sys import stdout
import random

mp = 29
powers = [1]
for i in range(32):
    powers.append(powers[-1] * 2)


def main(n):
    """
    n 用来控制生成的测试数据规模，这里简单地将 a,b 生成为与 n 相关的整数。
    为了保持算法结构不变，使用一个模拟的 get_ans，不再使用 input()。
    """

    # 根据 n 生成测试数据（可按需要修改生成逻辑）
    # 这里简单设计为在 [0, 2^(mp+1)) 范围内随机生成 a, b，且与 n 做一点关系
    random.seed(n)
    a = random.randint(0, (1 << (mp + 1)) - 1)
    b = random.randint(0, (1 << (mp + 1)) - 1)

    c, d = 0, 0

    # 模拟交互：根据真实的 a,b 返回比较结果
    def get_ans(c_local, d_local):
        # 原交互：如果 (a^c) > (b^d) 则返回 -1；如果 (a^c) < (b^d) 则返回 1；否则 0
        x = a ^ c_local
        y = b ^ d_local
        if x > y:
            return -1
        elif x < y:
            return 1
        else:
            return 0

    q = get_ans(0, 0)

    # 第一阶段：推断 a 与 b 的每一位关系
    for i in range(mp + 1):
        cp = mp - i
        c += powers[cp]
        d += powers[cp]
        if q == 0:
            continue
        t = get_ans(c, d)

        if t != q:
            if t == 1:
                # b^d > a^c
                a += powers[cp]
                c -= powers[cp]
            elif t == -1:
                # a^c > b^d
                b += powers[cp]
                d -= powers[cp]
            q = get_ans(c, d)

    # 第二阶段：精细确定 a,b 的具体位
    for i in range(mp + 1):
        cp = mp - i
        if (c & powers[cp]) > 0 and (d & powers[cp]) > 0:
            c -= powers[cp]
            t = get_ans(c, d)

            if t < 0:
                a += powers[cp]
                b += powers[cp]

            c += powers[cp]

    # 输出推断出来的 a, b 以及真实的 a, b 供校验
    # 由于算法中我们直接在 a,b 上累加修改，推断值即为 a,b 本身
    print('! (deduced_a, deduced_b) =', a, b)

    # 若想看初始真实值，可在上面保存一份 original_a, original_b
    # 这里演示保存与比较：
    # 为保持接口简单，此处重新生成同样随机值来展示（因为同一 seed）
    random.seed(n)
    true_a = random.randint(0, (1 << (mp + 1)) - 1)
    true_b = random.randint(0, (1 << (mp + 1)) - 1)
    print('(true_a, true_b)      =', true_a, true_b)


if __name__ == "__main__":
    # 示例：调用 main，并将 n 作为规模参数传入
    main(10)