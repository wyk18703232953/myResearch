import random

def main(n):
    # 测试数据生成：生成两个非负整数 A, B，数值在 [0, 2^n - 1] 范围内
    if n <= 0:
        n = 1
    max_val = (1 << n) - 1
    A = random.randint(0, max_val)
    B = random.randint(0, max_val)

    # 用于模拟交互时的返回值：
    # 对于给定的 (c, d)，返回：
    #   1  如果 (A ^ c) > (B ^ d)
    #  -1  如果 (A ^ c) < (B ^ d)
    #   0  如果 (A ^ c) == (B ^ d)
    def query(c, d):
        val_a = A ^ c
        val_b = B ^ d
        if val_a > val_b:
            return 1
        elif val_a < val_b:
            return -1
        else:
            return 0

    # 对应原始代码逻辑的实现
    a, b = 0, 0
    # 原代码 ops = 29，说明最高考虑到第 29 位（共 30 位），
    # 这里按 n 的规模自适应，但不少于 1
    ops = max(0, n - 1)

    agtb = query(0, 0)

    for i in range(ops, -1, -1):
        c = a | (1 << i)
        d = b
        x = query(c, d)

        c = a
        d = b | (1 << i)
        y = query(c, d)

        if x != y:
            if y == 1:
                a = a | (1 << i)
                b = b | (1 << i)
        else:
            if agtb == 1:  # a > b
                a = a | (1 << i)
            else:
                b = b | (1 << i)
            agtb = x

    # 输出推断出的 a, b，以及真实的 A, B 以便验证
    print("Guessed a, b:", a, b)
    print("Real    A, B:", A, B)


if __name__ == "__main__":
    # 示例：n = 30（与原代码等价的规模）
    main(30)