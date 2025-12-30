def main(n):
    # 生成隐藏的 a, b（规模由 n 控制，按位数生成）
    # 为了与原始算法结构保持一致，仍然用 30 位，但你可以根据 n 修改位数
    import random

    max_bits = 30  # 原程序固定 30 位
    # 若希望规模 n 控制位数，可改为：max_bits = n
    max_val = (1 << max_bits) - 1
    hidden_a = random.randint(0, max_val)
    hidden_b = random.randint(0, max_val)

    # 定义交互查询函数：模拟原来的输出 "? a b" 并返回 sign((a^hidden_a) - (b^hidden_b))
    def query(x, y):
        xa = x ^ hidden_a
        yb = y ^ hidden_b
        if xa > yb:
            return 1
        elif xa < yb:
            return -1
        else:
            return 0

    # 初始查询，对应原来的：
    # print("? 0 0")
    t = query(0, 0)

    A = [-1] * max_bits
    B = [-1] * max_bits
    a = 0
    b = 0

    i = max_bits - 1
    d = 1 << i

    # 第一阶段：从高位到低位
    while i >= 0:
        a += d
        b += d
        s = query(a, b)

        if s == -t:
            if s == 1:
                A[i] = 0
                B[i] = 1
                b -= d
                t = query(a, b)
            elif s == -1:
                A[i] = 1
                a -= d
                B[i] = 0
                t = query(a, b)
        i -= 1
        d //= 2

    # 第二阶段：填补未确定位
    d = 1
    for j in range(max_bits):
        if A[j] == -1:
            a ^= d
            s = query(a, b)
            if s == 1:
                A[j] = 1
                B[j] = 1
            else:
                A[j] = 0
                B[j] = 0
            a ^= d
        d *= 2

    # 根据 A、B 的位拼出最终 a、b
    d = 1
    a = 0
    b = 0
    for i in range(max_bits):
        a += d * A[i]
        b += d * B[i]
        d *= 2

    # 输出结果（模拟原来的最终输出）
    print("!", a, b)

    # 为了验证正确性，可以打印隐藏值与求得值（若不需要可注释）
    # print("hidden:", hidden_a, hidden_b)
    # print("found :", a, b)


if __name__ == "__main__":
    # n 作为规模参数，本实现中未直接用来控制逻辑，
    # 如需按 n 控制位数，可在 main 中用 n 替代 max_bits
    main(30)